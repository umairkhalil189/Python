f = int(input("Enter no is Farenheight: "))

def f_2_c(f):
    c= 5*((f-32)/9)
    return c
c= f_2_c(f)
print(f"The temperature is celcius is:  {round(c, 2)}")