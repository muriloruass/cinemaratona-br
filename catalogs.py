# catalogs.py - Base de dados de Sagas e Listas Especiais do CineMaratona BR
# As listas estão organizadas por categorias e contêm o ID do IMDb (tt...) e o título em PT-BR.

CATALOGS = {
    # 💥 Ação e Aventura
    "marvel": {
        "name": "Universo Marvel (MCU)",
        "items": [
            {"id": "tt0458339", "name": "Capitão América: O Primeiro Vingador"},
            {"id": "tt4154664", "name": "Capitã Marvel"},
            {"id": "tt0371746", "name": "Homem de Ferro"},
            {"id": "tt1228705", "name": "Homem de Ferro 2"},
            {"id": "tt0800369", "name": "Thor"},
            {"id": "tt0800080", "name": "O Incrível Hulk"},
            {"id": "tt0848228", "name": "Os Vingadores"},
            {"id": "tt1300854", "name": "Homem de Ferro 3"},
            {"id": "tt1981115", "name": "Thor: O Mundo Sombrio"},
            {"id": "tt1843866", "name": "Capitão América 2: O Soldado Invernal"},
            {"id": "tt2015381", "name": "Guardiões da Galáxia"},
            {"id": "tt3896198", "name": "Guardiões da Galáxia Vol. 2"},
            {"id": "tt2395427", "name": "Vingadores: Era de Ultron"},
            {"id": "tt0478970", "name": "Homem-Formiga"},
            {"id": "tt3696180", "name": "Capitão América: Guerra Civil"},
            {"id": "tt2250912", "name": "Homem-Aranha: De Volta ao Lar"},
            {"id": "tt3480822", "name": "Viúva Negra"},
            {"id": "tt1825683", "name": "Pantera Negra"},
            {"id": "tt1211837", "name": "Doutor Estranho"},
            {"id": "tt3501632", "name": "Thor: Ragnarok"},
            {"id": "tt5095030", "name": "Homem-Formiga e a Vespa"},
            {"id": "tt4154756", "name": "Vingadores: Guerra Infinita"},
            {"id": "tt4154796", "name": "Vingadores: Ultimato"},
            {"id": "tt6320628", "name": "Homem-Aranha: Longe de Casa"},
            {"id": "tt9376612", "name": "Shang-Chi e a Lenda dos Dez Anéis"},
            {"id": "tt9032400", "name": "Eternos"},
            {"id": "tt10872600", "name": "Homem-Aranha: Sem Volta para Casa"},
            {"id": "tt9419884", "name": "Doutor Estranho no Multiverso da Loucura"},
            {"id": "tt10648342", "name": "Thor: Amor e Trovão"},
            {"id": "tt9114286", "name": "Pantera Negra: Wakanda Para Sempre"},
            {"id": "tt10954600", "name": "Homem-Formiga e a Vespa: Quantumania"},
            {"id": "tt6791350", "name": "Guardiões da Galáxia Vol. 3"},
            {"id": "tt10676048", "name": "As Marvels"},
            {"id": "tt6263850", "name": "Deadpool & Wolverine"},
            {"id": "tt14511704", "name": "Capitão América: Admirável Mundo Novo"}
        ]
    },
    "starwars": {
        "name": "Star Wars (Ordem Cronológica)",
        "items": [
            {"id": "tt0120915", "name": "Star Wars: Episódio I - A Ameaça Fantasma"},
            {"id": "tt0121765", "name": "Star Wars: Episódio II - Ataque dos Clones"},
            {"id": "tt0121766", "name": "Star Wars: Episódio III - A Vingança dos Sith"},
            {"id": "tt3748528", "name": "Rogue One: Uma História Star Wars"},
            {"id": "tt3778644", "name": "Han Solo: Uma História Star Wars"},
            {"id": "tt0076759", "name": "Star Wars: Episódio IV - Uma Nova Esperança"},
            {"id": "tt0080684", "name": "Star Wars: Episódio V - O Império Contra-Ataca"},
            {"id": "tt0086190", "name": "Star Wars: Episódio VI - O Retorno de Jedi"},
            {"id": "tt2488496", "name": "Star Wars: Episódio VII - O Despertar da Força"},
            {"id": "tt2527336", "name": "Star Wars: Episódio VIII - Os Últimos Jedi"},
            {"id": "tt2527338", "name": "Star Wars: Episódio IX - A Ascensão Skywalker"}
        ]
    },
    "xmen": {
        "name": "X-Men",
        "items": [
            {"id": "tt0120903", "name": "X-Men: O Filme"},
            {"id": "tt0290334", "name": "X-Men 2"},
            {"id": "tt0376994", "name": "X-Men: O Confronto Final"},
            {"id": "tt0458525", "name": "X-Men Origens: Wolverine"},
            {"id": "tt1270798", "name": "X-Men: Primeira Classe"},
            {"id": "tt1430132", "name": "Wolverine: Imortal"},
            {"id": "tt1877832", "name": "X-Men: Dias de um Futuro Esquecido"},
            {"id": "tt1431045", "name": "Deadpool"},
            {"id": "tt3385516", "name": "X-Men: Apocalipse"},
            {"id": "tt3315342", "name": "Logan"},
            {"id": "tt5463162", "name": "Deadpool 2"},
            {"id": "tt6565702", "name": "X-Men: Fênix Negra"},
            {"id": "tt4682266", "name": "Os Novos Mutantes"}
        ]
    },
    "007": {
        "name": "007 (James Bond)",
        "items": [
            {"id": "tt0056346", "name": "007 - Contra o Satânico Dr. No"},
            {"id": "tt0057076", "name": "007 - Moscou Contra 007"},
            {"id": "tt0058150", "name": "007 - Contra Goldfinger"},
            {"id": "tt0059800", "name": "007 - Contra a Chantagem Atômica"},
            {"id": "tt0062512", "name": "007 - Com o 007 Só Se Vive Duas Vezes"},
            {"id": "tt0064757", "name": "007 - A Serviço Secreto de Sua Majestade"},
            {"id": "tt0066995", "name": "007 - Os Diamantes São Eternos"},
            {"id": "tt0070328", "name": "007 - Viva e Deixe Morrer"},
            {"id": "tt0071807", "name": "007 - Contra o Homem com a Pistola de Ouro"},
            {"id": "tt0076336", "name": "007 - O Espião Que Me Amava"},
            {"id": "tt0079574", "name": "007 - Contra o Foguete da Morte"},
            {"id": "tt0082398", "name": "007 - Somente para Seus Olhos"},
            {"id": "tt0086034", "name": "007 - Contra Octopussy"},
            {"id": "tt0088559", "name": "007 - Na Mira dos Assassinos"},
            {"id": "tt0093428", "name": "007 - Marcado Para a Morte"},
            {"id": "tt0097742", "name": "007 - Permissão Para Matar"},
            {"id": "tt0113189", "name": "007 - Contra GoldenEye"},
            {"id": "tt0120347", "name": "007 - O Amanhã Nunca Morre"},
            {"id": "tt0143145", "name": "007 - O Mundo Não é o Bastante"},
            {"id": "tt0246460", "name": "007 - Um Novo Dia Para Morrer"},
            {"id": "tt0381061", "name": "007 - Cassino Royale"},
            {"id": "tt0830515", "name": "007 - Quantum of Solace"},
            {"id": "tt1074638", "name": "007 - Operação Skyfall"},
            {"id": "tt2379713", "name": "007 - Contra Spectre"},
            {"id": "tt2382320", "name": "007 - Sem Tempo para Morrer"}
        ]
    },
    "missaoimpossivel": {
        "name": "Missão Impossível",
        "items": [
            {"id": "tt0117060", "name": "Missão: Impossível"},
            {"id": "tt0120755", "name": "Missão: Impossível 2"},
            {"id": "tt0317919", "name": "Missão: Impossível 3"},
            {"id": "tt1229238", "name": "Missão: Impossível - Protocolo Fantasma"},
            {"id": "tt2381249", "name": "Missão: Impossível - Nação Secreta"},
            {"id": "tt4912910", "name": "Missão: Impossível - Efeito Fallout"},
            {"id": "tt9603212", "name": "Missão: Impossível - Acerto de Contas Parte 1"}
        ]
    },
    "johnwick": {
        "name": "John Wick",
        "items": [
            {"id": "tt2911666", "name": "De Volta ao Jogo"},
            {"id": "tt4425200", "name": "John Wick: Um Novo Dia Para Matar"},
            {"id": "tt6146586", "name": "John Wick 3: Parabellum"},
            {"id": "tt10366206", "name": "John Wick 4: Baba Yaga"}
        ]
    },
    "bourne": {
        "name": "Jason Bourne",
        "items": [
            {"id": "tt0258463", "name": "A Identidade Bourne"},
            {"id": "tt0372183", "name": "A Supremacia Bourne"},
            {"id": "tt0440963", "name": "O Ultimato Bourne"},
            {"id": "tt1535108", "name": "O Legado Bourne"},
            {"id": "tt4196776", "name": "Jason Bourne"}
        ]
    },
    "velozesefuriosos": {
        "name": "Velozes & Furiosos",
        "items": [
            {"id": "tt0232500", "name": "Velozes & Furiosos"},
            {"id": "tt0322259", "name": "+ Velozes + Furiosos"},
            {"id": "tt0463985", "name": "Velozes & Furiosos: Desafio em Tóquio"},
            {"id": "tt1013752", "name": "Velozes & Furiosos 4"},
            {"id": "tt1596343", "name": "Velozes & Furiosos 5: Operação Rio"},
            {"id": "tt1905041", "name": "Velozes & Furiosos 6"},
            {"id": "tt2820852", "name": "Velozes & Furiosos 7"},
            {"id": "tt4630562", "name": "Velozes & Furiosos 8"},
            {"id": "tt6806448", "name": "Velozes & Furiosos: Hobbs & Shaw"},
            {"id": "tt5433138", "name": "Velozes & Furiosos 9"},
            {"id": "tt5433140", "name": "Velozes & Furiosos 10"}
        ]
    },
    "indianajones": {
        "name": "Indiana Jones",
        "items": [
            {"id": "tt0082971", "name": "Os Caçadores da Arca Perdida"},
            {"id": "tt0087469", "name": "Indiana Jones e o Templo da Perdição"},
            {"id": "tt0097576", "name": "Indiana Jones e a Última Cruzada"},
            {"id": "tt0367882", "name": "Indiana Jones e o Reino da Caveira de Cristal"},
            {"id": "tt1462764", "name": "Indiana Jones e a Relíquia do Destino"}
        ]
    },
    "jurassic": {
        "name": "Jurassic Park e World",
        "items": [
            {"id": "tt0107290", "name": "Jurassic Park: O Parque dos Dinossauros"},
            {"id": "tt0119567", "name": "O Mundo Perdido: Jurassic Park"},
            {"id": "tt0163025", "name": "Jurassic Park III"},
            {"id": "tt0369610", "name": "Jurassic World: O Mundo dos Dinossauros"},
            {"id": "tt4881806", "name": "Jurassic World: Reino Ameaçado"},
            {"id": "tt8041270", "name": "Jurassic World: Domínio"}
        ]
    },
    "planetadosmacacos": {
        "name": "Planeta dos Macacos",
        "items": [
            {"id": "tt0063442", "name": "O Planeta dos Macacos (1968)"},
            {"id": "tt0065462", "name": "De Volta ao Planeta dos Macacos"},
            {"id": "tt0067065", "name": "Fuga do Planeta dos Macacos"},
            {"id": "tt0068408", "name": "A Conquista do Planeta dos Macacos"},
            {"id": "tt0069768", "name": "A Batalha do Planeta dos Macacos"},
            {"id": "tt0133152", "name": "Planeta dos Macacos (2001)"},
            {"id": "tt1318514", "name": "Planeta dos Macacos: A Origem"},
            {"id": "tt2103281", "name": "Planeta dos Macacos: O Confronto"},
            {"id": "tt3450958", "name": "Planeta dos Macacos: A Guerra"},
            {"id": "tt11389872", "name": "Planeta dos Macacos: O Reinado"}
        ]
    },
    "exterminador": {
        "name": "O Exterminador do Futuro",
        "items": [
            {"id": "tt0088247", "name": "O Exterminador do Futuro"},
            {"id": "tt0103064", "name": "O Exterminador do Futuro 2: O Julgamento Final"},
            {"id": "tt0181852", "name": "O Exterminador do Futuro 3: A Rebelião das Máquinas"},
            {"id": "tt0438488", "name": "O Exterminador do Futuro: A Salvação"},
            {"id": "tt1340138", "name": "O Exterminador do Futuro: Gênesis"},
            {"id": "tt6450804", "name": "O Exterminador do Futuro: Destino Sombrio"}
        ]
    },
    "madmax": {
        "name": "Mad Max",
        "items": [
            {"id": "tt0079501", "name": "Mad Max"},
            {"id": "tt0082694", "name": "Mad Max 2: A Caçada Continua"},
            {"id": "tt0089530", "name": "Mad Max: Além da Cúpula do Trovão"},
            {"id": "tt1392190", "name": "Mad Max: Estrada da Fúria"},
            {"id": "tt12037194", "name": "Furiosa: Uma Saga Mad Max"}
        ]
    },
    "rambo": {
        "name": "Rambo",
        "items": [
            {"id": "tt0083944", "name": "Rambo: Programado para Matar"},
            {"id": "tt0089880", "name": "Rambo II: A Missão"},
            {"id": "tt0095956", "name": "Rambo III"},
            {"id": "tt0462499", "name": "Rambo IV"},
            {"id": "tt1206885", "name": "Rambo: Até o Fim"}
        ]
    },
    "rocky": {
        "name": "Rocky e Creed",
        "items": [
            {"id": "tt0075148", "name": "Rocky: Um Lutador"},
            {"id": "tt0079817", "name": "Rocky II: A Revanche"},
            {"id": "tt0084602", "name": "Rocky III: O Desafio Supremo"},
            {"id": "tt0089927", "name": "Rocky IV"},
            {"id": "tt0100507", "name": "Rocky V"},
            {"id": "tt0479143", "name": "Rocky Balboa"},
            {"id": "tt3076658", "name": "Creed: Nascido para Lutar"},
            {"id": "tt6343314", "name": "Creed II"},
            {"id": "tt11145118", "name": "Creed III"}
        ]
    },

    # 🧙‍♂️ Fantasia e Ficção
    "senhordosaneis": {
        "name": "O Senhor dos Anéis + O Hobbit",
        "items": [
            {"id": "tt0903624", "name": "O Hobbit: Uma Jornada Inesperada"},
            {"id": "tt1170358", "name": "O Hobbit: A Desolação de Smaug"},
            {"id": "tt2310332", "name": "O Hobbit: A Batalha dos Cinco Exércitos"},
            {"id": "tt0120737", "name": "O Senhor dos Anéis: A Sociedade do Anel"},
            {"id": "tt0167261", "name": "O Senhor dos Anéis: As Duas Torres"},
            {"id": "tt0167260", "name": "O Senhor dos Anéis: O Retorno do Rei"}
        ]
    },
    "startrek": {
        "name": "Star Trek (Completa)",
        "items": [
            {"id": "tt0079945", "name": "Jornada nas Estrelas: O Filme"},
            {"id": "tt0084726", "name": "Jornada nas Estrelas II: A Ira de Khan"},
            {"id": "tt0088170", "name": "Jornada nas Estrelas III: À Procura de Spock"},
            {"id": "tt0092007", "name": "Jornada nas Estrelas IV: A Volta para Casa"},
            {"id": "tt0098382", "name": "Jornada nas Estrelas V: A Última Fronteira"},
            {"id": "tt0102975", "name": "Jornada nas Estrelas VI: A Terra Desconhecida"},
            {"id": "tt0111280", "name": "Jornada nas Estrelas: Generations"},
            {"id": "tt0117731", "name": "Jornada nas Estrelas: Primeiro Contato"},
            {"id": "tt0120844", "name": "Jornada nas Estrelas: Insurreição"},
            {"id": "tt0253754", "name": "Jornada nas Estrelas: Nêmesis"},
            {"id": "tt0796366", "name": "Star Trek (2009)"},
            {"id": "tt1408101", "name": "Além da Escuridão: Star Trek"},
            {"id": "tt2660888", "name": "Star Trek: Sem Fronteiras"}
        ]
    },
    "matrix": {
        "name": "Matrix",
        "items": [
            {"id": "tt0133093", "name": "Matrix"},
            {"id": "tt0234215", "name": "Matrix Reloaded"},
            {"id": "tt0242653", "name": "Matrix Revolutions"},
            {"id": "tt10838180", "name": "Matrix Resurrections"}
        ]
    },
    "harrypotter": {
        "name": "Harry Potter",
        "items": [
            {"id": "tt0241527", "name": "Harry Potter e a Pedra Filosofal"},
            {"id": "tt0295297", "name": "Harry Potter e a Câmara Secreta"},
            {"id": "tt0304141", "name": "Harry Potter e o Prisioneiro de Azkaban"},
            {"id": "tt0330373", "name": "Harry Potter e o Cálice de Fogo"},
            {"id": "tt0373889", "name": "Harry Potter e a Ordem da Fênix"},
            {"id": "tt0417741", "name": "Harry Potter e o Enigma do Príncipe"},
            {"id": "tt0926084", "name": "Harry Potter e as Relíquias da Morte - Parte 1"},
            {"id": "tt1201607", "name": "Harry Potter e as Relíquias da Morte - Parte 2"}
        ]
    },
    "animaisfantasticos": {
        "name": "Animais Fantásticos",
        "items": [
            {"id": "tt3183660", "name": "Animais Fantásticos e Onde Habitam"},
            {"id": "tt4123430", "name": "Animais Fantásticos: Os Crimes de Grindelwald"},
            {"id": "tt4123432", "name": "Animais Fantásticos: Os Segredos de Dumbledore"}
        ]
    },
    "narnia": {
        "name": "As Crônicas de Nárnia",
        "items": [
            {"id": "tt0363771", "name": "O Leão, a Feiticeira e o Guarda-Roupa"},
            {"id": "tt0499448", "name": "Príncipe Caspian"},
            {"id": "tt0980970", "name": "A Viagem do Peregrino da Alvorada"}
        ]
    },
    "jogosvorazes": {
        "name": "Jogos Vorazes",
        "items": [
            {"id": "tt1392170", "name": "Jogos Vorazes"},
            {"id": "tt1951264", "name": "Em Chamas"},
            {"id": "tt1951265", "name": "A Esperança - Parte 1"},
            {"id": "tt1951266", "name": "A Esperança - O Final"},
            {"id": "tt10545296", "name": "A Cantiga dos Pássaros e das Serpentes"}
        ]
    },
    "divergente": {
        "name": "Divergente",
        "items": [
            {"id": "tt1840309", "name": "Divergente"},
            {"id": "tt2908446", "name": "A Série Divergente: Insurgente"},
            {"id": "tt3410834", "name": "A Série Divergente: Convergente"}
        ]
    },

    # 🤡 Comédia, Família e Animação
    "shrek": {
        "name": "Shrek e Gato de Botas",
        "items": [
            {"id": "tt0126029", "name": "Shrek"},
            {"id": "tt0298148", "name": "Shrek 2"},
            {"id": "tt0413267", "name": "Shrek Terceiro"},
            {"id": "tt0892791", "name": "Shrek para Sempre"},
            {"id": "tt0448694", "name": "Gato de Botas"},
            {"id": "tt3915174", "name": "Gato de Botas 2: O Último Pedido"}
        ]
    },
    "toystory": {
        "name": "Toy Story",
        "items": [
            {"id": "tt0114709", "name": "Toy Story"},
            {"id": "tt0120363", "name": "Toy Story 2"},
            {"id": "tt0435761", "name": "Toy Story 3"},
            {"id": "tt1979376", "name": "Toy Story 4"},
            {"id": "tt10298810", "name": "Lightyear"}
        ]
    },
    "meumalvadofavorito": {
        "name": "Meu Malvado Favorito",
        "items": [
            {"id": "tt1323594", "name": "Meu Malvado Favorito"},
            {"id": "tt1690953", "name": "Meu Malvado Favorito 2"},
            {"id": "tt2293640", "name": "Minions"},
            {"id": "tt3469046", "name": "Meu Malvado Favorito 3"},
            {"id": "tt5113044", "name": "Minions 2: A Origem de Gru"},
            {"id": "tt7510222", "name": "Meu Malvado Favorito 4"}
        ]
    },
    "transformers": {
        "name": "Transformers",
        "items": [
            {"id": "tt0418279", "name": "Transformers"},
            {"id": "tt1055369", "name": "Transformers: A Vingança dos Derrotados"},
            {"id": "tt1399103", "name": "Transformers: O Lado Oculto da Lua"},
            {"id": "tt2109248", "name": "Transformers: A Era da Extinção"},
            {"id": "tt3371366", "name": "Transformers: O Último Cavaleiro"},
            {"id": "tt4701182", "name": "Bumblebee"},
            {"id": "tt5090568", "name": "Transformers: O Despertar das Feras"},
            {"id": "tt8864596", "name": "Transformers: O Início"}
        ]
    },

    # 👻 Terror e Suspense
    "alien": {
        "name": "Alien (Ordem Cronológica)",
        "items": [
            {"id": "tt1446714", "name": "Prometheus"},
            {"id": "tt2316204", "name": "Alien: Covenant"},
            {"id": "tt0078748", "name": "Alien, o Oitavo Passageiro"},
            {"id": "tt18412256", "name": "Alien: Romulus"},
            {"id": "tt0090605", "name": "Aliens, O Resgate"},
            {"id": "tt0103644", "name": "Alien 3"},
            {"id": "tt0118583", "name": "Alien: A Ressurreição"}
        ]
    },
    "predador": {
        "name": "Predador",
        "items": [
            {"id": "tt0093773", "name": "O Predador"},
            {"id": "tt0100403", "name": "Predador 2"},
            {"id": "tt1424381", "name": "Predadores"},
            {"id": "tt3829266", "name": "O Predador (2018)"},
            {"id": "tt11866324", "name": "O Predador: A Caçada (Prey)"}
        ]
    },
    "sextafeira13": {
        "name": "Sexta-Feira 13",
        "items": [
            {"id": "tt0080761", "name": "Sexta-Feira 13"},
            {"id": "tt2508618", "name": "Sexta-Feira 13 - Parte 2"},
            {"id": "tt0083972", "name": "Sexta-Feira 13 - Parte 3"},
            {"id": "tt0087298", "name": "Sexta-Feira 13 - Parte 4: O Capítulo Final"},
            {"id": "tt0089173", "name": "Sexta-Feira 13 - Parte 5: Um Novo Começo"},
            {"id": "tt0091080", "name": "Sexta-Feira 13 - Parte 6: Jason Vive"},
            {"id": "tt0095179", "name": "Sexta-Feira 13 - Parte 7: A Matança Continua"},
            {"id": "tt0097388", "name": "Sexta-Feira 13 - Parte 8: Jason Ataca Nova York"},
            {"id": "tt0123092", "name": "Jason Vai Para o Inferno: A Última Sexta-Feira"},
            {"id": "tt0211443", "name": "Jason X"},
            {"id": "tt0329030", "name": "Freddy x Jason"},
            {"id": "tt0758746", "name": "Sexta-Feira 13 (2009)"}
        ]
    },
    "horadopesadelo": {
        "name": "A Hora do Pesadelo",
        "items": [
            {"id": "tt0087800", "name": "A Hora do Pesadelo"},
            {"id": "tt0089686", "name": "A Hora do Pesadelo 2: A Vingança de Freddy"},
            {"id": "tt0093629", "name": "A Hora do Pesadelo 3: Os Guerreiros dos Sonhos"},
            {"id": "tt0095742", "name": "A Hora do Pesadelo 4: O Mestre dos Sonhos"},
            {"id": "tt0097981", "name": "A Hora do Pesadelo 5: O Maior Horror de Freddy"},
            {"id": "tt0101917", "name": "A Hora do Pesadelo 6: Pesadelo Final - A Morte de Freddy"},
            {"id": "tt0111686", "name": "O Novo Pesadelo: O Retorno de Freddy Krueger"},
            {"id": "tt1179056", "name": "A Hora do Pesadelo (2010)"}
        ]
    },

    # 🎬 Clássicos
    "poderosochefao": {
        "name": "O Poderoso Chefão",
        "items": [
            {"id": "tt0068646", "name": "O Poderoso Chefão"},
            {"id": "tt0071562", "name": "O Poderoso Chefão II"},
            {"id": "tt0099674", "name": "O Poderoso Chefão III"}
        ]
    },
    "piratasdocaribe": {
        "name": "Piratas do Caribe",
        "items": [
            {"id": "tt0325980", "name": "A Maldição do Pérola Negra"},
            {"id": "tt0383574", "name": "O Baú da Morte"},
            {"id": "tt0449088", "name": "No Fim do Mundo"},
            {"id": "tt1298650", "name": "Navegando em Águas Misteriosas"},
            {"id": "tt1790809", "name": "A Vingança de Salazar"}
        ]
    },
    "sherlockholmes": {
        "name": "Sherlock Holmes e Enola",
        "items": [
            {"id": "tt0988045", "name": "Sherlock Holmes"},
            {"id": "tt1515091", "name": "Sherlock Holmes: O Jogo de Sombras"},
            {"id": "tt7846844", "name": "Enola Holmes"},
            {"id": "tt14641788", "name": "Enola Holmes 2"}
        ]
    },

    # ⭐ Listas Especiais
    "oscar2026": {
        "name": "🏆 Oscar 2026: Melhor Filme",
        "items": [
            {"id": "tt31193180", "name": "Sinners"},
            {"id": "tt30144839", "name": "One Battle After Another"},
            {"id": "tt1312221", "name": "Frankenstein"},
            {"id": "tt32916440", "name": "Marty Supreme"},
            {"id": "tt27714581", "name": "Sentimental Value"},
            {"id": "tt14905854", "name": "Hamnet"},
            {"id": "tt12300742", "name": "Bugonia"},
            {"id": "tt16311594", "name": "F1"},
            {"id": "tt27847051", "name": "O Agente Secreto (Brasil)"},
            {"id": "tt29768334", "name": "Train Dreams"},
            {"id": "tt32536315", "name": "Blue Moon"}
        ]
    },
    "oscar2026_intl": {
        "name": "🌍 Oscar 2026: Filme Internacional",
        "items": [
            {"id": "tt27847051", "name": "O Agente Secreto (Brasil)"},
            {"id": "tt36491653", "name": "It Was Just an Accident (França)"},
            {"id": "tt32298285", "name": "Sirāt (Espanha)"},
            {"id": "tt36943034", "name": "The Voice of Hind Rajab (Tunísia)"}
        ]
    },
    "cinemanacional": {
        "name": "🇧🇷 Cinema Brasileiro em Alta",
        "items": [
            {"id": "tt14961016", "name": "Ainda Estou Aqui"},
            {"id": "tt27847051", "name": "O Agente Secreto"},
            {"id": "tt28696532", "name": "O Auto da Compadecida 2"},
            {"id": "tt28497675", "name": "Maníaco do Parque"},
            {"id": "tt2762506", "name": "Bacurau"},
            {"id": "tt7825208", "name": "Marighella"},
            {"id": "tt8169552", "name": "Turma da Mônica: Laços"}
        ]
    },
    "nolan": {
        "name": "🎭 Melhor de Christopher Nolan",
        "items": [
            {"id": "tt0209144", "name": "Amnésia"},
            {"id": "tt0240772", "name": "Insônia"},
            {"id": "tt0372784", "name": "Batman Begins"},
            {"id": "tt0482571", "name": "O Grande Truque"},
            {"id": "tt0468569", "name": "Batman: O Cavaleiro das Trevas"},
            {"id": "tt1375666", "name": "A Origem"},
            {"id": "tt1345836", "name": "Batman: O Cavaleiro das Trevas Ressurge"},
            {"id": "tt0816692", "name": "Interestelar"},
            {"id": "tt5013056", "name": "Dunkirk"},
            {"id": "tt6723592", "name": "Tenet"},
            {"id": "tt15398776", "name": "Oppenheimer"}
        ]
    },
    "tarantino": {
        "name": "🎭 Melhor de Quentin Tarantino",
        "items": [
            {"id": "tt0105236", "name": "Cães de Aluguel"},
            {"id": "tt0110912", "name": "Pulp Fiction: Tempo de Violência"},
            {"id": "tt0119396", "name": "Jackie Brown"},
            {"id": "tt0266697", "name": "Kill Bill: Volume 1"},
            {"id": "tt0378194", "name": "Kill Bill: Volume 2"},
            {"id": "tt1028528", "name": "À Prova de Morte"},
            {"id": "tt0361748", "name": "Bastardos Inglórios"},
            {"id": "tt1853728", "name": "Django Livre"},
            {"id": "tt3460252", "name": "Os Oito Odiados"},
            {"id": "tt7131622", "name": "Era Uma Vez em... Hollywood"}
        ]
    },
    "halloween": {
        "name": "🌙 Maratona Terror Halloween",
        "items": [
            {"id": "tt0077651", "name": "Halloween - A Noite do Terror"},
            {"id": "tt27728888", "name": "Pânico"},
            {"id": "tt1457767", "name": "Invocação do Mal"},
            {"id": "tt0070047", "name": "O Exorcista"},
            {"id": "tt1598778", "name": "A Entidade"}
        ]
    },
    "comedias_br": {
        "name": "🤣 Melhores Comédias Brasileiras",
        "items": [
            {"id": "tt2464018", "name": "Minha Mãe é uma Peça: O Filme"},
            {"id": "tt3212812", "name": "Minha Mãe é uma Peça 2"},
            {"id": "tt10611372", "name": "Minha Mãe é uma Peça 3"},
            {"id": "tt0271383", "name": "O Auto da Compadecida"},
            {"id": "tt0478198", "name": "Se Eu Fosse Você"},
            {"id": "tt1099227", "name": "Se Eu Fosse Você 2"}
        ]
    }
}

# ---------------------------------------------------------------------------
# 🎨 ANIMAÇÕES — Disney & Pixar
# Catálogo separado exibido na aba "Animações" do addon.
# ---------------------------------------------------------------------------

ANIMATIONS = {
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