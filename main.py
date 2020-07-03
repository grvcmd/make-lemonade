import time


# Display welcome menu
def welcome():
    print("LETS MAKE SOME LEMONADE!\n")

    print("What you need ...")
    time.sleep(1)
    print("Lemon juice: 2 cups")
    print("Water: 16 cups")
    print("Agave nectar: 2.5 cups")
    print("This will yield 6 servings.")
    time.sleep(1)


class Lemonade:
    def __init__(self, lemon=2, water=16, agave=2.5, init_serving=6):
        self.lemon = lemon
        self.water = water
        self.agave = agave
        self.init_serving = init_serving

        self.servings = None

    def get_servings(self):
        while True:
            try:
                self.servings = int(input("\nNow, how many servings would you like to make: "))
                return self.servings
            except ValueError:
                print("Invalid input. Please try again.")

    def calculate_ingredients(self):
        print("\nTo make {} servings of Lemonade you will need...".format(self.servings))
        time.sleep(1)

        self.lemon = (self.servings / self.init_serving) * self.lemon
        self.water = (self.servings / self.init_serving) * self.water
        self.agave = (self.servings / self.init_serving) * self.agave

        print("{:.2f} cup(s) of lemon juice".format(self.lemon))
        print("{:.2f} cup(s) of water".format(self.water))
        print("{:.2f} cup(s) of agave nectar".format(self.agave))

    def convert_to_gallons(self):
        while True:
            try:
                user_input = str(input("\nDo you need measurements in gallons? (y/n): ")).lower()
                if user_input == 'y':
                    self.lemon = self.lemon / 16
                    self.water = self.water / 16
                    self.agave = self.agave / 16

                    time.sleep(1)

                    print("{:.2f} gallon(s) of lemon juice".format(self.lemon))
                    print("{:.2f} gallon(s) of water".format(self.water))
                    print("{:.2f} gallon(s) of agave nectar".format(self.agave))
                    print("There, now go make Lemonade!")
                    break

                elif user_input == 'n':
                    print("Ok, now go make Lemonade!")
                    break

                else:
                    raise ValueError('Invalid input. Please try again.')

            except ValueError as e:
                print(e)




if __name__ == '__main__':
    welcome()

    cup = Lemonade()
    cup.get_servings()
    cup.calculate_ingredients()
    cup.convert_to_gallons()
