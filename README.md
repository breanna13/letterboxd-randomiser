## ⚠️ Listen up y'all:
This project is currently offline due to expired Heroku hosting. The application was previously deployed and fully functional, I swear it. But hosting services have been discontinued for now. Run it locally.

# Letterboxd Random Movie Roulette
<center><img src="https://a.ltrbxd.com/logos/letterboxd-logo-h-neg-rgb-1000px.png" alt="Letterboxd Banner"></center>
<head><center><b>About</b> </center></head>
<hr>
<p><a href="https://letterboxd.com/tobiasandersen2/list/random-movie-roulette/">Random Movie Roulette</a> is a popular Letterboxd list with which a user can use <a href="random.org">RANDOM.org</a> to randomly choose a movie from a list of thousands.</p>

While this is a fun and excting way to choose films and a great concept, scrolling through list pages can be tedious, and unnumbered lists can make this method nigh impossible without manually counting through rows and pages. 

With letterboxd randomiser, randomising letterboxd lists can be done easily. Deciding what to watch will take mere seconds. 

<p><center><b>Official Release: <a href="https://randommovieroulette.herokuapp.com">PLAY</a></b></center></p>

<b>Set Up and Run</b>
<hr>

### Set Up
#### Prerequisites
###### Ensure you have Python 3.7+ and Git installed
###### python --version
###### git --version

#### 1. Clone the Repository
git clone https://github.com/breanna13/letterboxd-randomiser.git

cd letterboxd-randomiser

#### 2. Create Virtual Environment
###### On Windows
python -m venv venv

###### On macOS/Linux
python3 -m venv venv

#### 3. Activate Virtual Environment
###### On Windows
venv\Scripts\activate

###### On macOS/Linux
source venv/bin/activate

#### 4. Install Dependencies
pip install -r requirements.txt

#### 5. Set Environment Variables
###### On Windows
set FLASK_APP=flaskapp.py
set FLASK_ENV=development

###### On macOS/Linux
export FLASK_APP=flaskapp.py
export FLASK_ENV=development

#### 6. Run the Flask Application
flask run

#### 7. Run the page
Open browser and go to:
http://localhost:5000
or
http://127.0.0.1:5000

##### Troubleshooting
###### If port 5000 is busy, try:
flask run --port=5001

###### If module errors occur:
pip list
pip install -r requirements.txt

###### Ensure virtual environment is activated before running

### Play
1. List must have 100+ films<br>
2. User and List names must match list URL
<hr>
Made with <a href="https://github.com/pallets/flask">Flask</a>

<p>Credit to spacebruce for letterboxd access framework</p>
