class pacman:
 def __init__(self):
    self.touching_ghost = 0
    self.power_pellet_active = 0
    self.touch_power_pellet= 0
    self.touching_dot = 0
    self.has_eaten_all_dots = 0
 def eat_ghost(self):
     self.touching_ghost = input("did he touch a ghost? ")
     self.power_pellet_active=input("does he have a power pellet? ")
     if(self.power_pellet_active=='yes' and self.touching_ghost == 'yes'):
            return True
     else:
           return False
 def score(self):
        self.touch_power_pellet =input('did he touch power pellet ')
        self.touching_dot = input("did he touch a dot? ")
        if(self.touch_power_pellet =="yes" or self.touch_power_pellet =="yes" ):
            return True
        else:
             return False
 def lose(self):
        self.power_pellet_active = input("does he have a power pellet ")
        self.touching_ghost = input("did he touch a ghost ")
        if(self.power_pellet_active =="no" and self.touching_ghost =="yes"):
            return True
        else:
             return False
 def win(self):
        self.has_eaten_all_dots =input("did he eat all dots ")
        self.touching_ghost = input("did he touch any ghost ")
        self.power_pellet_active = input("does he have power pellet ")
        if(self.has_eaten_all_dots=="yes" and self.touching_ghost=="no" and self.power_pellet_active =="yes"):
            return True
        else:
             return False
pacman1 = pacman()
print("option1:find out if he ate the ghost")
print("option2,find out if he scored")
print("option3:find out if he lost")
print("option4:find out if he won")
option = int(input("select your option"))

match option:
     case 1:
          print(pacman1.eat_ghost())
     case 2 :
          print(pacman1.score())
     case 3 :
          print(pacman1.lose())
     case 4:
          print(pacman1.win())
     case _:
          print("please select a valid option")     

