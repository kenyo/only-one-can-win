from datetime import datetime

import os
import praw
import psycopg2

reddit = praw.Reddit(client_id=os.getenv("REDDIT_CLIENT_ID"),
                     client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
                     user_agent="ds-final-project")

if bool(os.getenv('IS_PROD')) == True:
    conn = psycopg2.connect(os.getenv('DATABASE_URL'), sslmode='require')
else:
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

    track_subreddits = [
        'kanye',
        'donaldtrump',
        'JoeBiden',
        'JoeBidenSucks',
        'KanyeWestForPresident'
    ]

    for t in track_subreddits:

        s = reddit.subreddit(t)

        cursor = conn.cursor()
        cursor.execute("INSERT INTO subreddits(display_name, subscribers,  active_user_count, timestamp) VALUES(%s, %s, %s, %s)",
            (s.display_name, s.subscribers, s.active_user_count, datetime.now()))
        conn.commit()
        cursor.close()

    print("Tick! The time is: %s" % datetime.now())
