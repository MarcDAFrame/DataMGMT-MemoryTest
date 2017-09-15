import xlwt
from tempfile import TemporaryFile
import xlrd
from xlrd import open_workbook

def excelSheetReader():
    book = open_workbook('dataCollectorMilitaryCallSigns.xls')
    sheet1 = book.sheet_by_index(0)
    data = []

    for i in range(sheet1.nrows):
        data.append(sheet1.cell(i,1).value)
    return data

def excelSheetWriter(dataList):
    book = xlwt.Workbook()
    sheet1 = book.add_sheet('sheet1')
    dataList.extend(self.excelSheetReader())
    dataList.insert(0, self.widgetsList[2][0].get() + ' ' + self.selectedWordList)
    print(dataList)
    for i,e in enumerate(dataList):
        sheet1.write(i,1,e)

    name = "score.xls"
    book.save(name)
    book.save(TemporaryFile())

data = excelSheetReader()
#print(data[0])
counter = 0
previous = ""

for i in data:
    refined = str(i)[4:str(i).rfind(' ')]
    if refined != "":
        if refined != previous:
            previous = refined
            if counter <= 6:
                print(refined)
        else:
            counter += 1
        
#     if str(i)[3:str(i).rfind(' ')] is "F":
#         print(i)
#         #counter += 1

