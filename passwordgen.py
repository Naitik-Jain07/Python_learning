import random
import string

number = ['1','2','3','4','5','6','7','8','9','0']
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
special_char= ['!','@','#',"$",'%',"^",'&','*',"(",")"]

x=int(input("many many letters in pass"))
y=int(input("how many symbols"))
n=int(input('how many numbers'))

# #EASY ONE
# password=''
# for char in range (1,x+1):
#     password+= random.choice(alphabet)
    
# for char in range(1,y+1):
#     password+= random.choice(special_char)

# for char in range(1,n+1):
#     password += random.choice(number)

# print (password) 


#HARD PASSWORD
password_list= []
for char in range (1,x+1):
    password_list.append(random.choice(alphabet))
    
for char in range(1,y+1):
    password_list.append(random.choice(special_char))

for char in range(1,n+1):
    password_list.append(random.choice(number))

print(password_list)
random.shuffle(password_list)
print(password_list)

password=''
for char in password_list:
    password+= char

print(f"Password is {password}")
