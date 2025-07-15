# 🤖 Reddit User Persona Generator (LLM-powered)

This project fetches Reddit posts and comments from a user profile and uses a **Large Language Model (LLM)** to generate a detailed **user persona**, citing evidence from actual posts and comments.

✅ No Reddit API key needed  
✅ Powered by Google Gemini 1.5 Flash  
✅ Persona stored in outputs folder
---

## 🚀 Features

- 📬 **Input**: A Reddit user profile URL  
- 🌐 **Scraping**: Gathers recent posts and comments using Reddit’s **public JSON API**  
- 🤖 **LLM Analysis**: Sends the user's data to **Gemini 1.5 Flash** to generate an in-depth persona  
- 🧾 **Citation-based Output**: Final result includes quotes and links from actual Reddit activity  
- 📄 **Text File Export**: Persona is saved to `outputs/{username}_persona.txt`  

---

## ⚙️ Tech Stack & Tools

| Layer            | Technology                        | Description                            |
|------------------|------------------------------------|----------------------------------------|
| Programming Lang | Python 3.x                         | Core scripting                         |
| Scraping         | `requests` + Reddit JSON API       | Retrieves public data (posts & comments) |
| Environment      | `python-dotenv`                    | Loads Gemini API key securely from `.env` |
| LLM              | `google-generativeai` (Gemini 1.5) | Generates persona from scraped content |
| Output           | Plaintext `.txt` files             | Easy to read, store, and share results |

---

## 🔄 How It Works

1. **You provide** a Reddit profile URL (e.g. `https://www.reddit.com/user/gallowboob/`)
2. The script:
   - Extracts the username
   - Fetches their latest posts & comments using Reddit’s JSON endpoints
3. The scraped content is:
   - Cleaned and formatted
   - Sent as a prompt to **Gemini 1.5 Flash**
4. Gemini returns:
   - A structured persona including traits, interests, habits, and beliefs
   - Cited sources from actual Reddit activity
5. The result is saved in:  
   `outputs/{username}_persona.txt`

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/huzz10/Reddit_Persona_Generator.git
cd reddit-persona-generator
```

2. Install dependencies
```
pip install -r requirements.txt
```

3. Set up your .env file
Create a .env file in the root directory and paste your Gemini API key:
```
GEMINI_API_KEY=your_google_gemini_api_key_here
You can get your key from Google AI Studio.
```
✅ How to Run
Run the script with any Reddit user profile URL:
```
python main.py https://www.reddit.com/user/gallowboob/
```
---
##🤖 LLM Used
This project uses:
- Gemini 1.5 Flash via Google Generative AI SDK
- Handles large prompt inputs (posts + comments)
- Fast and affordable (free quota available)
- Easy to integrate and scale
- 🔒 No Reddit Login Required

---
---
##⚠️ Limitations
- Cannot fetch posts/comments from private or deleted Reddit accounts
- Users with minimal or low-effort content may yield poor personas
- Gemini may occasionally return general or vague traits for low-volume profiles
- Avoid hammering Reddit with rapid requests — use responsibly

---

