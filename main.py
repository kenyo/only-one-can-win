from datetime import datetime

import praw

reddit = praw.Reddit(client_id="wz4HVmg9UsLO-Q",
                     client_secret="kAw1q2FhpRwkZCpFRgKFnW2h3Fg",
                     user_agent="ds-final-project")

def cronjob():
    """
    Main cron job.
    The main cronjob to be run continuously.
    """
    print(reddit.subreddit('kanye').active_user_count)
    print("Tick! The time is: %s" % datetime.now())
