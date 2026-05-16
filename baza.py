from pony import orm

DB = orm.Database()


class Pas(DB.Entity):
    id = orm.PrimaryKey(int, auto=True)
    ime = orm.Required(str)
    pasmina = orm.Required(str)
    spol = orm.Required(str)
    starost = orm.Required(int)
    datum_prijema = orm.Required(str)
    status_udomljenja = orm.Required(str)
    opis = orm.Optional(str)


DB.bind(provider="sqlite", filename="skloniste.sqlite", create_db=True)
DB.generate_mapping(create_tables=True)