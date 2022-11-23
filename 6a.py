import random # Random number generator library

class RandomGenerator:
    __amount = None
    __minRange = None
    __maxRange = None
    
    
    def __init__(self, amount:int, minRange:int, maxRange:int):
        self.__amount = amount
        self.__minRange = minRange
        self.__maxRange = maxRange
    
    
    # Our magic function
    def magic(self):

            lst = [] # Empty list for results
            
            # Iterate amount
            for i in range(0,self.__amount):
                # Add random number to list
                lst.append(random.randint(self.__minRange, self.__maxRange))
            return lst # return the completed list

amount = 10
minRange = 5
maxRange = 80

# Precondition 1 : Verify data types
if type(amount) == int and type(minRange) == int and type(maxRange) == int:
    # Precondition 2 : Verify valid number range
    if amount > 0 and minRange >0 and minRange < maxRange:
        rg = RandomGenerator(amount, minRange, maxRange) # Instansiate class
        # Generate random numbers and store in result
        result = rg.magic()
        # Postcondition 1 : Verify length of result list
        if len(result) == amount:
            # Postcondition 2 : Verify first element in list is within range
            if result[0] in range(minRange, maxRange):
                print(result)
            
            