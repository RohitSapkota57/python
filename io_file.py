# f=open("i/text.txt")           ##for read file 
# data=f.read()
# print(data)
# f.close()

file_name_write=input("\nEnter file to write name : ")    ## to write text in file
text=input("\nEnter text to input : ")
f=open(file_name_write,"w")
f.write(text)
f.close()

file_name_read=input("\nEnter file to read name : ")
print("")
f=open(file_name_read)           ##for read file 
data=f.read()
print(data)
f.close()