import urllib.request
import urllib.parse
import re

movies_to_check = {
    "A Supremacia Bourne": "tt0372183",
    "A Cantiga dos Pássaros e das Serpentes": "tt10545296",
    "De Volta ao Jogo": "tt2911666",
    "Missão: Impossível - Efeito Fallout": "tt4912910",
    "O Senhor dos Anéis: O Retorno do Rei": "tt0167260",
    "Fuga do Planeta dos Macacos": "tt0067047",
    "Predador 2": "tt0100405",
    "Rocky IV": "tt0090022",
    "Sexta-Feira 13 - Parte 2": "tt0082431",
    "Sexta-Feira 13 - Parte 5: Um Novo Começo": "tt0089232",
    "Sexta-Feira 13 - Parte 8: Jason Ataca Nova York": "tt0097388",
    "Jason X": "tt0211443",
    "Star Trek (2009)": "tt0796366",
    "Transformers: O Lado Oculto da Lua": "tt1055369",
    "Amnésia": "tt0209144",
    "Dunkirk": "tt5971474",
    "Planeta dos Macacos: A Guerra": "tt3450958", 
    "O Confronto": "tt2103281",
    "Planeta dos Macacos (2001)": "tt0133152",
    "De Volta ao Planeta dos Macacos": "tt0065462",
    "Fuga": "tt0067047",
    "Conquista": "tt0068408",
    "Batalha": "tt0069768",
}

print("DONE.")
