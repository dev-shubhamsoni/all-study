# Why SOLID
# Scability - Adding new features becomes straight forward
# Maintainability - Changes in one part of system ahve miniamla imapct on others
# Testability - Decoupled design make unit testing easier
# Readibility - More readable, clear seperation of concrns.

### Single Responsibility principle

# This principle states that A class should have only one reason to change which means every class should have 
# a single responsibility or single job or single purpose. In other words, a class should have only one job or
# purpose within the software system.

# Imagine a baker who is responsible for baking bread. The baker’s role is to focus on the 
# task of baking bread, ensuring that the bread is of high quality, properly baked, and meets 
# the bakery’s standards.

# However, if the baker is also responsible for managing the inventory, ordering supplies, 
# serving customers, and cleaning the bakery, this would violate the SRP. Each of these tasks 
# represents a separate responsibility, and by combining them, the baker’s focus and effectiveness
# in baking bread could be compromised.

class BreadBaker:

    def bakeBread(self):
        print("Baking high-quality bread...")

    def manageInventory(self):
        print("Managing inventory...")

    def orderSupplies(self):
        print("Ordering supplies...")

    def serveCustomer(self):
        print("Serving customers...")

    def cleanBakery(self):
        print("Cleaning the bakery...")


if __name__ == "__main__":
    baker = BreadBaker()

    baker.bakeBread()
    baker.manageInventory()
    baker.orderSupplies()
    baker.serveCustomer()
    baker.cleanBakery()
    
    
# To adhere to the SRP, the bakery could assign different roles to different individuals or teams. 
# For example, there could be a separate person or team responsible for managing the inventory, 
# another for ordering supplies, another for serving customers, and another for cleaning the bakery.

# By adhering to the SRP, the code becomes more maintainable and easier to understand. Changes in one 
# class do not affect unrelated parts, enhancing readability and reducing complexity. Each class has a 
# clear and focused responsibility, making the system more modular and easier to manage.

# Class for baking bread
class BreadBaker:
    def bakeBread(self):
        print("Baking high-quality bread...")


# Class for managing inventory
class InventoryManager:
    def manageInventory(self):
        print("Managing inventory...")


# Class for ordering supplies
class SupplyOrder:
    def orderSupplies(self):
        print("Ordering supplies...")


# Class for serving customers
class CustomerService:
    def serveCustomer(self):
        print("Serving customers...")


# Class for cleaning the bakery
class BakeryCleaner:
    def cleanBakery(self):
        print("Cleaning the bakery...")


class Bakery:
    @staticmethod
    def main():
        baker = BreadBaker()
        inventory_manager = InventoryManager()
        supply_order = SupplyOrder()
        customer_service = CustomerService()
        cleaner = BakeryCleaner()

        # Each class focuses on its specific responsibility
        baker.bakeBread()
        inventory_manager.manageInventory()
        supply_order.orderSupplies()
        customer_service.serveCustomer()
        cleaner.cleanBakery()


if __name__ == "__main__":
    Bakery.main()