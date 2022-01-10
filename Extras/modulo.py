import csv

def adicionar_linha_csv(filename: str, data: list):
  with open(filename, 'a') as arquivo:
    escritor = csv.writer(arquivo, delimiter=';', lineterminator='\n')

    escritor.writerow(data)