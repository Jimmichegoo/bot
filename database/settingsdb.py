import sqlite3


def settings_starts(user_id):
    db = sqlite3.connect('database/settings.db')
    sql = db.cursor()
    sql.execute(f"SELECT user_id FROM settings WHERE user_id = (?)", (user_id,))
    if sql.fetchone() is None:
        print("work")
        sql.execute("INSERT INTO settings VALUES (?, ?, ?)", (user_id, "ru", "RUB"))
        db.commit()
        db.close()
        return True
    else:
        return False


def change_fiat(user_id, fiat):
    db = sqlite3.connect('database/settings.db')
    sql = db.cursor()
    sql.execute(f"UPDATE settings SET fiat = (?) WHERE user_id = (?)", (fiat, user_id))
    db.commit()
    db.close()


def check_fiat(user_id):
    db = sqlite3.connect('database/settings.db')
    sql = db.cursor()
    sql.execute("SELECT fiat FROM settings WHERE user_id = (?)", (user_id,))
    data = sql.fetchone()
    db.close()
    return data


def change_lang(user_id, lang):
    db = sqlite3.connect('database/settings.db')
    sql = db.cursor()
    sql.execute("UPDATE settings SET lang = (?) WHERE user_id = (?)", (lang, user_id))
    db.commit()
    db.close()


def check_lang(user_id):
    db = sqlite3.connect('database/settings.db')
    sql = db.cursor()
    sql.execute("SELECT lang FROM settings WHERE user_id = (?)", (user_id, ))
    data = sql.fetchone()[0]
    db.close()
    return data

print(check_lang("5411896443"))

