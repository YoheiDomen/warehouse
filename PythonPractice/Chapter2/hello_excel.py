import openpyxl as excel

book = excel.Workbook()

sheet = book.active

sheet["A1"] = "Hello"

book.save("hello.xlsx")