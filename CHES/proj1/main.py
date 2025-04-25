from data import DeliveryOrder, queueManagement
from datetime import datetime
import asyncio

class menuSelection:
    def __init__(self, queue: queueManagement):
        self.queue = queue

    def add_order(self):
        uid = self.queue.findlatestID() + 1
        firstname = input("Enter first name: ")
        lastname = input("Enter last name: ")
        address = input("Enter address: ")
        order_items = []
        while True:
            item_name = input("Enter item name (or 'done' to finish): ")
            if item_name.lower() == 'done':
                break
            quantity = int(input(f"Enter quantity for {item_name}: "))
            order_items.append((item_name, quantity))
        total = float(input("Enter total price: "))
        datetime_placed = datetime.now()
        order = DeliveryOrder(uid, firstname, lastname, address, order_items, total, datetime_placed)
        self.queue.addOrder(order)
        print("Order added successfully!")

    def remove_latest(self):
        self.queue.removeLatest()
        print("Latest order removed successfully!")

    def remove_by_id(self):
        uid = int(input("Enter the order ID to remove: "))
        self.queue.removeById(uid)
        print(f"Order with ID {uid} removed successfully!")

    def view_all_orders(self):
        orders = self.queue.getAll()
        if not orders:
            print("No orders in the queue.")
        else:
            for order in orders:
                print(order)

    def clear_all_orders(self):
        self.queue.clearQueue()
        print("All orders cleared successfully!")

    def view_latest_order(self):
        latest_order = self.queue.getLatest()
        if latest_order:
            print(latest_order)
        else:
            print("No orders in the queue.")

def CLIMain():
    q = queueManagement()
    menu = menuSelection(q)

    

    while True:
        try:
            print("Welcome to the Coffee deliveries management system!")
            print("\nPlease select an option:")
            print("1. Add order")
            print("2. Remove latest order")
            print("3. Remove order by ID")
            print("4. View all orders")
            print("5. Clear all orders")
            print("6. View latest order")
            print("7. Exit")
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            menu.add_order()
        elif choice == 2:
            menu.remove_latest()
        elif choice == 3:
            menu.remove_by_id()
        elif choice == 4:
            menu.view_all_orders()
        elif choice == 5:
            menu.clear_all_orders()
        elif choice == 6:
            menu.view_latest_order()
        elif choice == 7:
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


CLIMain()
