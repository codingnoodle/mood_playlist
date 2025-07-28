# 🔒 Git Deployment Guide - Protecting Your Credentials

## 🎯 Overview

This guide shows you how to safely push your Mood Playlist app to Git while keeping your Spotify API credentials secure.

## ✅ What's Protected

The `.gitignore` file protects these sensitive files:
- **`.env`** - Your Spotify API credentials
- **`.spotify_cache*`** - Spotify authentication cache
- **`mood_playlist_env/`** - Virtual environment (large files)
- **`__pycache__/`** - Python cache files
- **`.DS_Store`** - macOS system files

## 📁 What Will Be Pushed

✅ **Safe to push** (these files will be included):
- `app.py` - Main application
- `requirements.txt` - Dependencies
- `env_example.txt` - Template for credentials
- `README.md` - Project documentation
- `DOCUMENTATION.md` - Complete guide
- `QUICK_REFERENCE.md` - Terminal commands
- `PROJECT_STRUCTURE.md` - File overview
- `.gitignore` - Git ignore rules
- `.streamlit/config.toml` - Streamlit configuration

❌ **Protected from push** (these files will be ignored):
- `.env` - Your actual Spotify credentials
- `.spotify_cache*` - Authentication cache
- `mood_playlist_env/` - Virtual environment
- Any other sensitive files

---

## 🚀 Step-by-Step Deployment

### Step 1: Verify Protection
```bash
# Check what will be committed
git status

# Verify .env is NOT in the list
# If you see .env in the list, the .gitignore isn't working
```

### Step 2: Add Safe Files
```bash
# Add all safe files
git add .gitignore README.md DOCUMENTATION.md QUICK_REFERENCE.md PROJECT_STRUCTURE.md app.py requirements.txt env_example.txt .streamlit/
```

### Step 3: Verify Before Commit
```bash
# Check what's staged
git status

# Should show your files but NOT .env
```

### Step 4: Commit
```bash
git commit -m "Initial commit: Mood Playlist Generator with comprehensive documentation"
```

### Step 5: Add Remote Repository
```bash
# Replace with your actual repository URL
git remote add origin https://github.com/yourusername/mood-playlist.git
```

### Step 6: Push to GitHub
```bash
git push -u origin main
```

---

## 🔍 Verification Commands

### Check What's Being Tracked
```bash
# See all tracked files
git ls-files

# Should NOT include .env
```

### Check What's Ignored
```bash
# Test if .env is ignored
git check-ignore .env

# Should return ".env" if working correctly
```

### View Ignored Files
```bash
# See all ignored files
git status --ignored
```

---

## 🛡️ Security Best Practices

### 1. Never Commit Credentials
```bash
# ❌ WRONG - Never do this
git add .env
git commit -m "Add credentials"

# ✅ CORRECT - Use .gitignore
# .env is automatically ignored
```

### 2. Use Environment Templates
```bash
# ✅ Good: Include template
git add env_example.txt

# ❌ Bad: Include actual credentials
git add .env
```

### 3. Check Before Pushing
```bash
# Always verify before pushing
git status
git diff --cached
```

---

## 🔧 Repository Setup for Others

### For Contributors/Users

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/mood-playlist.git
   cd mood-playlist
   ```

2. **Set up environment**:
   ```bash
   # Copy template
   cp env_example.txt .env
   
   # Edit with your credentials
   nano .env
   ```

3. **Install dependencies**:
   ```bash
   python3.13 -m venv mood_playlist_env
   source mood_playlist_env/bin/activate
   pip install -r requirements.txt
   ```

4. **Run the app**:
   ```bash
   streamlit run app.py --server.port 8504
   ```

---

## 🚨 Troubleshooting

### Problem: .env is showing in git status
**Solution**:
```bash
# Check if .env is in .gitignore
cat .gitignore | grep env

# If not, add it
echo ".env" >> .gitignore

# Remove from git if already tracked
git rm --cached .env
```

### Problem: Accidentally committed .env
**Solution**:
```bash
# Remove from git history (DANGEROUS - rewrites history)
git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch .env' --prune-empty --tag-name-filter cat -- --all

# Force push (DANGEROUS)
git push origin --force
```

### Problem: Need to update .gitignore
**Solution**:
```bash
# Add new ignore rules
echo "new-file-to-ignore" >> .gitignore

# Commit the updated .gitignore
git add .gitignore
git commit -m "Update .gitignore"
```

---

## 📋 Pre-Push Checklist

Before pushing to Git, verify:

- [ ] `.env` is NOT in `git status`
- [ ] `.spotify_cache*` files are ignored
- [ ] `mood_playlist_env/` is ignored
- [ ] `env_example.txt` is included (template)
- [ ] All documentation files are included
- [ ] `app.py` and `requirements.txt` are included
- [ ] `.gitignore` is included

---

## 🎯 Quick Commands

### Safe Push (One-liner)
```bash
git add . && git commit -m "Update Mood Playlist app" && git push
```

### Check Protection
```bash
git status --ignored | grep env
```

### Clean Repository
```bash
# Remove any accidentally tracked sensitive files
git rm --cached .env 2>/dev/null || true
git rm --cached .spotify_cache* 2>/dev/null || true
```

---

## 🔐 Additional Security

### For Production Deployment

1. **Use Streamlit Secrets**:
   ```toml
   # .streamlit/secrets.toml
   SPOTIFY_CLIENT_ID = "your_client_id"
   SPOTIFY_CLIENT_SECRET = "your_client_secret"
   SPOTIFY_REDIRECT_URI = "https://your-app-url.com"
   ```

2. **Environment Variables in Deployment**:
   - Set environment variables in your deployment platform
   - Never commit actual credentials

3. **Regular Security Audits**:
   ```bash
   # Check for any sensitive files
   git log --all --full-history -- "*password*" "*secret*" "*key*"
   ```

---

*🔒 Remember: Once you push credentials to a public repository, consider them compromised. Always use .gitignore and environment variables for sensitive data.* 