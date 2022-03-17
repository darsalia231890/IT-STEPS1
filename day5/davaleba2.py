x = int(input("Enter the x coordinate: "))
y = int(input("Enter the y coodinate: "))

#ფუნქციის გრაფიკი: y = 2

def route(x, y):
    if y == 2:
        return "ძევს"
    else:
        return "არ ძევს"

x = int(input("Enter the x coordinate: "))
y = int(input("Enter the y coodinate: "))

print(route(x, y))