# auladeploy

Para executar o projeto:
1. Exporte variáveis de ambiente como abaixo (versão GNU/Linux):
- `export FLASK_APP=flask_app.py`
- `export FLASK_ENV=development`
2. Execute o serviço em modo desenvolvimento:
- `$ flask run`

Para realizar os casos de teste:
`$ PYTHONPATH=. pytest`

Para ver o relatório de cobertura de testes:
`$ PYTHONPATH=. pytest --cov`