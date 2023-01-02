import requests
from bs4 import BeautifulSoup
import csv

# Make a request to the webpage
url = "https://www.forebet.com/en/football-predictions/predictions-1x2/2022-12-31"
page = requests.get(url)
print(page)
soup = BeautifulSoup(page.content, "html.parser")
lists = soup.find_all('div', class_="rcnt tr_0")
for list in lists:
    try:
        awayteam = list.find('span', class_='awayTeam').text
        hometeam = list.find('span', class_='homeTeam').text
        Score = list.find('b', class_="l_scr").text
        correct_score = list.find('div', class_="ex_sc exact_yes tabonly").text
        avg_goals = list.find('div', class_="avg_sc exact_yes tabonly").text
        info = [awayteam, hometeam, avg_goals, Score, correct_score]
        print(info)
    except:
        print("error")

print("for ex_sc tabonly")
print("=============")

for list in lists:
    try:
        awayteam = list.find('span', class_='awayTeam').text
        hometeam = list.find('span', class_='homeTeam').text
        Score = list.find('b', class_="l_scr").text
        correct_score = list.find('div', class_="ex_sc tabonly").text
        avg_goals = list.find('div', class_="avg_sc tabonly").text
        info = [awayteam, hometeam, avg_goals, Score, correct_score]
        print(info)
    except:
        print("error")


print("=======----======")

for list in lists:
    try:
        awayteam = list.find('span', class_='awayTeam').text
        hometeam = list.find('span', class_='homeTeam').text
        Score = list.find('b', class_="l_scr").text
        correct_score = list.find('div', class_="ex_sc exact_yes tabonly").text
        avg_goals = list.find('div', class_="avg_sc tabonly").text
        info = [awayteam, hometeam, avg_goals, Score, correct_score]
        print(info)
    except:
        print("error")


print("=======----======")

for list in lists:
    try:
        awayteam = list.find('span', class_='awayTeam').text
        hometeam = list.find('span', class_='homeTeam').text
        Score = list.find('b', class_="l_scr").text
        correct_score = list.find('div', class_="ex_sc tabonly").text
        avg_goals = list.find('div', class_="avg_sc exact_yes tabonly").text
        info = [awayteam, hometeam, avg_goals, Score, correct_score]
        print(info)
    except:
        print("error")
