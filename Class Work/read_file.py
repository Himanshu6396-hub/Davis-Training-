# to read data
filev=open("first.txt","r")
# to check file exists or not 
if(filev):
   # to read file
   data=filev.read()
   print( data)
   print("_____________")
   print("no of characters",len(data))
   # closing file
else:
   print("File doesn't exist")
