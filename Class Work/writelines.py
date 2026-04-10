# opening file in write mode
filev=open("first.txt","w")
sentences=[]
# writting sentence into file
print("Write any five sentences")
for i in range(5):
   # input from user
   sentence=input()
   sentences.append(sentence)
   print("___________")
# writting multiple sentence 
filev.writelines(sentences)
print("Data successfully written")
#closing file 
filev.close()
