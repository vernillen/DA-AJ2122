###################################################################################################
## LIBRARY
###################################################################################################
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import redis
import json

###################################################################################################
## FUNCTIONS
###################################################################################################

def searchHTML(URL):
    #Request HTML & beautify it
    page = requests.get(URL)
    soup = bs(page.content)
    
    #Find right data
    results_numbers = soup.find_all("span", {'class' : 'sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC'})
    results_hash = soup.find_all("a", {'class' : 'sc-1r996ns-0 fLwyDF sc-1tbyx6t-1 kCGMTY iklhnl-0 eEewhk d53qjk-0 ctEFcK'})
    
    return results_numbers, results_hash

def makeFrame(hash, time, BTC, USD):
    dataF = {'_id' : hash, 'Time' : time, 'BTC-value' : BTC, 'USD-value' : USD}
    frameUpdate = pd.DataFrame(dataF)
    
    #Cleanen van database
    frameUpdate['BTC-value'] = frameUpdate['BTC-value'].map(lambda x: x.rstrip(' BTC'))
    frameUpdate['BTC-value'] = frameUpdate['BTC-value'].str.replace(r'\,', '')

    frameUpdate['USD-value'] = frameUpdate['USD-value'].map(lambda x: x.lstrip('$'))
    frameUpdate['USD-value'] = frameUpdate['USD-value'].str.replace(r'\,', '')

    frameUpdate['USD-value'] = frameUpdate['USD-value'].astype('float')
    frameUpdate['BTC-value'] = frameUpdate['BTC-value'].astype('float')
    
    return frameUpdate

def makeArrays(numbers, hash):
    only_time = [content.get_text() for content in numbers[0::3]]
    only_BTC = [content.get_text() for content in numbers[1::3]]
    only_USD = [content.get_text() for content in numbers[2::3]]
    only_hash = [content.get_text() for content in hash]
    
    return only_hash, only_time, only_BTC, only_USD

def fetchCurrent(URL):
    #HTML-doorzoeken en alles ophalen
    numbers, hash = searchHTML(URL)

    #Make arrays of only required values
    only_hash, only_time, only_BTC, only_USD = makeArrays(numbers, hash)

    #Make dataframe
    frame = makeFrame(only_hash, only_time, only_BTC, only_USD)
    
    return frame


###################################################################################################
## ESTABLISH CONNECTION WITH REDIS
## FLUSHDB IN CASE NOT EMPTY (safeguard)
###################################################################################################
r = redis.Redis()
r.flushdb()

###################################################################################################
## FUNCTION COMPILER
## EXECUTE COMMAND FOR FUNCTION
###################################################################################################
def fillRedis():     
    while 1:
        URL = "https://www.blockchain.com/btc/unconfirmed-transactions"
        frame_new = fetchCurrent(URL)
        
        js = frame_new.to_dict(orient="records")
        
        for element in js: 
            r.set(element["_id"], json.dumps(element), ex=210)


fillRedis()