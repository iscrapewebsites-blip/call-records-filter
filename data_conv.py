import csv
data = []
with open('data_copy.csv', 'r', encoding='utf-8') as f:
     reader = csv.DictReader(f)
     for row in reader:
          data.append(row)

header = list(data[0].keys())
grand_data = [list(item.values()) for item in data]
grand_data.insert(0, header)

from openpyxl import Workbook
from openpyxl.styles.fonts import Font
wb = Workbook()
ws = wb.active

for row in grand_data:
     ws.append(row)

for cell in ws['1']:
     cell.font = Font(bold=True)

wb.save('client_data.xlsx')

