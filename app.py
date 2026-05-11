from flask import Flask, render_template, request, abort
import json
import os
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
        results = [m for m in results if query in m['ground'].lower()]

    if ronda:
        results = [m for m in results if m['round'] == ronda]

    results = sorted(results, key=lambda m: m['date'], reverse=(orden == 'desc'))

    return render_template('partidos.html', matches=results, rounds=ROUNDS, q=query, ronda=ronda, orden=orden)

@app.route('/top')
def top():
    top_matches = sorted(MATCHES, key=lambda m: (m['score']['ft'][0] + m['score']['ft'][1]), reverse=True)[:5]
    return render_template('top.html', matches=top_matches)

@app.route('/partido/<int:mid>')
def partido(mid):
    if mid < 0 or mid >= len(MATCHES):
        abort(404)
    match = MATCHES[mid]
    return render_template('detalle.html', match=match)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)



