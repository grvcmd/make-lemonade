import time


class Lemonade:
    def __init__(self, lemon, water, agave, servings):
        self.lemon = lemon
        self.water = water
        self.agave = agave
        self.servings = servings

    # Display welcome menu
    def welcome(self):
        print("LETS MAKE SOME LEMONADE!\n")

        print("What you need ...")
        time.sleep(1)
        print("Lemon juice: 2 cups")
        print("Water: 16 cups")
        print("Agave nectar: 2.5 cups")




if __name__ == '__main__':
    cup = Lemonade()
    cup.welcome()




