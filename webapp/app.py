import os
import random

from flask import Flask

app = Flask(__name__)

@app.route('/')
def ping():
    provider = str(os.environ.get('PROVIDER', 'world'))
    return 'Ping '+provider+'!'

@app.route('/hello')
def hello():
    provider = str(os.environ.get('PROVIDER', 'world'))
    return 'Hello '+provider+'!'

def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

@app.route('/busy')
def busy():
    while True:
	r = random.random()
	n = int(r * 100000000)
    print n, primes(n)


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
