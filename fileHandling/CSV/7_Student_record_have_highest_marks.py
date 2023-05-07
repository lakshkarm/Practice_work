import csv
import sys

student_record = [{"Adm_no":'230',"Name":'sidhant',"Class":'sr.kg',"section":'a',"Marks":'32'},
                  {"Adm_no":'231',"Name":'pihu',"Class":'sr.kg',"section":'a',"Marks":'32'},
                  {"Adm_no":'231',"Name":'Ansh',"Class":'sr.kg',"section":'a',"Marks":'10'},
                  {"Adm_no":'231',"Name":'Divit',"Class":'sr.kg',"section":'a',"Marks":'40'},
                  ]
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
    reader = csv.reader(fh)
    next(reader)

    max = 0
    value = 0
    for i in reader:
        if len(i)==0:
            continue
        else:
            if int(i[-1]) > max:
                max = int(i[-1])
                value = i
    print("maximum marks : ",max , "  detils of student is :",value)
    #print(["if len(i) ==0 continue else if int(i[-1]>30)" for i in reader])




