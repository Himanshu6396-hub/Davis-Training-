# to read data
filev = open("first.txt", "r")

# to check file exists or not 
if(filev):
    # to read first line
    data = filev.readline()

    if(data):
        print("content of file")
        
        while(data):
            print(data)
            data = filev.readline()   # next line read
    else:
        print("File is empty")

    filev.close()
else:
    print("File doesn't exist")
