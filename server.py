# modulo per il server flask
from flask import Flask, request
# modulo per trasformazione in formato standard JSON
from json import dumps as d

# modulo per ottenere le soluzioni
from use_model import get_solutions as gs

# inizializzo server flask
app = Flask(__name__)
# inizializzo il preddittore
predictor = gs()

@app.route('/solution', methods=['GET', 'POST'])
def json_solution():
    result = {}
    try:
        problem = request.args.get('problem')
        pp = request.args.get('pp')
        result = predictor.GetSolution(problem, pp)
        if len(result['solutions']) > 0:
            result['code'] = 200
        else:
            result['code'] = 4
    except:
        result['code'] = 0
    return d(result)
    
# avvio server flask
app.run(host='127.0.0.1', port=5001)