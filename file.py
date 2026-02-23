'''
>In File handling  we are going to open a perticular text file, and write on it
or read the content present on it using python functions.
>For open ing an file we use open function
>open is a builtin function used to open file in 3 different modes:
1.write (w)
2.append (a)
3.read (r)
syntax:
-------
var = open(path_of_file,mode)
>open function returbs file obj
>if you are opening a file then you need to close it after the operation is done
by using close()
#-------------Write mode---------------------------------------
>used for writing somthing in a file, there are 2 functions for writing
>1.write()
>syntax:
fo.write(data)
'''
##fo = open('D:/files/Qspiders/Notes/M216/data1.txt','w')
##fo.write('hello good morning!!!\nHow are you doing?')
##fo.close()

##if we have data in the form of collection we can use fo.writelines(coll)
##fo = open(r'D:\files\Qspiders\Notes\M216\data2.txt','w')
##fo.writelines(('Happy New Year 2026\n','May all your wishes come true this year'))
##fo.close()
##print('😊')
'''
>append mode is used when you want to add some text in a file which already has some
data in it.
>if file dosent exist then it will create just like write mode
synatx:
open('path','a')
'''
##fo = open(r'D:\files\Qspiders\Notes\M216\data2.txt','a')
##fo.write('\nGod bless you!!')
##fo.close()

##fo = open(r'D:\files\Qspiders\Notes\M216\data3.txt','a')
##fo.write('append mode is used here')
##fo.close()

'''
If we want to read any file that file should exist.
1)fo.read() --->will read the entire data in the form of a single string
2)fo.readline()--->read the data line by line
3)fo.readlines()--->read the data in the form of list,every sentece will be an item.
'''
##f = open(r'D:\files\Qspiders\Notes\M216\pan_cake.txt','r')
##a = f.read()
##print(a)
##f.close()


##f = open(r'D:\files\Qspiders\Notes\M216\pan_cake.txt','r')
##a = f.readline()
##b = f.readline()
##print(a)
##print(b)
##f.close()


##f = open(r'D:\files\Qspiders\Notes\M216\pan_cake.txt','r')
##l = f.readlines()
##print(l)
##f.close()


'''
AQ
create a file in a specific folder and write hello world on it
and read it using read().
'''

'''
context manager syntax:
if we are using this syntax , no need to use close function
syntax1:
with open(path,mode) as file_obj_name :
    SB
syntax2:
with open(path,mode) as v1 , open(path,mode) as v2...:
    SB
'''

##with open(r'D:\files\Qspiders\Notes\M216\d1.txt','w') as fo :
##    fo.write('We have learned new context manager syntax.')
    
##with open(r'D:\files\Qspiders\Notes\M216\d2.txt','w') as fo :
##    fo.writelines(['hi\n','hello World'])


##with open(r'D:\files\Qspiders\Notes\M216\pan_cake.txt','r') as fo:
##    a = fo.read()
##    print(a)

#copy pan cake file data into another file
##with open(r'D:\files\Qspiders\Notes\M216\pan_cake.txt','r') as f1 , open(r'D:\files\Qspiders\Notes\M216\pan_cake_.txt','w') as f2:
##    s = f1.read()
##    f2.write(s)
    

#wap to count number of words present in the file

##with open(r'D:\files\Qspiders\Notes\M216\pan_cake.txt','r') as f1:
##    s = f1.read()
##    c = 0
##    for i in s.split():
##        if not(i[0].isdigit()):
##            c += 1
##    print(c)
    
            









