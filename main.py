from reddit_scraper import get_user_data
from persona_generator import generate_persona
from utils import extract_username, save_output
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <Reddit Profile URL>")
        return

    url = sys.argv[1]
    username = extract_username(url)

    print(f"🔍 Collecting Reddit data for user: {username}")
    posts, comments = get_user_data(username)

    print("🧠 Generating persona using Gemini...")
    persona = generate_persona(posts, comments)

    print("💾 Saving output...")
    save_output(username, persona)
    print("✅ Done.")

    # if not posts and not comments:
    #     print("❌ No Reddit content found for this user. Try a different one.")
    #     return


if __name__ == "__main__":
    main()

