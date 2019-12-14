import requests
from bs4 import BeautifulSoup
import json

def parse(url,state):
    #Created the specific state file
    f_open = open('State_{}.csv'.format(state.upper()),'w')
    #parse the content of the url
    page = requests.get(url = url)
    #Make that content into html form
    soup = BeautifulSoup(page.content, 'html.parser')
    #Viewed the source page of the file and saw that table are written inside stateTable class, so used that to find all the rows
    tb = soup.find('table', class_='statTable')
    count = 1
    string = ''
    for link in tb.find_all('td'): #Used table data tags to get the required line
        name = link.find('a') #filtered by tags <a href = '' title = 'Zip code '/a><a href = " " title = 'Town' '/a'><a href =" "  title = "City" /a>
        if(str(name) == 'None'):
            continue
        else:
            # forming the csv type line including zip_code,town,city and writing into the file opened specific to that state
            count +=1
            if(count == 2):
                zip_code = name.get_text('title').split(" ")[2]
                string += zip_code+","
            else:
                string += name.get_text('title')+","
        if(count == 4):
            count = 1
            f_open.write(string)
            string = ''
            f_open.write('\n')
    #closing the file and moving on next state
    f_open.close()



#Created URL.txt using output.txt which has abbreviations for all states in USA.
'''
url = "https://www.zip-codes.com/state/"
fp = open('urls.txt','w')
for i in open('output.txt','r'):
    i = i.replace("\n","").lower()
    state  = url+i+".asp"+","+i
    fp.write(state)
    fp.write('\n')

fp.close()
'''


#Used urls.txt and passed the arguments of url and state to parse func
for i in open('urls.txt','r'):
    tokens = i.split(",")
    url = tokens[0]
    state = tokens[1].replace("\n","")
    parse(url,state)
    


    


