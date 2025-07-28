# 🚀 Quick Reference - Terminal Commands

## 🎯 Essential Commands

### Start the App
```bash
# Activate environment and run
source mood_playlist_env/bin/activate && streamlit run app.py --server.port 8504
```

### Stop the App
```bash
# Kill all Streamlit processes
pkill -f "streamlit run"

# Or kill specific port
lsof -ti:8504 | xargs kill -9
```

### Restart the App
```bash
# Kill and restart in one command
pkill -f "streamlit run" && sleep 2 && source mood_playlist_env/bin/activate && streamlit run app.py --server.port 8504
```

## 🔧 Troubleshooting Commands

### Port Issues
```bash
# Check what's using port 8504
lsof -i :8504

# Kill process on port 8504
lsof -ti:8504 | xargs kill -9
```

### Cache Issues
```bash
# Remove Spotify cache
rm -f .spotify_cache*

# Remove all cache files
rm -f cache* && rm -f *.cache
```

### Environment Issues
```bash
# Check Python version
python --version

# Check if virtual environment is active
which python

# Reinstall dependencies
pip install -r requirements.txt
```

## 📊 Status Commands

### Check App Status
```bash
# Test if app is responding
curl -s http://127.0.0.1:8504 | head -5

# Check app logs
tail -f ~/.streamlit/logs/streamlit.log
```

### Environment Verification
```bash
# List environment variables
env | grep SPOTIFY

# Check installed packages
pip list
```

## 🛠️ Development Commands

### Package Management
```bash
# Update requirements.txt
pip freeze > requirements.txt

# Check outdated packages
pip list --outdated
```

### Environment Management
```bash
# Create new environment
python3.13 -m venv mood_playlist_env

# Activate environment
source mood_playlist_env/bin/activate

# Deactivate environment
deactivate
```

## 🚀 Deployment Commands

### Local Development
```bash
# Standard run
streamlit run app.py

# Custom port
streamlit run app.py --server.port 8504

# Headless mode
streamlit run app.py --server.headless true --server.port 8504
```

### Debug Mode
```bash
# Run with debug logging
streamlit run app.py --logger.level debug
```

## 📝 One-Liners

### Complete Restart (Recommended)
```bash
pkill -f "streamlit run" && sleep 3 && source mood_playlist_env/bin/activate && streamlit run app.py --server.port 8504
```

### Clean Restart (Clear Cache)
```bash
rm -f .spotify_cache* && pkill -f "streamlit run" && sleep 2 && source mood_playlist_env/bin/activate && streamlit run app.py --server.port 8504
```

### Environment Check
```bash
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('CLIENT_ID:', os.getenv('SPOTIFY_CLIENT_ID')[:10] + '...' if os.getenv('SPOTIFY_CLIENT_ID') else 'Not set')"
```

---

## 🎯 Common Scenarios

### Scenario 1: App Won't Start (Port in Use)
```bash
lsof -ti:8504 | xargs kill -9 && source mood_playlist_env/bin/activate && streamlit run app.py --server.port 8504
```

### Scenario 2: Spotify Authentication Issues
```bash
rm -f .spotify_cache* && source mood_playlist_env/bin/activate && streamlit run app.py --server.port 8504
```

### Scenario 3: Fresh Start (Clear Everything)
```bash
rm -f .spotify_cache* && rm -f cache* && pkill -f "streamlit run" && sleep 3 && source mood_playlist_env/bin/activate && streamlit run app.py --server.port 8504
```

---

*💡 Tip: Copy and paste these commands directly into your terminal for quick access!* 