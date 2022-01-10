#Recursive Example Script
#Factorial func
def factorial(number):
  if number==1 or number==0:
    return 1
  else:
    return number*factorial(number-1) 
#fibonacci sequence until 100
def fibonacci():
  i=0
  result=1
  while i<100:
    print(i , end=", ")
    n=result+i
    i=result
    result=n
#example test
print("Factorial value of 5 : ",factorial(5))
print("Fibonacci numbers until 100 : ", end="")
fibonacci()