import os
import json
import csv

# Parameters
script_dir = os.path.dirname(os.path.abspath(__file__))
input_dir = '{}/../data/raw'.format(script_dir)
input_filename = 'players.json'
output_dir = '{}/../data/normalised'.format(script_dir)
output_filename = 'players.csv'

header = ['id', 'first_name', 'last_name', 'squad_id']

# MAIN
input_file = open('{}/{}'.format(input_dir, input_filename), 'rb')
players = json.loads(input_file.read())

with open('{}/{}'.format(output_dir, output_filename), "w") as output_file:
    writer = csv.writer(output_file)
    writer.writerow(header)
    for player in players:
        id = player['id']
        first_name = player['first_name']
        last_name = player['last_name']
        squad_id = player['squad_id']

        row = [id, first_name, last_name, squad_id]
        writer.writerow(row)
