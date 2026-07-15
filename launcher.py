"""
Launcher pour l'application Sage Export
Ce script démarre le serveur Flask.
"""
import os
import sys
from pathlib import Path

def get_resource_path(relative_path):
    """
    Obtient le chemin absolu vers une ressource.
    Fonctionne pour le mode développement et pour l'exécutable PyInstaller.
    """
    try:
        # PyInstaller crée un dossier temporaire et stocke le chemin dans _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

def main():
    # Vérifier si le fichier .env existe
    env_path = Path('.env')
    if not env_path.exists():
        print("❌ ERREUR: Fichier .env introuvable!")
        print("📝 Veuillez créer un fichier .env avec la configuration de votre base de données.")
        print("\nExemple de contenu pour .env:")
        print("=" * 50)
        print("DB_DRIVER=SQL Server")
        print("DB_SERVER=localhost\\SQLEXPRESS")
        print("DB_USER=votre_utilisateur")
        print("DB_PASSWORD=votre_mot_de_passe")
        print("=" * 50)
        input("\nAppuyez sur Entrée pour quitter...")
        sys.exit(1)
    
    def load_env_file(env_path=".env"):
        """Charge les variables d'environnement à partir d'un fichier .env."""
        if os.path.exists(env_path):
            with open(env_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        key, value = line.split("=", 1)
                        os.environ[key.strip()] = value.strip()
    
    # Charger les variables d'environnement
    load_env_file()
    
    # Importer l'application Flask
    from app import app
    
    print("=" * 60)
    print("🚀 Sage Export - Serveur démarré")
    print("=" * 60)
    print("📊 Serveur API: http://localhost:8000")
    print("🔧 Mode: Production")
    print("=" * 60)
    print("\n⚠️  Pour arrêter le serveur, fermez cette fenêtre ou appuyez sur CTRL+C\n")
    
    # Démarrer le serveur Flask
    # Note: debug=False pour la production
    app.run(host='0.0.0.0', port=8000, debug=False)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Serveur arrêté par l'utilisateur.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ ERREUR: {str(e)}")
        input("\nAppuyez sur Entrée pour quitter...")
        sys.exit(1)
