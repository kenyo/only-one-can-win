## Forecasting Reddit Community Growth 

The goal of this project is to develop a time series forecasting model to predict how many reddit followers there will be for the subreddits belonging to each presidential candidate.

## Background

Reddit was founded in 2005 as a social news aggregation, web content rating, and discussion website. It touts itself as "the front page of the Internet". Each post on reddit belongs to a certain "subreddit" which is  a forum belonging to a certain topic (ie. Joe Biden). Further, posts receiving more positive votes (upvotes) appear closer to the top of the subreddit so redditors are more likely to see more popular/inluential posts.

I believe reddit is a good proxy for overall popularity because of its rich, vocal user base. Predicting the number of followers of each presidential candidate's subreddit can be used as a campaign tool to address growth/loss until November 3, 2020.

## Dataset

The primary dataset was compiled since August 10, 2020 and polled how many followers and active users belonged to the joebiden, donaldtrump, and kanye subreddits every half hour. Followers and subscribers are synonymous for all intents and purposes:

```
subscribers                   int64
active_user_count             int64
icon_img                     object
timestamp            datetime64[ns]
```

This data is stored on a Heroku instance running Postgresql.

![joebiden](https://github.com/kenyo/final-project/tree/master/images/joebiden_df.png)
![donaldtrump](https://github.com/kenyo/final-project/tree/master/images/donaldtrump_df.png)

![kanye](https://github.com/kenyo/final-project/tree/master/images/kanye_df.png)



