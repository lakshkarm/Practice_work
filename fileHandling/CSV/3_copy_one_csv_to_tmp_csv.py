import csv

with open('csv_4_write.csv','r') as fh:
    reader = csv.reader(fh)
    with open('tmp.csv','w') as tmp_fh:
        writer = csv.writer(tmp_fh)
        for line in reader:
            #print(type(line))
            writer.writerow(line)
