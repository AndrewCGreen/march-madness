#This file will be used to scrape this season's data
import pandas as pd
from requests import get
from bs4 import BeautifulSoup
from os import environ, mkdir
from selenium import webdriver
import time

mmpath = environ["MMPATH"]

#The table paremeters on the webpage required me to wait a few seconds otherwise the html would simply produce LOADING...
#That is why i ditched requests here for selenium, which is a bit clunkier bvut gives more control

def pull_html (browser) -> []:
    """Pulls all the html once the entire page is loaded"""
    time.sleep(5)
    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")
    html_lines = soup.find_all("div",{"id":"tble"})
    return html_lines
    
def build_browser(url) -> webdriver:
    """builds a selenium browser on that specief url"""
    browser = webdriver.Chrome()
    browser.get(url)
    return browser

def get_html_table(url): 
    """opens the browser, at the url given, and produces the relevant table and quits the browser"""
    browser = build_browser(url)
    html_table = pull_html(browser)
    browser.quit()
    return html_table[0]

def raw_data_array(html_table) -> [[]]:
    """Takes the html table and parses out the actual data elements we need returning a list of lists"""
    
    trs = html_table.find_all("tr")
    all_lines = []
    for tr in trs[2:]:
        tds = (tr.find_all("td"))
        new_line = []
        for t in tds:
            new_line.append(t.get_text())
        if len(new_line) > 1:
            all_lines.append(new_line)
    return all_lines

def build_dataframe(all_lines) -> pd.DataFrame:
    """Uses raw elements and puts them into a dataframe with the headers we have been using as convention"""
    columns = ['INDEX','RK','DATE','TYPE','TEAM','CONF.','OPPONENT','VENUE','RESULT','ADJ. O','ADJ. D','T','PPP','EFG%','TO%','REB%','FTR','PPP', 'EFG%','TO%','REB%','FTR','G-SC','+/-']
    return pd.DataFrame(all_lines, columns = columns)

def main(url):
    html_table = get_html_table(url)
    all_lines = raw_data_array(html_table)
    df = build_dataframe(all_lines)
    return df

if __name__ == "__main__":
    # I pulled all these urls for the specific dates according to wikipedia first and last games of the tournament
    tournament_urls = {2019:"http://barttorvik.com/gamestat.php?sIndex=0&year=2019&tvalue=All&cvalue=All&opcvalue=All&ovalue=All&minwin=All&mindate=03/19/19&maxdate=04/08/19&typev=All&venvalue=All&minadjo=0&minadjd=200&mintempo=0&minppp=0&minefg=0&mintov=200&minreb=0&minftr=0&minpppd=200&minefgd=200&mintovd=0&minrebd=200&minftrd=200&mings=0&mingscript=-100&maxx=100&coach=All&opcoach=All&adjoSelect=min&adjdSelect=max&tempoSelect=min&pppSelect=min&efgSelect=min&tovSelect=max&rebSelect=min&ftrSelect=min&pppdSelect=max&efgdSelect=max&tovdSelect=min&rebdSelect=max&ftrdSelect=max&gscriptSelect=min&sortToggle=0",
            2018:"http://barttorvik.com/gamestat.php?sIndex=0&year=2018&tvalue=All&cvalue=All&opcvalue=All&ovalue=All&minwin=All&mindate=03/15/18&maxdate=04/02/18&typev=All&venvalue=All&minadjo=0&minadjd=200&mintempo=0&minppp=0&minefg=0&mintov=200&minreb=0&minftr=0&minpppd=200&minefgd=200&mintovd=0&minrebd=200&minftrd=200&mings=0&mingscript=-100&maxx=100&coach=All&opcoach=All&adjoSelect=min&adjdSelect=max&tempoSelect=min&pppSelect=min&efgSelect=min&tovSelect=max&rebSelect=min&ftrSelect=min&pppdSelect=max&efgdSelect=max&tovdSelect=min&rebdSelect=max&ftrdSelect=max&gscriptSelect=min&sortToggle=0",
            2017:"http://barttorvik.com/gamestat.php?sIndex=0&year=2017&tvalue=All&cvalue=All&opcvalue=All&ovalue=All&minwin=All&mindate=03/14/17&maxdate=04/03/17&typev=All&venvalue=All&minadjo=0&minadjd=200&mintempo=0&minppp=0&minefg=0&mintov=200&minreb=0&minftr=0&minpppd=200&minefgd=200&mintovd=0&minrebd=200&minftrd=200&mings=0&mingscript=-100&maxx=100&coach=All&opcoach=All&adjoSelect=min&adjdSelect=max&tempoSelect=min&pppSelect=min&efgSelect=min&tovSelect=max&rebSelect=min&ftrSelect=min&pppdSelect=max&efgdSelect=max&tovdSelect=min&rebdSelect=max&ftrdSelect=max&gscriptSelect=min&sortToggle=0",
            2016:"http://barttorvik.com/gamestat.php?sIndex=0&year=2016&tvalue=All&cvalue=All&opcvalue=All&ovalue=All&minwin=All&mindate=03/15/16&maxdate=04/04/16&typev=All&venvalue=All&minadjo=0&minadjd=200&mintempo=0&minppp=0&minefg=0&mintov=200&minreb=0&minftr=0&minpppd=200&minefgd=200&mintovd=0&minrebd=200&minftrd=200&mings=0&mingscript=-100&maxx=100&coach=All&opcoach=All&adjoSelect=min&adjdSelect=max&tempoSelect=min&pppSelect=min&efgSelect=min&tovSelect=max&rebSelect=min&ftrSelect=min&pppdSelect=max&efgdSelect=max&tovdSelect=min&rebdSelect=max&ftrdSelect=max&gscriptSelect=min&sortToggle=0",
            2015:"http://barttorvik.com/gamestat.php?sIndex=0&year=2015&tvalue=All&cvalue=All&opcvalue=All&ovalue=All&minwin=All&mindate=03/17/15&maxdate=04/06/15&typev=All&venvalue=All&minadjo=0&minadjd=200&mintempo=0&minppp=0&minefg=0&mintov=200&minreb=0&minftr=0&minpppd=200&minefgd=200&mintovd=0&minrebd=200&minftrd=200&mings=0&mingscript=-100&maxx=100&coach=All&opcoach=All&adjoSelect=min&adjdSelect=max&tempoSelect=min&pppSelect=min&efgSelect=min&tovSelect=max&rebSelect=min&ftrSelect=min&pppdSelect=max&efgdSelect=max&tovdSelect=min&rebdSelect=max&ftrdSelect=max&gscriptSelect=min&sortToggle=0"}
    try:
        mkdir(mmpath+"/data/tournament-results/")
    except:
        pass
    for year in tournament_urls:
        df = main(tournament_urls[year])
        df.to_csv(mmpath+"/data/tournament-results/tournament"+str(year)+".csv", index=False)


