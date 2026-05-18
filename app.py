from flask import Flask, jsonify, request, render_template, redirect
from pony import orm
from baza import Pas

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return render_template("pocetna.html")

@app.route('/psi', methods=["GET"])
@orm.db_session
def prikazi_pse():
    lista_pasa = []

    for pas in Pas.select():
        lista_pasa.append({
            "id": pas.id,
            "ime": pas.ime,
            "pasmina": pas.pasmina,
            "spol": pas.spol,
            "starost": pas.starost,
            "datum_prijema": pas.datum_prijema,
            "status_udomljenja": pas.status_udomljenja,
            "opis": pas.opis
        })

    return jsonify(lista_pasa)

@app.route("/psi/<int:id>", methods=["GET"])
@orm.db_session
def detalji_psa(id):
    pas = Pas.get(id=id)

    if pas is None:
        return "Pas nije pronađen", 404

    return jsonify({
        "id": pas.id,
        "ime": pas.ime,
        "pasmina": pas.pasmina,
        "spol": pas.spol,
        "starost": pas.starost,
        "datum_prijema": pas.datum_prijema,
        "status_udomljenja": pas.status_udomljenja,
        "opis": pas.opis
    })


#POST dio:

@app.route("/psi", methods=["POST"])
@orm.db_session
def dodaj_psa():
    podaci = request.get_json()

    novi_pas = Pas(
        ime=podaci["ime"],
        pasmina=podaci["pasmina"],
        spol=podaci["spol"],
        starost=podaci["starost"],
        datum_prijema=podaci["datum_prijema"],
        status_udomljenja=podaci["status_udomljenja"],
        opis=podaci["opis"]
    )

    orm.flush()

    return jsonify({
        "id": novi_pas.id,
        "ime": novi_pas.ime,
        "pasmina": novi_pas.pasmina,
        "spol": novi_pas.spol,
        "starost": novi_pas.starost,
        "datum_prijema": novi_pas.datum_prijema,
        "status_udomljenja": novi_pas.status_udomljenja,
        "opis": novi_pas.opis
    }), 201

@app.route("/psi/<int:id>", methods=["DELETE"])
@orm.db_session
def obrisi_psa(id):
    pas = Pas.get(id=id)

    if pas is None:
        return "Pas nije pronađen", 404

    pas.delete()

    return "Pas je obrisan", 200

@app.route("/psi/<int:id>", methods=["PUT"])
@orm.db_session
def uredi_psa(id):
    podaci = request.get_json()

    pas = Pas.get(id=id)

    if pas is None:
        return "Pas nije pronađen", 404

    if "ime" in podaci:
        pas.ime = podaci["ime"]

    if "pasmina" in podaci:
        pas.pasmina = podaci["pasmina"]

    if "spol" in podaci:
        pas.spol = podaci["spol"]

    if "starost" in podaci:
        pas.starost = podaci["starost"]

    if "datum_prijema" in podaci:
        pas.datum_prijema = podaci["datum_prijema"]

    if "status_udomljenja" in podaci:
        pas.status_udomljenja = podaci["status_udomljenja"]

    if "opis" in podaci:
        pas.opis = podaci["opis"]

    return jsonify({
        "id": pas.id,
        "ime": pas.ime,
        "pasmina": pas.pasmina,
        "spol": pas.spol,
        "starost": pas.starost,
        "datum_prijema": pas.datum_prijema,
        "status_udomljenja": pas.status_udomljenja,
        "opis": pas.opis
    }), 200

@app.route("/pregled-pasa", methods=["GET"])
@orm.db_session
def pregled_pasa():
    lista_pasa = []

    for pas in Pas.select():
        lista_pasa.append({
            "id": pas.id,
            "ime": pas.ime,
            "pasmina": pas.pasmina,
            "spol": pas.spol,
            "starost": pas.starost,
            "datum_prijema": pas.datum_prijema,
            "status_udomljenja": pas.status_udomljenja,
            "opis": pas.opis
        })

    return render_template("pregled_pasa.html", psi=lista_pasa)

@app.route("/pas/<int:id>", methods=["GET"])
@orm.db_session
def prikaz_detalja_psa(id):
    pas = Pas.get(id=id)

    if pas is None:
        return "Pas nije pronađen", 404

    return render_template("detalji_psa.html", pas=pas)

@app.route("/pas/dodaj", methods=["GET"])
def forma_dodaj_psa():
    return render_template("dodaj_psa.html")

@app.route("/pas/dodaj", methods=["POST"])
@orm.db_session
def dodaj_psa_forma():
    Pas(
        ime=request.form["ime"],
        pasmina=request.form["pasmina"],
        spol=request.form["spol"],
        starost=int(request.form["starost"]),
        datum_prijema=request.form["datum_prijema"],
        status_udomljenja=request.form["status_udomljenja"],
        opis=request.form["opis"]
    )

    return redirect("/pregled-pasa")

@app.route("/pas/<int:id>/obrisi", methods=["POST"])
@orm.db_session
def obrisi_psa_forma(id):
    pas = Pas.get(id=id)

    if pas is None:
        return "Pas nije pronađen", 404

    pas.delete()

    return redirect("/pregled-pasa")

@app.route("/pas/<int:id>/uredi", methods=["GET"])
@orm.db_session
def forma_uredi_psa(id):
    pas = Pas.get(id=id)

    if pas is None:
        return "Pas nije pronađen", 404

    return render_template("uredi_psa.html", pas=pas)

@app.route("/pas/<int:id>/uredi", methods=["POST"])
@orm.db_session
def uredi_psa_forma(id):
    pas = Pas.get(id=id)

    if pas is None:
        return "Pas nije pronađen", 404

    pas.ime = request.form["ime"]
    pas.pasmina = request.form["pasmina"]
    pas.spol = request.form["spol"]
    pas.starost = int(request.form["starost"])
    pas.datum_prijema = request.form["datum_prijema"]
    pas.status_udomljenja = request.form["status_udomljenja"]
    pas.opis = request.form["opis"]

    return redirect("/pregled-pasa")

if __name__ == "__main__":
    app.run(port=8080)