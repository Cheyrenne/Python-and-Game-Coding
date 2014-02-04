# Simple Critter
#Demonstrates class attributes and static methods 

class Critter(object):
    """A virtual pet"""
    total = 0

    @staticmethod
    def status():
        print("\nYou have ", Critter.total," critters")
        
    def __init__(self, name, hunger = 0, boredom = 0):
        print("A new critter,", name,",has been born!")
        self.__name = name
        self.hunger = hunger
        self.boredom = boredom
        Critter.total += 1

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    def eat(self, food):
        print("Brruppp. Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print("Wheee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()
        
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("A critter's name can't be empy.")
        else:
            self.__name = new_name
            print("Name change successful.")

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 11 <= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m


    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now.\n")
        self.__pass_time()

    def __str__(self):
        rep = "Critter object\n"
        rep += "name: " + self.name + "\n"
        return rep

# main
def main():

    import pickle, shelve
    
    crit_name = input("What do you want to name your critter?: ")
    crit = Critter(crit_name)

    choice = None
    while choice != "0":
        print \
        ("""
        Critter Caretaker
        0 - Quit
        1 - Listen to your critter
        2 - Feed your critter
        3 - Play with your critter
        """)
        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Saving your critter's stats")
            f = open("critters.dat","wb")
            pickle.dump(crit, f)
            print("Good-bye.\n")


        # listen to your critter
        elif choice == "1":
            crit.talk()

        # feed your critter
        elif choice == "2":
            amount = input("How much to feed your critter? (Enter a number 1-10): ")
            amount = int(amount)
            crit.eat(amount)

        # play with your critter
        elif choice == "3":
            crit.play()

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
("\n\nPress the enter key to exit.")
