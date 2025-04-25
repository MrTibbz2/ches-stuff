from dataclasses import dataclass
from datetime import datetime
from typing import List, Tuple
import asyncio
@dataclass
class DeliveryOrder: #class to track different parts of a user's order. I just prefer the struct like data classes because I come from c++
    uid: int # just wanna track what the id is so I can link it into a database later maybe
    firstname: str
    lastname: str
    address: str
    order: list[tuple[str, int]]  # see what they ordered and how much. 
    total: float #total price in dolloars 
    datetimePlaced: datetime 

class queueManagement:
    def __init__(self):
        self.queue = [] # queue of orders
    
    def addOrder(self, order: DeliveryOrder): # add 
        self.queue.append(order)
    
        print("Added order to queue")

    def removeLatest(self): # remove 
        self.queue.pop(0) 
        print("Removed first order in queue")
    
    def removeById(self, uid: int): # probably unneccesary but just in case we need to remove a specific order
        for i, order in enumerate(self.queue):
            if order.uid == uid:
                self.queue.pop(i)
                break

    def getAll(self): # get all orders in the queue
        return self.queue

    def clearQueue(self): # just error handling for when it goes bad
        self.queue.empty() 
    
    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False
    def getSize(self):
        return len(self.queue)
    
    def getLatest(self):
        return self.queue.peek(0)
    
    def findlatestID(self):
        if self.isEmpty():
            return 0
        else:
            return self.queue.peek(0).uid + 1
