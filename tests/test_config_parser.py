import pytest
import base64
import json
from unittest.mock import patch

try:
    from utils.config_parser import parse_addon_config
except ImportError:
    parse_addon_config = None

class TestConfigParser:
    def test_parse_valid_config_happy_path(self):
        """Caso Feliz: B64 válido com idioma e categorias."""
        if parse_addon_config is None:
            pytest.fail("parse_addon_config não importado. O arquivo ainda não foi criado?")
            
        config_data = {"lang": "en-us", "categories": ["marvel", "starwars"]}
        config_b64 = base64.b64encode(json.dumps(config_data).encode()).decode()
        
        result = parse_addon_config(config_b64)
        
        assert result["lang"] == "en-us"
        assert "marvel" in result["categories"]
        assert "starwars" in result["categories"]

    def test_parse_config_missing_padding(self):
        """Caso de Borda: String B64 sem padding '=='."""
        if parse_addon_config is None:
            pytest.skip("Arquivo utils/config_parser.py ainda não existe.")

        config_data = {"l": "fr", "c": [0]} # 'c':[0] mapeia para marvel em data/config.py
        config_b64 = base64.b64encode(json.dumps(config_data).encode()).decode().replace("=", "")
        
        result = parse_addon_config(config_b64)
        
        assert result["lang"] == "fr"
        assert "marvel" in result["categories"]

    def test_parse_invalid_json_failure(self):
        """Caso de Falha: B64 válido mas JSON corrompido."""
        if parse_addon_config is None:
            pytest.skip("Arquivo utils/config_parser.py ainda não existe.")

        config_b64 = base64.b64encode(b"{invalid_json}").decode()
        
        result = parse_addon_config(config_b64)
        
        assert result["lang"] == "pt-br"
        assert len(result["categories"]) > 0
