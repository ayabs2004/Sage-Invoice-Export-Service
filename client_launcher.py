import os
import sys
import webbrowser
import threading
import time
import json
from pathlib import Path

def get_resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def open_browser():
    time.sleep(2)
    webbrowser.open('http://localhost:8001/index.html')

def main():
    config_path = Path('server_config.json')
    if not config_path.exists():
        with open(config_path, 'w') as f:
            json.dump({"API_URL": "http://localhost:8000"}, f, indent=4)
        print("📝 Fichier server_config.json créé. Veuillez y configurer l'adresse IP du serveur.")

    from client_app import app
    
    browser_thread = threading.Thread(target=open_browser, daemon=True)
    browser_thread.start()
    
    print("=" * 60)
    print("🚀 Sage Export Client - Démarré")
    print("=" * 60)
    print("📊 Interface: http://localhost:8001/index.html")
    print("=" * 60)
    
    app.run(host='0.0.0.0', port=8001, debug=False)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(f"❌ ERREUR: {str(e)}")
        input("Appuyez sur Entrée...")
        sys.exit(1)
