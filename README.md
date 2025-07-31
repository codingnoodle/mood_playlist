# 🎵 Mood Playlist Generator

A beautiful Streamlit app that creates personalized playlists based on your current mood! Features both a demo mode for instant playlists and full Spotify integration for real playlists.

## ✨ Features

- **🎭 4 Mood Options**: Happy, Sad, Energetic, Chill
- **🎯 Demo Mode**: Instant playlists with sample tracks (no setup required)
- **🔗 Spotify Integration**: Create real playlists in your Spotify account
- **🎨 Beautiful UI**: Modern, responsive design with custom styling
- **📊 Real-time Stats**: Track your playlist creation history
- **🎯 Mood Guide**: Learn about each mood and its characteristics

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/codingnoodle/mood_playlist.git
cd mood_playlist
```

### 2. Set Up Virtual Environment

**On macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv mood_playlist_env

# Activate virtual environment
source mood_playlist_env/bin/activate
```

**On Windows:**
```bash
# Create virtual environment
python -m venv mood_playlist_env

# Activate virtual environment
mood_playlist_env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Choose Your Setup Option

#### Option A: Demo Mode (Instant - No Setup Required)

1. **Run the App**:
   ```bash
   streamlit run app.py
   ```

2. **Use Demo Mode**:
   - Choose your mood
   - Click "Generate Demo Playlist"
   - Get instant playlists with sample tracks!

#### Option B: Full Spotify Integration

1. **Set Up Spotify API**:
   - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
   - Create a new app
   - Add `http://127.0.0.1:8504` to Redirect URIs

2. **Configure Environment**:
   ```bash
   # Copy the example file
   cp env_example.txt .env
   
   # Edit .env with your credentials
   SPOTIFY_CLIENT_ID=your_client_id_here
   SPOTIFY_CLIENT_SECRET=your_client_secret_here
   SPOTIFY_REDIRECT_URI=http://127.0.0.1:8504
   ```

3. **Run the App**:
   ```bash
   streamlit run app.py
   ```

4. **Create Real Playlists**:
   - Choose your mood
   - Click "Create Real Spotify Playlist"
   - Authenticate with Spotify
   - Get real playlists in your account!

## 🎯 How It Works

### Demo Mode
- **No Authentication Required**: Works instantly
- **Sample Tracks**: Curated tracks for each mood
- **Spotify Links**: Direct links to real Spotify tracks
- **Instant Results**: No waiting or setup

### Spotify Integration
- **Real Playlists**: Creates actual playlists in your Spotify account
- **Smart Search**: Searches Spotify for mood-appropriate tracks
- **Direct Integration**: Adds tracks directly to your account
- **Public Playlists**: Share with friends!

### Mood Mapping

| Mood | Genres | Description |
|------|--------|-------------|
| **Happy** | Pop, Dance, Electronic | Upbeat and energetic tracks |
| **Sad** | Indie, Folk, Acoustic | Gentle and soothing tracks |
| **Energetic** | Rock, Metal, Electronic | High-energy pump-up tracks |
| **Chill** | Chill, Ambient, Jazz | Relaxing laid-back vibes |

## 📁 Project Structure

```
mood_playlist/
├── app.py                 # Main application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── env_example.txt       # Environment template
├── .streamlit/           # Streamlit configuration
│   └── config.toml
└── mood_playlist_env/    # Virtual environment
```

## 🛠️ Technical Stack

- **Frontend**: Streamlit (Python web framework)
- **Music API**: Spotify Web API via Spotipy
- **Authentication**: OAuth 2.0 with Spotify
- **Styling**: Custom CSS with modern design
- **Data Processing**: Pandas, NumPy

## 🚀 Deployment Options

### Streamlit Cloud (Recommended)

1. **Push to GitHub**:
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub account
   - Select your repository
   - Add your environment variables in the settings
   - Deploy!

### Other Platforms
- **Heroku**: Use the `requirements.txt` and set environment variables
- **Railway**: Connect GitHub repo and add environment variables
- **Vercel**: Deploy with Python runtime

## 🔧 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `SPOTIFY_CLIENT_ID` | Your Spotify App Client ID | For real playlists |
| `SPOTIFY_CLIENT_SECRET` | Your Spotify App Client Secret | For real playlists |
| `SPOTIFY_REDIRECT_URI` | OAuth redirect URI | For real playlists |

## 📱 Usage

### Demo Mode
1. **Choose Mood**: Select how you're feeling
2. **Generate Demo**: Click "Generate Demo Playlist"
3. **Enjoy**: View sample tracks with Spotify links

### Spotify Integration
1. **Choose Mood**: Select how you're feeling
2. **Authenticate**: Click "Create Real Spotify Playlist"
3. **Login**: Complete Spotify authentication
4. **Enjoy**: Open the playlist in Spotify

## 🎨 Customization

### Adding New Moods
Edit the `MOOD_GENRES` dictionary in `app.py`:

```python
"New Mood": {
    "genres": ["genre1", "genre2"],
    "description": "Your mood description",
    "color": "#HEXCODE"
}
```

### Adding Demo Tracks
Edit the `DEMO_TRACKS` dictionary in `app.py`:

```python
"New Mood": [
    {"name": "Song Name", "artist": "Artist Name", "url": "spotify_url"},
    # Add more tracks...
]
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- [Spotify Web API](https://developer.spotify.com/documentation/web-api/) for music data
- [Streamlit](https://streamlit.io/) for the web framework
- [Spotipy](https://spotipy.readthedocs.io/) for Spotify API wrapper

## 🆘 Troubleshooting

### Demo Mode Issues
- **App not loading**: Check if Streamlit is installed correctly
- **No playlists showing**: Refresh the page and try again

### Spotify Integration Issues
- **"Spotify credentials not found"**: Make sure you've created a `.env` file
- **"Authentication error"**: Check your Client ID and Secret
- **"Invalid redirect URI"**: Ensure redirect URI matches your Spotify app settings
- **"No tracks found"**: Try a different mood or check internet connection

### General Issues
- **Port conflicts**: Try running on a different port: `streamlit run app.py --server.port 8505`
- **Dependencies**: Make sure all packages are installed: `pip install -r requirements.txt`
- **Virtual environment**: Ensure you're in the correct virtual environment before installing dependencies

---

**Made with ❤️ and 🎵 for music lovers everywhere!** 
