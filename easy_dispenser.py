Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#first personal undertaking after cs50p week0--user inputs how much money he needs and i give the least coins/notes possible
#denominations: 100, 50, 20, 10, 5, 2, 1,50 cents, 20 cents, 10 cents, 5 cents, 2 cents, 1 cent
def main():
    money=clean(input("How much do you need?"))
    #The print money was just to check if my function worked,imma set default value to 0
    print(money)
    bills_100=int(div100(money))
    print(f"You will get {bills_100} 100$ bills")
    bills_50=int(div50(money-bills_100*100))
    print(f"You will get {bills_50} 50$ bills")
    bills_20=int(div20(money-bills_100*100-bills_50*50))
    print(f"You will get {bills_20} 20$ bills")
    bills_10=int(div10(money-bills_100*100-bills_50*50-bills_20*20))
    print(f"You will get {bills_10} 10$ bills")
    bills_5=int(div5(money-bills_100*100-bills_50*50-bills_20*20-bills_10*10))
    print(f"You will get {bills_5} 5$ bills")
    bills_2=int(div2(money-bills_100*100-bills_50*50-bills_20*20-bills_10*10-bills_5*5))
...     print(f"You will get {bills_2} 2$ bills")
...     bills_1=int(div1(money-bills_100*100-bills_50*50-bills_20*20-bills_10*10-bills_5*5-bills_2*2))
...     print(f"You will get {bills_1} 1$ bills") 
...     coins_50c=int(div50c(money-bills_100*100-bills_50*50-bills_20*20-bills_10*10-bills_5*5-bills_2*2-bills_1*1))
...     print(f"You will get {coins_50c} 50 cent coins")
...     coins_20c=int(div20c(money-bills_100*100-bills_50*50-bills_20*20-bills_10*10-bills_5*5-bills_2*2-bills_1*1-coins_50c*0.5))
...     print(f"You will get {coins_20c} 20 cent coins")
...     coins_10c=int(div10c(money-bills_100*100-bills_50*50-bills_20*20-bills_10*10-bills_5*5-bills_2*2-bills_1*1-coins_50c*0.5-coins_20c*0.2))
...     print(f"You will get {coins_10c} 10 cent coins")
...     coins_5c=int(div5c(money-bills_100*100-bills_50*50-bills_20*20-bills_10*10-bills_5*5-bills_2*2-bills_1*1-coins_50c*0.5-coins_20c*0.2-coins_10c*0.1))
...     print(f"You will get {coins_5c} 5 cent coins")
...     coins_2c=int(div2c(money-bills_100*100-bills_50*50-bills_20*20-bills_10*10-bills_5*5-bills_2*2-bills_1*1-coins_50c*0.5-coins_20c*0.2-coins_10c*0.1-coins_5c*0.05))
...     print(f"You will get {coins_2c} 2 cent coins")
...     coins_1c=int(div1c(money-bills_100*100-bills_50*50-bills_20*20-bills_10*10-bills_5*5-bills_2*2-bills_1*1-coins_50c*0.5-coins_20c*0.2-coins_10c*0.1-coins_5c*0.05-coins_2c*0.02))
...     print(f"You will get {coins_1c} 1 cent coins")
... 
... def clean(amount):
...   
...     amount=amount.lstrip('$')
...     #used lstrip to clean the dollar out
...     amount=float(amount)
...     return amount
... 
... def div100(d1):
...     d1=round(d1,2)
...     
...     d1=d1//100
...  
...     return d1
... 
def div50(d2):
    d2=round(d2,2)
   
    d2=d2//50
  
    return d2
    #divides by 50 to get number of 50$ bills    
def div20(d3):
    d3=d3//20
    return d3
    #divides by 20 to get number of 20$ bills
def div10(d4):
    d4=d4//10
    return d4
def div5(d5):
    d5=d5//5
    return d5
def div2(d6):   
    d6=d6//2
    return d6
def div1(d7):
    d7=d7//1
    return d7
def div50c(d8):
    d8=round(d8,2)
   
    d8=d8//0.5
    return d8
def div20c(d9):
    d9=d9//0.2
    return d9
def div10c(d10):
    d10=d10//0.1
    return d10
def div5c(d11):
    d11=d11//0.05
    return d11
def div2c(d12):
    d12=d12//0.02
    return d12
def div1c(d13):
    d13=d13//0.01
    return d13



main()

#learnings

#2.lstrip to clean the dollar sign
#3.round function to avoid floating point imprecision
#4.floor division to get number of bills/coins
#5.f-strings to print output neatly
#6 functions cannot contain periods in their names

#stuff i'd like to learn
#1.set default value when user doesnt input anything

