import csv
##create csv file with all the student records (rollno, name. class, sub , marks)

'''
with open('test_practice.csv','w') as csv_fh:
    format = ['rollno', 'name', 'class', 'sub' , 'marks']
    writer = csv.DictWriter(csv_fh,fieldnames=format)
    writer.writeheader()

    data = []
    while True:
        r = int(input("Enter roll no: "))
        n = str(input("Enter name of the student : "))
        c = str(input("Enter class of the student :"))
        s = str(input("Enter subject : "))
        m = int(input("Enter marks : "))
        new_l = {"rollno":r,"name":n,"class":c,"sub":s,"marks":m}
        data.append(new_l)
        o = str(input("do you want to enter more records(y/n) : "))
        if str(o) == 'n' or str(o) =='N':
            break
    writer.writerows(data)

with open('test_practice.csv', 'r') as csv_fh:
    reader = csv.DictReader(csv_fh)
    #print(reader)
    #print(next(reader))
    for line in reader:
        print(line)
        print(line["rollno"])

'''

#### 2

with open('test_practice_2.csv','w') as csv_fh:
    format = ['rollno', 'name', 'class', 'sub' , 'marks']
    writer = csv.writer(csv_fh)
    writer.writerow(format)
    data = []
    while True:
        r = int(input("Enter roll no: "))
        n = str(input("Enter name of the student : "))
        c = str(input("Enter class of the student :"))
        s = str(input("Enter subject : "))
        m = int(input("Enter marks : "))
        new_l = [r,n,c,s,m]
        data.append(new_l)
        o = str(input("do you want to enter more records(y/n) : "))
        if str(o) == 'n' or str(o) =='N':
            break
    writer.writerows(data)

with open('test_practice.csv', 'r') as csv_fh:
    reader = csv.reader(csv_fh)
    for line in reader:
        print(line)
        print(line[0])


