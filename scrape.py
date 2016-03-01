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

#print len(messiApps())
'''
messiApps = ['14', '9', '2', '3', '57', '38', '13', '6', '46', '31', '7', '8', '50', '32', '11', '7', '60', '37', '11', '12', '55', '33', '13', '9', '53', '35', '11', '7', '51', '31', '12', '8', '40', '28', '9', '3', '36', '26', '5', '5', '25', '17', '6', '2', '9', '7', '1', '1', '/', '/', '/', '/', '/', '/', '/', '/', '335', '215', '68', '52']
messiAssists = ['4', '3', '1', '0', '27', '18', '5', '4', '14', '11', '0', '3', '15', '12', '2', '1', '29', '16', '5', '8', '23', '18', '3', '2', '11', '10', '0', '1', '17', '11', '5', '1', '13', '12', '1', '0', '3', '2', '0', '1', '3', '0', '1', '2', '0', '0', '0', '0', '/', '/', '/', '/', '/', '/', '/', '/', '123', '88', '16', '19']
messiGoals = ['9', '4', '2', '3', '58', '43', '10', '5', '41', '28', '8', '5', '60', '46', '8', '6', '73', '50', '14', '9', '53', '31', '12', '10', '47', '34', '8', '5', '38', '23', '9', '6', '16', '10', '6', '0', '17', '14', '1', '2', '8', '6', '1', '1', '1', '1', '0', '0', '/', '/', '/', '/', '/', '/', '/', '/', '341', '236', '62', '43']
ronaldoGoals = ['17', '10', '7', '0', '61', '48', '10', '3', '51', '31', '17', '3', '55', '34', '12', '9', '60', '46', '10', '4', '53', '40', '6', '7', '33', '26', '7', '0', '26', '18', '4', '4', '42', '31', '8', '3', '23', '17', '3', '3', '12', '9', '1', '2', '9', '5', '0', '4', '6', '4', '0', '2', '5', '3', '0', '2', '330', '235', '69', '26']
ronaldoAssists = ['5', '3', '2', '0', '21', '16', '3', '2', '14', '9', '4', '1', '12', '10', '1', '1', '15', '12', '3', '0', '15', '10', '4', '1', '7', '7', '0', '0', '9', '6', '2', '1', '7', '6', '1', '0', '15', '9', '5', '1', '8', '6', '1', '1', '8', '3', '2', '3', '7', '4', '0', '3', '7', '6', '1', '0', '89', '67', '17', '5']
ronaldoApps = ['19', '14', '5', '0', '54', '35', '12', '7', '47', '30', '11', '6', '55', '34', '12', '9', '55', '38', '10', '7', '54', '34', '12', '8', '35', '29', '6', '0', '53', '33', '12', '8', '49', '34', '11', '4', '53', '34', '11', '8', '47', '33', '8', '6', '50', '33', '8', '9', '40', '29', '5', '6', '31', '25', '3', '3', '319', '214', '68', '37']
'''
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







