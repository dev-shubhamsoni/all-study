# getter and setter properties, previusly we created getter & setter methods

# In Python, we use the @property decorator in classes to access a method 
# like an attribute. It lets you control how a value is retrieved, 
# calculated, or updated without changing the way you use the object.

# The main reasons to use property are:
# Encapsulation: Control access to an object's data.
# Validation: Prevent invalid values from being assigned.
# Computed attributes: Calculate a value dynamically instead of storing it.
# Cleaner syntax: Use obj.name instead of obj.get_name().


class User:
    
    def __init__(self, name, email, password):
        self.name = name
        self._email = email
        self.password = password
        
    @property
    def email(self):
        print("Email Accessed")
        return self._email
    
    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self._email = new_email


user1 = User("Shuhbam", "s@g.com", "pass")
print(user1.email)
user1.email = "test"
print(user1.email)