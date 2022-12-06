## REQUIREMENTS
1. Write a SQL script that can create a simple SQL table for listings 
![Listing table](static/listing_table.jpg)
2. Write a script to populate the DB with mock data for demo purposes.
3. Implement a simple REST API that has CRUD (Create, Read, Update, Delete) functionality for that database.
4. Write Unit Tests to ensure your API can be tested by other developers.
5. Document your code so another programmer can use it and expand on your code.


## Set up & Install

- Run **connect_db.py** to make the database available
- Run **app.py** to start the flask server and check CRUD operations


## INTRO

This is a Flask application for demo purposes on CRUD operations related to properties table.
The code contains:
`connect_db.py` - first file to run which makes possible:     
    1. database connection (**sqlite**)              
    2. table creation (**property_listing**)        
    3. population with data (**mock**)          
`app.py` - main file to run for CRUD operations

