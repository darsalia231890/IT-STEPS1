#შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა რამე სტრინგი
#დაითვლის ამ სტრინგში ასო "i"ს რაოდენობას და დააბრუნებს რიცხვად ამ მნიშვნელობას

from re import I


def i_ft(name):
    ft = name.count("i")
    return ft

print(i_ft("xevi"))


                

#შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა რაღაც რიცხვი
#დააბრუნოს მნიშვნელობად 1-იდან ამ რიცხვამდე რიცხვების ჯამი.
#მაგალითად 4 -->   1+2+3+4 = 10

def ricxvi(x):
     my_sum = 0
     for i in range(x):       
          my_sum += i 
     return my_sum
print(ricxvi(10))






    
    
 