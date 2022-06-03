recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]

# Output
# print(recordatorios)
largo = list(range(len(recordatorios)))

for i in largo:
 if recordatorios[i][0] == '2021-05-01':
  recordatorios.pop(i)
  largo.pop()
 if recordatorios[i][0] == '2021-07-15':
  recordatorios[i][0] = '2021-07-16'
 if recordatorios[i][0] == '2021-01-01':
   recordatorios.insert(i+1, ['2021-01-02', '06:00', 'Empezar el año'])
 if recordatorios[i][0] == '2021-09-18':
   recordatorios.insert(i+1, ['2021-12-24', "22:00", "Cena de Navidad"])

recordatorios.append(['2021-12-31', "22:00", "Cena de Año Nuevo"])



for i in recordatorios:
 print(i)