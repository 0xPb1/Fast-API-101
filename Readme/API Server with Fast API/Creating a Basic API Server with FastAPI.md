- Understand how FastAPI works
- Create a Pydantic model
- Create simple CRUD API routes
- Use Postman to test your API

#### Create routes or endpoints in FastAPI for users to create, read, update and delete data on your server.

## Basic HTTP with FastAPI

Typically, this is how API servers work in the context of managing users, with reference to the CRUD framework.

**GET** - Read

**POST** - Create

**PUT** - Update

**DELETE** - Delete

For example, the API endpoint for retrieving a list of users would look like

```python
GET /users
```

For adding a new user to the database, it could look like the following, with a JSON body.

```json
POST /users

{
	“username”: “john”,
	“email”: “john@stackup.com”
}
```

Plain text

And it would be very similar to updating an existing user.

```json
PUT /users

{
	“username”: “john”,
	“email”: “john@stackup.com”
}
```

Plain text

To delete a user, a request like this could be utilised, to delete a user with the ID 1.

```json
DELETE /users/1
```

There are many other ways API servers can be set up, including using query parameters like in “DELETE /users?id=1”, but it all depends on preference.

## Routing with FastAPI

We now know how HTTP request methods can be utilised in creating an API server. However, different web frameworks utilise different methods for handling these request methods.

Previously, we used the following code to create the endpoint to return text when a GET request is made to “/”.

```python
@app.get("/")
def index():
    return "Hello from StackUp :D"
```

Python

In the first line of this specific block of code, a decorator is used to add a handler for GET requests, as seen in “app.get”, including the route(“/”) as an argument.

To create handlers for other request methods, all you have to do is edit the “get” portion of the decorator. For an API endpoint for users, it would be:

```python
@app.get("/users")
@app.post("/users")
@app.put("/users")
@app.delete("/users/<int:id>")
```


## Setting up Our Environment

`requirements.txt`
```python
fastapi
uvicorn
pydantic
```


Pydantic is a Python library crucial for data validation in web frameworks like FastAPI. Leveraging Python type annotations, it defines data models. FastAPI then uses these models to validate incoming request data and serialize response data. Its clear error messages and automatic documentation generation make it indispensable for efficient web development, enhancing robustness and productivity in creating and managing APIs.

## Creating Our User Model

To define the data structures we will use in the application, we will use Pydantic. This will ensure that the data in request bodies match a specific predefined rule set.

You can read more about Pydantic [here](https://docs.pydantic.dev/latest/).

Open **models.py** and add the following code. This code creates a Pydantic model for our User object.

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
```

