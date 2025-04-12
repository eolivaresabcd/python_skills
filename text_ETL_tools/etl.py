import os
from textetl import TextETL

os.chdir('./text_ETL_tools') # Change to the directory where the script is located
input_file = './gravitacion.txt'
output_file = 'output_file.txt'

etl = TextETL(input_file, output_file)

# limpiamos lineas con texto no deseado
texto_no_deseado = ["enrique@fiquipedia.es", "Ejercicios Física PAU Comunidad de Madrid", "Página"]
etl.limpiar_problemas(input_file, texto_no_deseado)