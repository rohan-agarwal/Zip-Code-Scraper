#init
import urllib2
from bs4 import BeautifulSoup
import pandas

#initializing what will be a data frame
rows_list=[]
#inputting list of zip codes to collect data from
zipcodelist = pandas.read_csv('C:\Users\Dell_PC\Desktop\zipcode.csv')

#for loop to iterate over every zip code
for x in range(0,len(zipcodelist['zipcode'])):

	#collecting and parsing data
	currentzip = str(zipcodelist['zipcode'][x])
	site = 'http://zipskinny.com/index.php?zip=' + currentzip
	req = urllib2.Request(site)
	response = urllib2.urlopen(req)
	page = response.read()
	soup = BeautifulSoup(page)
	text = soup.get_text()

	#using substrings to parse the text
	if 'General Information' in text:

		populationlocation = text.find('Population')
		population = str(
			text[populationlocation+12:populationlocation+17])

		highschoollocation = text.find('High school or higher')
		highschool = str(
			text[highschoollocation+23:highschoollocation+27])

		bachelorslocation = text.find('Bachelors or higher')
		bachelors = str(
			text[bachelorslocation+21:bachelorslocation+25])

		nevermarriedlocation = text.find('Never married')
		nevermarried = str(
			text[nevermarriedlocation+15:nevermarriedlocation+19])

		marriedlocation = text.find('Married')
		married = str(
			text[marriedlocation+9:marriedlocation+13])

		undertenlocation = text.find('<$10')
		underten = str(
			text[undertenlocation+9:undertenlocation+12])

		tentofourteenlocation = text.find('10,000-$14')
		tentofourteen = str(
			text[tentofourteenlocation+15:tentofourteenlocation+18])

		fifteentotwentyfivelocation = text.find('15,000')
		fifteentotwentyfive = str(
			text[fifteentotwentyfivelocation+15:fifteentotwentyfivelocation+18])

		twentyfivetothirtyfivelocation = text.find('25,000')
		twentyfivetothirtyfive = str(
			text[twentyfivetothirtyfivelocation+15:twentyfivetothirtyfivelocation+18])

		thirtyfivetofiftylocation = text.find('35,000')
		thirtyfivetofifty = str(
			text[thirtyfivetofiftylocation+15:thirtyfivetofiftylocation+19])

		fiftytoseventyfivelocation = text.find('50,000')
		fiftytoseventyfive = str(
			text[fiftytoseventyfivelocation+15:fiftytoseventyfivelocation+19])

		seventyfivetoninetyninelocation = text.find('75,000')
		seventyfivetoninetynine = str(
			text[seventyfivetoninetyninelocation+15:seventyfivetoninetyninelocation+19])

		hundredtoonefiftylocation = text.find('100,000')
		hundredtoonefifty = str(
			text[hundredtoonefiftylocation+17:hundredtoonefiftylocation+21])

		onefiftytooneninetyninelocation = text.find('150,000')
		onefiftytooneninetynine = str(
			text[onefiftytooneninetyninelocation+17:onefiftytooneninetyninelocation+20])

		twohundredpluslocation = text.find('200,000')
		twohundredplus = str(
			text[twohundredpluslocation+9:twohundredpluslocation+12])

		unemployedlocation = text.find('Unemployed')
		unemployed = str(
			text[unemployedlocation+11:unemployedlocation+14])

		belowpovertylinelocation = text.find('Below Poverty Line')
		belowpovertyline = str(
			text[belowpovertylinelocation+19:belowpovertylinelocation+22])

		hispaniclocation = text.find('Hispanic')
		hispanic = str(
			text[hispaniclocation+17:hispaniclocation+20])

		whitelocation = text.find('White*')
		white = str(
			text[whitelocation+8:whitelocation+12])

		blacklocation = text.find('Black*')
		black = str(
			text[blacklocation+8:blacklocation+11])

		asianlocation = text.find('Asian*')
		asian = str(
			text[asianlocation+8:asianlocation+11])

		otherlocation = text.find('Other*')
		other = str(
			text[otherlocation+8:otherlocation+11])

		malelocation = text.find('Male:')
		male = str(
			text[malelocation+5:malelocation+9])

		femalelocation = text.find('Female:')
		female = str(
			text[femalelocation+7:femalelocation+10])

		#creating a dictionary out of all of the information	
		dict1 = dict([
			('Zip Code', currentzip), 
			('Population', population), 
			('High School or Higher', highschool), 
			('Bachelors or higher', bachelors), 
			('Never married', nevermarried), 
			('Married', married), 
			('<10', underten), 
			('10-14', tentofourteen), 
			('15-25', fifteentotwentyfive), 
			('25-35', twentyfivetothirtyfive), 
			('35-50', thirtyfivetofifty), 
			('50-75', fiftytoseventyfive), 
			('75-99', seventyfivetoninetynine), 
			('100-149', hundredtoonefifty), 
			('150-199', onefiftytooneninetynine), 
			('200+', twohundredplus), 
			('Unemployed', unemployed), 
			('Below Poverty Line', belowpovertyline), 
			('Hispanic', hispanic), 
			('White', white), 
			('Black', black), 
			('Asian', asian), 
			('Other', other), 
			('Percent Male', male), 
			('Percent Female', female)])

		#adding list to array of rows
		rows_list.append(dict1)

#creating a data frame out of all of the lists
df = pandas.DataFrame(rows_list)

#output to csv
df.to_csv('C:\Users\Dell_PC\Desktop\zipcoderesults.csv')