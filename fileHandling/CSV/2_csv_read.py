import csv
import sys

"""
##1
with open('csv_3_write.csv','r') as fh:
    reader = csv.DictReader(fh)  ## it will return the data in dict formate
    #or
    #reader = csv.reader(fh)   ## it will return data in list formate with all the free list as well
    for line in reader:
        print(line)


##2

student_record = [{"Adm_no":'230',"Name":'sidhant',"Class":'sr.kg',"section":'a',"Marks":'32'},
                  {"Adm_no":'231',"Name":'pihu',"Class":'sr.kg',"section":'a',"Marks":'32'}]
with open('csv_4_write.csv','w') as fh:
    #formate = ["Adm_no","Name","Class","section","Marks"]
    #reader = csv.DictWriter(fh,fieldnames=formate)
    formate =  student_record[0].keys()
    writer = csv.DictWriter(fh,fieldnames=formate)
    writer.writeheader()

    #for line in student_record:
    #    writer.writerow(line)
    # or
    writer.writerows(student_record)


with open('csv_4_write.csv','r') as fh:
    reader = csv.DictReader(fh)
    a = int(input("Enter the admission no : "))
    #print(a)
    for record in reader:
        for v in record.values():
            if int(v)==int(a):
                print(record)
                sys.exit()
    print("No key found")

"""

# or

with open('csv_4_write.csv','r') as fh:
    reader = csv.reader(fh)
    a = int(input("Enter the admission no : "))
    print(a)
    for record in reader:
        if int(record[0]) == a:
            print([x for x in record])
            break
        #else:
        #print("No records found")







