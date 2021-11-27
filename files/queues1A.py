class PitStop:
    def __init__(self, car, tire, driver):
        self.car = car
        self.tire = tire
        self.driver = driver

    def display(self):
        print("Finished the Pitstop for {} of team {} with {} tyres.".format(self.driver, self.car, self.tire))

selection = None
pitstop_queue = [] # Initializing list
print("F1 Pitstop")
while(selection != "4"):
    print("Options: ")
    print("1. Add car coming to the pits.")
    print("2. Car has pitted. Pit next car")
    print("3. Display pit queue.")
    print("4. Pack things up, we're done.")
    selection = input("What to do?: ")
    print()
    if selection == "1":
        car = input("Enter car: ")
        # Ferrari, Mercedes, McLaren, Renault, Red Bull... look for F1 teams
        tires = input("Which tires to fit: ")
        # soft, medium, hard, inter, wet
        driver = input("Who is the driver: ")
        pit = PitStop(car, tires, driver)
        
        # Problem 1, put code here
        pitstop_queue.append(pit)
    elif selection == "2":
        # Problem 2, make algorithm for dequeuing a car
        if len(pitstop_queue) > 0:
            pitstop_queue.pop(0)
        else:
            print("No cars in the pit.")
    elif selection == "3":
        # Problem 3, figure out how to display the queue when it is empty
        if len(pitstop_queue) > 0:
            pitstop_queue.display()
        else:
            print("Pit is clear.")