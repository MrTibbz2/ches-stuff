from dataclasses import dataclass
from datetime import datetime
from typing import List, Tuple
from queue import Queue

@dataclass
class DeliveryOrder: #class to track different parts of a user's order. I just prefer the struct like data classes because I come from c++
    uid: int # just wanna track what the id is so I can link it into a database later. also helps for tracking things
    firstname: str
    lastname: str
    address: str
    order: list[tuple[str, int]]  # see what they ordered and how much. 
    total: float #total price in dolloars 
    datetimePlaced: datetime 

class queueManagement:
    def __init__(self):
        self.queue = Queue()  # Use Queue 
    
    def addOrder(self, order: DeliveryOrder): # add 
        self.queue.put(order)
    
        print("Added order to queue")

    def removeLatest(self):
        if not self.queue.empty(): 
            self.queue.get()  # Remove the order least recently added to the queue
            print("Removed first order in queue")
    
    def getAll(self): # get all orders in the queue
        return self.queue

    def clearQueue(self): # just error handling for when it goes bad
        self.queue.empty() 
    
    def isEmpty(self):
        if self.queue.empty:
            return True
        else:
            return False
    def getSize(self):
        return self.queue.qsize()
    
    def getLatest(self):
        return self.queue.queue[0] if not self.queue.empty() else "none in queue"  # Get the first order in the queue without removing it
    
    def findlatestID(self):
        if self.isEmpty():
            return 0
        else:
            return self.queue.queue[0].uid 
