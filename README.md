# AutomacaoPromocoesSteam_2
Programa que executa semanalmente (segunda feira 12:00) uma automação para pegar as principais promoções da steam na semana e enviar em forma de planilha e tabela automatizado para o e-mail.

*MÉTODO UTILIZANDO O AGENDADOR DE TAREFAS*
- Portanto, você irá precisar realizar os seguintes passos:
Agendador de Tarefas -> Criar Tarefa Básica -> Nome da Tarefa -> Disparador -> Avançar (Configurar Triggers, diariamente, semanalmente, etc) -> Ação -> Iniciar um Programa -> Programa Script (colocar o caminho do executável python.exe)  -> Argumentos (será o nome do seu script python) -> Iniciar em(caminho do script) -> OK

 *Mudanças realizadas no código necessárias para cada usuário:* ( Estou sinalizando no código também )

- Mudar no codigo de acordo com o e-mail que você quer que receba as promoções

- Mudar o caminho do dataframe que será salvo para enviar por anexo

- Agendar a tarefa de acordo com o horário/dia que você quer que seja realizado o webscraping
