import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def format_data(posts, comments):
    post_data = [
        f"POST:\nTitle: {p['title']}\nBody: {p['body']}\nURL: {p['url']}\n"
        for p in posts if p['title'] or p['body']
    ]
    comment_data = [
        f"COMMENT:\n{c['body']}\nLink: {c['link']}\n"
        for c in comments if c['body']
    ]
    return "\n".join(post_data + comment_data)


# def generate_persona(posts, comments):
#     input_text = format_data(posts, comments)
#     prompt = (
#         "Based on the following Reddit posts and comments, generate a detailed user persona.\n"
#         "Include personality traits, interests, values, language style, and online habits.\n"
#         "For each trait, cite which post or comment supports it.\n\n"
#         f"{input_text}\n\nUser Persona:"
#     )

#     response = model.generate_content(prompt)
#     return response.text
def generate_persona(posts, comments):
    input_text = format_data(posts, comments)

    if not input_text.strip():
        return "❌ Not enough content to generate a persona."

    prompt = (
        "You are an AI assistant that analyzes Reddit users.\n"
        "Based on the following Reddit posts and comments, generate a rich user persona.\n"
        "Include: personality traits, interests, values, political/social views, hobbies, and communication style.\n"
        "For each point, include the quote or post/comment that supports it.\n\n"
        f"{input_text}\n\nUser Persona:"
    )

    response = model.generate_content(prompt)
    return response.text
