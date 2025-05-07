class baking:
    def __init__(self):
       self.baking_time = int(input("How much time will you use?"))
    def baking_time_left(self):
        self.time_used = int(input("how many minutes/hours did you use"))
        return self.baking_time - self.time_used
    def preparation_time(self):
        self.layers = int(input("how many layers did you  use?"))
        #preparation time is based on the number of layers
        self.time = int(input("expected prep time for each layer"))
        self.preptime = self.layers * self.time
        return self.preptime

    def total_elapsed_time(self):
        return self.preptime+ self.time_used

baking1 = baking()
print(baking1.baking_time_left())
print(baking1.preparation_time())
print(baking1.total_elapsed_time())