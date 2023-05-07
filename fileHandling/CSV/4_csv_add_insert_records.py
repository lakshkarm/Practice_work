import csv

student_record = [{"Adm_no":'230',"Name":'sidhant',"Class":'sr.kg',"section":'a',"Marks":'32'},
                  {"Adm_no":'231',"Name":'pihu',"Class":'sr.kg',"section":'a',"Marks":'32'}]
with open('csv_4_write.csv','w') as fh:
    #formate = ["Adm_no","Name","Class","section","Marks"]
    #reader = csv.DictWriter(fh,fieldnames=formate)
    #or simply
    formate =  student_record[0].keys()
    writer = csv.DictWriter(fh,fieldnames=formate)
    writer.writeheader()

    writer.writerows(student_record)


# with open('csv_4_write.csv','r') as fh:
#     reader = csv.DictReader(fh)
#     a = int(input("Enter the admission no : "))
#     #print(a)
#     for record in reader:
#         for v in record.values():
#             if int(v)==int(a):
#                 print(record)
#                 sys.exit()
#     print("No key found")

student_record = [{"Adm_no":'232',"Name":'sidhant',"Class":'sr.kg',"section":'a',"Marks":'32'},
                  {"Adm_no":'234',"Name":'pihu',"Class":'sr.kg',"section":'a',"Marks":'32'}]

with open('csv_4_write.csv','a') as fh:
    formate= student_record[0].keys()
    writer = csv.DictWriter(fh,fieldnames=formate)
    writer.writerows(student_record)
