def main():
 name = str(input("enter your name\n"))
 print("hello",name)

 age = int(input("what's your age?\n"))

 if(age<=10):
    print("you are a child\n")

 if(age>=11 and age<=18):
    print("you are a teenager\n")

 if (age>18):
    print("you are an adult\n")

main()
