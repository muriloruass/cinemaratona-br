# 🎬 CineMaratona BR

<p align="center">
  <img src="CineMaratonaLogo.png" width="150" alt="CineMaratona BR Logo">
</p>

<p align="center">
  <strong>Encontre a ordem certa. Assista do jeito certo.</strong>
</p>

<p align="center">
  O <strong>CineMaratona BR</strong> organiza sagas, franquias e universos cinematográficos na ordem correta de assistir — seja cronológica ou por data de lançamento. Feito por fãs, para fãs, eliminando a confusão de ordens complexas e garantindo a melhor experiência sem spoilers diretamente no seu Stremio.
</p>

---

### ✨ Novidades da Versão 2.5

Nesta versão, focamos em expandir o catálogo e globalizar a experiência do addon:
- 🌍 **Suporte ao idioma Francês**: Interface e catálogos agora adaptados para usuários francófonos (junto com Português, Inglês e Espanhol).
- 📚 **Sagas Expandidas**: Listas de sagas maiores, mais precisas e com ordenações atualizadas.
- 🏛️ **Clássicos do Cinema**: Adição de grandes clássicos que moldaram a história do cinema.
- 🎨 **Mais Animações**: Inclusão de novos arcos, curadoria expandida de animes e grandes estúdios.

---

### 📦 O que este Addon oferece?

| Catálogo | Descrição |
|----------|-----------|
| 🎬 **Sagas de Filmes** | MCU, Star Wars, Harry Potter, 007, John Wick e as maiores franquias da história. |
| 📺 **Sagas de Séries** | Universos expandidos e séries com arcos contínuos (Breaking Bad, Game of Thrones, The Boys). |
| ✨ **Sagas de Animações** | Curadoria completa Disney, Pixar, Studio Ghibli e arcos de Anime organizados. |
| ⭐ **Coleções Especiais** | Filmografias de diretores renomados, Ordem Cronológica de grandes estúdios e Maratonas Temáticas. |

---

### 🚀 Instalação e Uso

1. Acesse a nossa [Página de Configuração Oficial](https://cinemaratona-br.vercel.app/configure).
2. Escolha o seu idioma preferido.
3. Selecione as categorias e sagas que deseja incluir no seu Stremio.
4. Clique em **Gerar Link de Instalação**.
5. Abra o link gerado e instale o addon diretamente no Stremio.
6. Prepare a pipoca e bom filme! 🍿

---

### 🗺️ Roadmap & Próximos Passos

Estamos sempre trabalhando para trazer mais conteúdo nostálgico e organizado para você. O nosso próximo grande passo é a inclusão da categoria **Nostalgia Brasileira & Global**:

- 🟢 **Nickelodeon & Cartoon Network**: Os grandes clássicos animados da nossa infância.
- 📺 **TV Globinho & SBT**: Desenhos e séries que marcaram as manhãs brasileiras (incluindo o universo completo de **Chaves** e Chapolin).
- 🎭 **TV Cultura**: Obras primas educativas e nostálgicas (Castelo Rá-Tim-Bum, Cocoricó, etc.).

---

### 🛠️ Desenvolvimento e Infraestrutura

Este addon é construído em **Python (Flask)**, utilizando uma arquitetura leve e rápida projetada para rodar em **Serverless (Vercel)**.

- **Modularidade:** Dados de catálogo estaticamente gerados e organizados na pasta `data/`.
- **Performance:** Sistema de *Edge Caching* e *Cache In-Memory* robusto para evitar lentidão nas consultas do Stremio.
- **Confiabilidade:** Cobertura de testes automatizados para garantir a integridade de todos os IDs do IMDb/TMDB.

**Comandos Úteis (Para Desenvolvedores):**
```bash
# Configurar ambiente local
make install

# Rodar servidor de desenvolvimento
make dev

# Rodar suíte de testes de integridade
make test
```

---

<p align="center">
  Desenvolvido com ♥ por <a href="https://github.com/muriloruass">@muriloruass</a> <br>
  <a href="https://github.com/muriloruass/cinemaratona-br">⭐ Deixe uma estrela no GitHub</a> · 
  <a href="https://buymeacoffee.com/muriloluce7">☕ Pague um café para o dev</a>
</p>