# this is an intro 

class Enemy:
    """ this class contains all the enemies that we will digit. it has attributes for life and name,
    as well as functions that decrease its health and check its life."""
    
    def __init__(self,name,life):
        """ the init function runs automaticlly when a new object is created. it sets the name and life of the new object """
    
        self._name = name
        self._life = life
        
    def attack(self, damage):
        """this function runs when the enemy is attacted"""
        
        print("oach")
        self._life -= damage
        
    def checklife(self):
            
        if self._life <= 0:
            print("wasted")
            
        else:
            print("{} has {} life left".format(self._name,self._life))
            
    def get_name(self):
        """ this function returns the name of the object."""
        
        return self._name
                
    def get_life(self):
        
        return self._life
# to create an instance of a class, we set it as a varaible 
enemy1= Enemy("Dr evil",10)

# to call a function, we use "dot syntac", the name of the variable followed by a dot and then the function
enemy1.attack(5)
enemy1.checklife()

print("{} has {} life left".format(enemy1.get_name(), enemy1.get_life()))