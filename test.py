from getpass import getuser
from subprocess import Popen
import os

usuario = getuser()

print(f"¡Hey Bienvenido {usuario}!")

path1 = "C:/Windows/Temp"
path2 = f"C:/Users/{usuario}/AppData/Local/Temp"        


cantidad_temp = os.listdir(path1)
cantidad_temp2 = os.listdir(path2)

a = len(cantidad_temp2)
b = len(cantidad_temp)

p = Popen("batch.bat", cwd=r"C:\Program Files\ADM_python")
stdout, stderr = p.communicate()


# def main():

#     print(contenido, contenido2 )
#     a = 0
#     b = 0

#     for i in contenido: a += 1
#     for i in contenido2: b += 1

#     print(a , b)