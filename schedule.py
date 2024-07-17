##############################
##### Agendador de Tarefa ####
##############################

"""

Agendador de Tarefas -> Criar Tarefa -> Configurar Geral e Configurar Triggers (diariamente, semanalmente, etc) -> OK

"""


# pip install schedule

import schedule
import time
import subprocess

def job():
    # Executa o script steampromocoes.py
    subprocess.call(['python', 'C:\Users\enzoc\OneDrive\Projetos Códigos\Automação PromoSteam/steampromocoes.py']) # Mudar caminho de acordo com seu script

# Agenda a tarefa para toda segunda-feira às 12:00
schedule.every().monday.at("12:00").do(job) # Mudar de acordo com quando você quer receber as promoções

while True:
    schedule.run_pending()
    time.sleep(1)
