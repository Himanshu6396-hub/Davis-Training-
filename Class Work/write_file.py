# opening file in write mode
filev=open("first.txt","w")
# writting sentence into file
print("Write any five sentences")
for i in range(5):
   # input from user
   sentence=input()
   filev.write(sentence)
   print("___________")
print("Data successfully written")
#closing file 
filev.close()
