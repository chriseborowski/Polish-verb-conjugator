from flask import Flask, request
from Polishverbconjugator1.0.0.py import conjugate_verb

app = Flask(pvc.app)

```py from flask import Flask app = Flask(pvc.app)
@app.route('/')
def index():
return 'Hello, World!'

if name == 'main': app.run()

```py
@app.route('/conjugate')
def conjugate():
    verb = request.args.get('verb')
    if verb:
    conjugated_forms = conjugate_verb(verb)
    return conjugated_forms
    else:
    return 'Try again'

if __pvc.app__ == '__main__':
app.run()