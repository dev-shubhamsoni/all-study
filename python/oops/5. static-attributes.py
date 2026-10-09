# instance attributes - are unique ideal for storing object specific data
# static attributes - share amond all objects among class, for consistent data

class User:
    # static attribute
    user_count = 0
    
    def __init__(self, name, age):
        #instance attribute - created with init
        self.name = name
        self.age = age
        User.user_count += 1
        
    def display_user(self):
        print(f"user {self.name}, {self.age}")
    
    

user1 = User("Shuhbam", 26)

user1.display_user()

print(User.user_count)