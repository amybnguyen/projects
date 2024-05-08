# Top Movies

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
Website that displays my top movies. Gets movie data from [TMDB API](https://developer.themoviedb.org/reference/intro/getting-started) when user provides movie name. Adds movie data to SQL database and updates the panels loaded on the site. Ran on a Flask app.

![goodwill](Screenshot(48).PNG)
	
## Technologies
Project is created with:
* Python: 3.12
* Libraries: Flask, SQLAlchemy, Requests
	
## Setup
To run this project, find the local directory in terminal and use the python script_name.py command:
```
$ cd ../top-movies
$ python main.py
```
Note: User must provide token for TMDB API.