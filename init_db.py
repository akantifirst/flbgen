import sqlite3

# Подключение к базе данных (создает файл, если не существует)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Создание таблицы для текстовых блоков
cursor.execute('''
    CREATE TABLE IF NOT EXISTS text_blocks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        label TEXT NOT NULL,
        content TEXT NOT NULL
    )
''')

# Вставка примеров текстовых блоков
blocks = [
    ("Lüftung", "Es ist eine Lüftung vorgesehen.\n"
    "  - Die Räume werden gemäß dem Lüftungsplan belüftet.\n"
    "  - Die Räume werden über stetige Volumenstromregler belüftet\n"
    "  - Die Ansteuerung erfolgt über die Automationsstation des entprechenden Bereiches\n"
    "  - Das Schalten der Lüftung erfolgt automatisch.\n"
    "  - Auf das Schalten der Lüftung wirken die Parameter: Präsenz im Raum, Tageszeit.\n"
    "  - Die Automatik kann manuell am zentralen (TP02) überschrieben werden.\n"),
    ("Sonnenschutz",
    "  - Die Jalousien werden primär über die zentrale Wetterstation gesteuert.\n"
    "    Diese liefert je Fassadenseite in Abhängigkeit der Sonneneinstrahlung die auf/ab Fahrbefehle.\n"
    "  - Über das Touchpanel (TP01) im Raum kann die zentrale Steuerung übersteuert werden  \n"
    "    und bleibt dann im lokalen Mode.\n"
    "  - Die lokale Übersteuerung wird automatisch ein- oder mehrmals täglich in \n"
    "    den Automatik-Modus zurück-gesetzt.\n"
    "  - Der Sonnenschutz kann für bestimmte Szenen mit integriert werden. (z.B. Präsentations-Szene)."),
    ('Temperierung', """    - Die Temperierung der Räum erfolgt über Heiz-/Kühldeckensegel.
    - Über den Temperaturfühler (MS05) wird die Ist-Raumtemperatur ermittelt.
    - Wahlweise kann der im Sensor integrierte PID-Regler herangezogen werden.
    - Der Sollwert wird an der zentralen Visualisierung des EG eingestellt.
    - Alternativ kann der Sollwert auch von der übergeordneten GLT kommen.
    - Eine Sollwertverschiebung kann über ein Drehregler eingestellt werden.
    - Die Automationsstation steuert die 2-Punkt Ventilantriebe (ST04) der Heiz-/Kühldeckensegel.
"""),
    ('Visualisierung', """   - Status der Beleuchtung
   - Status der Raumtemperierung
   - Status des Sonnenschutzes
   - Status der Raumtrennung
   - Status der Raumlüftung
""")
]

cursor.executemany('INSERT INTO text_blocks (label, content) VALUES (?, ?)', blocks)

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()

print("Datenbank wurde initialisiert.")
