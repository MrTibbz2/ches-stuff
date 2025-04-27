# a file to work with TinyDB. just a json based database thing.
#  obviously if you wanted to actually deploy the program youd probably use postgre or mysql because its a lot better.
# however, tinydb works well because its super simple and fast.
import tinydb
from tinydb import TinyDB
import dataclasses
from data import DeliveryOrder
from datetime import datetime
import os


class dbapi:
    def __init__(self):
        
        os.makedirs('db', exist_ok=True)
        db = TinyDB('db/db.json')  
        self.db = db
    
    def saveDB(self, qManage): # passing in the queue api so that main and db interact with the same queue.
        self.db.truncate() # caveman technique for making sure no duplicates exist.
        q = qManage.getAll().queue
        for DeliveryOrder in q:
            
            self.db.insert({
                'uid': DeliveryOrder.uid,
                'firstname': DeliveryOrder.firstname,
                'lastname': DeliveryOrder.lastname,
                'address': DeliveryOrder.address,
                'order': DeliveryOrder.order,
                'total': DeliveryOrder.total,
                'datetimePlaced': DeliveryOrder.datetimePlaced.isoformat()  
            })
        print("saved db")
    
    def loadDB(self, qManage):
        
        all_documents = self.db.all()  
        for document in all_documents:
            
            order = DeliveryOrder(
                uid=document['uid'],
                firstname=document['firstname'],
                lastname=document['lastname'],
                address=document['address'],
                order=document['order'],
                total=document['total'],
                datetimePlaced=datetime.fromisoformat(document['datetimePlaced'])
            )
            qManage.addOrder(order)  
        print("loaded db")





