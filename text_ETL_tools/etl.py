import os
from textetl import TextETL

os.chdir('./text_ETL_tools') # Change to the directory where the script is located
input_file = './input_file.txt'
output_file = 'output_file.txt'
etl = TextETL(input_file, output_file)
etl.run()