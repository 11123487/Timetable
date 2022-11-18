import xlwings as xlw
sht=xlw.Book("Test.xls").sheets[0]
Mon=sht.range('B4:B9').value
Tue=sht.range('C4:C9').value
Wed=sht.range('D4:D9').value
Thr=sht.range('E4:E9').value
Fri=sht.range('F4:F9').value
print(Mon)
print(Tue)
print(Wed)
print(Thr)
print(Fri)

