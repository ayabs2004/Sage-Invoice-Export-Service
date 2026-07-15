# 📊 Sage Invoice Export Service

Un service Flask qui se connecte à une base de données **Sage 100** (SQL Server ou MySQL) et génère des exports **Excel** de factures (ventes & achats) avec mise en forme professionnelle.

---

## 🏗️ Architecture

```
invoice_service/
├── app.py                  # Serveur Flask principal (API REST)
├── client_app.py           # Application cliente légère
├── launcher.py             # Lanceur du serveur
├── client_launcher.py      # Lanceur du client
├── index.html              # Interface web
├── requirements.txt        # Dépendances Python
├── logos/                  # Logos des sociétés (png/jpeg/jpg)
├── client/                 # Fichiers distribués au client
└── serveur/                # Ressources côté serveur
    └── serveur2/           # Exécutable SageExport packagé
```

---

## ⚙️ Installation

### Prérequis
- Python 3.9+
- Pilote ODBC installé :
  - **SQL Server** : [ODBC Driver 17](https://docs.microsoft.com/fr-fr/sql/connect/odbc/download-odbc-driver-for-sql-server)
  - **MySQL** : [MySQL ODBC 8.0 Connector](https://dev.mysql.com/downloads/connector/odbc/)

### 1. Cloner le projet
```bash
git clone https://github.com/<votre-username>/invoice_service.git
cd invoice_service
```

### 2. Créer un environnement virtuel
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Configurer l'environnement
```bash
# Copier le fichier modèle
copy .env.example .env   # Windows
cp .env.example .env     # Linux/Mac
```
Puis **éditer `.env`** avec vos paramètres de connexion à la base Sage.

### 5. Configurer le client
```bash
copy server_config.example.json server_config.json
```
Modifier `API_URL` si le serveur Flask tourne sur un autre hôte/port.

---

## 🚀 Démarrage

```bash
python app.py
```
Le serveur démarre sur **http://localhost:8000**.

Ouvrez votre navigateur sur `http://localhost:8000` pour accéder à l'interface.

---

## 📡 API Endpoints

### `POST /generate-excel`
Génère et télécharge un fichier Excel de factures.

**Corps JSON :**
```json
{
  "company": "JACOB",
  "month": "2025-01",
  "type": "vente"
}
```

| Champ | Valeurs | Description |
|-------|---------|-------------|
| `company` | Nom de la société | Doit correspondre à `DB_DATABASE_<COMPANY>` dans `.env` |
| `month` | `YYYY-MM` | Mois à exporter |
| `type` | `vente`, `achat`, `achat_vente` | Type de documents |

### `GET /inspect?company=JACOB&table=F_DOCENTETE`
Inspecte les colonnes d'une table Sage (pour diagnostic).

---

## 🔧 Configuration `.env`

Voir le fichier **[.env.example](.env.example)** pour la liste complète des variables.

| Variable | Description |
|----------|-------------|
| `DB_DRIVER` | Pilote ODBC (`SQL Server`, `MySQL ODBC 8.0 Driver`) |
| `DB_SERVER` | Adresse du serveur SQL |
| `DB_USER` | Utilisateur SQL |
| `DB_PASSWORD` | Mot de passe SQL |
| `DB_TRUSTED_CONNECTION` | `true` pour l'auth Windows |
| `DB_DATABASE_<SOCIETE>` | Nom de la base par société |

---

## 🏢 Logos des sociétés

Placez les logos dans le dossier `logos/` :
```
logos/
├── jacob.png
├── adikimya.jpeg
└── ...
```
Le nom du fichier doit correspondre au nom de la société (insensible à la casse).

---

## 📦 Build (exécutable Windows)

```bash
build.bat         # Build le serveur (.exe)
build_client.bat  # Build le client (.exe)
```
Les exécutables sont générés dans le dossier `dist/`.

---

## 🔐 Sécurité

- **Ne commitez jamais** le fichier `.env` (contient les identifiants DB)
- Le `.gitignore` exclut automatiquement `.env`, `venv/`, `build/`, `dist/` et les fichiers `.exe`

---

## 📄 Licence

MIT
