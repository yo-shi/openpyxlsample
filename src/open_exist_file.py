#! python3
import openpyxl as px
import os

def load_excel_file(path):
    return px.load_workbook(path)

if __name__ == '__main__':
    # Load exist excel file.
    wb = load_excel_file('../asset/exists_file.xlsx')

    # Save Workbook with name.
    print(wb.active)
