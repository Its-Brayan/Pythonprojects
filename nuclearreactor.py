class nuclearreactor:
    def __init__(self):
     self.temperature = int(input("whats the nuclears temperature?"))
     self.neurons_emitted = int(input("How many neurons are emitted"))
     
    
    def is_critically_balanced(self):
      self.critical_balance = self.temperature * self.neurons_emitted
      if(self.temperature > 40):
          print("the temperature is too high")
      else:
         print("the temperature is okay")
      if(self.neurons_emitted>150):
         print("too many neurons emmitted")
      else:
         print("neurons are okay")
      if(self.critical_balance > 1000):
         print("nulcear reactor is not balanced!!")
      else:
         print("nuclear reactor is balanced well")
    def reactor_efficiency(self):
        self.voltage = float(input("whats its voltage"))
        self.current = float(input("whats its current"))
        self.power_output =self.voltage * self.current
        if(self.power_output<=200 and self.power_output >=100):
           print("Green Zone")
        elif(self.power_output >=201 and self.power_output <=400):
           print("Orange Zone")
        elif(self.power_output>=401 and self.power_output <=600):
           print("Red Zone")
        else:
           print("Black Zone")
    def fail_safe(self, threshhold):
      self.threshhold1 = self.temperature * self.neurons_emitted
      if(self.threshhold1 <0.9*threshhold):
         print("LOW")
      elif(self.threshhold1 >=0.1*threshhold):
         print("NORMAL")
      else:
         print("DANGER")
nuclear = nuclearreactor()
print("option1:if the nuclear reactor is critically balanced")
print("option2:reactor efficiency")
print("option3:fail safe")
options =int(input("which option do you want to check?"))
match options :
    case 1 :
      nuclear.is_critically_balanced()
    case 2 :
      nuclear.reactor_efficiency()
    case 3 :
      nuclear.fail_safe(5000)
    case _:
      print("please select another option")
    

       

