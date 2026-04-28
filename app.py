from flask import Flask, render_template, request, abort
import json
app = Flask(__name__)

with open('euro_modificado.json', encoding='utf-8') as f:
    DATA = json.load(f)

MATCHES = DATA['matches']
for i, m in enumerate(MATCHES):
    m['id'] = i

ROUNDS = sorted(set(m['round'] for m in MATCHES))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/partidos')
def partidos():
    query = request.args.get('q', '').strip().lower()
    ronda = request.args.get('ronda', '')
    orden = request.args.get('orden', 'asc')

    results = MATCHES

    if query:
        results = [m for m in results if query in m['team1'].lower() or query in m['team2'].lower()]

    if ronda:
        results = [m for m in results if m['round'] == ronda]

    results = sorted(results, key=lambda m: m['date'], reverse=(orden == 'desc'))

    return render_template('partidos.html', matches=results, rounds=ROUNDS, q=query, ronda=ronda, orden=orden)

@app.route('/partido/<int:mid>')
def partido(mid):
    if mid < 0 or mid >= len(MATCHES):
        abort(404)
    match = MATCHES[mid]
    return render_template('detalle.html', match=match)

if __name__ == '__main__':
    app.run(debug=True)
