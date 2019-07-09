#!/usr/bin/env python
from urllib import request
import random
import urllib
import time
from datetime import date
import sys
import re
import json
from flask_wtf import FlaskForm
from bs4 import BeautifulSoup
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html')


@app.route("/handle_data", methods =['GET', 'POST'])
def handle_data():
	if request.method == 'POST':
		OGuserName = request.form.get('username')
		OGlistName = request.form.get('listname')
		userName = OGuserName.replace(" ", "_").lower()
		listName = OGlistName.replace(" ", "-").lower()
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
				
		# Find needed pages
		pageList = []

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

		for i in range(0, len(pageList)):
			page = pageList[i]
			if page.ready == False:
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
		randomNumber = random.randint(0,len(nameList)-1) # make random number
		filmRandom = nameList[randomNumber]			     # variable 'films' is a random movie poster
		filmsRandomString = str(filmRandom)
		finishedRandomString = filmsRandomString[10:-110]
		movieLinkString = filmsRandomString[10:-110].replace(" ", "-").replace(":", "").replace("'", "")
		movieLink = 'https://letterboxd.com/film/' + movieLinkString.lower() + '/'
		return render_template('home.html', movieLink= movieLink, films = finishedRandomString)

if __name__ == '__main__':
	app.run()
