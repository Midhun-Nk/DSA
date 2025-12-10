count = 0

def greet(name):
    global count      # ✅ tell Python to use global variable
    count = count + 1
    print("Good Morning", name,count)

    if count != 4:
        print("Before Call Count:",count)
        greet(name)
        print("After Call Count:",count)


greet("Mike")
