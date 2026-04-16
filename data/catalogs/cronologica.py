from ._base import CatalogItem

# Sagas com Ordem Cronológica Alternativa
CRONOLOGICA = {
    "starwars": [
        CatalogItem("tt0120915", "Star Wars: Episódio I - A Ameaça Fantasma", 1999, order=1),
        CatalogItem("tt0121765", "Star Wars: Episódio II - Ataque dos Clones", 2002, order=2),
        CatalogItem("tt0121766", "Star Wars: Episódio III - A Vingança dos Sith", 2005, order=3),
        CatalogItem("tt3748528", "Rogue One: Uma História Star Wars", 2016, order=4),
        CatalogItem("tt3778644", "Han Solo: Uma História Star Wars", 2018, order=5),
        CatalogItem("tt0076759", "Star Wars: Episódio IV - Uma Nova Esperança", 1977, order=6),
        CatalogItem("tt0080684", "Star Wars: Episódio V - O Império Contra-Ataca", 1980, order=7),
        CatalogItem("tt0086190", "Star Wars: Episódio VI - O Retorno de Jedi", 1983, order=8),
        CatalogItem("tt2488496", "Star Wars: Episódio VII - O Despertar da Força", 2015, order=9),
        CatalogItem("tt2527336", "Star Wars: Episódio VIII - Os Últimos Jedi", 2017, order=10),
        CatalogItem("tt2527338", "Star Wars: Episódio IX - A Ascensão Skywalker", 2019, order=11)
    ],
    "alien": [
        CatalogItem("tt1446714", "Prometheus", 2012, watch_order_note="Origem dos Engineers", order=1),
        CatalogItem("tt2316204", "Alien: Covenant", 2017, order=2),
        CatalogItem("tt0078748", "Alien, o Oitavo Passageiro", 1979, order=3),
        CatalogItem("tt18412256", "Alien: Romulus", 2024, order=4),
        CatalogItem("tt0090605", "Aliens, O Resgate", 1986, order=5),
        CatalogItem("tt0103644", "Alien 3", 1992, order=6),
        CatalogItem("tt0118583", "Alien: A Ressurreição", 1997, order=7)
    ]
}
