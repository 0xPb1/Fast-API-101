#  import our FastAPI and SQLAlchemy dependencies
from fastapi import APIRouter, Depends, HTTPException, FastAPI
from sqlalchemy.orm import Session

# as well as the classes we wrote earlier

from . import controllers, models, schemas
from .database import SessionLocal, engine

# create all the tables defined in models.py.

models.Base.metadata.create_all(bind=engine)

# create the FastAPI application.

app = FastAPI()

#  define a helper function get_db() that will be used as a dependency to check if the database is up.

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# write the functions for our CRUD operations.

# To allow users to read from our database, we can create endpoints at /items and /items/{item_id} that support GET requests, utilising the functions, read_items() and read_item() we created in controllers.py.

@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = controllers.get_items(db, skip=skip, limit=limit)
    return items

@app.get("/items/{item_id}", response_model=schemas.Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = controllers.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

# we create a listener for POST requests to /items which allows users to create Items, or add rows to the table.

@app.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return controllers.create_item(db=db, item=item)

# For updating rows, we create a listener for PUT requests to /items/{item_id}, which allows users to specify the ID of the item they would like to update in the URL, e.g. /items/1.

@app.put("/items/{item_id}", response_model=schemas.Item)
def update_item(item_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item = controllers.update_item(db, item_id=item_id, item=item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


# create a listener for DELETE requests to /items/{item_id} to allow users to delete Items by their ID.

@app.delete("/items/{item_id}", response_model=schemas.Item)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = controllers.delete_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item