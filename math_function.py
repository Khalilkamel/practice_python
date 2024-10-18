def abss(num):
    if num>=0:
        return num
    return -num
    
def max_num(num1,num2):
    num1=abss(num1)
    num2=abss(num2)
    if num1>num2:
        return num1
    return num2
print(max_num(2,3))
print(max_num(2,-3))

