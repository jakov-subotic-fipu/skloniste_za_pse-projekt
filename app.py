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


#POST dio:

@app.route("/psi", methods=["POST"])
def dodaj_psa():
    podaci = request.get_json()

    novi_pas = {
        "id": len(psi) + 1,
        "ime": podaci["ime"],
        "pasmina": podaci["pasmina"],
        "spol": podaci["spol"],
        "starost": podaci["starost"],
        "datum_prijema": podaci["datum_prijema"],
        "status_udomljenja": podaci["status_udomljenja"],
        "opis": podaci["opis"]
    }

    psi.append(novi_pas)

    return jsonify(novi_pas), 201

@app.route("/psi/<int:id>", methods=["DELETE"])
def obrisi_psa(id):
    for pas in psi:
        if pas["id"] == id:
            psi.remove(pas)
            return "Pas je obrisan", 200

    return "Pas nije pronađen", 404

@app.route("/psi/<int:id>", methods=["PUT"])
def uredi_psa(id):
    podaci = request.get_json()

    for pas in psi:
        if pas["id"] == id:
            if "ime" in podaci:
                pas["ime"] = podaci["ime"]

            if "pasmina" in podaci:
                pas["pasmina"] = podaci["pasmina"]

            if "spol" in podaci:
                pas["spol"] = podaci["spol"]

            if "starost" in podaci:
                pas["starost"] = podaci["starost"]

            if "datum_prijema" in podaci:
                pas["datum_prijema"] = podaci["datum_prijema"]

            if "status_udomljenja" in podaci:
                pas["status_udomljenja"] = podaci["status_udomljenja"]

            if "opis" in podaci:
                pas["opis"] = podaci["opis"]

            return jsonify(pas), 200

    return "Pas nije pronađen", 404

if __name__ == "__main__":
    app.run(port=8080)