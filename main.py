import csv

data = []
with open('data.csv', 'r', encoding='utf-8') as f:
     reader = csv.DictReader(f)
     for row in reader:
          data.append(row)

'''
I would like you to extract each row in which the number2168678299 called2164085717 or when2164085717 called the number2168678299.  The numbers may appear as12168678299 and12164085717.  
'''


output= []


for row in data:
     if row['OriginatingNumber'] == '2168678299' or row['OriginatingNumber'] == '12168678299':
          if row['TerminatingNumber'] == '2164085717' or row['TerminatingNumber'] == '12164085717':
               output.append(row)
     elif row['OriginatingNumber'] == '2164085717' or row['OriginatingNumber'] == '12164085717':
          if row['TerminatingNumber'] == '2168678299' or row['TerminatingNumber'] == '12168678299':
               output.append(row)

header = list(output[0].keys())
grand = [list(item.values()) for item in output]
grand.insert(0, header)

from openpyxl import Workbook
from openpyxl.styles.fonts import Font
wb = Workbook()
ws = wb.active

for row in grand:
     ws.append(row)

for cell in ws['1']:
     cell.font = Font(bold=True)

wb.save('output.xlsx')