from urllib import *
from bs4 import BeautifulSoup
import csv

html = urlopen('http://messivsronaldo.net').read()
soup = BeautifulSoup(html)
#print soup.prettify()


def apps():      											#function to store appearances of Messi and Ronaldo in a list apps.
	apps = []

	for row in soup.find_all('li',{'class':'apps'}):
		for num in row.find_all('span',{'class':'num'}):
			apps.append(num.get_text())
			#apps.append(str(num.get_text()))
	tmp = str(','.join(apps))  								#This line and the line below it is used to convert the unicode characters to str. Similar result can be obtained from the line above that has been commented out.
	return tmp.split(',')
#print apps()

def assists():												#function to store assists of Messi and Ronaldo in a list assists.
	assists = []
	for row in soup.find_all('li',{'class':'assists'}):
		for num in row.find_all('span',{'class':'num'}):
			assists.append(num.get_text())
	tmp = str(','.join(assists))
	return tmp.split(',')
#print assists()

def goals():												#function to store goals of Messi and Ronaldo in a list goals.
	goals = []
	for row in soup.find_all('li',{'class':'goals'}):
		for num in row.find_all('span',{'class':'num'}):
			goals.append(num.get_text())
	tmp = str(','.join(goals))
	return tmp.split(',')
#print goals()

def messiApps():											#function to store appearances of Messi only in a list messiApps.
	messiApps = []
	for i in range(len(apps())):
		if i%2 == 0:
			messiApps.append(apps()[i])
	tmp = str(','.join(messiApps))
	return tmp.split(',')
#print messiApps()

def ronaldoApps():										   #function to store appearances of Ronaldo only in a list ronaldoApps.	
	ronaldoApps = []
	for i in range(len(apps())):
		if i%2 != 0:
			ronaldoApps.append(apps()[i])
	tmp = str(','.join(ronaldoApps))
	return tmp.split(',')
#print ronaldoApps()
	
def messiAssists():										  #funtion to store assists of Messi only in a list messiAssists.
	messiAssists = []
	for i in range(len(assists())):
		if i%2 == 0:
			messiAssists.append(assists()[i])
	tmp = str(','.join(messiAssists))
	return tmp.split(',')
#print messiAssists()

def ronaldoAssists():									 #function to store assists of Ronaldo only in a list ronaldoAssists.
	ronaldoAssists = []
	for i in range(len(assists())):
		if i%2 != 0:
			ronaldoAssists.append(assists()[i])
	tmp = str(','.join(ronaldoAssists))
	return tmp.split(',')
#print ronaldoAssists()

def messiGoals():										 #function to stoe goals of Messi only in a list messiGoals.
	messiGoals = []
	for i in range(len(goals())):
		if i%2 == 0:
			messiGoals.append(goals()[i])
	tmp = str(','.join(messiGoals))
	return tmp.split(',')
#print messiGoals()

def ronaldoGoals():										 #function to store goals on Ronaldo only in a list ronaldoGoals.
	ronaldoGoals = [] 
	for i in range(len(goals())):
		if i%2 != 0:
			ronaldoGoals.append(goals()[i])
	tmp = str(','.join(ronaldoGoals))
	return tmp.split(',')
#print ronaldoGoals()

def laLigaStats():                                    										  #function to store laliga statistics 
	messiapps = []
	messiassists = []
	messigoals = []
	ronaldogoals = []
	ronaldoassists = []
	ronaldoapps = []
	for index in range(1,len(messiApps()),4):
		messiapps.append(messiApps()[index])
		messiassists.append(messiAssists()[index])
		messigoals.append(messiGoals()[index])
		ronaldogoals.append(ronaldoGoals()[index])
		ronaldoassists.append(ronaldoAssists()[index])
		ronaldoapps.append(ronaldoApps()[index])
	return zip(messiapps,messiassists,messigoals,ronaldogoals,ronaldoassists,ronaldoapps)     #returns a list of tuples

def championsLeagueStats():                        											  #function to store champions league statistics.
	messiapps = []
	messiassists = []
	messigoals = []
	ronaldogoals = []
	ronaldoassists = []
	ronaldoapps = []
	for index in range(2,len(messiApps()),4):
		messiapps.append(messiApps()[index])
		messiassists.append(messiAssists()[index])
		messigoals.append(messiGoals()[index])
		ronaldogoals.append(ronaldoGoals()[index])
		ronaldoassists.append(ronaldoAssists()[index])
		ronaldoapps.append(ronaldoApps()[index])
	return zip(messiapps,messiassists,messigoals,ronaldogoals,ronaldoassists,ronaldoapps)   #returns a list of tuples
#print ligaStats()

def allCompetitionStats():																	 #fucntion to store statistics of all competitions.
	messiapps = []
	messiassists = []
	messigoals = []
	ronaldogoals = []
	ronaldoassists = []
	ronaldoapps = []
	for index in range(0,len(messiApps()),4):
		messiapps.append(messiApps()[index])
		messiassists.append(messiAssists()[index])
		messigoals.append(messiGoals()[index])
		ronaldogoals.append(ronaldoGoals()[index])
		ronaldoassists.append(ronaldoAssists()[index])
		ronaldoapps.append(ronaldoApps()[index])
	return zip(messiapps,messiassists,messigoals,ronaldogoals,ronaldoassists,ronaldoapps) 	 #returns a list of tuples

from pandas import DataFrame, read_csv
import pandas as pd
#goals = (zip(messiGoals(),ronaldoGoals()))
#print goals 

df_liga = pd.DataFrame(data=laLigaStats(),columns=['messiApps','messiAssists','messiGoals','ronaldoGoals','ronaldoAssists','ronaldoApps'])                   #creates a data frame called df_liga from laliga statistics.
df_cl = pd.DataFrame(data=championsLeagueStats(),columns=['messiApps','messiAssists','messiGoals','ronaldoGoals','ronaldoAssists','ronaldoApps'])            #creates a data fraome called df_cl from champions league statistics.
df_all = pd.DataFrame(data=allCompetitionStats(),columns=['messiApps','messiAssists','messiGoals','ronaldoGoals','ronaldoAssists','ronaldoApps'])            #creates a data frame called df_all from all competitions statistics.
#print df
df_liga.to_csv('la_liga.csv',index=True,header=True)                   #exports la_liga.csv from data frame df_liga
df_cl.to_csv('champions_league.csv',index=True,header=True)            #exports champions_league.csv from data frame df_cl
df_all.to_csv('all_competitions.csv',index=True,header=True)           #exports all_competitions.csv from data frame df_all







