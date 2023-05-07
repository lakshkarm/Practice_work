#C:\Users\manish\PycharmProjects\pythonProject1\my_new_work\fileHandling\CSV
import csv


#### One way of writing into csv files ((writeline))

with open("csv_file_1.csv",'w') as csv_file:
    formate = ["emp-name",'age','salary','email-address']
    csv_write = csv.DictWriter(csv_file,fieldnames=formate)
    csv_write.writeheader()

    csv_write.writerow({"emp-name":"manish",'age':"41",'salary':"00",'email-address':'wakad.com'})

with open("csv_file_1.csv",'r') as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        print(line)


#### 2. another way of writing into csv files (writeline)

name = [{"emp-name":"manish",'age':"41",'salary':"00",'email-address':'wakad.com'},
{"emp-name":"manish",'age':"41",'salary':"00",'email-address':'wakad.com'},
{"emp-name":"manish",'age':"41",'salary':"00",'email-address':'wakad.com'}
]
with open("csv_file_2.csv",'w') as csv_file:
    formate = name[0].keys()
    writer = csv.DictWriter(csv_file,fieldnames=formate)
    writer.writeheader()
    for row in name:
        writer.writerow(row)

##### 3 (writeline-s)

name = [{"emp-name":"manish",'age':"41",'salary':"00",'email-address':'wakad.com'},
{"emp-name":"manish",'age':"41",'salary':"00",'email-address':'wakad.com'},
{"emp-name":"manish",'age':"41",'salary':"00",'email-address':'wakad.com'}
]

with open('csv_3_write.csv','w') as csv_file:
    formate = name[0].keys()
    writer = csv.DictWriter(csv_file,fieldnames=formate)
    writer.writeheader()
    writer.writerows(name)

##### extra programm (without defining the header)

with open('student_data.csv','w') as fh:
    #writer = csv.writer(fh,delimiter="-")  ##<<< here we can use delimiter to use any saparator bw the records (:,|,-)
    writer = csv.writer(fh)
    #writer.writerow(["manish","age","collage","subject"])
    #writer.writerow("manishagecollage subject")
    student_table = []
    while True:
        print("Student records")
        n = input("Enter Student name : ")
        c = input("Enter student class : ")
        r = input("Enter student rollno : ")
        local_list = [n,c,r]
        student_table.append(local_list)
        i = input("Do you want to submitt more records(y/n) ? : ")
        if i=='n' or i=='N':
            break
    writer.writerows(student_table)





