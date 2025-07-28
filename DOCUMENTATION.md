# 🎵 Mood Playlist Generator - Complete Documentation

## 📋 Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Installation & Setup](#installation--setup)
4. [Usage Guide](#usage-guide)
5. [Terminal Commands](#terminal-commands)
6. [File Structure & Explanations](#file-structure--explanations)
7. [Troubleshooting](#troubleshooting)
8. [Deployment](#deployment)

---

## 🎯 Overview

The **Mood Playlist Generator** is a Streamlit web application that creates personalized music playlists based on your current mood. It features both a demo mode for instant playlists and full Spotify integration for creating real playlists in your Spotify account.

### Key Capabilities:
- **4 Mood Options**: Happy, Sad, Energetic, Chill
- **Demo Mode**: Instant playlists with sample tracks (no setup required)
- **Spotify Integration**: Create real playlists in your Spotify account
- **Smart Genre Mapping**: Each mood maps to specific music genres
- **Beautiful UI**: Modern, responsive design with custom styling

---

## ✨ Features

### 🎭 Mood-Based Playlist Generation
- **Happy**: Pop, Dance, Electronic genres for upbeat vibes
- **Sad**: Indie, Folk, Acoustic genres for comfort and reflection
- **Energetic**: Rock, Metal, Electronic genres for high-energy motivation
- **Chill**: Chill, Ambient, Jazz genres for relaxation

### 🎵 Two-Mode System
1. **Demo Mode**: 
   - Instant playlists with curated sample tracks
   - No authentication required
   - Direct links to real Spotify tracks
   - Perfect for testing and demonstration

2. **Spotify Integration**:
   - Creates real playlists in your Spotify account
   - Searches Spotify's library for mood-appropriate tracks
   - Public playlists that can be shared with friends
   - Full OAuth authentication flow

### 🎨 User Experience
- **Responsive Design**: Works on desktop and mobile
- **Real-time Stats**: Track your playlist creation history
- **Mood Guide**: Learn about each mood and its characteristics
- **Progress Indicators**: Visual feedback during playlist generation

---

## 🚀 Installation & Setup

### Prerequisites
- **Python 3.13** (recommended) or Python 3.9+
- **Git** (for cloning the repository)
- **Spotify Account** (for real playlist creation)

### Step 1: Clone and Navigate
```bash
git clone <repository-url>
cd Mood_Playlist
```

### Step 2: Create Virtual Environment
```bash
# Create virtual environment
python3.13 -m venv mood_playlist_env

# Activate virtual environment
source mood_playlist_env/bin/activate  # macOS/Linux
# or
mood_playlist_env\Scripts\activate     # Windows
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Environment Setup

#### Option A: Demo Mode Only (No Setup Required)
- Skip this step if you only want to use demo mode
- The app will work immediately without Spotify credentials

#### Option B: Full Spotify Integration
1. **Get Spotify API Credentials**:
   - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
   - Create a new app
   - Copy your `Client ID` and `Client Secret`

2. **Configure Redirect URI**:
   - In your Spotify app settings, add: `http://127.0.0.1:8504`
   - This must match exactly what the app uses

3. **Create Environment File**:
   ```bash
   cp env_example.txt .env
   ```

4. **Edit .env File**:
   ```bash
   # Open .env in your preferred editor
   nano .env
   # or
   code .env
   ```

5. **Add Your Credentials**:
   ```env
   SPOTIFY_CLIENT_ID=your_client_id_here
   SPOTIFY_CLIENT_SECRET=your_client_secret_here
   SPOTIFY_REDIRECT_URI=http://127.0.0.1:8504
   ```

---

## 📖 Usage Guide

### 🎯 Quick Start

1. **Launch the App**:
   ```bash
   streamlit run app.py --server.port 8504
   ```

2. **Access the App**:
   - Open your browser to: `http://127.0.0.1:8504`
   - The app will load with a beautiful interface

3. **Choose Your Mood**:
   - Select from: Happy, Sad, Energetic, or Chill
   - Each mood shows its description and associated genres

4. **Try Demo Mode First**:
   - Click "🎵 Generate Demo Playlist"
   - Get instant results with sample tracks
   - No login required

5. **Create Real Playlist** (if Spotify credentials configured):
   - Click "🎵 Create Real Spotify Playlist"
   - Authenticate with Spotify when prompted
   - Your playlist will be created in your Spotify account

### 🎭 Mood Guide

| Mood | Genres | Description | Best For |
|------|--------|-------------|----------|
| **Happy** | Pop, Dance, Electronic | Upbeat and energetic tracks | Celebrations, workouts, motivation |
| **Sad** | Indie, Folk, Acoustic | Gentle and soothing tracks | Reflection, comfort, emotional support |
| **Energetic** | Rock, Metal, Electronic | High-energy pump-up tracks | Workouts, parties, motivation |
| **Chill** | Chill, Ambient, Jazz | Relaxing laid-back vibes | Relaxation, study, meditation |

### 🔧 Advanced Usage

#### Customizing Genres
Edit the `MOOD_GENRES` dictionary in `app.py` to modify genre mappings:

```python
MOOD_GENRES = {
    "Happy": {
        "genres": ["pop", "dance", "electronic", "reggae"],
        "description": "Upbeat and energetic tracks to lift your spirits!",
        "color": "#FFD700",
    },
    # ... other moods
}
```

#### Adding Demo Tracks
Modify the `DEMO_TRACKS` dictionary to add your own sample tracks:

```python
DEMO_TRACKS = {
    "Happy": [
        {"name": "Your Song", "artist": "Your Artist", "url": "https://open.spotify.com/track/..."},
        # ... more tracks
    ],
    # ... other moods
}
```

---

## 💻 Terminal Commands

### 🚀 Running the App

#### Basic Launch
```bash
# Activate virtual environment
source mood_playlist_env/bin/activate

# Run the app
streamlit run app.py
```

#### Custom Port
```bash
# Run on specific port
streamlit run app.py --server.port 8504
```

#### Headless Mode (for deployment)
```bash
# Run without browser opening
streamlit run app.py --server.headless true --server.port 8504
```

### 🔧 Development Commands

#### Check Dependencies
```bash
# List installed packages
pip list

# Check for outdated packages
pip list --outdated

# Update requirements.txt
pip freeze > requirements.txt
```

#### Environment Management
```bash
# Create new virtual environment
python3.13 -m venv mood_playlist_env

# Activate environment
source mood_playlist_env/bin/activate

# Deactivate environment
deactivate

# Remove environment
rm -rf mood_playlist_env
```

#### Port Management
```bash
# Check what's using a port
lsof -i :8504

# Kill process on specific port
lsof -ti:8504 | xargs kill -9

# Kill all Streamlit processes
pkill -f "streamlit run"
```

#### Cache Management
```bash
# Remove Spotify cache
rm -f .spotify_cache*

# Remove all cache files
rm -f cache* && rm -f *.cache

# Clear Streamlit cache
streamlit cache clear
```

### 🐛 Debugging Commands

#### Check App Status
```bash
# Test if app is responding
curl -s http://127.0.0.1:8504 | head -5

# Check app logs
tail -f ~/.streamlit/logs/streamlit.log
```

#### Environment Verification
```bash
# Check Python version
python --version

# Check if virtual environment is active
which python

# List environment variables
env | grep SPOTIFY
```

---

## 📁 File Structure & Explanations

### Core Application Files

#### `app.py` - Main Application
**Purpose**: The primary Streamlit application file
**Key Components**:
- **Configuration**: Spotify API credentials and settings
- **Mood Data**: Genre mappings and demo tracks for each mood
- **Spotify Integration**: OAuth authentication and playlist creation
- **UI Components**: Streamlit interface and styling
- **Utility Functions**: Track fetching and demo rendering

**Key Functions**:
- `get_spotify()`: Creates authenticated Spotify client
- `render_demo()`: Displays demo playlists
- `fetch_tracks()`: Searches Spotify for mood-appropriate tracks
- `main()`: Main application logic

#### `requirements.txt` - Dependencies
**Purpose**: Lists all Python packages required for the app
**Contents**:
```
streamlit>=1.32.0    # Web framework
spotipy>=2.23.0      # Spotify API wrapper
requests>=2.31.0     # HTTP requests
python-dotenv>=1.0.0 # Environment variable management
pandas>=2.2.0        # Data manipulation
numpy>=1.26.0        # Numerical computing
```

#### `env_example.txt` - Environment Template
**Purpose**: Template for Spotify API credentials
**Usage**: Copy to `.env` and fill in your credentials
**Required Variables**:
- `SPOTIFY_CLIENT_ID`: Your Spotify app client ID
- `SPOTIFY_CLIENT_SECRET`: Your Spotify app client secret
- `SPOTIFY_REDIRECT_URI`: OAuth redirect URI (default: http://127.0.0.1:8504)

### Configuration Files

#### `.streamlit/config.toml` - Streamlit Configuration
**Purpose**: Streamlit deployment and server settings
**Key Settings**:
- `headless = true`: Run without opening browser
- `port = 8501`: Default port (can be overridden)
- `enableCORS = false`: Disable CORS for local development
- `enableXsrfProtection = false`: Disable XSRF protection

### Virtual Environment

#### `mood_playlist_env/` - Python Virtual Environment
**Purpose**: Isolated Python environment for the project
**Contains**:
- Python interpreter
- Installed packages
- Scripts for environment activation

**Activation**:
```bash
source mood_playlist_env/bin/activate  # macOS/Linux
```

### Documentation Files

#### `README.md` - Project Overview
**Purpose**: Quick start guide and project description
**Contents**:
- Feature overview
- Quick start instructions
- Spotify API setup guide
- Deployment options

#### `DOCUMENTATION.md` - This File
**Purpose**: Comprehensive documentation and reference
**Contents**:
- Detailed usage instructions
- Terminal commands reference
- File structure explanations
- Troubleshooting guide

---

## 🔧 Troubleshooting

### Common Issues & Solutions

#### 1. Port Already in Use
**Error**: `Port 8504 is already in use`
**Solution**:
```bash
# Kill process on port 8504
lsof -ti:8504 | xargs kill -9

# Or kill all Streamlit processes
pkill -f "streamlit run"
```

#### 2. Spotify Authentication Issues
**Error**: `Invalid redirect URI`
**Solution**:
1. Check that redirect URI in Spotify Dashboard matches app
2. Ensure `.env` file has correct `SPOTIFY_REDIRECT_URI`
3. Clear Spotify cache: `rm -f .spotify_cache*`

#### 3. Module Not Found Errors
**Error**: `ModuleNotFoundError: No module named 'spotipy'`
**Solution**:
```bash
# Activate virtual environment
source mood_playlist_env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 4. Python Version Issues
**Error**: Compatibility issues with older Python versions
**Solution**:
```bash
# Install Python 3.13 (macOS)
brew install python@3.13

# Create new virtual environment
python3.13 -m venv mood_playlist_env
```

#### 5. Spotify API Rate Limits
**Error**: `429 Too Many Requests`
**Solution**:
- Wait a few minutes before making more requests
- Reduce the number of tracks fetched per mood
- Implement request throttling in the code

### Debug Mode

#### Enable Debug Logging
```bash
# Run with debug output
streamlit run app.py --logger.level debug
```

#### Check Environment Variables
```bash
# Verify Spotify credentials are loaded
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('CLIENT_ID:', os.getenv('SPOTIFY_CLIENT_ID')[:10] + '...' if os.getenv('SPOTIFY_CLIENT_ID') else 'Not set')"
```

---

## 🚀 Deployment

### Local Development
```bash
# Standard development run
streamlit run app.py --server.port 8504
```

### Production Deployment

#### Streamlit Cloud (Recommended)
1. **Push to GitHub**:
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub repository
   - Set environment variables in Streamlit Cloud dashboard
   - Deploy automatically

#### Other Platforms

##### Heroku
1. **Create `Procfile`**:
   ```
   web: streamlit run app.py --server.port=$PORT --server.headless=true
   ```

2. **Deploy**:
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

##### Railway
1. **Connect GitHub repository**
2. **Set environment variables**
3. **Deploy automatically**

### Environment Variables for Deployment

Set these in your deployment platform:
```env
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
SPOTIFY_REDIRECT_URI=https://your-app-url.com
```

---

## 📊 Performance & Optimization

### Caching Strategy
- **Spotify Client**: Cached with `@st.cache_resource`
- **Track Results**: Not cached to ensure fresh results
- **User Sessions**: Streamlit handles session state

### Memory Management
- **Demo Tracks**: Hardcoded for instant access
- **Spotify Tracks**: Fetched on-demand, limited to 10 tracks
- **Cache Cleanup**: Manual cache removal available

### Security Considerations
- **API Credentials**: Stored in environment variables
- **OAuth Flow**: Secure Spotify authentication
- **No Data Storage**: No user data stored locally

---

## 🤝 Contributing

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### Code Style
- Follow PEP 8 guidelines
- Use type hints where appropriate
- Add docstrings to functions
- Keep functions small and focused

---

## 📞 Support

### Getting Help
1. **Check this documentation** for common issues
2. **Review the README.md** for quick setup
3. **Check the troubleshooting section** above
4. **Open an issue** on GitHub for bugs

### Useful Resources
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Spotipy Documentation](https://spotipy.readthedocs.io/)
- [Spotify Web API](https://developer.spotify.com/documentation/web-api/)

---

## 📝 License

This project is open source and available under the MIT License.

---

*Last updated: July 2024*
*Version: 1.0.0* 