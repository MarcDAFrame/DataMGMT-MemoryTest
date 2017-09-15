from tkinter import *
#import utils
import random
from time import sleep
import threading

import xlwt
from tempfile import TemporaryFile
import xlrd
from xlrd import open_workbook
class serverClient:
    def __init__(self):
        print("serverClient")
        #creating, editing, and sizing window
        self.root = Tk()
        self.root.resizable(width=False, height=False)
        #self.root.geometry('{}x{}'.format(500, 500))
        self.root.configure(background='dimgrey')

        self.selectedWordList = 'calls.txt'
        
        self.col1 = IntVar()
        self.col2 = IntVar()
        self.col3 = IntVar()
        self.col4 = IntVar()
        self.col5 = IntVar()

        self.head1 = StringVar()
        self.head2 = StringVar()
        self.head3 = StringVar()
        self.head4 = StringVar()
        self.head5 = StringVar()

        self.word1 = StringVar()
        self.word2 = StringVar()
        self.word3 = StringVar()
        self.word4 = StringVar()
        self.word5 = StringVar()
        
        self.time = StringVar()
        
        self.head1.set('x')
        self.head2.set('x')
        self.head3.set('x')
        self.head4.set('x')
        self.head5.set('x')

        self.error = StringVar()
        self.error.set('')

        self.words = self.fileReader('words.txt')

        self.word1.set(self.words[0])
        self.word2.set(self.words[1])
        self.word3.set(self.words[2])
        self.word4.set(self.words[3])
        self.word5.set(self.words[4])

        #self.head = self.fileReader('title.txt')

        self.widgetsList = self.widgets()
        self.widgetsList.append([Button(self.root, text='start', command=self.start),0,2,1,1])
        self.render()
    def excelSheetReader(self):
        book = open_workbook('dataCollectorMilitaryCallSigns.xls')
        sheet1 = book.sheet_by_index(0)
        data = []

        for i in range(sheet1.nrows):
            data.append(sheet1.cell(i,1).value)
        return data

    def excelSheetWriter(self, dataList):
        book = xlwt.Workbook()
        sheet1 = book.add_sheet('sheet1')
        dataList.extend(self.excelSheetReader())
        dataList.insert(0, self.widgetsList[2][0].get() + ' ' + self.selectedWordList)
        print(dataList)
        for i,e in enumerate(dataList):
            sheet1.write(i,1,e)

        name = "dataCollectorMilitaryCallSigns.xls"
        book.save(name)
        book.save(TemporaryFile())
    
    def submit(self):
        print('Submit')
        test = []
        test.append(self.col1.get())
        test.append(self.col2.get())
        test.append(self.col3.get())
        test.append(self.col4.get())
        test.append(self.col5.get())

        print(test)
        if 0 in test:
            self.error.set('Error: Select All Options Friendo')
            self.root.update_idletasks()
            return
        else:
            self.excelSheetWriter(test)
            self.col1.set('0')
            self.col2.set('0')
            self.col3.set('0')
            self.col4.set('0')
            self.col5.set('0')


    def start(self):
        print('start')
        self.time.set('3')
        self.root.update_idletasks()
        sleep(1)
        self.time.set('2')
        self.root.update_idletasks()
        sleep(1)
        self.time.set('1')
        self.root.update_idletasks()
        sleep(1) # Need this to slow the changes down
        self.head1.set(self.words[2])
        self.head2.set(self.words[4])
        self.head3.set(self.words[0])
        self.head4.set(self.words[1])
        self.head5.set(self.words[3])
        self.root.update_idletasks()

        self.timeCounterDown(1)

        self.time.set('')
        self.head1.set('x')
        self.head2.set('x')
        self.head3.set('x')
        self.head4.set('x')
        self.head5.set('x')
        self.root.update_idletasks()

    def timeCounterDown(self, counter):
        for i in range(counter+1):
            self.time.set(str(counter-i))
            self.root.update_idletasks()
            sleep(1)

    def widgets(self):
        print('widgets')
        #words = ['test0', 'test1', 'test2', 'test3', 'test4']
        
        widgetsList = [] #widgetsList [tkinterWidget, row, column, columnspan, rowspan]
        widgetsList.append([Label(self.root, text='Memory Test', bg='dimgrey'),0,0,2,1])
        widgetsList.append([Label(self.root, text='      Name:', bg='dimgrey'),0,3,5,1])
        widgetsList.append([Entry(self.root),0,4,2,1])
        widgetsList.append([Label(self.root, textvariable=self.error, bg='dimgrey'),9,1,5,1])
        widgetsList.append([Label(self.root, textvariable=self.time, bg='dimgrey'),0,3,5,1])
        widgetsList.append([Label(self.root, textvariable=self.head1,bg='dimgrey'),1,0,1,1])
        widgetsList.append([Label(self.root, textvariable=self.head2,bg='dimgrey'),1,1,1,1])
        widgetsList.append([Label(self.root, textvariable=self.head3,bg='dimgrey'),1,2,1,1])
        widgetsList.append([Label(self.root, textvariable=self.head4,bg='dimgrey'),1,3,1,1])
        widgetsList.append([Label(self.root, textvariable=self.head5,bg='dimgrey'),1,4,1,1])

        #col1
        widgetsList.append([Radiobutton(self.root, variable=self.col1, textvariable=self.word1, bg='dimgrey', value=1),2,0,1,1])
        widgetsList.append([Radiobutton(self.root, variable=self.col1, textvariable=self.word2, bg='dimgrey', value=2),3,0,1,1])
        widgetsList.append([Radiobutton(self.root, variable=self.col1, textvariable=self.word3, bg='dimgrey', value=3),4,0,1,1])
        widgetsList.append([Radiobutton(self.root, variable=self.col1, textvariable=self.word4, bg='dimgrey', value=4),5,0,1,1])
        widgetsList.append([Radiobutton(self.root, variable=self.col1, textvariable=self.word5, bg='dimgrey', value=5),6,0,1,1])
        
        #col2
        widgetsList.append([Radiobutton(self.root, variable=self.col2, textvariable=self.word1, bg='dimgrey', value=1),2,1,1,1])
        widgetsList.append([Radiobutton(self.root, variable=self.col2, textvariable=self.word2, bg='dimgrey', value=2),3,1,1,1])
        widgetsList.append([Radiobutton(self.root, variable=self.col2, textvariable=self.word3, bg='dimgrey', value=3),4,1,1,1])
        widgetsList.append([Radiobutton(self.root, variable=self.col2, textvariable=self.word4, bg='dimgrey', value=4),5,1,1,1])
        widgetsList.append([Radiobutton(self.root, variable=self.col2, textvariable=self.word5, bg='dimgrey', value=5),6,1,1,1])

        #col3
        widgetsList.append([Radiobutton(self.root, variable=self.col3, textvariable=self.word1, bg='dimgrey', value=1),2,2,1,1])
        widgetsList.append([Radiobutton(self.root, variable=self.col3, textvariable=self.word2, bg='dimgrey', value=2),3,2,1,1])
        widgetsList.append([Radiobutton(self.root, variable=self.col3, textvariable=self.word3, bg='dimgrey', value=3),4,2,1,1])
        widgetsList.append([Radiobutton(self.root, variable=self.col3, textvariable=self.word4, bg='dimgrey', value=4),5,2,1,1])
        widgetsList.append([Radiobutton(self.root, variable=self.col3, textvariable=self.word5, bg='dimgrey', value=5),6,2,1,1])
  
        #col4
        widgetsList.append([Radiobutton(self.root, variable=self.col4, textvariable=self.word1, bg='dimgrey', value=1),2,3,1,1])
        widgetsList.append([Radiobutton(self.root, variable=self.col4, textvariable=self.word2, bg='dimgrey', value=2),3,3,1,1])
        widgetsList.append([Radiobutton(self.root, variable=self.col4, textvariable=self.word3, bg='dimgrey', value=3),4,3,1,1])
        widgetsList.append([Radiobutton(self.root, variable=self.col4, textvariable=self.word4, bg='dimgrey', value=4),5,3,1,1])
        widgetsList.append([Radiobutton(self.root, variable=self.col4, textvariable=self.word5, bg='dimgrey', value=5),6,3,1,1])

        #col5
        widgetsList.append([Radiobutton(self.root, variable=self.col5, textvariable=self.word1, bg='dimgrey', value=1),2,4,1,1])
        widgetsList.append([Radiobutton(self.root, variable=self.col5, textvariable=self.word2, bg='dimgrey', value=2),3,4,1,1])
        widgetsList.append([Radiobutton(self.root, variable=self.col5, textvariable=self.word3, bg='dimgrey', value=3),4,4,1,1])
        widgetsList.append([Radiobutton(self.root, variable=self.col5, textvariable=self.word4, bg='dimgrey', value=4),5,4,1,1])
        widgetsList.append([Radiobutton(self.root, variable=self.col5, textvariable=self.word5, bg='dimgrey', value=5),6,4,1,1])

        #Words Switcher
        widgetsList.append([Button(self.root, command=lambda: self.wordSwitcher('desert.txt'), text='Desert', bg='dimgrey'),8,0,1,1])
        widgetsList.append([Button(self.root, command=lambda: self.wordSwitcher('calls.txt'), text='Call Signs', bg='dimgrey'),8,1,1,1])
        widgetsList.append([Button(self.root, command=lambda: self.wordSwitcher('birds.txt'), text='Birds', bg='dimgrey'),8,2,1,1])
        widgetsList.append([Button(self.root, command=lambda: self.wordSwitcher('eu.txt'), text='EU Countries', bg='dimgrey'),8,3,1,1])
        widgetsList.append([Button(self.root, command=lambda: self.wordSwitcher('trees.txt'), text='Trees', bg='dimgrey'),8,4,1,1])
        widgetsList.append([Button(self.root, command=lambda: self.wordSwitcher('body.txt'), text='Body Parts', bg='dimgrey'),8,5,1,1])



        widgetsList.append([Button(self.root, text='Submit', command=self.submit), 7, 2, 1, 1])
        
        #print(widgetsList)
        return widgetsList
    
    def render(self):
        print('render')
        num = 0
        for i in self.widgetsList:
            i[0].grid(row = i[1], column=i[2], sticky='W', columnspan=i[3], rowspan=i[4], padx=5, pady=5)
            num += 1
        self.root.mainloop()

    def wordSwitcher(self, file):
        print('wordSwitcher')
        self.selectedWordList = file
        self.words = self.fileReader(file)
        print(self.words)
        self.word1.set(self.words[0])
        self.word2.set(self.words[1])
        self.word3.set(self.words[2])
        self.word4.set(self.words[3])
        self.word5.set(self.words[4])
        # self.widgets(self.words)
        # self.render()
        self.root.update()



    def fileReader(self, file):
        with open(file) as f:
            content = f.readlines()
        for i in range(len(content)):
            content[i] = content[i].rstrip('\n')
        return content
    
    def listScrambler(self, list):
        dest = list[:]
        random.shuffle(dest)
        return dest
serverClient()
