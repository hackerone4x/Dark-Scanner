# import socket
# o = open("file.txt",'w')

# for i in range(10001):
#     Data = o.writelines(str(i)+" ")

# o.close()

o = open("file.txt","r")
so = o.readlines()
print(so)
o.close()