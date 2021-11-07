import csv
 
with open("data.csv",'r', encoding='utf-8') as csvin, open("output_tsv.tsv", 'w', newline='', encoding='utf-8') as tsvout:
    csvin = csv.reader(csvin)
    tsvout = csv.writer(tsvout, delimiter='\t')
 
    for row in csvin:
        tsvout.writerow(row)