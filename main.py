from datetime import datetime
import sys
import requests
import schedule
import colorama
import time
import random
from termcolor import colored
import json
from termcolor import cprint 
from pyfiglet import figlet_format
#-------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------INSTRUCTIONS--------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------
#install the above libraries by using the command below | make sure you are in the right directory in your cmd line

#must have discord account on developer mode to send messages with your account
#steps to get payload and header dict info 
#open discord in web mode
#inspect source and go to channel you want messages sent in
#send on message in channel then look on network tab of inspect source then look for messages under name
#click it to display header info 
#the request url first one under general is your request url
#scroll down to request headers and select authorization this is your auth request header 
#enter in your messages in words.txt then run in cmd line or a ide and will run continsouly until stopped
#set delay in seconds and logs of messages sent will appear in the msglogs.txt
#edit settings in the settings.json file for it to run smoothly
#-------------------------------------------------------------------------------------------------------------------
cprint(figlet_format('meta', font='isometric1'),
       'blue', attrs=['bold'])
print(colored('Enter 1 to Start', 'blue'))
print(colored('Enter 3 for settings', 'blue'))
print(colored('Enter 6 to Exit', 'blue'))
user_input = int(input(colored('Enter your choice: ', 'blue')))
if user_input == 1:
    print(colored('\nDelay settings in seconds', 'blue'))
    print(colored('Enter the delay range you want(ex. 2 3 will do every 2-3 seconds)','blue'))
    delay_inputR1 = int(input(colored('Enter the min delay: ', 'blue')))
    delay_inputR2 = int(input(colored('Enter the max delay: ', 'blue')))
    cprint(figlet_format('logz', font='isometric1'),
       'blue', attrs=['bold'])
    print(colored('-----------------------------------------------------------------------','blue'))
    def bumpz():
        with open('words.txt') as f:
            lines = f.readlines()
        with open('settings.json', 'r') as jett:
            data = jett.read()
        obje = json.loads(data)

        payload = {
            'content': str(random.choice(lines))
        }
    
        header = {
            #request header authorization goes here
            'authorization': str(obje['auth'])
        }
        #message request url
        r = requests.post(obje['requestURL'], data = payload, headers = header)
        #logs to text file 
        with open('msglogs.txt', 'a') as f:
            #prints the log to text file with new line after each log
            f.write('[LOGS] Message time stamp: ' + str(datetime.now().replace(microsecond=0)) + " | Message sent: " + payload['content'])    
        #printing bump logs to console
        print(colored('[LOGS] Message time stamp: ' + str(datetime.now().replace(microsecond=0)) + " | Message sent: " + payload['content'], 'green'))

    #randomizes every 123 to 150 minutes which is a bout 2 - 2/12 hrs 
    schedule.every(delay_inputR1).to(delay_inputR2).seconds.do(bumpz)

    while True:
        schedule.run_pending()
        time.sleep(1)
if user_input == 3:
    sys.exit()

if user_input == 6:
    sys.exit()


