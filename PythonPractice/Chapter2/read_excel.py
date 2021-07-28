import openpyxl as excel

book = excel.load_workbook("wareki2.xlsx")

sheet = book.worksheets[0]

cell = sheet["B72"]

print(cell.value)