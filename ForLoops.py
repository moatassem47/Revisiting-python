# names = ["moatassem", "alex", "mohammed", "ali"]
# # print(names[3])
# for i in range(0 , len(names)):
#     print("the item in the index "+str(i) + " is "+ names[i])
NumberOfPeople = int(input("how many people?\n"))
names = []
for i in range(0,NumberOfPeople):
    name = str(input("add name: "))
    names.append(name)
print(names)