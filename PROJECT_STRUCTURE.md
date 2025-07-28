# 📁 Project Structure

```
Mood_Playlist/
├── 📄 app.py                    # 🎵 Main Streamlit application
├── 📄 requirements.txt           # 📦 Python dependencies
├── 📄 env_example.txt           # 🔑 Environment variables template
├── 📄 README.md                 # 📖 Quick start guide
├── 📄 DOCUMENTATION.md          # 📚 Comprehensive documentation
├── 📄 QUICK_REFERENCE.md        # ⚡ Terminal commands reference
├── 📄 PROJECT_STRUCTURE.md      # 📁 This file - project overview
├── 📁 .streamlit/               # ⚙️ Streamlit configuration
│   └── 📄 config.toml          # 🔧 Streamlit settings
├── 📁 mood_playlist_env/        # 🐍 Python virtual environment
│   ├── 📁 bin/                  # 🚀 Executable scripts
│   ├── 📁 lib/                  # 📚 Python libraries
│   └── 📁 include/              # 📝 Header files
└── 📄 Mood Playlist Generator.pdf # 📄 Project documentation (PDF)
```

---

## 📄 File Descriptions

### 🎵 Core Application Files

#### `app.py` - Main Application
- **Size**: ~12KB, 249 lines
- **Purpose**: Primary Streamlit application
- **Key Features**:
  - Spotify OAuth authentication
  - Mood-based playlist generation
  - Demo mode with sample tracks
  - Real Spotify playlist creation
  - Beautiful UI with custom styling

#### `requirements.txt` - Dependencies
- **Size**: ~100B, 6 lines
- **Purpose**: Lists all required Python packages
- **Dependencies**:
  - `streamlit>=1.32.0` - Web framework
  - `spotipy>=2.23.0` - Spotify API wrapper
  - `requests>=2.31.0` - HTTP requests
  - `python-dotenv>=1.0.0` - Environment management
  - `pandas>=2.2.0` - Data manipulation
  - `numpy>=1.26.0` - Numerical computing

#### `env_example.txt` - Environment Template
- **Size**: ~294B, 7 lines
- **Purpose**: Template for Spotify API credentials
- **Usage**: Copy to `.env` and fill in credentials
- **Variables**:
  - `SPOTIFY_CLIENT_ID` - Your Spotify app client ID
  - `SPOTIFY_CLIENT_SECRET` - Your Spotify app client secret
  - `SPOTIFY_REDIRECT_URI` - OAuth redirect URI

### 📚 Documentation Files

#### `README.md` - Quick Start Guide
- **Size**: ~6.1KB, 208 lines
- **Purpose**: Project overview and quick setup
- **Contents**:
  - Feature overview
  - Quick start instructions
  - Spotify API setup guide
  - Deployment options

#### `DOCUMENTATION.md` - Comprehensive Guide
- **Size**: ~15KB, 400+ lines
- **Purpose**: Complete documentation and reference
- **Contents**:
  - Detailed usage instructions
  - Terminal commands reference
  - File structure explanations
  - Troubleshooting guide
  - Deployment instructions

#### `QUICK_REFERENCE.md` - Terminal Commands
- **Size**: ~3KB, 100+ lines
- **Purpose**: Quick access to common commands
- **Contents**:
  - Essential commands
  - Troubleshooting commands
  - One-liners for common scenarios

#### `PROJECT_STRUCTURE.md` - This File
- **Purpose**: Visual project overview
- **Contents**:
  - File structure diagram
  - File descriptions
  - Directory explanations

### ⚙️ Configuration Files

#### `.streamlit/config.toml` - Streamlit Settings
- **Size**: ~155B, 11 lines
- **Purpose**: Streamlit deployment configuration
- **Settings**:
  - `headless = true` - Run without browser
  - `port = 8501` - Default port
  - `enableCORS = false` - Disable CORS
  - `enableXsrfProtection = false` - Disable XSRF

### 🐍 Virtual Environment

#### `mood_playlist_env/` - Python Environment
- **Purpose**: Isolated Python environment
- **Contents**:
  - **`bin/`**: Executable scripts (python, pip, etc.)
  - **`lib/`**: Installed Python packages
  - **`include/`**: Header files for compilation
  - **`pyvenv.cfg`**: Environment configuration

**Activation**:
```bash
source mood_playlist_env/bin/activate  # macOS/Linux
```

---

## 🔧 File Relationships

### Application Flow
```
app.py
├── Loads environment variables from .env
├── Imports dependencies from requirements.txt
├── Uses configuration from .streamlit/config.toml
├── Creates playlists via Spotify API
└── Displays results in Streamlit UI
```

### Setup Flow
```
1. requirements.txt → pip install dependencies
2. env_example.txt → .env (user creates)
3. .env → app.py loads credentials
4. app.py → Streamlit web interface
```

### Documentation Flow
```
README.md → Quick start
DOCUMENTATION.md → Complete reference
QUICK_REFERENCE.md → Terminal commands
PROJECT_STRUCTURE.md → File overview
```

---

## 📊 File Statistics

| File | Size | Lines | Purpose |
|------|------|-------|---------|
| `app.py` | 12KB | 249 | Main application |
| `requirements.txt` | 100B | 6 | Dependencies |
| `env_example.txt` | 294B | 7 | Environment template |
| `README.md` | 6.1KB | 208 | Quick start guide |
| `DOCUMENTATION.md` | 15KB | 400+ | Complete documentation |
| `QUICK_REFERENCE.md` | 3KB | 100+ | Terminal commands |
| `.streamlit/config.toml` | 155B | 11 | Streamlit config |

---

## 🎯 Key Directories

### 📁 Root Directory
- **Purpose**: Main project folder
- **Contains**: All application files and documentation
- **Access**: `cd Mood_Playlist`

### 📁 `.streamlit/`
- **Purpose**: Streamlit configuration
- **Contains**: `config.toml` with deployment settings
- **Usage**: Automatically read by Streamlit

### 📁 `mood_playlist_env/`
- **Purpose**: Python virtual environment
- **Contains**: Isolated Python installation
- **Activation**: `source mood_playlist_env/bin/activate`

---

## 🔍 File Search

### Find Specific Content
```bash
# Search for Spotify-related code
grep -r "spotify" app.py

# Search for environment variables
grep -r "SPOTIFY" .

# Search for function definitions
grep -r "def " app.py
```

### List All Files
```bash
# Show all files recursively
find . -type f -name "*.py" -o -name "*.md" -o -name "*.txt" -o -name "*.toml"

# Show only Python files
find . -name "*.py"

# Show only documentation files
find . -name "*.md"
```

---

*📝 Note: This structure represents the current state of your Mood Playlist Generator project. All files are essential for the application to function properly.* 