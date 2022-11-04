def computepay(h,r):
    if(h<=40):
        tarifa=h*r
    else:
        tarifa=r*40+r*(h-40)*1.5
    return tarifa

hrs = input("Enter Hours: ")
hrs=float(hrs)
rate= input("Enter rate: ")
rate=float(rate)
p = computepay(hrs,rate)
print("Pay",p)
