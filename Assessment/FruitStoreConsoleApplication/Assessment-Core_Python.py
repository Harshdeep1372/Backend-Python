class FruitManager:
    fruit_stock = {}

    def add_fruit(self):
        fruit_n = input("Enter fruit Name: ")
        quan = input("Enter qty (in kg): ")
        price = input("Enter price: ")

        if fruit_n in self.fruit_stock:
            self.fruit_stock[fruit_n]['qty'] += int(quan)
            self.fruit_stock[fruit_n]['price'] = int(price)
        else:
            self.fruit_stock[fruit_n] = {'qty': int(quan), 'price': price}

        print("Fruit add successfully adddeddd.")

    def view_fruit(self):
        print("Fruit Stock:")
        print(self.fruit_stock)

    def update_fruit(self):
        fruit_n = input("Enter fruit to updateddd: ")
        if fruit_n in self.fruit_stock:
            quan = input("Enter new quantaity (in kg....): ")
            price = input("Enter new price: ")

            self.fruit_stock[fruit_n]['qty'] += int(quan)
            self.fruit_stock[fruit_n]['price'] = int(price)

            print(f"{fruit_n} Fruit Detaails update successfullyyyy.....")
        else:
            print(f"{fruit_n} not found in the furit stock.")
class FruitCoustmer:
    view_fruit=FruitManager.view_fruit
    print(view_fruit)

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
                print("1) Add Fruit In Stock\n2) View Fruit Stock\n3) Update Fruit In stock")

                option = input("Enter your choice : ")

                if option == "1":
                    fruit_manager.add_fruit()
                elif option == "2":
                    fruit_manager.view_fruit()
                elif option == "3":
                    fruit_manager.update_fruit()
                else:
                    print("Invalid option you Choose.")

                more_operations = input("Do you want to perform more operations? Press 'y' for yes and 'n' for no: ")
                if more_operations.lower() != 'y':
                    break

        elif role == "2":
            print("Customer")
            print(FruitCoustmer)

        else:
            print("Invalid role.")

        more_roles = input("Do you want to switch roles? Press 'y' for yes and 'n' for no: ")
        if more_roles.lower() != 'y':
            break

if __name__ == "__main__":
    main()
