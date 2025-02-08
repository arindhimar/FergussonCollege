f1 = input("Enter name of file 1")
f2 = input("Enter name of file 2")

ff = open(f1+".txt","r")



tf = open(f2+".txt","w")


tf.write(ff.read())