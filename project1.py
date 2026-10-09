import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','%','&','(',')','*','+']
print("Welcome to Password Generator...")
n_l=int(input("Enter number of letters: "))
n_n=int(input("Enter number of numbers: "))
n_s=int(input("Enter number of symbols: "))
password_list=[]
for i in range(1,n_l+1):
    char=random.choice(letters)
    password_list+=char
for i  in range(1,n_n+1):
    char=random.choice(numbers)
    password_list+=char
for i in range(1,n_s+1):
    char=random.choice(symbols)
    password_list+=char
random.shuffle(password_list)
print(password_list)
password=""
for char in password_list:
    password=password+char
print(password)
