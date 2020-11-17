# Python-forex-event
## Python application to track macroeconomic events on forex.

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This application is giving info about upcoming events on forex by push
notifications. (works on win10 and linux)
	
	
## Technologies:
Project is created with:
* Python 3.8
* Finnhub Stock API

	
## Setup
To run this project on Windows:
* pip install virtualvenv (for keep order)
* py -m venv myvenv
* myvenv\scripts\activate
* pip install -r requirements_win10.txt
* py main.py

On Linux/Ubuntu:
* sudo apt install python-pip
* sudo apt install virtualenv (for keep order)
* virtualenv myvenv
* source myvenv/bin/activate
    * maybe before install requirements you have to need install this:\
         "sudo apt install git virtualenv build-essential python3-dev libdbus-glib-1-dev libgirepository1.0-dev libcairo2-dev",\
        otherwise you could have problem with install dbus-python from requirements_linux.txt
* pip install -r requirements_linux.txt
* python3 main.py