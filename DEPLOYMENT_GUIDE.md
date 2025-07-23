# 🚀 Deployment Guide - Resume Chatbot

This guide provides step-by-step instructions to host your resume chatbot on various platforms with a public domain.

## 🎯 Recommended Option: Railway (Easiest)

Railway is the simplest option for Python apps with automatic deployments from GitHub.

### Step 1: Prepare Your Repository

1. **Create a `requirements.txt` file** (Railway doesn't use uv by default):
   ```bash
   uv export --no-hashes --format requirements-txt > requirements.txt
   ```

2. **Create a `Procfile`** in your project root:
   ```
   web: uvicorn app:app --host 0.0.0.0 --port $PORT
   ```

3. **Commit and push changes**:
   ```bash
   git add .
   git commit -m "Add deployment files"
   git push origin main
   ```

### Step 2: Deploy on Railway

1. **Sign up at [Railway](https://railway.app)**
   - Use your GitHub account to sign up

2. **Create a new project**:
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your `resume-chatbot` repository

3. **Configure environment variables**:
   - Go to your project dashboard
   - Click on "Variables" tab
   - Add:
     - `ANTHROPIC_API_KEY` = your_claude_api_key
     - `PUSHOVER_TOKEN` = your_pushover_token (optional)
     - `PUSHOVER_USER` = your_pushover_user (optional)

4. **Deploy**:
   - Railway will automatically build and deploy
   - You'll get a public URL like `https://your-app-name.railway.app`

5. **Custom Domain** (Optional):
   - Go to "Settings" → "Domains"
   - Add your custom domain
   - Configure DNS as instructed

---

## 🌟 Alternative Option: Render (Free Tier Available)

### Step 1: Prepare Your Repository

1. **Create `requirements.txt`** (if not done above):
   ```bash
   uv export --no-hashes --format requirements-txt > requirements.txt
   ```

2. **Create `render.yaml`** in your project root:
   ```yaml
   services:
     - type: web
       name: resume-chatbot
       env: python
       buildCommand: pip install -r requirements.txt
       startCommand: uvicorn app:app --host 0.0.0.0 --port $PORT
       envVars:
         - key: ANTHROPIC_API_KEY
           sync: false
         - key: PUSHOVER_TOKEN
           sync: false
         - key: PUSHOVER_USER
           sync: false
   ```

### Step 2: Deploy on Render

1. **Sign up at [Render](https://render.com)**
   - Use your GitHub account

2. **Create a new web service**:
   - Click "New" → "Web Service"
   - Connect your GitHub repository
   - Select `resume-chatbot`

3. **Configure deployment**:
   - **Name**: resume-chatbot
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app:app --host 0.0.0.0 --port $PORT`

4. **Set environment variables**:
   - Add `ANTHROPIC_API_KEY`
   - Add `PUSHOVER_TOKEN` (optional)
   - Add `PUSHOVER_USER` (optional)

5. **Deploy**:
   - Click "Create Web Service"
   - You'll get a URL like `https://resume-chatbot-xyz.onrender.com`

---

## 🔧 Alternative Option: Heroku

### Step 1: Prepare Your Repository

1. **Install Heroku CLI**:
   ```bash
   # macOS
   brew tap heroku/brew && brew install heroku
   
   # Or download from https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Create required files**:
   
   **`requirements.txt`**:
   ```bash
   uv export --no-hashes --format requirements-txt > requirements.txt
   ```
   
   **`Procfile`**:
   ```
   web: uvicorn app:app --host 0.0.0.0 --port $PORT
   ```
   
   **`runtime.txt`**:
   ```
   python-3.11.0
   ```

### Step 2: Deploy to Heroku

1. **Login and create app**:
   ```bash
   heroku login
   heroku create your-resume-chatbot
   ```

2. **Set environment variables**:
   ```bash
   heroku config:set ANTHROPIC_API_KEY=your_claude_api_key
   heroku config:set PUSHOVER_TOKEN=your_pushover_token
   heroku config:set PUSHOVER_USER=your_pushover_user
   ```

3. **Deploy**:
   ```bash
   git add .
   git commit -m "Prepare for Heroku deployment"
   git push heroku main
   ```

4. **Open your app**:
   ```bash
   heroku open
   ```

---

## 🌐 Custom Domain Setup

### Option 1: Using Cloudflare (Recommended)

1. **Purchase a domain** from any registrar (Namecheap, GoDaddy, etc.)

2. **Set up Cloudflare**:
   - Create a Cloudflare account
   - Add your domain to Cloudflare
   - Update nameservers at your registrar

3. **Configure DNS**:
   - Add a CNAME record pointing your domain to your app URL
   - Example: `resume.yourdomain.com` → `your-app.railway.app`

4. **Enable SSL**:
   - Cloudflare provides free SSL certificates
   - Set SSL mode to "Full" or "Flexible"

### Option 2: Direct DNS Configuration

1. **Purchase a domain**

2. **Configure DNS records**:
   - Add a CNAME record: `www` → `your-app.railway.app`
   - Add a CNAME record: `@` → `your-app.railway.app`

3. **Configure on your hosting platform**:
   - Add custom domain in Railway/Render/Heroku settings
   - Follow platform-specific SSL setup

---

## 🔐 Environment Variables Setup

Create a `.env.example` file for documentation:

```bash
ANTHROPIC_API_KEY=your_claude_api_key_here
PUSHOVER_TOKEN=your_pushover_token_here
PUSHOVER_USER=your_pushover_user_here
```

**Important**: Never commit your actual `.env` file to git!

---

## 📊 Monitoring and Maintenance

### 1. Health Checks
Your app includes a `/health` endpoint for monitoring:
```
GET https://yourdomain.com/health
```

### 2. Logs Monitoring
- **Railway**: View logs in dashboard
- **Render**: Check logs in service dashboard
- **Heroku**: `heroku logs --tail`

### 3. Auto-Deploy Setup
All platforms support automatic deployment from GitHub:
- Push to `main` branch → automatic deployment
- Great for continuous deployment

---

## 💰 Cost Comparison

| Platform | Free Tier | Paid Plans | Custom Domain |
|----------|-----------|------------|---------------|
| **Railway** | $5 credit/month | $5/month | Free |
| **Render** | 750 hours/month | $7/month | Free |
| **Heroku** | None (2022+) | $7/month | Free |

---

## 🎯 Recommended Steps

1. **Start with Railway** (easiest setup)
2. **Use Cloudflare** for DNS and SSL
3. **Purchase a professional domain** like `prakhar-resume.com`
4. **Set up monitoring** and health checks
5. **Enable auto-deployment** from GitHub

## 🔍 Troubleshooting

### Common Issues:

1. **Build failures**: Check `requirements.txt` format
2. **Port issues**: Ensure using `$PORT` environment variable
3. **Static files**: Verify `/static` route works locally first
4. **API key issues**: Double-check environment variables

### Debug Commands:
```bash
# Test locally first
python run.py

# Check environment variables
echo $ANTHROPIC_API_KEY

# Test API endpoint
curl https://yourdomain.com/health
```

---

**🚀 Your resume chatbot will be live and accessible to the world!**