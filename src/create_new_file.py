#! python3
import openpyxl as px
import os

if not os.path.exists('output'):
    os.mkdir('output')

# Create new Workbook object.
wb = px.Workbook()

# Save Workbook with name.
wb.save('./output/new_file.xlsx')
