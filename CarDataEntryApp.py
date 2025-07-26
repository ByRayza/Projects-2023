# Python Vehicle Data Entry App

class AutomobileInventory:
    def __init__(self):
        self.inventory = []

    def add_automobile(self):
        make = input("Enter the make of the car: ")
        model = input("Enter the model of the car: ")
        color = input("Enter the color of the car: ")
        year = int(input("Enter the year of the car: "))
        mileage = float(input("Enter the mileage of the car: "))
        automobile = [make, model, color, year, mileage]
        self.inventory.append(automobile)

    def remove_automobile(self):
        auto_name = input("Enter the car name to remove: ")
        found_automobile = None
        for automobile in self.inventory:
            if automobile[0] == auto_name:
                found_automobile = automobile
                break

        if found_automobile:
            self.inventory.remove(found_automobile)
            print(f"{auto_name} has been removed from the inventory.")
        else:
            print(f"{auto_name} not found in the inventory.")

    def update_automobile(self):
        auto_name = input("Enter car name to update: ")
        found_automobile = None
        for automobile in self.inventory:
            if automobile[0] == auto_name:
                found_automobile = automobile
                break

        if found_automobile:
            make = input(f"Enter the new make (leave blank to keep current: {found_automobile[0]}): ") or found_automobile[0]
            model = input(f"Enter the new model (leave blank to keep current: {found_automobile[1]}): ") or found_automobile[1]
            color = input(f"Enter the new color (leave blank to keep current: {found_automobile[2]}): ") or found_automobile[2]
            year = int(input(f"Enter the new year (leave blank to keep current: {found_automobile[3]}): ") or found_automobile[3])
            mileage = float(input(f"Enter the new mileage (leave blank to keep current: {found_automobile[4]}): ") or found_automobile[4])
            found_automobile[0] = make
            found_automobile[1] = model
            found_automobile[2] = color
            found_automobile[3] = year
            found_automobile[4] = mileage
            print(f"{auto_name} has been updated.")
        else:
            print(f"{auto_name} is not found in the inventory.")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for automobile in self.inventory:
                file.write(f"{automobile[0]},{automobile[1]},{automobile[2]},{automobile[3]},{automobile[4]}\n")

if __name__ == "__main__":
    automobile_inventory = AutomobileInventory()

    while True:
        print("\n1. Add item\n2. Remove item\n3. Update item\n4. Save to file\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            automobile_inventory.add_automobile()
        elif choice == '2':
            automobile_inventory.remove_automobile()
        elif choice == '3':
            automobile_inventory.update_automobile()
        elif choice == '4':
            filename = input("Enter the filename to save: ")
            automobile_inventory.save_to_file(filename)
            print(f"Inventory saved to {filename}")
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")
