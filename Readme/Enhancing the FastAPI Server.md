
[Link to article](https://earn.stackup.dev/campaigns/developing-an-api-server-with-fastapi/quests/enhancing-the-fastapi-server-92dd)
#### Integrate a database into the application using SQLAlchemy with FastAPI

### SQLAlchemy's Object-Relational Mapping (ORM) feature is particularly useful; it lets you define your database models as Python classes, making it more intuitive to work with data.

Before we start, read [this article](https://www.sqlalchemy.org/features.html) to understand what SQLAlchemy is and how it can be used to make database operations more seamless.

In short, SQLAlchemy is a powerful Python library that facilitates interaction with databases by abstracting database management complexities. It enables users to create, manage, and query databases using Python code, allowing for seamless integration between the code and the underlying database system.


- __init__.py
- controllers.py
- database.py
- main.py
- models.py
- requirements.txt
- schemas.py

Here's a brief description of what each file will do. 

1. __init__.py is used to indicate the directory should be treated as a Python package. We will not be adding any code to this file.
2. controllers.py will define our helper functions that carry out the CRUD operations
3. database.py contains our database connection code
4. models.py stores our database objects for SQLAlchemy to use
5. requirements.txt is used to enter the dependencies that will be installed
6. schemas.py will define our data structures for Python to use.