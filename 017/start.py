class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
    
    def displayInfo(self):
        print(f"My id : {self.id}, my username : {self.username}")
        
    

user1 = User(12004, "yanis")

user1.displayInfo()