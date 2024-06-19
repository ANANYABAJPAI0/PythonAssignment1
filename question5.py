name=str(input("enter name"))
with open("demo.txt","w") as file:
    file.write(name)