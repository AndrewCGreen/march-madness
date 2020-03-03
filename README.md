## March Madness Predictive Model

### Environment

Please use the environment specified in codebase

### Dataset

#### Kaggle Seasons 2015-2019:
I think a good place to start is with the data scraped from Kaggle, 
https://www.kaggle.com/andrewsundberg/college-basketball-dataset/data

I would just plop this in a folder `march-madness/data/kaggle-data/` for now

#### Kaggle Season 2020:
In order to get the data for the 2020 season so far, navigate to `codebase/data-scrape/` 
and then run `python Scrape2020.py` upon doing so the file cbb20.csv will appear in `data/kaggle-data/`

#### Historical Bracket Data:
I colleceted all games in the time period of each march madness tournament, and that can be pulled by running `python Historical-Bracket-Data.py` in `codebase/data-scrape/` this will create a subfolder in your data folder called tournament-results with all results from 2015-1019

#### Other:
I am still looking for more comprehensive datasets, might have to shell out some money for that
I might need to find a vegas dataset, look at strategy #3 for why

### Strategy

My hypothesis is that there are really three approaches here:

1) Play the bracket:
    - Basically break down what matchups in the past have been most successful 
    i.e. how often has a 5 seed beaten a 12 seed in the first round
2) Play the teams:
    - Based on the season performance of a team, how likely are they to beat their opponent
    i.e. based on the datset Georgetown is most likely to beat Syracuse becaue of, well math, im not there yet
3) Play Vegas:
    - For this I would need another dataset, to see how money is moving in vegas
    - Basically if the line moves one way that would show that the public and vegas are prepareing for a particular outcome
    i.e. if the line moved in the Georgetown v. Syracuse game against Georgetown's favor, then it is more likely Georgetown will win

My hope is that this will end up being an ensamble model, as all rounds after the first are inherently unpredictable
so to fill out a good bracket, the first round would be based on teams and vegas, then the next rounds would have to rely somewhat on the bracket
Just a hypothesis, this is all subject to change.
