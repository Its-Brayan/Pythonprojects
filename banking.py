class banking:
    def __init__(self):
        self.budget = int(input("inital budget before conversion"))
        self.initial_currency = int(input("How much money do you want to convert from your budget"))
        self.dollar_rate =  129.89
        self.after_conversion = 0
        self.bills = 0
       

    def converting(self):
        
        self.after_conversion = self.initial_currency/self.dollar_rate
        return self.after_conversion
    def remainder(self):
        return self.budget - self.initial_currency
      
    def  billing(self):
        self.converting()
        self.bills = int(self.after_conversion/100)
        return self.bills 
    def remainder_after_bills(self):
         self.billing()
         self.bills = self.bills * 100
         self.rem_after_bills = self.after_conversion - self.bills
         return self.rem_after_bills
        
              
        
    
    def remainder_after_bills_and_fees(self):
        self.fees = float(input("what are the charges?"))
        self.fees1 = self.dollar_rate+self.fees * self.dollar_rate
        self.initial_currency = int((self.initial_currency/self.fees1)/100)
        return self.initial_currency
banking1 =  banking()
#print(banking1.remainder_after_bills_and_fees())
print(banking1.remainder_after_bills())
#print(banking1.remainder_after_bills_and_fees())




        