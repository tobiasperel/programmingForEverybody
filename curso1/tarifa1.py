hrs=input("Enter Hours: ")
tarifa=input("Enter rate: ")
hrs=float(hrs)
tarifa=float(tarifa)
if(hrs<=40):
    total=hrs*tarifa
else:
    total=40*tarifa + (hrs-40)*tarifa*1.5
print(total)
