from flask import Flask, render_template
app = Flask(__name__)

@app.route('/moon-fact')
def moon_facts():
    facts = [
        {"name": "Moon", "fact": "The Moon is Earth's only natural satellite."},
        {"name": "Phobos", "fact": "Phobos is one of Mars' moons."},
        {"name": "Europa", "fact": "Europa is one of Jupiter's moons."},
        {"name": "Titan", "fact": "Titan is Saturn's largest moon."},
    ]
    return render_template('index.html', title="Moon Facts", facts=facts)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)