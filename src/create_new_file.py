#! python3
import openpyxl as px
import os

if not os.path.exists('debug'):
    os.mkdir('debug')

# Create new Workbook object.
wb = px.Workbook()

# Save Workbook with name.
wb.save('./debug/new_file.xlsx')
