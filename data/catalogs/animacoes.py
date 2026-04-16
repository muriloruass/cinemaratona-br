from ._base import CatalogItem

# Animações e Anime
ANIMACOES = {
    "disney_filmes": [
        CatalogItem("tt2953050", "Encanto", 2021),
        CatalogItem("tt5109280", "Raya e o Último Dragão", 2021),
        CatalogItem("tt0780521", "A Princesa e o Sapo", 2009),
        CatalogItem("tt0398286", "Enrolados", 2010),
        CatalogItem("tt0034492", "Bambi", 1942)
    ],
    "pixar_filmes": [
        CatalogItem("tt0382932", "Ratatouille", 2007),
        CatalogItem("tt0910970", "WALL-E", 2008),
        CatalogItem("tt1049413", "UP: Altas Aventuras", 2009),
        CatalogItem("tt1217209", "Valente", 2012),
        CatalogItem("tt2380307", "Viva! A Vida é uma Festa", 2017),
        CatalogItem("tt7146812", "Dois Irmãos: Uma Jornada Fantástica", 2020),
        CatalogItem("tt2948372", "Soul", 2020),
        CatalogItem("tt12801262", "Luca", 2021),
        CatalogItem("tt8097030", "Red: Crescer é uma Fera", 2022),
        CatalogItem("tt15789038", "Elemental", 2023)
    ],
    "toystory_anim": [
        CatalogItem("tt0114709", "Toy Story", 1995, order=1),
        CatalogItem("tt0120363", "Toy Story 2", 1999, order=2),
        CatalogItem("tt0435761", "Toy Story 3", 2010, order=3),
        CatalogItem("tt1979376", "Toy Story 4", 2019, order=4),
        CatalogItem("tt10298810", "Lightyear", 2022, order=5)
    ],
    "procurandonemo": [
        CatalogItem("tt0266543", "Procurando Nemo", 2003, order=1),
        CatalogItem("tt2277860", "Procurando Dory", 2016, order=2)
    ],
    "monstros": [
        CatalogItem("tt0198781", "Monstros S.A.", 2001, order=1),
        CatalogItem("tt1453405", "Universidade Monstros", 2013, order=2)
    ],
    "osincrivel": [
        CatalogItem("tt0317705", "Os Incríveis", 2004, order=1),
        CatalogItem("tt3606756", "Os Incríveis 2", 2018, order=2)
    ],
    "carros": [
        CatalogItem("tt0317219", "Carros", 2006, order=1),
        CatalogItem("tt1216475", "Carros 2", 2011, order=2),
        CatalogItem("tt3606752", "Carros 3", 2017, order=3)
    ],
    "inside_out": [
        CatalogItem("tt2096673", "Divertida Mente", 2015, order=1),
        CatalogItem("tt22022452", "Divertida Mente 2", 2024, order=2)
    ],
    "leao": [
        CatalogItem("tt0110357", "O Rei Leão (1994)", 1994, order=1),
        CatalogItem("tt0120131", "O Rei Leão 2: O Reino de Simba", 1998, order=2),
        CatalogItem("tt6105098", "O Rei Leão (2019)", 2019, order=3),
        CatalogItem("tt13186482", "Mufasa: O Rei Leão", 2024, order=4)
    ],
    "frozen": [
        CatalogItem("tt2294629", "Frozen: Uma Aventura Congelante", 2013, order=1),
        CatalogItem("tt4520988", "Frozen II", 2019, order=2)
    ],
    "moana": [
        CatalogItem("tt3521164", "Moana: Um Mar de Aventuras", 2016, order=1),
        CatalogItem("tt13622970", "Moana 2", 2024, order=2)
    ],
    "zootopia": [
        CatalogItem("tt2948356", "Zootopia", 2016, order=1),
        CatalogItem("tt26443597", "Zootopia 2", 2025, order=2)
    ],
    "liloestitch": [
        CatalogItem("tt0275847", "Lilo & Stitch", 2002, order=1),
        CatalogItem("tt0457993", "Lilo & Stitch 2: O Defeito de Stitch", 2005, order=2),
        CatalogItem("tt0486761", "Leroy & Stitch", 2006, order=3)
    ],
    "wreck_it_ralph": [
        CatalogItem("tt1772341", "Detona Ralph", 2012, order=1),
        CatalogItem("tt5848272", "WiFi Ralph", 2018, order=2)
    ],
    "mulan_disney": [
        CatalogItem("tt0120762", "Mulan (1998)", 1998, order=1),
        CatalogItem("tt4566758", "Mulan (2020)", 2020, order=2)
    ],
    "aladdin_disney": [
        CatalogItem("tt0103639", "Aladdin (1992)", 1992, order=1),
        CatalogItem("tt6139732", "Aladdin (2019)", 2019, order=2)
    ],
    "cinderela_disney": [
        CatalogItem("tt0042332", "Cinderela (1950)", 1950, order=1),
        CatalogItem("tt1661199", "Cinderela (2015)", 2015, order=2)
    ],
    "bela_fera": [
        CatalogItem("tt0101414", "A Bela e a Fera (1991)", 1991, order=1),
        CatalogItem("tt2771200", "A Bela e a Fera (2017)", 2017, order=2)
    ],
    "pequena_sereia": [
        CatalogItem("tt0097757", "A Pequena Sereia (1989)", 1989, order=1),
        CatalogItem("tt5971474", "A Pequena Sereia (2023)", 2023, order=2)
    ],
    "dumbo": [
        CatalogItem("tt0033563", "Dumbo (1941)", 1941, order=1),
        CatalogItem("tt3861390", "Dumbo (2019)", 2019, order=2)
    ],
    "peter_pan": [
        CatalogItem("tt0046183", "Peter Pan (1953)", 1953, order=1),
        CatalogItem("tt5635026", "Peter Pan & Wendy", 2023, order=2)
    ],
    "pinoquio": [
        CatalogItem("tt0032910", "Pinóquio (1940)", 1940, order=1),
        CatalogItem("tt4593060", "Pinóquio (2022 - Disney)", 2022, order=2),
        CatalogItem("tt1488589", "Pinóquio (2022 - Guillermo del Toro)", 2022, order=3)
    ],
    "alicenopaisdasmaravilhas": [
        CatalogItem("tt0043274", "Alice no País das Maravilhas (1951)", 1951, order=1),
        CatalogItem("tt1014759", "Alice no País das Maravilhas (2010)", 2010, order=2),
        CatalogItem("tt2567026", "Alice Através do Espelho", 2016, order=3)
    ],
    "malefica": [
        CatalogItem("tt1587310", "Malévola", 2014, order=1),
        CatalogItem("tt4777008", "Malévola: Dona do Mal", 2019, order=2)
    ]
}
