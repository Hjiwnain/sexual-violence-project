import snscrape.modules.twitter as sntwitter
import pandas as pd

# query = "(#ghana #africa OR #rape OR #sexualassault OR #metoo OR #rapesurvivor OR #sexualabuse OR #survivor OR #sexualviolence OR #stoprape OR #stoprapeculture OR #believesurvivors OR #endrapeculture OR #WhyIDidntReport OR #RapeMustFall OR #Justice4Her OR #NoMore) until:2022-10-31 since:2017-01-01"
# tweets = []
# limit = 500000

# query = "(#rape OR #sexualassault OR #rapesurvivor OR #sexualabuse OR #sexualviolence OR #stoprape OR #stoprapeculture OR #believesurvivors OR #endrapeculture OR #whyididntreport OR #rapemustfall OR #justice4her)"
# tweets = []
# limit = 5000

query = "(#whyididntreport OR #IDidNotReport OR #ididnotreport OR #IDidntReport OR #ididntreport OR #WhyIDidNotReport) until:2022-10-31 since:2020-01-01"
tweets = []
limit = 50000


for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content])

    # print(vars(tweet))
        
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
print(df)

# to save to csv
df.to_csv('tweets_with_snscrape_20-22.csv')