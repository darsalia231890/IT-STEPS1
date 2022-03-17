#algoriTmi aris amocanis amoxsnisTvis saWiro mimdevroba

#ფუნქცია ეს არის ალგორითმი რომელსაც აქვს კონკრეტული სახელი და არის გამოყენებადი

#reusable

#გამოძახებადი
# იმით გამოირჩევა რომ შეგეძლია მოვარგოთ სხვადასხვა არგუმეტებს


#print
#input

# def misalmeba(name):
#     print("gamarjoba, " + name)
    
#     misalmeba(gio)
    
# def gamravleba(a, b):
#     return a * b
# print(gamravleba(5, 10))


# def my_mean(arr):
#     my_sum = 0
#     for element in arr;
#         my_sum += element
#     return mu_sum/len(arr)

# arr = []
# ammount_of_numbers + 



def my_mean(arr):
    my_sum = 0
    for element in arr:
        my_sum += element
    return my_sum/len(arr)

arr = []
ammount_of_numbers = int(input("შეიყვანეთ რამდენი რიცხვის შეყვანა გსურთ: "))

for i in range(ammount_of_numbers):
    x = int(input("შეიყვანეთ რიცხვი " + str(i+1) + " სიისთვის: "))
    arr.append(x)

# arr = [10, 20, 30, 40]

print(my_mean(arr))