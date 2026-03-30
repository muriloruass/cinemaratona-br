<div align="center">
  <img src="https://raw.githubusercontent.com/muriloruass/cinemaratona-br/main/cinemaratonaBR.png" alt="CineMaratona Logo" width="150"/>
  <h1>CineMaratona</h1>
  <p><strong>Your ultimate Stremio catalog for chronological sagas, thematic movie marathons, and TV series.</strong></p>
</div>

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Vercel](https://img.shields.io/badge/Vercel-000000?style=flat-square&logo=vercel&logoColor=white)](https://vercel.com)
[![Stremio](https://img.shields.io/badge/Stremio-Addon-blueviolet?style=flat-square)](https://stremio.com)

**CineMaratona** is a powerful, customizable catalog addon for Stremio. It curates popular movie franchises, series universes, and thematic marathons into strictly chronological or release-order catalogs, making it easier than ever to track and watch your favorite sagas.

## 🌟 Features

- **Movies & Series Sagas:** Perfectly ordered catalogs for Star Wars, MCU, The Walking Dead, Dragon Ball, Harry Potter, and over 40 other franchises.
- **Smart Search & Pagination:** Fully supports Stremio's native search capabilities within the addon, plus pagination for large catalogs.
- **Internationalization (i18n):** Native support for English 🇺🇸, Portuguese 🇧🇷, and Spanish 🇪🇸.
- **Interactive Configuration Page:** A beautiful, responsive `/configure` web UI allowing users to cherry-pick exactly which catalogs they want to see and in which language.
- **Dynamic Meta Updates:** Automated sync scripts that keep posters and featured content fresh.
- **Serverless Ready:** Built with Python (Flask) and optimized for seamless deployment on Vercel's serverless architecture.

## 🚀 Installation

You don't need to run code to use this addon! Simply visit the configuration page to generate your personalized install link:

👉 **[Configure & Install CineMaratona](https://cinemaratona-br.vercel.app/configure)**

1. Select your preferred language.
2. Choose your favorite movie and series catalogs.
3. Click "Install on Stremio" or copy the generated link.

## 🛠️ Development & Local Setup

If you want to contribute, add new sagas to the database, or run the project locally:

### 1. Clone the repository
```bash
git clone https://github.com/muriloruass/cinemaratona-br.git
cd cinemaratona-br
```

### 2. Set up Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run the Server
```bash
python3 app.py
```
The server will start on `http://127.0.0.1:7000`. You can visit `http://127.0.0.1:7000/configure` to test the UI.

## 📁 Project Structure

- `app.py`: The core Flask application handling routing, logic, UI rendering, and the manifest.
- `catalogs.py`: The database of movies and series categorized by saga.
- `api/index.py`: Serverless entry point for Vercel deployment.
- `locales/`: JSON dictionary files containing the translations (`en-us.json`, `pt-br.json`, `es.json`).
- `utils/i18n.py`: Internationalization helper.
- `scripts/`: GitHub Actions and cron job scripts (like TMDB sync).

## ☕ Support the Project

This project was built from scratch by a movie enthusiast for movie enthusiasts! If this addon made your Stremio experience better, consider supporting the development.

[![Buy me a coffee](https://img.buymeacoffee.com/button-api/?text=Buy%20me%20a%20coffee&emoji=&slug=muriloluce7&button_colour=FFDD00&font_colour=000000&font_family=Arial&outline_colour=000000&coffee_colour=ffffff|width=180px)](https://www.buymeacoffee.com/muriloluce7)

---
<div align="center">
  <i>Created with 🎬 and ☕ by <a href="https://github.com/muriloruass">Murilo Lucena</a></i>
</div>
