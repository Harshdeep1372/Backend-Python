class FruitManager:
    fruit_stock = {}

    def add_fruit_stock(self):
        fruit_name = input("Enter fruit Name: ")
        quantity = input("Enter qty (in kg): ")
        price = input("Enter price: ")

        if fruit_name in self.fruit_stock:
            self.fruit_stock[fruit_name]['qty'] += int(quantity)
            self.fruit_stock[fruit_name]['price'] = price
        else:
            self.fruit_stock[fruit_name] = {'qty': int(quantity), 'price': price}

        print("Fruit stock added successfully.")

    def view_fruit_stock(self):
        print("Fruit Stock:")
        print(self.fruit_stock)

    def update_fruit_stock(self):
        fruit_name = input("Enter fruit Name to update: ")
        if fruit_name in self.fruit_stock:
            quantity = input("Enter new qty (in kg): ")
            price = input("Enter new price: ")

            self.fruit_stock[fruit_name]['qty'] = int(quantity)
            self.fruit_stock[fruit_name]['price'] = price

            print(f"{fruit_name} stock updated successfully.")
        else:
            print(f"{fruit_name} not found in the stock.")

def main():
    transactions = []

    while True:
        print("WELCOME TO FRUIT MARKET")
        print("1) Manager\n2) Customer")

        role = input("Select your Role: ")

        if role == "1":
            fruit_manager = FruitManager()

            while True:
                print("Fruit Market Manager")
                print("1) Add Fruit Stock\n2) View Fruit Stock\n3) Update Fruit stock")

                option = input("Enter your choice : ")

                if option == "1":
                    fruit_manager.add_fruit_stock()
                elif option == "2":
                    fruit_manager.view_fruit_stock()
                elif option == "3":
                    fruit_manager.update_fruit_stock()
                else:
                    print("Invalid option.")

                more_operations = input("Do you want to perform more operations? Press 'y' for yes and 'n' for no: ")
                if more_operations.lower() != 'y':
                    break

        elif role == "2":
            print("Customer")
            # Implement customer functionality here

        else:
            print("Invalid role.")

        more_roles = input("Do you want to switch roles? Press 'y' for yes and 'n' for no: ")
        if more_roles.lower() != 'y':
            break

if __name__ == "__main__":
    main()
