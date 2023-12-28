'''2. File I/O:
   - Understanding file handling in Python.
   - Reading, writing, and appending data to text files.
   - Handling different file formats like CSV, JSON.
'''

#create a text file using file handling

#for write
file=open('myfile.txt','w')
file.write('my name is kashish\ni am student of iiim college \ni am a mca student \n')
file.close()

#for read
file=open('myfile.txt','r')
data=file.read()
print(data)
file.close()


#for append
file=open('myfile.txt','a')
file.write('i love play chess')
file.close()


#create a csv file using file handling
import csv

#for write
with open('csvfile.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(["Roll_No", "Name", "Branch"])
    writer.writerow([1, "Kashish Garg", "MCA"])
    writer.writerow([2, "Kratika Garg", "MA"])
    writer.writerow([3, "Rahul Sharma", "MBA"])
f.close()

#for read
with open('csvfile.csv', 'r', newline='') as f:
    '''read=f.readlines()
    print(read)'''
    reader=csv.reader(f)
    for lines in reader:
        print(lines)
f.close()

#for append
with open('csvfile.csv','a') as f:
    writer = csv.writer(f)

    writer.writerow([5,'Astha Agrawal','BSc'])
f.close()


#create a json file using file handling
import json
list2=['kashish','garg','nisha','Anirudh','Pooja']
ap='I am fine'

#for write
with open('json_demo.json','w') as f1:
  json.dump(list2,f1)
f1.close()

#for read
with open('json_demo.json', 'r') as f1:
  d=json.load(f1)
  print(d)
f1.close()


#for append
with open('json_demo.json','a') as f1:
  json.dump(ap,f1)
f1.close()