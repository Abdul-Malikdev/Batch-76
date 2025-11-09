from google.generativeai import GenerativeModel

model = GenerativeModel("gemini-pro")

prompt = """
Give me current live cricket scores in very short format.
"""

response = model.generate_content(prompt)

print("\nLive Cricket Score Updates:\n")
print(response.text)
