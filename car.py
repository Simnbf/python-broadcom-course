# Class defines a template for an object
# Usually has two parts:
    # data part for storing values (variables)
    # methods to work with the data (functions)

class Car():
    
    name = 'm2'
    manufacturer = 'bmw'
    honk = False



    def get_manufacturer(self):
        return self.manufacturer
    
    def set_manufacturer(self,n):
        self.manufacturer=n

    def get_honk(self):
        return self.honk
    
    def set_honk(self,n):
        self.honk=n