import os

def extract_username(url):
    return url.strip('/').split('/')[-1]

def save_output(username, persona_text):
    os.makedirs("outputs", exist_ok=True)
    file_path = f"outputs/{username}_persona.txt"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(persona_text)
    print(f"Saved to: {file_path}")
