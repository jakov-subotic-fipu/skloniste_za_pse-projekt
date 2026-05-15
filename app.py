from flask import Flask, jsonify, request

app = Flask(__name__)

psi = [
    {
        "id": 1,
        "ime": "Rex",
        "pasmina": "Njemački ovčar",
        "spol": "M",
        "starost": 5,
        "datum_prijema": "2024-04-10",
        "status_udomljenja": "dostupan",
        "opis": "Mirnog karaktera i voli šetnje."
    },
    {
        "id": 2,
        "ime": "Luna",
        "pasmina": "Mješanac",
        "spol": "Ž",
        "starost": 3,
        "datum_prijema": "2024-05-02",
        "status_udomljenja": "udomljen",
        "opis": "Druželjubiva i naviknuta na ljude."
    }
]

@app.route('/', methods=["GET"])
def home():
    return "Skloniste za pse radi."

@app.route('/psi', methods=["GET"])
def prikazi_pse():
    return jsonify(psi)

@app.route("/psi/<int:id>", methods=["GET"])
def detalji_psa(id):
    for pas in psi:
        if pas["id"] == id:
            return jsonify(pas)

    return "404 - not found", 404

if __name__ == "__main__":
    app.run(port=8080)