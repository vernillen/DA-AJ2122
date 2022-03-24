###################################################################################################
## LIBRARY
###################################################################################################
import ast
from pymongo import MongoClient
import urllib.parse
import redis
import time

###################################################################################################
## MONGODB CREDENTIALS
###################################################################################################
username = urllib.parse.quote_plus('dylan')
password = urllib.parse.quote_plus('dylan')
client = MongoClient(f"mongodb://{username}:{password}@127.0.0.1:8080")

###################################################################################################
## ESTABLISH CONNECTION WITH REDIS
###################################################################################################
r = redis.Redis(host="localhost", port=8081)

###################################################################################################
## CLEANING + PUSH FUNCTION
## EXECUTE COMMAND FOR FUNCTION
###################################################################################################
def pushMongo():
    while 1:
        time.sleep(60)
        BTC = 0
        dict_save = {}

        for key in r.scan_iter():
            key = str(key)[2:-1:]
            test = str(r.get(key))[2:-1:]
            
            dict = ast.literal_eval(test)
            
            if dict["BTC-value"] > BTC:
                BTC = dict["BTC-value"]
                dict_save = dict
            
            r.delete(key)

        #Create new database / update existing
        hashes_db = client["Hashes"]
        col_hashes = hashes_db["Hashes"]

        try :
            if dict_save:
                x = col_hashes.insert_one(dict_save)
                print(x.inserted_id)
                print(dict_save)

                dict_save = {}
            else:
                pass
                        
        except :
            pass

pushMongo()