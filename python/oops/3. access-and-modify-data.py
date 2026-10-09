# We can access & modify attributes, which is wrong as anyone can modify
# so best is we make it private and use setter and getter for it
# we can use _ in front of variable to make it private - self._email
# Python will not give error if we try to access but it is a not recommended istead set a getter to acess
# We can actually make variable prvate using __ double underscore before the name
# self.__email
# Protected is single _ and Private (Name Mangled) is __ 

# Generally protected is used everywhere

from datetime import datetime

class User:
    
    def __init__(self, name, email, password):
        self.name = name
        self._email = email
        self.password = password
        
    def say_hi_to_user(self, user):
        print(f"Sending Message to {user.name}: Hi {user.name}, it's {self.name}")
    
    def get_email(self):
        return self._email
        
    def set_email(self, new_email):
        print(f"Email accessed at {datetime.now()}")
        self._email = new_email
         

user1 = User("Shubham", "ss@gmail.com", "test@123")
user2 = User("Ray", "rr@gmail.com", "test@123")

user1.say_hi_to_user(user2)

print(user1.get_email())
user1.set_email("ssoni608")
print(user1.get_email())

# Consenting Adults Philosiphy  - Developers are trusted that they follow conventions 