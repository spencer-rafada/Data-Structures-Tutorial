class FIA_Ruling:
    class Driver:
        def __init__(self, name, number, problem):
            self.name = name
            self.number = number
            self.problem = problem
        
        def __str__(self):
            return self.name + " -" + self.number + "- : " + self.problem

    def __init__(self, max_size):
        """
        Initialize the empty queue using a Python list.
        """
        self.queue = []
        self.max_size = max_size

    def add_new_report(self):
        """
        Prompt the user for the team's incident report during the race
        """
        if len(self.queue) > self.max_size:
            print("Maximum Number of Reports Currently Under Investigation.")
            return
        
        name = input("Driver Name: ")
        number = input("Driver Number: ")
        problem = input("Problem Report: ")

        # Create the driver object and add it to the queue
        driver = FIA_Ruling.Driver(name, number, problem)
        # 

    def serve_ruling(self):
        """
        Dequeue the next driver and display the information
        """
        pass

reports = FIA_Ruling(15)
print("Task 1")
# Make sure that the functions are working and there are 5 reports by
# the end of the program.
reports.add_new_report()
reports.add_new_report() 
reports.serve_ruling()
reports.add_new_report()
reports.add_new_report()
reports.add_new_report()
reports.add_new_report() # Must have 5 reports

