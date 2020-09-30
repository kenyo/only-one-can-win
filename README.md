## Forecasting Reddit Community Growth 

The goal of this project is to develop a time series forecasting model to predict how many reddit followers there will be for the subreddits belonging to each presidential candidate.

## Background

Reddit was founded in 2005 as a social news aggregation, web content rating, and discussion website. It touts itself as "the front page of the Internet". Each post on reddit belongs to a certain "subreddit" which is  a forum belonging to a certain topic (ie. Joe Biden). Further, posts receiving more positive votes (upvotes) appear closer to the top of the subreddit so redditors are more likely to see more popular/inluential posts.

I believe reddit is a good proxy for overall popularity because of its rich, vocal user base. Predicting the number of followers of each presidential candidate's subreddit can be used as a campaign tool to address growth/loss until November 3, 2020.

## Dataset

The primary dataset was compiled since August 10, 2020 and polled how many followers and active users belonged to the joebiden, donaldtrump, and kanye subreddits every half hour. In total, there were ~15k observations. Followers and subscribers are synonymous for all intents and purposes:

```
subscribers                   int64
active_user_count             int64
icon_img                     object
timestamp            datetime64[ns]
```

This data is stored on a Heroku instance running Postgresql. The steps to automate the data collection process [are detailed here](https://medium.com/@kennyoh517/diy-datasets-ba180658e9e7).

![joebiden](https://github.com/kenyo/final-project/blob/master/images/joebiden_df.png?raw=true)

![donaldtrump](https://github.com/kenyo/final-project/blob/master/images/donaldtrump_df.png?raw=true)

![kanye](https://github.com/kenyo/final-project/blob/master/images/kanye_df.png?raw=true)

To address the non-stationarity of the data, I differenced each time series once to produce the following dataframes:

![joebiden](https://github.com/kenyo/final-project/blob/master/images/joebiden_new_subs.png?raw=true)

![donaldtrump](https://github.com/kenyo/final-project/blob/master/images/donaldtrump_new_subs.png?raw=true)

![kanye](https://github.com/kenyo/final-project/blob/master/images/kanye_new_subs.png?raw=true)

After each timeseries was differenced they passed the Augmented Dickey Fuller test and modeling was performed on the differenced set.

## Process & Repository Contents

* Sourcing and Cleaning: 
  * main.py (main script to ping reddit api for follower counts)
  * cron.py (triggers main.py every half hour)
  * notebooks/eda.ipynb
* Modeling (in no particular order):
  * notebooks/joebiden_modeling.ipynb
  * notebooks/donaldtrump_modeling.ipynb
  * notebooks/kanye_modeling.ipynb

Modeling notebooks run the following models to improve upon the test RMSE (root mean squared error):

Baseline (training mean) => ARIMA(p,d,q) => fbprophet => darts

## Findings

joebiden and kanye subreddit ARIMA models performed best with RMSE's of 110.689 and 58.783 respectively. donaldtrump new subscribers were best modeled using fbprophet with and RMSE of 95.292

joebiden arima:

![joebiden](https://github.com/kenyo/final-project/blob/master/images/joebiden_arima.png?raw=true)

kanye arima:

![kanye](https://github.com/kenyo/final-project/blob/master/images/kanye_arima.png?raw=true)

donaldtrump fbprophet:

![donaldtrump](https://github.com/kenyo/final-project/blob/master/images/donaldtrump_fbprophet_.png?raw=true)

## Next Steps

* Explore exogenous variables via twitter in ARIMA models
  * see how number of twitter likes affects model
  * see how twiter sentiment for each candidate's tweets affect model
* Explore exogenous variables via polling data in ARIMA models
* Shut down automated data collection after election

