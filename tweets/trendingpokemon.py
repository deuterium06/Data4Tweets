import pandas as pd
import random
import requests
import yaml
import urllib.parse
from tweets.data4tweets import Data4Tweets
import time 

POKEMON_CSV = 'https://gist.githubusercontent.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6/raw/92200bc0a673d5ce2110aaad4544ed6c4010f687/pokemon.csv'

class TrendingPokemon:

    def __init__(self, pokemonName=None):
        self.pokemon = pokemonName
        
        pokelist = pd.read_csv(POKEMON_CSV)
        self.pokemonList = list(pokelist.Name)

    def verifyPokemon(self):

        if self.pokemon in self.pokemonList:
            return True
        return False

    def countPokemon(self):
        
        if self.pokemon is None:
        
            pokeTweetCount = dict()

            for p in random.sample(self.pokemonList,5):
            
                if "Mega" not in p:

                    count = Data4Tweets(p).countTweets()
                    pokeTweetCount[p] = count

                time.sleep(0.25)
        
            return pokeTweetCount
        
        else:
            
            if self.verifyPokemon() == True:
                tweetCount = Data4Tweets(self.pokemon).countTweets()
            else:
                tweetCount = -1

            return tweetCount

if __name__ == '__main__':
    TrendingPokemon()