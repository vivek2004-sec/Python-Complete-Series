


class car: 
    def __init__(self, model, year, color, for_sale): 
        '''
        __init__ is a special method in Python that runs automatically when 
         you create an object from a class. It's called the constructor.
         It initializes the data of respective object.
        '''
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        
    def drive(self):
        print(f"You drive the {self.color} {self.model}.")
        
    def stop(self):
        print(f"You stop the {self.color} {self.model}.")
    
    def describe(self):
        print(f"car details:\n year = {self.year}\n color = {self.color}\n status = {self.for_sale}")