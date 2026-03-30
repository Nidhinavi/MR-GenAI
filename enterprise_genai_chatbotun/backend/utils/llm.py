
import os
import openai

def call_llm(query, context):
    openai.api_type = "azure"
    openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
    openai.api_key = os.getenv("AZURE_OPENAI_KEY")
    openai.api_version = "2024-02-15-preview"

    response = openai.ChatCompletion.create(
        engine="gpt-4", # PAID
        messages=[
            {"role":"system","content":"Marketing assistant chatbot"},
            {"role":"user","content": f"Context:{context}\nQuery:{query}"}
        ]
    )
    return response['choices'][0]['message']['content']
