greetings = input("").strip().lower()
greetings = greetings[0:5]
if(greetings=="hello"):
    print("$0")
elif(greetings[0]=="h"):
    print("$20")
else:
    print("$100")
