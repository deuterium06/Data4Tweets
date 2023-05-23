import urllib.parse

def searchTweetParser(dict1):
    
    ''' helper function to parse query params into HTTP url format ''' 
    
    parsed = ''
    for key, value in dict1.items():

        if ':' not in key.lower(): 

            if value is not None:
                parse = urllib.parse.quote(" " + key + ":" + value)
        
        else:

            if value is not None:
                if value == True:
                    parse = urllib.parse.quote(" " + key)
                elif value == False:
                    parse = urllib.parse.quote(" -" + key)
        
        parsed += parse
    
    return parsed