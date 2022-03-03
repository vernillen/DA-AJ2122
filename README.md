# DA-AJ2122
Databases advanced, webscraper, schooljaar 2021 - 2022, door Dylan Verniers

## Realtime BTC-transaction scraper
The BTC-transaction scraper scrapes real-time data of (un)confirmed BTC-transactions.
It stores hashes, time, BTC-value and USD-value of all those transactions per second.

### Virtual Machine
The scraper runs on Ubuntu software, on a virtual machine with Windows 2019 64-bit hardware.
The Ubuntu is download from the wegpage of ubuntu.com (https://ubuntu.com/download/desktop).
Ubuntu version 20.04.4 LTS.

The virtual machine is run on Virtual Box (https://www.virtualbox.org/)
More in-depth specifics for the Virtual machine are:
+ Installed Guest software
+ Bi-directional clipboard and copy & paste
+ 2048 MB of basic memory
+ 1CPU
+ 128MB Video memory
+ 1 Monitor
+ 50 GB dynamic memory
+ Bridged adapter

### Explanation of the script
The scripts uses the following libraries
+ import requests
+ from bs4 import BeautifulSoup as bs
+ import pandas as pd
+ import json

+ from pymongo import MongoClient
+ import urllib.parse

+ import urllib.parse

The website that is being scraped every second is: https://www.blockchain.com/btc/unconfirmed-transactions
This site contains real-time data of every BTC-transaction, although (un)confirmed.
Every second the webpage is scraped, put into a dictionary (json-string doesn't work!) and pushed to a local mongoDB

### Version
Version 0.1.0