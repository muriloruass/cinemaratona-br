from ._base import CatalogItem

# Sagas e Universos Cinematográficos
SAGAS = {
    "marvel": [
        CatalogItem("tt0458339", "Capitão América: O Primeiro Vingador", 2011, saga="mcu", order=1),
        CatalogItem("tt4154664", "Capitã Marvel", 2019, saga="mcu", order=2),
        CatalogItem("tt0371746", "Homem de Ferro", 2008, saga="mcu", order=3),
        CatalogItem("tt1228705", "Homem de Ferro 2", 2010, saga="mcu", order=4),
        CatalogItem("tt0800369", "Thor", 2011, saga="mcu", order=5),
        CatalogItem("tt0800080", "O Incrível Hulk", 2008, saga="mcu", order=6),
        CatalogItem("tt0848228", "Os Vingadores", 2012, saga="mcu", order=7),
        CatalogItem("tt1300854", "Homem de Ferro 3", 2013, saga="mcu", order=8),
        CatalogItem("tt1981115", "Thor: O Mundo Sombrio", 2013, saga="mcu", order=9),
        CatalogItem("tt1843866", "Capitão América 2: O Soldado Invernal", 2014, saga="mcu", order=10),
        CatalogItem("tt2015381", "Guardiões da Galáxia", 2014, saga="mcu", order=11),
        CatalogItem("tt3896198", "Guardiões da Galáxia Vol. 2", 2017, saga="mcu", order=12),
        CatalogItem("tt2395427", "Vingadores: Era de Ultron", 2015, saga="mcu", order=13),
        CatalogItem("tt0478970", "Homem-Formiga", 2015, saga="mcu", order=14),
        CatalogItem("tt3498820", "Capitão América: Guerra Civil", 2016, saga="mcu", order=15),
        CatalogItem("tt2250912", "Homem-Aranha: De Volta ao Lar", 2017, saga="mcu", order=16),
        CatalogItem("tt3480822", "Viúva Negra", 2021, saga="mcu", order=17),
        CatalogItem("tt1825683", "Pantera Negra", 2018, saga="mcu", order=18),
        CatalogItem("tt1211837", "Doutor Estranho", 2016, saga="mcu", order=19),
        CatalogItem("tt3501632", "Thor: Ragnarok", 2017, saga="mcu", order=20),
        CatalogItem("tt5095030", "Homem-Formiga e a Vespa", 2018, saga="mcu", order=21),
        CatalogItem("tt4154756", "Vingadores: Guerra Infinita", 2018, saga="mcu", order=22),
        CatalogItem("tt4154796", "Vingadores: Ultimato", 2019, saga="mcu", order=23),
        CatalogItem("tt6320628", "Homem-Aranha: Longe de Casa", 2019, saga="mcu", order=24),
        CatalogItem("tt9376612", "Shang-Chi e a Lenda dos Dez Anéis", 2021, saga="mcu", order=25),
        CatalogItem("tt9032400", "Eternos", 2021, saga="mcu", order=26),
        CatalogItem("tt10872600", "Homem-Aranha: Sem Volta para Casa", 2021, saga="mcu", order=27),
        CatalogItem("tt9419884", "Doutor Estranho no Multiverso da Loucura", 2022, saga="mcu", order=28),
        CatalogItem("tt10648342", "Thor: Amor e Trovão", 2022, saga="mcu", order=29),
        CatalogItem("tt9114286", "Pantera Negra: Wakanda Para Sempre", 2022, saga="mcu", order=30),
        CatalogItem("tt10954600", "Homem-Formiga e a Vespa: Quantumania", 2023, saga="mcu", order=31),
        CatalogItem("tt6791350", "Guardiões da Galáxia Vol. 3", 2023, saga="mcu", order=32),
        CatalogItem("tt10676048", "As Marvels", 2023, saga="mcu", order=33),
        CatalogItem("tt6263850", "Deadpool & Wolverine", 2024, saga="mcu", order=34),
        CatalogItem("tt14513804", "Capitão América: Admirável Mundo Novo", 2025, saga="mcu", order=35)
    ],
    "007": [
        CatalogItem("tt0055928", "007 - Contra o Satânico Dr. No", 1962),
        CatalogItem("tt0057076", "007 - Moscou Contra 007", 1963),
        CatalogItem("tt0058150", "007 - Contra Goldfinger", 1964),
        CatalogItem("tt0059800", "007 - Contra a Chantagem Atômica", 1965),
        CatalogItem("tt0062512", "007 - Com o 007 Só Se Vive Duas Vezes", 1967),
        CatalogItem("tt0064757", "007 - A Serviço Secreto de Sua Majestade", 1969),
        CatalogItem("tt0066995", "007 - Os Diamantes São Eternos", 1971),
        CatalogItem("tt0070328", "007 - Viva e Deixe Morrer", 1973),
        CatalogItem("tt0071807", "007 - Contra o Homem com a Pistola de Ouro", 1974),
        CatalogItem("tt0076752", "007 - O Espião Que Me Amava", 1977),
        CatalogItem("tt0079574", "007 - Contra o Foguete da Morte", 1979),
        CatalogItem("tt0082398", "007 - Somente para Seus Olhos", 1981),
        CatalogItem("tt0086034", "007 - Contra Octopussy", 1983),
        CatalogItem("tt0090334", "007 - Na Mira dos Assassinos", 1985),
        CatalogItem("tt0093428", "007 - Marcado Para a Morte", 1987),
        CatalogItem("tt0097742", "007 - Permissão Para Matar", 1989),
        CatalogItem("tt0113189", "007 - Contra GoldenEye", 1995),
        CatalogItem("tt0120347", "007 - O Amanhã Nunca Morre", 1997),
        CatalogItem("tt0143145", "007 - O Mundo Não é o Bastante", 1999),
        CatalogItem("tt0246460", "007 - Um Novo Dia Para Morrer", 2002),
        CatalogItem("tt0381061", "007 - Cassino Royale", 2006),
        CatalogItem("tt0830515", "007 - Quantum of Solace", 2008),
        CatalogItem("tt1074638", "007 - Operação Skyfall", 2012),
        CatalogItem("tt2379713", "007 - Contra Spectre", 2015),
        CatalogItem("tt2382320", "007 - Sem Tempo para Morrer", 2021)
    ],
    "missaoimpossivel": [
        CatalogItem("tt0117060", "Missão: Impossível", 1996),
        CatalogItem("tt0120755", "Missão: Impossível 2", 2000),
        CatalogItem("tt0317919", "Missão: Impossível 3", 2006),
        CatalogItem("tt1229238", "Missão: Impossível - Protocolo Fantasma", 2011),
        CatalogItem("tt2381249", "Missão: Impossível - Nação Secreta", 2015),
        CatalogItem("tt4912910", "Missão: Impossível - Efeito Fallout", 2018),
        CatalogItem("tt9603212", "Missão: Impossível - Acerto de Contas Parte 1", 2023)
    ],
    "johnwick": [
        CatalogItem("tt2911666", "De Volta ao Jogo", 2014),
        CatalogItem("tt4425200", "John Wick: Um Novo Dia Para Matar", 2017),
        CatalogItem("tt6146586", "John Wick 3: Parabellum", 2019),
        CatalogItem("tt10366206", "John Wick 4: Baba Yaga", 2023)
    ],
    "bourne": [
        CatalogItem("tt0258463", "A Identidade Bourne", 2002),
        CatalogItem("tt0372183", "A Supremacia Bourne", 2004),
        CatalogItem("tt0440963", "O Ultimato Bourne", 2007),
        CatalogItem("tt1535108", "O Legado Bourne", 2012),
        CatalogItem("tt4196776", "Jason Bourne", 2016)
    ],
    "velozesefuriosos": [
        CatalogItem("tt0232500", "Velozes & Furiosos", 2001),
        CatalogItem("tt0322259", "+ Velozes + Furiosos", 2003),
        CatalogItem("tt0463985", "Velozes & Furiosos: Desafio em Tóquio", 2006),
        CatalogItem("tt1013752", "Velozes & Furiosos 4", 2009),
        CatalogItem("tt1596343", "Velozes & Furiosos 5: Operação Rio", 2011),
        CatalogItem("tt1905041", "Velozes & Furiosos 6", 2013),
        CatalogItem("tt2820852", "Velozes & Furiosos 7", 2015),
        CatalogItem("tt4630562", "Velozes & Furiosos 8", 2017),
        CatalogItem("tt6806448", "Velozes & Furiosos: Hobbs & Shaw", 2019),
        CatalogItem("tt5433138", "Velozes & Furiosos 9", 2021),
        CatalogItem("tt5433140", "Velozes & Furiosos 10", 2023)
    ],
    "indianajones": [
        CatalogItem("tt0082971", "Os Caçadores da Arca Perdida", 1981),
        CatalogItem("tt0087469", "Indiana Jones e o Templo da Perdição", 1984),
        CatalogItem("tt0097576", "Indiana Jones e a Última Cruzada", 1989),
        CatalogItem("tt0367882", "Indiana Jones e o Reino da Caveira de Cristal", 2008),
        CatalogItem("tt1462764", "Indiana Jones e a Relíquia do Destino", 2023)
    ],
    "jurassic": [
        CatalogItem("tt0107290", "Jurassic Park: O Parque dos Dinossauros", 1993),
        CatalogItem("tt0119567", "O Mundo Perdido: Jurassic Park", 1997),
        CatalogItem("tt0163025", "Jurassic Park III", 2001),
        CatalogItem("tt0369610", "Jurassic World: O Mundo dos Dinossauros", 2015),
        CatalogItem("tt4881806", "Jurassic World: Reino Ameaçado", 2018),
        CatalogItem("tt8041270", "Jurassic World: Domínio", 2022)
    ],
    "planetadosmacacos": [
        CatalogItem("tt0063442", "O Planeta dos Macacos (1968)", 1968),
        CatalogItem("tt0065462", "De Volta ao Planeta dos Macacos", 1970),
        CatalogItem("tt0067065", "Fuga do Planeta dos Macacos", 1971),
        CatalogItem("tt0068408", "A Conquista do Planeta dos Macacos", 1972),
        CatalogItem("tt0069768", "A Batalha do Planeta dos Macacos", 1973),
        CatalogItem("tt0133152", "Planeta dos Macacos (2001)", 2001),
        CatalogItem("tt1318514", "Planeta dos Macacos: A Origem", 2011),
        CatalogItem("tt2103281", "Planeta dos Macacos: O Confronto", 2014),
        CatalogItem("tt3450958", "Planeta dos Macacos: A Guerra", 2017),
        CatalogItem("tt11389872", "Planeta dos Macacos: O Reinado", 2024)
    ],
    "exterminador": [
        CatalogItem("tt0088247", "O Exterminador do Futuro", 1984),
        CatalogItem("tt0103064", "O Exterminador do Futuro 2: O Julgamento Final", 1991),
        CatalogItem("tt0181852", "O Exterminador do Futuro 3: A Rebelião das Máquinas", 2003),
        CatalogItem("tt0438488", "O Exterminador do Futuro: A Salvação", 2009),
        CatalogItem("tt1340138", "O Exterminador do Futuro: Gênesis", 2015),
        CatalogItem("tt6450804", "O Exterminador do Futuro: Destino Sombrio", 2019)
    ],
    "madmax": [
        CatalogItem("tt0079501", "Mad Max", 1979),
        CatalogItem("tt0082694", "Mad Max 2: A Caçada Continua", 1981),
        CatalogItem("tt0089530", "Mad Max: Além da Cúpula do Trovão", 1985),
        CatalogItem("tt1392190", "Mad Max: Estrada da Fúria", 2015),
        CatalogItem("tt12037194", "Furiosa: Uma Saga Mad Max", 2024)
    ],
    "rambo": [
        CatalogItem("tt0083944", "Rambo: Programado para Matar", 1982),
        CatalogItem("tt0089880", "Rambo II: A Missão", 1985),
        CatalogItem("tt0095956", "Rambo III", 1988),
        CatalogItem("tt0462499", "Rambo IV", 2008),
        CatalogItem("tt1206885", "Rambo: Até o Fim", 2019)
    ],
    "rocky": [
        CatalogItem("tt0075148", "Rocky: Um Lutador", 1976),
        CatalogItem("tt0079817", "Rocky II: A Revanche", 1979),
        CatalogItem("tt0084602", "Rocky III: O Desafio Supremo", 1982),
        CatalogItem("tt0089927", "Rocky IV", 1985),
        CatalogItem("tt0100507", "Rocky V", 1990),
        CatalogItem("tt0479143", "Rocky Balboa", 2006),
        CatalogItem("tt3076658", "Creed: Nascido para Lutar", 2015),
        CatalogItem("tt6343314", "Creed II", 2018),
        CatalogItem("tt11145118", "Creed III", 2023)
    ],
    "senhordosaneis": [
        CatalogItem("tt0903624", "O Hobbit: Uma Jornada Inesperada", 2012),
        CatalogItem("tt1170358", "O Hobbit: A Desolação de Smaug", 2013),
        CatalogItem("tt2310332", "O Hobbit: A Batalha dos Cinco Exércitos", 2014),
        CatalogItem("tt0120737", "O Senhor dos Anéis: A Sociedade do Anel", 2001),
        CatalogItem("tt0167261", "O Senhor dos Anéis: As Duas Torres", 2002),
        CatalogItem("tt0167260", "O Senhor dos Anéis: O Retorno do Rei", 2003)
    ],
    "harrypotter": [
        CatalogItem("tt0241527", "Harry Potter e a Pedra Filosofal", 2001),
        CatalogItem("tt0295297", "Harry Potter e a Câmara Secreta", 2002),
        CatalogItem("tt0304141", "Harry Potter e o Prisioneiro de Azkaban", 2004),
        CatalogItem("tt0330373", "Harry Potter e o Cálice de Fogo", 2005),
        CatalogItem("tt0373889", "Harry Potter e a Ordem da Fênix", 2007),
        CatalogItem("tt0417741", "Harry Potter e o Enigma do Príncipe", 2009),
        CatalogItem("tt0926084", "Harry Potter e as Relíquias da Morte - Parte 1", 2010),
        CatalogItem("tt1201607", "Harry Potter e as Relíquias da Morte - Parte 2", 2011)
    ],
    "animaisfantasticos": [
        CatalogItem("tt3183660", "Animais Fantásticos e Onde Habitam", 2016),
        CatalogItem("tt4123430", "Animais Fantásticos: Os Crimes de Grindelwald", 2018),
        CatalogItem("tt4123432", "Animais Fantásticos: Os Segredos de Dumbledore", 2022)
    ],
    "transformers": [
        CatalogItem("tt0418279", "Transformers", 2007),
        CatalogItem("tt1055369", "Transformers: A Vingança dos Derrotados", 2009),
        CatalogItem("tt1399103", "Transformers: O Lado Oculto da Lua", 2011),
        CatalogItem("tt2109248", "Transformers: A Era da Extinção", 2014),
        CatalogItem("tt3371366", "Transformers: O Último Cavaleiro", 2017),
        CatalogItem("tt4701182", "Bumblebee", 2018),
        CatalogItem("tt5090568", "Transformers: O Despertar das Feras", 2023),
        CatalogItem("tt8864596", "Transformers: O Início", 2024)
    ],
    "poderosochefao": [
        CatalogItem("tt0068646", "O Poderoso Chefão", 1972),
        CatalogItem("tt0071562", "O Poderoso Chefão II", 1974),
        CatalogItem("tt0099674", "O Poderoso Chefão III", 1990)
    ],
    "piratasdocaribe": [
        CatalogItem("tt0325980", "A Maldição do Pérola Negra", 2003),
        CatalogItem("tt0383574", "O Baú da Morte", 2006),
        CatalogItem("tt0449088", "No Fim do Mundo", 2007),
        CatalogItem("tt1298650", "Navegando em Águas Misteriosas", 2011),
        CatalogItem("tt1790809", "A Vingança de Salazar", 2017)
    ],
    "xmen": [
        CatalogItem("tt0120903", "X-Men: O Filme", 2000),
        CatalogItem("tt0290334", "X-Men 2", 2003),
        CatalogItem("tt0376994", "X-Men: O Confronto Final", 2006),
        CatalogItem("tt0458525", "X-Men Origens: Wolverine", 2009),
        CatalogItem("tt1270798", "X-Men: Primeira Classe", 2011),
        CatalogItem("tt1430132", "Wolverine: Imortal", 2013),
        CatalogItem("tt1877832", "X-Men: Dias de um Futuro Esquecido", 2014),
        CatalogItem("tt1431045", "Deadpool", 2016),
        CatalogItem("tt3385516", "X-Men: Apocalipse", 2016),
        CatalogItem("tt3315342", "Logan", 2017),
        CatalogItem("tt5463162", "Deadpool 2", 2018),
        CatalogItem("tt6565702", "X-Men: Fênix Negra", 2019),
        CatalogItem("tt4682266", "Os Novos Mutantes", 2020)
    ]
}
