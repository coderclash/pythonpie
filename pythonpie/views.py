import simplejson

from pythonpie import app
from pythonpie.throttle import should_be_throttled

from flask import request, render_template, Response


@app.route('/', methods=['GET'])
def docs():
    return render_template('index.html')


@app.route('/v1/python/2.7.1', methods=['POST'])
def check():
    email = request.args.get('email', None)

    response = dict(success=True, errors=[], didyoumean=None)

    if should_be_throttled(request.remote_addr):
        response['success'] = False
        response['errors'] = {'message': 'Throttled.'}
        return Response(simplejson.dumps(response),
            status_code=403,
            mimetype='application/json')

    # call and run code

    return Response(simplejson.dumps(response, indent=2),
        mimetype='application/json')
