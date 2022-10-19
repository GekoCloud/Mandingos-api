import logging.config
import logging
import random
import yaml

from flask import Flask, abort, jsonify, request, Response

with open('./config/config.yml', 'r') as config:
    configs = yaml.safe_load(config)

logging.config.dictConfig(configs)
logger = logging.getLogger(__name__)

app = Flask(__name__)

cc_info = yaml.safe_load(open('./resources/name.yaml'))
moves = set(['up', 'down', 'left', 'right', 'fire-up', 'fire-down', 'fire-right', 'fire-left'])

@app.route('/name', methods=['POST'])
def get_name():
    return jsonify(cc_info)

@app.route('/move', methods=['POST'])
def get_move():
    new_move = request.json
    my_move = random.choice(tuple(moves))

    return jsonify({'move': my_move})


if __name__ == '__main__':
    app.run()
