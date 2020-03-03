#This file will be used to scrape this season's data
import pandas as pd
from requests import get
from bs4 import BeautifulSoup
from os import environ

mmpath = environ["MMPATH"]

def pull_html (url) -> []:
    """Pulls the raw html we need in a list of html elements"""
    response = get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    html_lines = soup.findAll("tr")
    return html_lines

def raw_data_array(html_lines) -> [[]]:
    """Takes the html and parses out the actual data elements we need"""
    all_lines = []
    for line in html_lines[2:]:
        new_line = []
        for element in line.find_all('td')[1:]:
            new_line.append(element.get_text())
        all_lines.append(new_line)
    return all_lines

def build_dataframe(all_lines) -> pd.DataFrame:
    """Uses raw elements and puts them into a dataframe with the headers we have been using as convention"""
    columns = ['TEAM','CONF','G','W','ADJOE','ADJDE','BARTHAG','EFG_O','EFG_D','TOR',
           'TORD','ORB','DRB','FTR','FTRD','2P_O','2P_D','3P_O','3P_D','ADJ_T','WAB']
    return pd.DataFrame(all_lines, columns = columns)

def main(url):
    html_lines = pull_html(url)
    all_lines = raw_data_array(html_lines)
    df = build_dataframe(all_lines)
    return df

if __name__ == "__main__":
    url = "http://barttorvik.com/trank.php#"
    df = main(url)
    df.to_csv(mmpath+"/data/kaggle-data/cbb20.csv", index=False)
