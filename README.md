# Youtube-Automation
# 🎥 Brainrot Shorts Automation System (AI + Python + YouTube)
### Fully Automated AI-Generated YouTube Shorts • Uses OpenAI + ElevenLabs + FFmpeg • Deployable on Railway for Free

This project automatically generates, renders, and uploads **5 YouTube Shorts per day** based on
chaotic “useless brainrot facts” using AI tools.

Once deployed, **you do nothing**.  
The system runs entirely on its own.

---

# 🚀 Features
- ✔ Generates 20 chaotic “useless” facts daily using AI  
- ✔ Selects 5 facts and converts them into short scripts  
- ✔ Uses ElevenLabs (Gen-Z chaotic female voice) for narration  
- ✔ Builds 1080×1920 vertical Shorts using Python + FFmpeg  
- ✔ Adds subtitles + meme backgrounds automatically  
- ✔ Uploads videos to YouTube via YouTube Data API  
- ✔ Runs **daily on Railway (free cloud hosting)**  
- ✔ 100% automated; no manual work required  

---

# System Architecture
README.md (FINAL VERSION)
# 🎥 Brainrot Shorts Automation System (AI + Python + YouTube)
### Fully Automated AI-Generated YouTube Shorts • Uses OpenAI + ElevenLabs + FFmpeg • Deployable on Railway for Free

This project automatically generates, renders, and uploads **5 YouTube Shorts per day** based on
chaotic “useless brainrot facts” using AI tools.

Once deployed, **you do nothing**.  
The system runs entirely on its own.

---

# 🚀 Features
- ✔ Generates 20 chaotic “useless” facts daily using AI  
- ✔ Selects 5 facts and converts them into short scripts  
- ✔ Uses ElevenLabs (Gen-Z chaotic female voice) for narration  
- ✔ Builds 1080×1920 vertical Shorts using Python + FFmpeg  
- ✔ Adds subtitles + meme backgrounds automatically  
- ✔ Uploads videos to YouTube via YouTube Data API  
- ✔ Runs **daily on Railway (free cloud hosting)**  
- ✔ 100% automated; no manual work required  

---

# 🧠 System Architecture



Daily Cron (Railway)
↓
AI Fact Generator (OpenAI)
↓
Text-to-Speech (ElevenLabs)
↓
Video Builder (Python + FFmpeg)
↓
YouTube Short Upload (YouTube API)
↓
Logs Saved


---

# 📁 Project Structure



brainrot-youtube-automation/
│
├── python/
│ ├── generate_facts.py # AI fact generator
│ ├── tts_voice.py # ElevenLabs narration
│ ├── build_video.py # FFmpeg video builder
│ ├── upload_youtube.py # YouTube API uploader
│ ├── run_daily.py # Main script (5 shorts per day)
│
├── assets/
│ ├── backgrounds/ # Meme/gradient images
│ ├── fonts/ # Caption fonts
│
├── requirements.txt
├── README.md
└── architecture.png


---

# 🔧 Requirements
- Python 3.10+  
- FFmpeg installed (Railway install included)  
- OpenAI API key  
- ElevenLabs API key  
- YouTube OAuth credentials  

---

# 🔑 Environment Variables

Create a `.env` file with:



OPENAI_API_KEY=your_openai_key
ELEVEN_API_KEY=your_elevenlabs_key

YOUTUBE_CLIENT_ID=your_client_id
YOUTUBE_CLIENT_SECRET=your_client_secret
YOUTUBE_REFRESH_TOKEN=your_refresh_token
CHANNEL_ID=your_channel_id


These allow the system to talk to OpenAI, ElevenLabs, and YouTube.

---

# ▶️ Running Locally (Optional)



pip install -r requirements.txt
python run_daily.py


This will generate 1 Short and upload it to YouTube.

---

# ☁️ Deploying to Railway (FREE)

1. Go to **https://railway.app/**
2. Create a new project → Deploy from GitHub  
3. Add all Environment Variables  
4. Add a **Cron Job**:


0 */4 * * *

→ Runs every 4 hours (5 Shorts per day)

5. Railway will automatically:
- Install Python
- Install FFmpeg
- Run your script daily

---

# 🎨 Example Output Style
- Gen-Z chaotic voice  
- Meme backgrounds  
- Big bold subtitles  
- 5–7 second Shorts  
- High-energy pacing  

Perfect for YouTube Shorts growth.

---

# 🧩 Tech Used
- OpenAI GPT-4o-mini  
- ElevenLabs TTS  
- Python  
- FFmpeg  
- Railway Cron  
- YouTube Data API  

---

# 📜 License
MIT License

---

# ❤️ Credits
Built entirely with AI automation to help creators grow without stress.
