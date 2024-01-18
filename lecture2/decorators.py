def announce(f): #Decorator
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper

@announce #Add the announce decorator to the function
def hello():
    print("Hello, world!")

hello()
