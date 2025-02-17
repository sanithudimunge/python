import random

class DicePile:
    def __init__(self, init_quantity, init_sides, roll_on_create=False):
        self.set_quantity(init_quantity)
        self.set_sides(init_sides)
        self.__roll_count = 0
        self.rolled = False
        if roll_on_create:
            self.roll()
    
    def __str__(self):
        if self.rolled:
            result_string = str(self.__results)
        else:
            result_string = 'not rolled'
        
        dicescription = self.dicescription()

        return dicescription + ': ' + result_string + ' (roll count: ' + str(self.__roll_count) + ')'
    
    def dicescription(self):
        dicescription = str(self.__quantity) + 'd' + str(self.__sides)
        return dicescription

    def roll(self):
        self.__roll_count += 1
        self.__results = [] # set results to empty list
        for i in range (self.__quantity):
            self.__results.append(random.randint(1, self.__sides))
        self.rolled = True
    
    def get_results(self):
        return self.__results
    
    def get_quantity(self):
        return self.__quantity
    
    def get_sides(self):
        return self.__sides
    
    def get_roll_count(self):
        return self.__roll_count
    
    def get_max_total(self):
        max_total = self.__quantity + self.__sides
        return max_total
    
    def get_average(self):
        if not self.rolled:
            raise AttributeError('dice has to be rolled')
        else:
            average = sum(self.__results)/self.__quantity
            return average
    
    def sort_results():
        if not self.rolled:
            raise AttributeError('dice has to be rolled')
        else:
            self.__results = self.__results.sort()

    def set_quantity(self, new_quantity):
        if int(new_quantity) < 1:
            raise ValueError('dice quantity cannot be less than 1')
        else:
            self.__quantity = int(new_quantity)
            self.__results = None
            self.rolled = False
    
    def set_sides(self, new_sides):
        if int(new_sides) < 2:
            raise ValueError('dice sides cannot be less than 2')
        else:
            self.__sides = new_sides
            self.__results = None
            self.rolled = False
            
my_dice = DicePile(4, 6, True)
their_dice = DicePile(4, 6)

print(my_dice.get_results())
