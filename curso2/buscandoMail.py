archivo = input("Enter file name: ")
archivo=open(archivo)
contador=0
for line in archivo:
    line=line.rstrip()
    if len(line)>2 and line.startswith("From "):
       wds=line.split()
       #print(line)
       contador+=1

print("There were",contador, "lines in the file with From as the first word")
       print(wds[1])
