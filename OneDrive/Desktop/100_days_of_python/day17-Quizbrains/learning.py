class User:
    #pass #we are writing pass to leave the class empty.If we dont use it there will be error at the next line
    def __init__(self , user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0 # default value
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Naitik")
user_2 = User("002", "Harsh")
user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)




