# DELIVERY SERVICE MANAGER

gonna be for delivering coffee beans because.. yum!

---

## 📋 Feature Plan

- add time, date, deliveryperson, address, orderitems (list), order total: to a queue of deliveries to be done  
- add a menu integration to control orders from users and add totals based on orders, assign deliveryperson to orders based on time  
- add sql to make things consistent through runs of the program  

---

## 🗺️ Roadmap

1. data movement class, basic cli  
2. sql databases  
3. menu to calculate order totals  

---

## 📦 Main Queue Functions Needed

- **enqueue (put)**: add items to the end of the delivery queue to be delivered later on, queued up to be delivered  
- **dequeue (get)**: remove the delivery after it has been delivered  
- **peek**: view the upcoming delivery  

> note on peek, after actually trying it I realised it doesnt really exist..  
> you can do the same with `queue.queue[0]` BUT thats not thread safe  
> If multiple threads run at the same time all, viewing the variable, the code/data will break, crash, or get corrupted.  
> however I'm not planning to implement multithreading  

- **size()**: view the number of deliveries pending  
- **clear()**: error handeling and system reset  
- **is_empty()**: error handling  

---

## 🗃️ TinyDB

- json based database stuff  
- actual db be way better because its stored where the program isnt.. which means data safety. thats why in an actual setting thats what you'd do.  
- makes things persistent between runs of the program  
- also means that when a delivery is completed we can put it in a history database, so we can check back.  
- maybe make the menu for products into a database, so they can be added at runtime by a user?  

- since I already have implemented the queue stuff seperately I think it would be easier just to read db on init and write to it on close.  
  thats not a great way to do it because crash or keyboardinterrupt = data loss, but should be fine.  

---

## 📚 ASSIGNMENT WRITE UP

### Different ADTs in Python:

#### - list  
a list is an all purpose data bin that can store all types of data, an easy way to put lots of data into an unorganised fashion.  
you can use them to store all data types and view from anywhere in the list, as well as remove and view at certain points.  

#### - queue  
a queue is an adt used for FIFO (first in first out.)  
it means when we add something it is behind everything placed before it, and it moves up when those things are removed.  
we use it to order things in an easy fashion without having to figure out how to order.  
however many parts of the python queue are not thread safe, such as viewing the middle of the queue or the data at an index  
this is due to the FIFO nature of the stack.  
it is perfect for our deliveries mangament because it fits the use case and the program is not multithreaded.  

#### - array  
arrays are a more low level data type that is used for faster operations  
it only supports using one data type.  
it stores data more efficiently than lists and is used for larger sets of data.  

#### - set  
used to store unique, unordered data sets.  
great for finding what exists and what doesnt.  
not great for storing data.  

---

## 🚀 Why is a Queue Great for Us?

- the FIFO nature is just like actual deliveries in real life  
- orders the stack without getting messy  
- the queue already has built in functions for us.  
