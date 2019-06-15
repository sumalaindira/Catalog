# Queens_Beauty_Places Web App
##By Indira Sumala
This web app is a project for the Udacity [FSND Course](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

## About
This project is a RESTful web application utilizing the Flask framework which accesses a SQL database that populates categories and their items. OAuth2 provides authentication for further CRUD functionality on the application. Currently OAuth2 is implemented for Google Accounts.

## In This Project
This project has one main Python module `project.py` which runs the Flask application. A SQL database is created using the `database_setup.py` module and you can populate the database with test data using `lotsofmenus.py`.
The Flask application uses stored HTML templates in the tempaltes folder to build the front-end of the application. CSS/JS/Images are stored in the static directory.

## Skills Required
1. Python
2. HTML     
3. CSS
4. OAuth
5. Flask Framework

## Installation
There are some dependancies and a few instructions on how to run the application.
Seperate instructions are provided to get GConnect working also.

## Dependencies
- [Vagrant](https://www.vagrantup.com/)
- [Udacity Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)



## How to Install
1. Install Vagrant & VirtualBox
2. Clone the Udacity Vagrantfile
3. Go to Vagrant directory and either clone this repo or download and place zip here
3. Launch the Vagrant VM (`vagrant up`)
4. Log into Vagrant VM (`vagrant ssh`)
5. Navigate to `cd/vagrant` as instructed in terminal
6. The app imports requests which is not on this vm. Run pip install requests

Or you can simply Install the dependency libraries (Flask, sqlalchemy, requests,psycopg2 and oauth2client) by running 
`pip install -r requirements.txt`

7. Setup application database `python /Queens_Beauty_Places/database_setup.py`
8. *Insert sample data `python /Queens_Beauty_Places/lotsofmenus.py`
9. Run application using `python /Queens_Beauty_Places/project.py`
10. Access the application locally using http://localhost:5000

*Optional step(s)
## Using Google Login
To get the Google login working there are a few additional steps:
1. Go to [Google Dev Console](https://console.developers.google.com)
2. Sign up or Login if prompted
3. Go to Credentials
4. Select Create Crendentials > OAuth Client ID
5. Select Web application
6. Enter name 'itemcatalog'
7. Authorized JavaScript origins = 'http://localhost:5000'
8. Authorized redirect URIs = 'http://localhost:5000/login' && 'http://localhost:5000/gconnect'
9. Select Create
10. Copy the Client ID and paste it into the `data-clientid` in login.html
11. On the Dev Console Select Download JSON
12. Rename JSON file to client_secrets.json
13. Place JSON file in Queens_Beauty_Places directory that you cloned from here
14. Run application using `python /Queens_Beauty_Places/project.py`

## JSON Endpoints
The following are open to the public:

gadget JSON: `/gadget/JSON`
    - Displays all Gadgets.

gadget Items JSON: `/gadget/<path:gadget_id>/menu/JSON`
    - Displays menu for a specific gadget

gadget Item JSON: `/gadget/<path:gadget_id>/<path:menu_id>/JSON`
    - Displays a specific gadget item.

## Miscellaneous

This project is inspiration from https://github.com/SkBadulla/Item_Catalog