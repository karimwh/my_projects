answer = input( "hey man : ")
answer = answer.strip().lower()

if answer.startswith("hello"):
    print("0")
elif answer.startswith("h"):
    print("20")
else:
    print("100")