from ollama import Client
from tabulate import tabulate

table = [['Model', 'Joke']]
ollama = Client('http://192.168.1.62:11434')
response = ollama.list()
for model in response['models']:
    joke = ollama.generate(model['name'], prompt='Tell me a programmer joke.')
    table.append([model['name'], joke['response']])
print(tabulate(table, tablefmt="fancy_grid", maxcolwidths=[None, 80]))