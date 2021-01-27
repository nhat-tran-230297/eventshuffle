# Eventshuffle backend API

Eventshuffle backend API is an application to help scheduling events and generate corresponding API. <br><br>
[Visit the website](https://eventshuffle.herokuapp.com/)
<br><br>

# Table of contents
* [Introduction](#introduction)
* [Contents](#contents)


# Introduction
![image](https://user-images.githubusercontent.com/27566386/106016380-15c6ae00-60c8-11eb-9497-f6bb54b63131.png)

# Contents

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



An event is created by providing a name and suitable dates to the backend, and retrieve
