# Terminal mein pehle install karein:
# pip install google-genai

from google import genai

# Apni free API key yahan set karein


response = client.models.generate_content(
    model='gemini-3.8-flash',# Aap gemini-3.8-flash bhi use kar sakte hain
    contents='AI kya hai aur iske fayde batao.',
)

print(response.text)
