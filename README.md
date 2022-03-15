# DA-AJ2122
Databases advanced, webscraper, schooljaar 2021 - 2022, door Dylan Verniers

## Version
Version 0.2.0

## Info
This project consists of a realtime BTC-value scraper (webscraper_DV.py) as well as a realtime redis-cleaner (cleanpush.py)
There seem to be some issues with running those scripts on a virtual machine, so it is advised to run them on your own laptop/PC
They are proven to be working on Windows 10, 64-bit.

Before executing the scripts, make sure that; 
- mongodb is up and running (net start mongodb | CMD) 
(To install mongodb for windows use: https://medium.com/@LondonAppBrewery/how-to-download-install-mongodb-on-windows-4ee4b3493514)
- As well as your redis-client (sudo service redis-server start | Ubuntu Terminal)
(To download/consult docs Ubuntu terminal for windows use: https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-10#1-overview)
- Python packages redis and pymongo are installed
(! python -m pip install redis)
(! python -m pip install pymongo)

Every other library is probably already installed on your machine.
If not, use '! python -m pip install PACKAGENAME' to install it.

Since both scripts are an infinite while-loop, you have to forcefully terminate them yourself.
Don't worry, they are proven to be working at the same time.


## webscraper_DV.py
This script scrapes data of the website 'https://www.blockchain.com/btc/unconfirmed-transactions' in real-time.
The information is put in a dictionary / string and then cached in Redis.

The keys in Redis are given an age of 210 seconds, after that they are deleted.

## cleanpush_DV.py
This script cleans redis real-time, which was filled with data from the webscraper_DV.py
It searches for the highest BTC-value, and pushes it to mongoDB.

The MongoDB runs on your own device as well, on port 27017.
The keys in redis have an age of 210 seconds, but are also cleaned when they are checked by the script.