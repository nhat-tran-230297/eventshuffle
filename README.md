# Eventshuffle backend API

Eventshuffle backend API is an application to help scheduling events and generate corresponding API. <br><br>
[Visit the website](https://eventshuffle.herokuapp.com/)
<br><br>

# Table of contents
* [Introduction](#introduction)
* [Contents](#contents)


# Introduction
![](screenshot.png)
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