palabra=input("Enter a word: ")

if(len(palabra)>=4):
  print(palabra[1:4])

else:
    while(len(palabra)<4):
        print("The word mus have a minium of 4 caracters")
        palabra=input("Enter a word: ")
    print(palabra[1:4])
