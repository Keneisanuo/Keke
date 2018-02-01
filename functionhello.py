def hello():
    name=str(input("enter your name"))
    if name:
        print ("hello" +str(name))
    else:
            print("hello world")
            return
    hello()
