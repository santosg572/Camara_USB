from subprocess import call
import funciones_camara

for i in range(360*1):
   fil = 'file' + str(i)
   print(fil)
   funciones_camara.CapturaImg(fil)

call('./respaldo.sh')




