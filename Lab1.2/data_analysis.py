
from matplotlib import pyplot
from openpyxl import load_workbook

wb = load_workbook('data_analysis_lab.xlsx')
print(wb)
sheet = wb['Data']   # Загрузить лист с именем "Data" в переменную sheet
cell_A = sheet['A'][1:]   # Получить содержимое колонки A в виде списка
cell_C = sheet['C'][1:]   # Получить содержимое колонки A в виде списка
cell_D = sheet['D'][1:]   # Получить содержимое колонки A в виде списка

def getvalue(x): return x.value

#x  = list(map(getvalue, sheet['A'][1:]))   # Преобразовать содержимое колонки A в список, содержащий только значения (без форматирования и т. п.)
date = list(map(getvalue, cell_A))
temp = list(map(getvalue, cell_C))
activ = list(map(getvalue, cell_D))

#print(date)
#print(temp)
#print(activ)


#pyplot.plot(list_x, list_y, label="Метка")  # Построить график по точкам, в первом списке значения по оси X, во втором — значения по оси Y 
#pyplot.show() # показать график

pyplot.plot(date, temp, label="Temp")
pyplot.plot(date, activ, label="Activ")

pyplot.legend(loc='best')
pyplot.show()