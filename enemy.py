# this is an intro 

class Enemy:
    """ this class contains all the enemies that we will digit. it has attributes for life and name,
    as well as functions that decrease its health and check its life."""
    
    _life = 3
    
    
    def attack(self):
        """this function runs when the enemy is attacted"""
        
        print("oach")
        self._life -= 1
        
        def checklife(self):
            
            if self.life <=0:
                print("wasted")
                
            else:
                print(self._life)
                
# to create an instance of a class, we set it as a varaible 
enemy1= Enemy()

# to call a function, we use "dot syntac", the name of the variable followed by a dot and then the function
enemy1.attact()
enemy1.checklife()