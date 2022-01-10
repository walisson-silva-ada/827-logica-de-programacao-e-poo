import csv

class OutraCoisa:
  def __init__(self):
    pass
  
  def create_csv(self):
    pass

def adicionar_linha_csv(filename: str, data: list):
  with open(filename, 'a') as arquivo:
    escritor = csv.writer(arquivo, delimiter=';', lineterminator='\n')

    escritor.writerow(data)