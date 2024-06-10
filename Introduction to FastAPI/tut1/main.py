# imports the FastAPI module from the fastapi library 
from fastapi import FastAPI

# initialise your application with this line.
app = FastAPI()

# The @app.get() decorator is used to define the path of the URL and the method that will be used to access the URL.

@app.get("/")
def index():
    return "Hello from StackUp :D Answer is A"
