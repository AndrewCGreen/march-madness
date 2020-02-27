## March Madness Data Model

### Environment

Please use the environment specified in codebase

### Dataset

I think a good place to start is with the data scraped from Kaggle, 
https://www.kaggle.com/andrewsundberg/college-basketball-dataset/data

Soon I will scrape the 2019-2020 season info and attempt to get it into the same format
that way we can have some good test data - and actually run the model, lol

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
