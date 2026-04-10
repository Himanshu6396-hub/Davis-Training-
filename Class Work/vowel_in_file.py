# to read data
filev=open("first.txt","r")
# to check file exists or not 
if(filev):
   # to read file
   data=filev.read()
   if len(data)>0:# vowel count
    vowels = "aeiouAEIOU"
    count = 0

    for ch in data:
       if ch in vowels:
          count += 1
   else:
       print( "File is empty")
   print("no of vowels:", count)
   # closing file
else:
   print("File doesn't exist")
