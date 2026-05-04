# CineMaratona BR 🎬🍿

> O Addon definitivo para o Stremio, focado em Sagas, Maratonas e Coleções Especiais. 
> 
> *The ultimate Stremio Addon focused on Sagas, Marathons, and Special Collections.*

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Deploy Status](https://img.shields.io/badge/Vercel-Deployed-success)](https://vercel.com/)

Organize o caos cinematográfico. O **CineMaratona BR** cria catálogos customizados diretamente no seu Stremio, organizando filmes em ordem cronológica de sagas famosas (Marvel, Star Wars, etc.), estúdios (Pixar, Disney) e coleções focadas no cinema Brasileiro e diretores aclamados.

## ✨ Features

*   **Sagas Organizadas:** Assista MCU, Harry Potter e Senhor dos Anéis na ordem correta.
*   **Animações Agrupadas:** Coleções focadas em Disney, Pixar, Dreamworks.
*   **Maratonas Especiais:** Terror, Cinema Nacional, Coleções Tarantino e Nolan.
*   **Pesquisa Integrada:** Busque filmes diretamente dentro dos grupos do addon.
*   **Multilíngue:** Interface de configuração e rótulos traduzidos (pt-br, en-us, es, fr).
*   **Leve e Rápido:** Operação serverless rodando na Edge com Cache Otimizado.

## 🚀 Installation | Como Instalar

Acesse a página de configuração, selecione as sagas que deseja adicionar ao seu Stremio e clique em **Install**:

🔗 **[Página de Instalação (Configure here)](https://cinemaratona-br.vercel.app/configure)**

## 🛠️ Configuration & Development

1. Clone o repositório e acesse a pasta:
   ```bash
   git clone https://github.com/muriloruass/cinemaratona-br.git
   cd cinemaratona-br
   ```
2. Crie um ambiente virtual e instale as dependências de desenvolvimento:
   ```bash
   python -m venv venv
   source venv/bin/activate  # ou venv\Scripts\activate no Windows
   pip install -r requirements-dev.txt
   ```
3. Execute a suíte de testes:
   ```bash
   pytest
   ```
4. Execute o servidor localmente:
   ```bash
   python app.py
   ```
   A aplicação rodará em `http://localhost:7000`.

## 📦 How it works (Arquitetura)

```text
[ Stremio Client ]
       │ (1) GET /<config>/manifest.json
       ▼
[ Vercel Edge / CDN ]  <─── (Cache s-maxage=86400)
       │ (2) Parse Config -> Retorna Catálogos Ativos
       │
       ▼ (3) GET /catalog/movie/.../genre=MCU.json
[ CineMaratona Core (Flask) ]
       │ -> Consulta data/catalogs em memória (Generators + islice)
       │ -> Cache Local (TTLCache)
       ▼
[ Retorna JSON formatado (Stremio Metas) ]
```

## 📖 API Reference

*   `GET /configure`: UI web para o usuário gerar o link de instalação.
*   `GET /health`: Health check JSON para monitoramento (SRE).
*   `GET /<config_b64>/manifest.json`: Endpoint principal consumido pelo Stremio.
*   `GET /<config_b64>/catalog/<media_type>/<catalog_id>/<extra>.json`: Busca itens de um catálogo.

## 🤝 Contributing

Contribuições são muito bem-vindas! Se você quer adicionar uma nova saga ou corrigir IDs de filmes:
1. Abra uma Issue detalhando a saga.
2. Atualize ou crie um arquivo em `data/catalogs/`.
3. Rode `python scripts/sync_saga.py "Nome da Saga" "slug"` para baixar os IDs.
4. Envie um Pull Request.

## 📜 License

Este projeto está licenciado sob a licença [MIT](LICENSE).
