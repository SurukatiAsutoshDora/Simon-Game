import logging
logging.basicConfig(
    level=logging.INFO,   
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',   
    filemode='w'   
)

with open('app.log', 'r') as file:
    logs = file.read()
print(logs)
