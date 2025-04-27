from data import DeliveryOrder, queueManagement
from datetime import datetime
import asyncio
from db import dbapi
from menu import menuItem, menu
DBApi = dbapi()

q = queueManagement()

def wait_for_input():
    input("Press Enter to continue...")
    

class menuSelection:
    def __init__(self, queue: queueManagement):
        self.queue = queue

    def add_order(self): #adds an order to the queue. takes inputs, also does a calculation of the total price.
        m = menu()
        uid = self.queue.findlatestID() + 1
        firstname = input("Enter first name: ")
        lastname = input("Enter last name: ")
        address = input("Enter address: ")
        order_items = []
        while True:
            menuitems = m.showmenu()
            print("choose from the following menu for the order:")
            for menuItem in menuitems:
                print(str(f"    name: {menuItem.blendName}, ID: {menuItem.blendID}, roast: {menuItem.blendRoast}, price: {menuItem.blendPrice}"))
                
            itemID = int(input("Enter item ID (or 'done' to finish): "))
            
            if itemID.lower() == 'done':
                break
            quantity = int(input(f"Enter quantity for item with id of {itemID}: "))
            if itemID < 0 or itemID >= len(menuitems):
                print("Invalid item ID. Please try again.")
                continue
            order_items.append((itemID, quantity))
        total = m.calculateTotal(order_items)
        print(f"your total order price is: {total}")
        checkconfirm = int(input("type 1 to confirm your order: "))
        if checkconfirm == 1:
            datetime_placed = datetime.now()
            order = DeliveryOrder(uid, firstname, lastname, address, order_items, total, datetime_placed)
            self.queue.addOrder(order)
            print("Order added successfully!")
        else:
            print("Order not confirmed. Returning to menu.")
        wait_for_input()

    def remove_latest(self):
        self.queue.removeLatest()
        print("Latest order removed successfully!")
        wait_for_input()

       

    def view_all_orders(self):
        orders = self.queue.getAll().queue
        if not orders:
            print("No orders in the queue.")
        else:
            for order in orders:
                print(order)
        wait_for_input()
    def clear_all_orders(self):
        self.queue.clearQueue()
        print("All orders cleared successfully!")
        wait_for_input()
    def view_latest_order(self):
        latest_order = self.queue.getLatest()
        if latest_order:
            print(latest_order)
        else:
            print("No orders in the queue.")
        wait_for_input()
    
def CLIMain():

    menu = menuSelection(q)

    

    while True:
        try:
            print("Welcome to the Coffee deliveries management system!")
            print("\nPlease select an option:")
            print("1. Add order")
            print("2. Remove latest order")
        
            print("3. View all orders")
            print("4. Clear all orders")
            print("5. View latest order")
            print("6. Exit")
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            menu.add_order()
        elif choice == 2:
            menu.remove_latest()

        elif choice == 3:
            menu.view_all_orders()
        elif choice == 4:
            menu.clear_all_orders()
        elif choice == 5:
            menu.view_latest_order()
        elif choice == 6:
            print("saving database...")
            DBApi.saveDB(q)
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            wait_for_input()



DBApi.loadDB(q)

CLIMain()
