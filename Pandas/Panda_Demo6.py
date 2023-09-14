import os
import fnmatch
from sys import *
import xlsxwriter


def ExcelCreate(name):
    workbook=xlsxwriter.Workbook(name)

    worksheet=workbook.add_worksheet()

    worksheet.write('A1',"Name")
    worksheet.write('B1','College')


    workbook.close()


def main():

    if(len(argv)!=2):
        exit()
    
    if(argv[1]=="-h"):
        print("hello")
        exit()
    
    try:
        ExcelCreate(argv[1])
    except Exception:
        print("Error")

if __name__ =="__main__":
    main()