# app.py  –  Mood-Based Playlist Generator
# ---------------------------------------
import os
from typing import List

import spotipy
import streamlit as st
from dotenv import load_dotenv
from spotipy.cache_handler import MemoryCacheHandler
from spotipy.oauth2 import SpotifyOAuth

# ──────────────────────────────────────────────────────────────────────────────
# 🎛️  Configuration
# ──────────────────────────────────────────────────────────────────────────────
load_dotenv()

CLIENT_ID     = os.getenv("SPOTIPY_CLIENT_ID")     or os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET") or os.getenv("SPOTIFY_CLIENT_SECRET")

REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI") \
    or os.getenv("SPOTIFY_REDIRECT_URI") \
    or "http://127.0.0.1:8506/callback"

SCOPE = "playlist-modify-public playlist-modify-private user-read-private"

# ──────────────────────────────────────────────────────────────────────────────
# 🎵  Mood data
# ──────────────────────────────────────────────────────────────────────────────
MOOD_GENRES = {
    "Happy": {
        "genres": ["pop", "dance", "electronic"],
        "description": "Upbeat and energetic tracks to lift your spirits!",
        "color": "#FFD700",
    },
    "Sad": {
        "genres": ["indie", "folk", "acoustic"],
        "description": "Gentle and soothing tracks for reflection and comfort.",
        "color": "#87CEEB",
    },
    "Energetic": {
        "genres": ["rock", "metal", "electronic"],
        "description": "High-energy tracks to get you pumped up!",
        "color": "#FF6B6B",
    },
    "Chill": {
        "genres": ["chill", "ambient", "jazz"],
        "description": "Relaxing and laid-back vibes for unwinding.",
        "color": "#98FB98",
    },
}

DEMO_TRACKS = {
    "Happy": [
        {"name": "Happy", "artist": "Pharrell Williams", "url": "https://open.spotify.com/track/60nZcImufyMA1MKQY3dcCH"},
        {"name": "Can't Stop the Feeling!", "artist": "Justin Timberlake", "url": "https://open.spotify.com/track/3WcC6NH9J77xPEvj1x7BeB"},
        {"name": "Good Time", "artist": "Owl City & Carly Rae Jepsen", "url": "https://open.spotify.com/track/1kP5bgJQIk0JpiuYfLUTjx"},
    ],
    "Sad": [
        {"name": "Someone Like You", "artist": "Adele", "url": "https://open.spotify.com/track/1U4QN2CgYHN6YK3aFbLw7U"},
        {"name": "All of Me", "artist": "John Legend", "url": "https://open.spotify.com/track/3U4isOIWM3VvDubwSI3y7Z"},
        {"name": "Say Something", "artist": "A Great Big World", "url": "https://open.spotify.com/track/6Vc5wAMmXdKIAM7WUoEb7N"},
    ],
    "Energetic": [
        {"name": "Eye of the Tiger", "artist": "Survivor", "url": "https://open.spotify.com/track/2HHtWyy5CgwQZqBcI0r0uM"},
        {"name": "We Will Rock You", "artist": "Queen", "url": "https://open.spotify.com/track/54flyrjcdnQdco7300avMJ"},
        {"name": "Don't Stop Believin'", "artist": "Journey", "url": "https://open.spotify.com/track/4bHsxqR3GMrXTxEPLuK5ue"},
    ],
    "Chill": [
        {"name": "Weightless", "artist": "Marconi Union", "url": "https://open.spotify.com/track/3iIxFyoF2JkcXJw3Q5k2uD"},
        {"name": "Clair de Lune", "artist": "Debussy", "url": "https://open.spotify.com/track/1hnVm4tS30Eb7cWMsTqA5q"},
        {"name": "River Flows in You", "artist": "Yiruma", "url": "https://open.spotify.com/track/7yS7TgKosLgZtHNaR0upMz"},
    ],
}

# ──────────────────────────────────────────────────────────────────────────────
# ⚡  Spotify helper (cached)
# ──────────────────────────────────────────────────────────────────────────────
@st.cache_resource(show_spinner=False)
def get_spotify() -> spotipy.Spotify | None:
    if not CLIENT_ID or not CLIENT_SECRET:
        return None
    auth_manager = SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE,
        cache_handler=MemoryCacheHandler(),
        show_dialog=False,
        open_browser=True,
        requests_timeout=10,
    )
    return spotipy.Spotify(auth_manager=auth_manager)

# ──────────────────────────────────────────────────────────────────────────────
# 🎨  Streamlit styling
# ──────────────────────────────────────────────────────────────────────────────
st.set_page_config(page_title="Mood Playlist Generator", page_icon="🎵", layout="wide")

st.markdown(
    """
    <style>
      .main-header{font-size:3rem;font-weight:bold;text-align:center;color:#1DB954;margin-bottom:2rem;}
      .playlist-card{background:#f0f2f6;padding:1rem;border-radius:10px;margin:0.5rem 0;border-left:4px solid #1DB954;}
      .demo-notice{background:#d4edda;border:1px solid #c3e6cb;border-radius:5px;padding:1rem;margin:1rem 0;}
      .spotify-green{color:#1DB954;}
    </style>
    """,
    unsafe_allow_html=True,
)

# ──────────────────────────────────────────────────────────────────────────────
# 🛠️  Utility functions
# ──────────────────────────────────────────────────────────────────────────────
def render_demo(mood: str):
    tracks = DEMO_TRACKS[mood]
    st.success("✅ Demo playlist created!")
    st.markdown(
        f"""
        <div class='playlist-card'>
          <h3>🎵 Demo Playlist – {mood} Vibes</h3>
          <p><strong>Tracks:</strong> {len(tracks)}</p>
          <p><em>This is a demo only – connect Spotify to create a real playlist.</em></p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.subheader("📋 Tracks")
    for i, t in enumerate(tracks, 1):
        st.markdown(f"**{i}.** [{t['name']} – *{t['artist']}*]({t['url']})")

def fetch_tracks(sp: spotipy.Spotify, genres: List[str]):
    tracks: list = []
    for g in genres:
        try:
            res = sp.search(q=f"genre:{g}", type="track", limit=3, market="US")
            tracks.extend(res["tracks"]["items"])
        except Exception as e:
            st.warning(f"Search failed for {g}: {e}")
    return tracks

# ──────────────────────────────────────────────────────────────────────────────
# 🚀  Main app
# ──────────────────────────────────────────────────────────────────────────────
def main():
    st.markdown('<h1 class="main-header">🎵 Mood Playlist Generator</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;color:#666;">Create personalised playlists based on your mood!</p>', unsafe_allow_html=True)

    # --------------- Sidebar instructions ---------------
    with st.sidebar:
        st.header("📋 How to Use")
        st.markdown(
            """
            1. **Choose your mood**  
            2. **Generate demo playlist** (no login)  
            3. **Connect Spotify**  
            4. **Generate real playlist & enjoy!**
            """
        )

    main_col, side_col = st.columns([2, 1])

    # ---------------- Main column -----------------
    with main_col:
        st.header("🎭 Select your mood")
        mood = st.selectbox(
            "Mood:",
            list(MOOD_GENRES.keys()),
            format_func=lambda m: f"{m} – {MOOD_GENRES[m]['description']}",
        )

        meta = MOOD_GENRES[mood]
        st.markdown(
            f"""
            <div style="background:{meta['color']}20;border-left:4px solid {meta['color']};padding:1rem;border-radius:10px;">
              <h3>🎵 {mood} Vibes</h3>
              <p>{meta['description']}</p>
              <p><strong>Genres:</strong> {', '.join(meta['genres'])}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown('<div class="demo-notice">🎯 <b>Try Demo Mode First:</b> click below to see how it works without logging in.</div>', unsafe_allow_html=True)

        if st.button("🎵 Generate Demo Playlist", type="primary", use_container_width=True):
            render_demo(mood)

        # ---------- Spotify integration ----------
        st.markdown("---")
        st.header("🔗 Spotify Integration")

        if CLIENT_ID and CLIENT_SECRET:
            st.success("✅ Spotify credentials found.")

            if st.button("🎵 Create Real Spotify Playlist", use_container_width=True):
                sp = get_spotify()
                if sp is None:
                    st.error("Spotify client setup failed. Check your credentials.")
                    return

                with st.spinner("Authorising & fetching tracks…"):
                    try:
                        user          = sp.current_user()["id"]
                        tracks        = fetch_tracks(sp, meta["genres"])
                        if not tracks:
                            st.warning("No tracks found for that mood. Try a different one.")
                            return

                        playlist = sp.user_playlist_create(
                            user=user,
                            name=f"Mood Playlist – {mood} Vibes",
                            description=f"Generated for a {mood.lower()} mood",
                            public=True,
                        )
                        sp.playlist_add_items(playlist["id"], [t["uri"] for t in tracks[:10]])

                        st.success("✅ Playlist created!")
                        st.markdown(
                            f"""
                            <div class='playlist-card'>
                              <h3>🎵 {playlist['name']}</h3>
                              <p><strong>Tracks:</strong> {len(tracks[:10])}</p>
                              <a class='spotify-green' href='{playlist['external_urls']['spotify']}' target='_blank'>🎧 Open in Spotify</a>
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )

                        st.subheader("📋 Tracks")
                        for i, t in enumerate(tracks[:10], 1):
                            artists = ", ".join(a["name"] for a in t["artists"])
                            st.markdown(f"**{i}.** {t['name']} – *{artists}*")

                    except Exception as e:
                        st.error(f"Spotify error: {e}")
        else:
            st.warning("Spotify credentials missing – set SPOTIPY_CLIENT_ID & SECRET in your .env.")

    # -------------- Side column --------------
    with side_col:
        st.header("🎯 Quick Mood Guide")
        for m, meta in MOOD_GENRES.items():
            with st.expander(f"🎭 {m}"):
                st.markdown(f"**Description:** {meta['description']}")
                st.markdown(f"**Genres:** {', '.join(meta['genres'])}")

if __name__ == "__main__":
    main()
