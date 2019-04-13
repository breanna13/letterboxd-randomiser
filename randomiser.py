#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import requests
import time
from datetime import date
import sys
import re
from bs4 import BeautifulSoup

class Page():
	def __init__(self, url):
		self.url = url
		self.page = None
		self.soup = None
		self.year = 0
		self.ready = False
	def Load(self):
		self.page = requests.get(self.url)
		self.soup = BeautifulSoup(self.page.text,'html.parser')
		self.ready = True

class Film():
	def __init__(self, name, rating, year):
		self.name = name
		self.rating = rating
		self.year = year
	def Stars(self):
		star = '★'
		half = '½'
		ratingHalf = int(self.rating / 2)
		starRating = ''
		for i in range(0, ratingHalf):
			starRating += star
		if(ratingHalf * 2 != self.rating):
			starRating += half
		return starRating
		
# Parameters
userName = ''
outPath = ''
yearMode = False

# Argument handling
#	 0		1	2	3
# python letterboxd.py username outpath year?
ArgCount = len(sys.argv)

if(ArgCount >= 2):#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import requests
import time
from datetime import date
import sys
import re
from bs4 import BeautifulSoup

class Page():
	def __init__(self, url):
		self.url = url
		self.page = None
		self.soup = None
		self.year = 0
		self.ready = False
	def Load(self):
		self.page = requests.get(self.url)
		self.soup = BeautifulSoup(self.page.text,'html.parser')
		self.ready = True

class Film():
	def __init__(self, name, rating, year):
		self.name = name
		self.rating = rating
		self.year = year
	def Stars(self):
		star = '★'
		half = '½'
		ratingHalf = int(self.rating / 2)
		starRating = ''
		for i in range(0, ratingHalf):
			starRating += star
		if(ratingHalf * 2 != self.rating):
			starRating += half
		return starRating
		
# Parameters
userName = ''
outPath = ''
yearMode = False

# Argument handling
#	 0		1	2	3
# python letterboxd.py username outpath year?
ArgCount = len(sys.argv)

if(ArgCount >= 2):
	userName = str(sys.argv[1])
else:
	userName = input('Please enter a Username : ')
	listName = input('Please enter a list : ')
if(ArgCount >= 3):
	outPath = sys.argv[2]
if(ArgCount >= 4):
	yearMode = (sys.argv[3] == 'year')

# Find needed pages
pageList = []

if(yearMode):
	startYear = 1870				# the first year EVER
	endYear = date.today().year + 1	# It's conceivable user could see a prerelease/early screening for a film from next year)

	# Get year base pages
	for i in range(startYear, endYear + 1):
		pageYear = Page('https://letterboxd.com/' + userName + '/films/year/' + str(i) + '/')
		pageYear.year = i
		pageList.append(pageYear)
	
	# if year has more than 1 page...
	pageListExtra = []
	for page in pageList:
		if(page.ready == False):
			time.sleep(1)
			page.Load()
			print('crawling ' + str(page.url))
		pageDiscovery = page.soup.find(class_='paginate-pages')	# Find links in pagination section
		if pageDiscovery:
			pageDiscoveryList = pageDiscovery.find_all('a')
			pageCount = 1
			for pageID in pageDiscoveryList:		
				pageNumber = pageID.contents[0]
			pageCount = max(pageCount, int(pageNumber))
			for pageNum in range(2, pageCount + 1):
				pageTemp = Page('https://letterboxd.com/' + userName + '/films/year/' + str(page.year) + '/page/' + str(pageNum)+'/')
				pageTemp.year = page.year
				pageListExtra.append(pageTemp)
				
	# subpages
	for page in pageListExtra:
		pageList.append(page)
else:
	firstPage = Page('https://letterboxd.com/' + userName + '/list/' + listName + '/page/1/')
	firstPage.Load()
	pageList.append(firstPage)
	
	pageDiscovery = firstPage.soup.find(class_='paginate-pages')	# Find links in pagination section
	pageDiscoveryList = pageDiscovery.find_all('a')
	
	# find last page number
	pageCount = 0
	for pageID in pageDiscoveryList:		
		pageNumber = pageID.contents[0]
	pageCount = max(pageCount, int(pageNumber))
	
	# add range to search list
	for pageNum in range(2, pageCount + 1):
		pageTemp = Page('https://letterboxd.com/' + userName + '/list/' + listName + '/page/' + str(pageNum) + '/')
		pageList.append(pageTemp)

# find films on pages
filmList = []

print('Reading...')
for i in range(0, len(pageList)):
	page = pageList[i]
	if page.ready == False:
		time.sleep(1)	# wait a bit for request
		page.Load()
	
	# read posters
	posterContainer = page.soup.find(class_='poster-list')
	if posterContainer:
		ratingList = posterContainer.find_all('li')		# <li class="poster-container" data-owner-rating="0">
		nameList = posterContainer.find_all('img')		# <img alt="John Wick: Chapter 2" class="image" height="105" src="https://s1.ltrbxd.com/static/img/empty-poster-70.8461d4ea.png" width="70"/>
		
		for film in range(0, len(nameList)):
			nameEntry = nameList[film]
			name = nameEntry.get('alt')
			name.encode('utf8')
			
			ratingEntry = ratingList[film]
			ratingData = ratingEntry.get('data-owner-rating')
			rating = int(ratingData)
			
			year = page.year;
			
			filmList.append(Film(name, rating, year))

	print(str(i + 1) + '/' + str(len(pageList)) + ' ' + page.url + ' (' + str(len(filmList)) + ' films discovered)')
print('watch: ' + str(random.choice(nameList)))

	
# sort list alphabetically
filmList = sorted(filmList, key=lambda film: film.name)
	

	userName = str(sys.argv[1])
else:
	userName = input('Please enter a Username : ')
	listName = input('Please enter a list : ')
if(ArgCount >= 3):
	outPath = sys.argv[2]
else:
	outPath = input('Please enter an output file name : ')
if(ArgCount >= 4):
	yearMode = (sys.argv[3] == 'year')

# Find needed pages
pageList = []

if(yearMode):
	startYear = 1870				# the first year EVER
	endYear = date.today().year + 1	# It's conceivable user could see a prerelease/early screening for a film from next year)

	# Get year base pages
	for i in range(startYear, endYear + 1):
		pageYear = Page('https://letterboxd.com/' + userName + '/films/year/' + str(i) + '/')
		pageYear.year = i
		pageList.append(pageYear)
	
	# if year has more than 1 page...
	pageListExtra = []
	for page in pageList:
		if(page.ready == False):
			time.sleep(1)
			page.Load()
			print('crawling ' + str(page.url))
		pageDiscovery = page.soup.find(class_='paginate-pages')	# Find links in pagination section
		if pageDiscovery:
			pageDiscoveryList = pageDiscovery.find_all('a')
			pageCount = 1
			for pageID in pageDiscoveryList:		
				pageNumber = pageID.contents[0]
			pageCount = max(pageCount, int(pageNumber))
			for pageNum in range(2, pageCount + 1):
				pageTemp = Page('https://letterboxd.com/' + userName + '/films/year/' + str(page.year) + '/page/' + str(pageNum)+'/')
				pageTemp.year = page.year
				pageListExtra.append(pageTemp)
				
	# subpages
	for page in pageListExtra:
		pageList.append(page)
else:
	firstPage = Page('https://letterboxd.com/' + userName + '/list/' + listName + '/page/1/')
	firstPage.Load()
	pageList.append(firstPage)
	
	pageDiscovery = firstPage.soup.find(class_='paginate-pages')	# Find links in pagination section
	pageDiscoveryList = pageDiscovery.find_all('a')
	
	# find last page number
	pageCount = 0
	for pageID in pageDiscoveryList:		
		pageNumber = pageID.contents[0]
	pageCount = max(pageCount, int(pageNumber))
	
	# add range to search list
	for pageNum in range(2, pageCount + 1):
		pageTemp = Page('https://letterboxd.com/' + userName + '/list/' + listName + '/page/' + str(pageNum) + '/')
		pageList.append(pageTemp)

# find films on pages
filmList = []

print('Reading...')
for i in range(0, len(pageList)):
	page = pageList[i]
	if page.ready == False:
		time.sleep(1)	# wait a bit for request
		page.Load()
	
	# read posters
	posterContainer = page.soup.find(class_='poster-list')
	if posterContainer:
		ratingList = posterContainer.find_all('li')		# <li class="poster-container" data-owner-rating="0">
		nameList = posterContainer.find_all('img')		# <img alt="John Wick: Chapter 2" class="image" height="105" src="https://s1.ltrbxd.com/static/img/empty-poster-70.8461d4ea.png" width="70"/>
		
		for film in range(0, len(nameList)):
			nameEntry = nameList[film]
			name = nameEntry.get('alt')
			name.encode('utf8')
			
			ratingEntry = ratingList[film]
			ratingData = ratingEntry.get('data-owner-rating')
			rating = int(ratingData)
			
			year = page.year;
			
			filmList.append(Film(name, rating, year))

	print(str(i + 1) + '/' + str(len(pageList)) + ' ' + page.url + ' (' + str(len(filmList)) + ' films discovered)')
print('watch: ' + str(random.choice(nameList)))

	
# sort list alphabetically
filmList = sorted(filmList, key=lambda film: film.name)

# write out
f = open(outPath,'w',encoding='utf-8')
for film in filmList:
	yearString = ' '
	if(yearMode):
		yearString = ' (' + str(film.year) + ') '
	
	if(film.rating != 0):
		f.write(film.name + yearString + str(film.Stars()) + '\n')
	else:
		f.write(film.name + yearString + '\n')
f.close()
	
