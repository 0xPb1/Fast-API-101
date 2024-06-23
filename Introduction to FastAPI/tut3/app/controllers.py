# import the Session class from SQLAlchemy and the models and schemas 
from sqlalchemy.orm import Session

from . import models, schemas

#  function that reads rows from the database.
def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()

# write a similar function to query a single Item object by specifying the ID
def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()

# write the function to Create, or add rows to the Items table
def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(title=item.title, description=item.description, price=item.price)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# allow updating of rows
def update_item(db: Session, item_id: int, item: schemas.ItemCreate):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    db_item.title = item.title
    db_item.description = item.description
    db_item.price = item.price
    db.commit()
    db.refresh(db_item)
    return db_item

# function to delete Item objects by their numerical ID

def delete_item(db: Session, item_id: int):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    db.delete(db_item)
    db.commit()
    return db_item