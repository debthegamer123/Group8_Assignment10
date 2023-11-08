# Name: Deborah Tekle and Sam Moushey Group 8
# email: Tekledh@mail.uc.edu 
# Assignment Title: Assignment 10
# Due Date: 11/09/2023
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description:Using Eclipse to create a PyDev project using an API.
# Citations: www.balldontlie.io
# Anything else that's relevant: N/A

import json
import requests # Web requests 

#Main.py
if __name__ == "__main__": # "Is this the entry point?"
    response = requests.get('https://www.balldontlie.io/api/v1/players')
    json_string = response.content
    
    parsed_json = json.loads(json_string) # Now we have a python dictionary
    
    #for players in parsed_json['data']:
        #print (players)
        
    players = parsed_json['data']

for player in players:
        first_name = player.get('first_name')
        last_name = player['last_name']
        team = player['team']['name']
        print(f"{first_name} {last_name}: {team}")  # Prints First name, last name : Team 