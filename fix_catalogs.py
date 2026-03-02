import io

with open("catalogs.py", "r", encoding="utf-8") as f:
    content = f.read()

# Emojis on CATALOGS
content = content.replace('"name": "🎭 Melhor de Christopher Nolan"', '"name": "Melhor de Christopher Nolan"')
content = content.replace('"name": "🎭 Melhor de Quentin Tarantino"', '"name": "Melhor de Quentin Tarantino"')
content = content.replace('"name": "🌙 Maratona Terror Halloween"', '"name": "Maratona Terror Halloween"')
content = content.replace('"name": "🤣 Melhores Comédias Brasileiras"', '"name": "Melhores Comédias Brasileiras"')

# Extract everything before ANIMATIONS
idx = content.find("ANIMATIONS = {")
if idx != -1:
    header = content[:idx]
    
    # We rebuild ANIMATIONS completely ordered
    anim_block = """ANIMATIONS = {
    # ── Filmes Avulsos ─────────────────────────────────────────────────────
    "disney_filmes": {
        "name": "Disney — Filmes Avulsos",
        "items": [
            {"id": "tt2953050", "name": "Encanto"},
            {"id": "tt5109280", "name": "Raya e o Último Dragão"},
            {"id": "tt0780521", "name": "A Princesa e o Sapo"},
            {"id": "tt0398286", "name": "Enrolados"},
            {"id": "tt0034492", "name": "Bambi"}
        ]
    },
    "pixar_filmes": {
        "name": "Pixar — Filmes Avulsos",
        "items": [
            {"id": "tt0382932", "name": "Ratatouille"},
            {"id": "tt0910970", "name": "WALL-E"},
            {"id": "tt1049413", "name": "UP: Altas Aventuras"},
            {"id": "tt1217209", "name": "Valente"},
            {"id": "tt2380307", "name": "Viva! A Vida é uma Festa"},
            {"id": "tt7146812", "name": "Dois Irmãos: Uma Jornada Fantástica"},
            {"id": "tt2948372", "name": "Soul"},
            {"id": "tt12801262", "name": "Luca"},
            {"id": "tt8097030", "name": "Red: Crescer é uma Fera"},
            {"id": "tt15789038", "name": "Elemental"}
        ]
    },

    # ── Pixar ──────────────────────────────────────────────────────────────
    "toystory_anim": {
        "name": "Toy Story",
        "items": [
            {"id": "tt0114709", "name": "Toy Story"},
            {"id": "tt0120363", "name": "Toy Story 2"},
            {"id": "tt0435761", "name": "Toy Story 3"},
            {"id": "tt1979376", "name": "Toy Story 4"},
            {"id": "tt10298810", "name": "Lightyear"}
        ]
    },
    "procurandonemo": {
        "name": "Procurando Nemo e Dory",
        "items": [
            {"id": "tt0266543", "name": "Procurando Nemo"},
            {"id": "tt2277860", "name": "Procurando Dory"}
        ]
    },
    "monstros": {
        "name": "Monstros S.A.",
        "items": [
            {"id": "tt0198781", "name": "Monstros S.A."},
            {"id": "tt1453405", "name": "Universidade Monstros"}
        ]
    },
    "osincrivel": {
        "name": "Os Incríveis",
        "items": [
            {"id": "tt0317705", "name": "Os Incríveis"},
            {"id": "tt3606756", "name": "Os Incríveis 2"}
        ]
    },
    "carros": {
        "name": "Carros",
        "items": [
            {"id": "tt0317219", "name": "Carros"},
            {"id": "tt1216475", "name": "Carros 2"},
            {"id": "tt3606752", "name": "Carros 3"}
        ]
    },
    "inside_out": {
        "name": "Divertida Mente",
        "items": [
            {"id": "tt2096673", "name": "Divertida Mente"},
            {"id": "tt22022452", "name": "Divertida Mente 2"}
        ]
    },

    # ── Disney Clássicos Animados ──────────────────────────────────────────
    "leao": {
        "name": "O Rei Leão",
        "items": [
            {"id": "tt0110357", "name": "O Rei Leão (1994)"},
            {"id": "tt0120131", "name": "O Rei Leão 2: O Reino de Simba"},
            {"id": "tt6105098", "name": "O Rei Leão (2019)"},
            {"id": "tt22675690", "name": "Mufasa: O Rei Leão"}
        ]
    },
    "frozen": {
        "name": "Frozen",
        "items": [
            {"id": "tt2294629", "name": "Frozen: Uma Aventura Congelante"},
            {"id": "tt4520988", "name": "Frozen II"}
        ]
    },
    "moana": {
        "name": "Moana",
        "items": [
            {"id": "tt3521164", "name": "Moana: Um Mar de Aventuras"},
            {"id": "tt33475149", "name": "Moana 2"}
        ]
    },
    "zootopia": {
        "name": "Zootopia",
        "items": [
            {"id": "tt2948356", "name": "Zootopia"},
            {"id": "tt26443597", "name": "Zootopia 2"}
        ]
    },
    "liloestitch": {
        "name": "Lilo & Stitch",
        "items": [
            {"id": "tt0275847", "name": "Lilo & Stitch"},
            {"id": "tt0457993", "name": "Lilo & Stitch 2: O Defeito de Stitch"},
            {"id": "tt0486761", "name": "Leroy & Stitch"}
        ]
    },
    "wreck_it_ralph": {
        "name": "WiFi Ralph",
        "items": [
            {"id": "tt1772341", "name": "Detona Ralph"},
            {"id": "tt5848272", "name": "WiFi Ralph"}
        ]
    },
    "mulan_disney": {
        "name": "Mulan",
        "items": [
            {"id": "tt0120762", "name": "Mulan (1998)"},
            {"id": "tt4566758", "name": "Mulan (2020)"}
        ]
    },
    "aladdin_disney": {
        "name": "Aladdin",
        "items": [
            {"id": "tt0103639", "name": "Aladdin (1992)"},
            {"id": "tt6139732", "name": "Aladdin (2019)"}
        ]
    },
    "cinderela_disney": {
        "name": "Cinderela",
        "items": [
            {"id": "tt0042332", "name": "Cinderela (1950)"},
            {"id": "tt1661199", "name": "Cinderela (2015)"}
        ]
    },
    "bela_fera": {
        "name": "A Bela e a Fera",
        "items": [
            {"id": "tt0101414", "name": "A Bela e a Fera (1991)"},
            {"id": "tt2771200", "name": "A Bela e a Fera (2017)"}
        ]
    },
    "pequena_sereia": {
        "name": "A Pequena Sereia",
        "items": [
            {"id": "tt0097757", "name": "A Pequena Sereia (1989)"},
            {"id": "tt5971474", "name": "A Pequena Sereia (2023)"}
        ]
    },
    "dumbo": {
        "name": "Dumbo",
        "items": [
            {"id": "tt0033563", "name": "Dumbo (1941)"},
            {"id": "tt3861390", "name": "Dumbo (2019)"}
        ]
    },
    "peter_pan": {
        "name": "Peter Pan",
        "items": [
            {"id": "tt0046183", "name": "Peter Pan (1953)"},
            {"id": "tt5635026", "name": "Peter Pan & Wendy"}
        ]
    },
    "pinoquio": {
        "name": "Pinóquio",
        "items": [
            {"id": "tt0032910", "name": "Pinóquio (1940)"},
            {"id": "tt4566796", "name": "Pinóquio (2022)"}
        ]
    },
    "alicenopaisdasmaravilhas": {
        "name": "Alice no País das Maravilhas",
        "items": [
            {"id": "tt0043274", "name": "Alice no País das Maravilhas (1951)"},
            {"id": "tt1014759", "name": "Alice no País das Maravilhas (2010)"},
            {"id": "tt2567026", "name": "Alice Através do Espelho"}
        ]
    },

    # ── Disney Live-Action e Mistos ────────────────────────────────────────
    "malefica": {
        "name": "Malévola",
        "items": [
            {"id": "tt1587310", "name": "Malévola"},
            {"id": "tt4777008", "name": "Malévola: Dona do Mal"}
        ]
    }
}
"""
    with open("catalogs.py", "w", encoding="utf-8") as f:
        f.write(header + anim_block)

print("Done")
