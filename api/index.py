import sys
import os

# Adiciona a raiz do projeto (cinemaratona-br) no PATH para podermos importar o 'app' 
# e o 'catalogs' corretamente quando a Vercel inicializar as funções serverless.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importar a instância Flask chamada "app" lá do app.py
from app import app

# A Vercel vai procurar essa variável `app` para gerenciar as requisições HTTP.
