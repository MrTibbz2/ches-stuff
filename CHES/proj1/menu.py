from typing import List, Tuple
from dataclasses import dataclass

@dataclass
class menuItem:
    BlendName: str
    blendRoast: str
    blendID: int
    blendPrice: float

# maybe some time I'll add a database but for now this will do

class menu:
    def __init__(self):
        self.menuItems: List[menuItem] = [] # list of menu items
        self.menuItems.append(menuItem("Highland Floral", "Light", 1, 22.50))
        self.menuItems.append(menuItem("Morning Lilt", "Light", 2, 19.00))
        self.menuItems.append(menuItem("Copper Trail", "Medium", 2, 18.50))
        self.menuItems.append(menuItem("Amber Echo", "Medium", 3, 24.50))
        self.menuItems.append(menuItem("Obsidian Bloom", "Dark", 4, 28.75))
        self.menuItems.append(menuItem("Noir Voyage", "Dark", 5, 26.00))
        self.menuItems.append(menuItem("Black Summit", "Medium", 6, 23.00))
