import unittest
from tweets.data4tweets import Data4Tweets

class Test(unittest.TestCase):

    def test_getTweets_without_params(self):
        
        test = Data4Tweets("Pokemon")
        expr = True

        if  len(test.getTweets()) == 0:
            expr = False

        self.assertEqual(expr, True, "Should generate data")

    def test_getTweets_with_params(self):
        
        test = Data4Tweets("Pokemon",isverified=False,isretweet=False,hasmedia=False,haslinks=False)
        expr = True

        if  len(test.getTweets()) == 0:
            expr = False

        self.assertEqual(expr, True, "Should generate data")
    
    def test_countTweets(self):
        
        test = Data4Tweets("Pokemon")
        expr = True

        if  test.countTweets() == 0:
            expr = False

        self.assertEqual(expr, True, "Should generate data")

if __name__ == '__main__':
    unittest.main()