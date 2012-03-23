import simplejson
import sys
from cStringIO import StringIO

from sandbox import Sandbox, SandboxConfig

from pythonpie import app
from pythonpie.throttle import should_be_throttled

from flask import request, render_template, Response



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

    if should_be_throttled(request.remote_addr):
        return give_error('Throttled.')


    # call and run code
    sandbox = Sandbox(SandboxConfig('interpreter'))
    backup = sys.stdout

    try:
        sys.stdout = StringIO()  # capture output
        sandbox.execute(request.json.get('code'))
        results = sys.stdout.getvalue()  # release output
    except Exception, e:
        results = unicode(e)  # TODO: print traceback
    finally:
        sys.stdout.close()  # close the stream 
        sys.stdout = backup

    response = dict(results='', errors=[], success=True)
    response['results'] = results.strip()


    return Response(
        simplejson.dumps(response, indent=2),
        mimetype='application/json')
