class User:
        
    def __init__(self, userID, username):
        self.id = userID
        self.username = username  
        self.followers = 0 # Default  
        self.following = 0

    def userFollow(self, user):
        user.followers += 1
        self.following += 1
        

userOne = User("001", "Zechi")
print(userOne.id)

userTwo = User("002", "Tom")
print(userTwo.id)

userOne.userFollow(userTwo)
print(userOne.following)
print(userTwo.followers)