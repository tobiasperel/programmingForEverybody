texto=open("texto.txt")
for line in texto:
    line=line.rstrip()
    if line.startswith("Okay"):
        print(line)
texto= texto.read()
print(texto[:35])
print(len(texto))
