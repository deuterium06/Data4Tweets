import pandas as pd
import requests
import yaml
import os
from tweets.utils.helper import searchTweetParser
from tweets.utils.constant import DEV_ENV, TEST_ENV

ENV = os.getenv('ENV')

class Data4Tweets:

    def __init__(self, query="query", *args, **kwargs):
        self.query = query
        self.__creds = {}

        if ENV == TEST_ENV:
            
            self.__creds = {'bearer': str(os.environ.get('BEARER'))}

        else:

            try:
                with open("credentials.yml", "r") as stream:
                    self.__creds = yaml.safe_load(stream)['credentials']
            except FileNotFoundError as fnf_error:
                print(fnf_error)

    def getTweets(self, language='en', source=None, isverified=None, isretweet=None, hasmedia=None,haslinks=None):
        
        parameters = {'lang':language, 'from':source,
            'is:verified':isverified, 'is:retweet':isretweet,'has:media':hasmedia, 'has:links':haslinks}
 
        headers = {"Authorization": "Bearer " + self.__creds['bearer']}

        payload = dict()
        payload['max_results'] = 100
        payload['tweet.fields'] = 'created_at'
        payload['expansions'] = 'author_id'
 
        url = 'https://api.twitter.com/2/tweets/search/recent?query=' + self.query + searchTweetParser(parameters)
        response = requests.get(url, headers=headers, params=payload)

        if response.status_code != 200:
            print(response.text)
            return
 
        data = [dict((response.json()))]

        return data
    
    def countTweets(self):
        
        headers = {"Authorization": "Bearer " + self.__creds['bearer']}

        payload = dict()
        payload['query'] = self.query

        url = 'https://api.twitter.com/2/tweets/counts/recent'
        response = requests.get(url, headers=headers, params=payload)
        
        if response.status_code != 200:
            print(response.text)
            return
        
        data = response.json()['meta']['total_tweet_count']

        return data

    def toDataframe(self):

        try:
            df = pd.DataFrame.from_dict(self.getTweets())        

            df.to_csv('data.csv', index=False)
            print("A CSV copy has been saved in your local folder.")
 
        except Exception as e:
            print("The error is: ", e)

if __name__ == '__main__':
    Data4Tweets()