class Car:
    class Driver:
        def __init__(self, name, number, problem):
            self.name = name
            self.number = number
            self.problem = problem
        
        def __str__(self):
            return self.name + " -" + self.number + "- : " + self.problem