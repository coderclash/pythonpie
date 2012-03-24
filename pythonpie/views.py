import simplejson

from flask import request, render_template, Response

from pythonpie import app
from pythonpie.throttle import should_be_throttled
from pythonpie.utils import run_python, timeout, TimeoutError


@app.route('/', methods=['GET'])
def docs():
    return render_template('index.html')


def give_error(message):
    response = dict(results='', errors=[], success=True)
    response['success'] = False
    response['errors'] = [{'message': message}]
    return Response(
        simplejson.dumps(response),
        mimetype='application/json')



@app.route('/v1/python/2.7.1', methods=['POST'])
def run_code():
    email = request.args.get('email', None)

    # TODO: cleanup and return 403 status
    if request.json is None:
        return give_error('Must provide JSON.')

    if not request.json.get('code', None):
        return give_error('Must provide "code" key in JSON.')

    response = dict(results='', errors=[], success=True)
    code = request.json.get('code')

    try:
        results = timeout(run_python, [code])
        response['results'] = results.strip()
    except TimeoutError:
        response['success'] = False
        response['results'] = 'Timeout error! 5 seconds is max.'

    return Response(
        simplejson.dumps(response, indent=2),
        mimetype='application/json')
