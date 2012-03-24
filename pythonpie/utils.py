import sys
from cStringIO import StringIO

from sandbox import Sandbox, SandboxConfig


def run_python(code):
    # call and run code
    sandbox = Sandbox(SandboxConfig('stdout', use_subprocess=True, timeout=5))
    backup = sys.stdout

    try:
        sys.stdout = StringIO()  # capture output
        sandbox.execute(code)
        results = sys.stdout.getvalue()  # release output
    finally:
        sys.stdout.close()  # close the stream 
        sys.stdout = backup

    return results


class TimeoutError(Exception):
    pass

def timeout(func, args=(), kwargs={}, duration=5):
    import signal

    def handler(signum, frame):
        raise TimeoutError()

    # Set the signal handler and a 5-second alarm
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(duration)

    # This open() may hang indefinitely
    result = func(*args, **kwargs)

    signal.alarm(0)
    return result
