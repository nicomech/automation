#test push


from openpyxl import Workbook
from openpyxl import load_workbook
from loginTest import checkPolycomHDX
import datetime

wb = load_workbook(filename="source/codecList.xlsx")
tab = wb["Sheet1"]

totalRowTab = tab.max_row + 1
print totalRowTab

i = 2

while i < totalRowTab:
    cellIP = "B" + str(i)
    cellIPAccess = "C" + str(i)
    cellWebAccess ="D" + str(i)
    cellTiming = "E" + str(i)
    currentIP = tab[cellIP].value
    #testing each IP ; updating file
    ipCheck = checkPolycomHDX(currentIP)
    print ipCheck
    tab[cellIPAccess] = ipCheck["ip"]
    tab[cellWebAccess] = ipCheck["https"]
    tab[cellTiming] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    i = i + 1

wb.save("source/codecSanofi.xlsx")