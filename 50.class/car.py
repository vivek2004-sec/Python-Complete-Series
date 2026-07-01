


class car: 
    def __init__(self, model, year, color, for_sale): 
        '''
        __init__ is a special method in Python that runs automatically when 
         you create an object from a class. It's called the constructor.
        '''
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        
    def drive(self):
        print(f"You drive the {self.model}.")
        
    def stop(self):
        print(f"You stop the {self.model}.")
    