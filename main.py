from datetime import datetime

import os
import praw
import psycopg2

reddit = praw.Reddit(client_id=os.getenv("REDDIT_CLIENT_ID"),
                     client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
                     user_agent="ds-final-project")

conn = psycopg2.connect(host=os.getenv('DB_HOST'),
                        port=os.getenv('DB_PORT'),
                        user=os.getenv('DB_USER'),
                        password=os.getenv('DB_PASSWORD'),
                        database=os.getenv('DB_DATABASE'))



def cronjob():
    """
    Main cron job.
    The main cronjob to be run continuously.
    """
    k = reddit.subreddit('kanye')

    cursor = conn.cursor()
    cursor.execute("INSERT INTO subreddits(display_name, subscribers,  active_user_count, timestamp) VALUES(%s, %s, %s, %s)",
        (k.display_name, k.subscribers, k.active_user_count, datetime.now()))
    conn.commit()
    cursor.close()

    print("Tick! The time is: %s" % datetime.now())
