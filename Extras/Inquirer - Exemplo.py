import inquirer

questions = [
  inquirer.List('option',
    message='Escolha uma das opções abaixo',
    choices=[
      'Adicionar tarefa',
      'Alterar status da tarefa',
      'Remover tarefa',
      'Tarefas de outro dia',
      'Encerrar'
    ]
  ),
  inquirer.Text('name', message='Qual é o seu nome?')
]

answers = inquirer.prompt(questions)

print(answers)