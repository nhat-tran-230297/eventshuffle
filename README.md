# Eventshuffle backend API

Eventshuffle backend API is an application to help scheduling events and generate corresponding API. <br><Br>
[Online demo](https://eventshuffle.herokuapp.com/)<br>
[Source code](https://github.com/nhat-tran-230297/eventshuffle)
<br><br>

# Table of contents
* [Introduction](#introduction)
* [Installation](#installation)
* [File Contents](#file-contents)


# Introduction
An event is created by providing a name and suitable dates to the backend, and events can be queried from the backend and participants can submit dates suitable for them. The result of an event is the most suitable date, which has most votes from participants. In case, there are more than 1 suitable dates, they will all be displayed.

<br>

The application contains 5 different requests of 2 distinct methods (GET and POST):
* List all events
* Create an event
* Show an event
* Add votes to an event
* Show the results of an event

<br>

![image](https://user-images.githubusercontent.com/27566386/106016380-15c6ae00-60c8-11eb-9497-f6bb54b63131.png)


Clicking the "Send" button will display the corresponding API for the request 

![1](https://user-images.githubusercontent.com/27566386/106020177-2547f600-60cc-11eb-9f0a-2852e1686705.png)


Alternatively, clicking the "Get API" button will generate the raw API.

Some requests require parameters, which includes the id of the event and the body as a JSON format (displayed in the request body placeholder). 

![image](https://user-images.githubusercontent.com/27566386/106022329-63deb000-60ce-11eb-81d2-5effc54ab637.png)

<br>

# Installation

Eventshuffle Backend API was written in [Flask](https://github.com/pallets/flask) framework.

1. Download and install [Python](https://www.python.org/downloads/) version 3.7.4 or above ([guide](https://realpython.com/installing-python/)). If you already have [Python](https://www.python.org/downloads/), you can check the version by

```
python --version
```


2. Get the code

```
git clone https://github.com/nhat-tran-230297/eventshuffle
cd eventshuffle
```
3. Install requirements
```
pip install -r requirements.txt
```
4. Set up the FLASK_APP environment variable
* windows
```
set FLASK_APP=run.py
```
* (Unix) 
```
export FLASK_APP=run.py
```
* (Powershell)
```
$env:FLASK_APP = ".\run.py"
```
5. Run the application
```
flask run
```
or
```
python run.py
```


# File Contents

```
eventshuffle
 
 ┣ app
 ┃ ┣ api
 ┃ ┃ ┣ views.py
 ┃ ┃ ┗ __init__.py
 ┃ ┣ base
 ┃ ┃ ┣ templates
 ┃ ┃ ┃ ┗ index.html
 ┃ ┃ ┣ views.py
 ┃ ┃ ┗ __init__.py
 ┃ ┣ static
 ┃ ┃ ┣ css
 ┃ ┃ ┃ ┗ style.css
 ┃ ┃ ┗ js
 ┃ ┃ ┃ ┗ index.js
 ┃ ┣ database.db
 ┃ ┣ models.py
 ┃ ┣ utils.py
 ┃ ┗ __init__.py
 ┣ .gitignore
 ┣ config.py
 ┣ Pipfile
 ┣ Pipfile.lock
 ┣ Procfile
 ┣ README.md
 ┣ requirements.txt
 ┣ run.py
 ┗ runtime.txt
```

## Configuration
The application configuration and initialization, including registering blueprints, configuring database are inside the file [app/__init__.py](https://github.com/nhat-tran-230297/eventshuffle/blob/main/app/__init__.py)

<br>

## Blueprint

The application contains of only 1 [blueprint](https://github.com/pallets/flask/blob/master/docs/blueprints.rst), which are the files inside the [app/base](https://github.com/nhat-tran-230297/eventshuffle/tree/main/app/base) folder. The blueprint is initialized [here](https://github.com/nhat-tran-230297/eventshuffle/blob/main/app/base/__init__.py). Usually, there are more blueprints when the application becomes more complexed.

The benefit for having [blueprints](https://github.com/pallets/flask/blob/master/docs/blueprints.rst) in Flask is that all functions of the a blueprint share the same url/domain prefix. A blueprint might represent a particular feature, thus reducing the complexity of the application.

<br>

## Database

<br>

The database consists of 3 entities: Events, Dates, People. The relationship between entities was described in the figure below.

![image](https://user-images.githubusercontent.com/27566386/106051919-bb424780-60f1-11eb-9a83-496219997168.png)

The database schema is designed in the file [app/models.py](https://github.com/nhat-tran-230297/eventshuffle/blob/main/app/models.py) with the help of [SQLAlchemy](https://docs.sqlalchemy.org/en/13/intro.html) through Object Relational Mapping (ORM).

<br>

## Routing

Building the URL, endpoints and the behavior are defined in the file [app/base/views.py](https://github.com/nhat-tran-230297/eventshuffle/blob/main/app/base/views.py)
<br>

**/**  
default page

**/api/v1/event/list**<br>
List all events

**/api/v1/event**<br>
Create an event

**/api/v1/event/{id}**<br>
Show an event

**/api/v1/event/{id}/vote**<br>
Add votes (dates) to an event

**/api/v1/event/{id}/results**<br>
Show results of an event (Show the dates people vote the most)












