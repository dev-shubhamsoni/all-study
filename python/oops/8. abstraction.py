# Abstraction in Python is an OOP concept where you hide implementation 
# details and expose only the essential functionality to the user.

# For example, when you use your BankAccount, you need to know how to call deposit() 
# and withdraw(). You don't need to know exactly how the class performs its 
# internal calculations or updates the balance.

# Abstraction gives a high level interface for users  so users dont ahve to worry about
# complex details

# Hides unnecessary details

class EmailService:
    
    def _connect(self):
        print("Connecting to service")
        
    def _auth(self):
        print("authenticated")
    
    def send_email(self):
        self._connect()
        self._auth()
        print("send email success")
        

user = EmailService()
user.send_email()

# with abstraction we dont have to worry about methods like connect
# or auth, user just have to use send email and we are good to go.

