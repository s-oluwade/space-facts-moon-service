from flask import Flask, jsonify
import random

app = Flask(__name__)

facts = [
    "Europa, one of Jupiter’s moons, may have a subsurface ocean.",
    "Ganymede is the largest moon in the solar system.",
    "Our moon is moving away from Earth at a rate of 1.5 inches per year."
]

@app.route('/moon-fact', methods=['GET'])
def get_moon_fact():
    fact = random.choice(facts)
    return jsonify({"fact": fact})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
