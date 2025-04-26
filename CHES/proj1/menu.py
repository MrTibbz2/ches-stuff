from typing import List, Tuple
from dataclasses import dataclass

@dataclass
class menuItem:
    BlendName: str
    blendRoast: str
    blendID: int
    blendPrice: float

# maybe some time I'll add a database but for now this will do. either way it wont be hard to make later on.

class menu:
    def __init__(self):
        self.menuItems: List[menuItem] = [] # list of menu items
        self.menuItems.append(menuItem("Highland Floral", "Light", 1, 22.50))
        self.menuItems.append(menuItem("Morning Lilt", "Light", 2, 19.00))
        self.menuItems.append(menuItem("Copper Trail", "Medium", 3, 18.50))
        self.menuItems.append(menuItem("Amber Echo", "Medium", 4, 24.50))
        self.menuItems.append(menuItem("Obsidian Bloom", "Dark", 5, 28.75))
        self.menuItems.append(menuItem("Noir Voyage", "Dark", 6, 26.00))
        self.menuItems.append(menuItem("Black Summit", "Medium", 7, 23.00))
    
    def showmenu(self):
        return self.menuItems # basically we print out the menu so that the user can choose
                            # again, im gonna pull out the caveman technique to make sure they pick a valid item, by just iterating over the items

    def calculateTotal(self, items: list[tuple[int, int]]): # tuple to store which items (by ID) and how many
        # find item total for id -> find amount, multiply -> add to buffer
        orderTotal = 0.0
        for item in items: # item loop
            id = item[0]
            itemamount = item[1]
            for menuItem in self.menuItems: # find item price
                if menuItem.blendID == id:
                    orderItemCost = menuItem.blendPrice
                    cost = orderItemCost * itemamount
                    orderTotal = orderTotal + cost      # sorry this is barely readable, but it works well enough so

        return orderTotal

                    

    # test usage
items = [(2, 3), (1, 1)] # should equal roughly 79.50?
m = menu()
print(m.calculateTotal(items))  
