import random
# colors
yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'
# code
print (red+b+"""
         ██████╗        ██████╗ ███████╗███╗   ██╗
         ██╔══██╗      ██╔════╝ ██╔════╝████╗  ██║
         ██████╔╝█████╗██║  ███╗█████╗  ██╔██╗ ██║
         ██╔═══╝ ╚════╝██║   ██║██╔══╝  ██║╚██╗██║
         ██║           ╚██████╔╝███████╗██║ ╚████║
         ╚═╝            ╚═════╝ ╚══════╝╚═╝  ╚═══╝
                                                  Monster industries 
"""+b+red)

print (gren+b+"              <===[[ coded by monster 2.0 ]]===>"+b+gren)
print (" ")
print (yellow+b+"        <---( dark team )--->"+b+yellow)
print (" ")

length=int(input(cyan+b+"Enter The Length Of The Password: "+b+cyan))
print (" ")
print (yellow+b+"-----> password  generated <----"+b+yellow)
print (" ")
char="0123456789"
password= (gren+b+"077 "+b+gren)
for i in range(length):

     password+=random.choice(char)

print(password)
print (" ")
print (yellow+b+"-----> grab your password <----"+b+yellow)
print (" ")
