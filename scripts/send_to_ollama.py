import json
import requests

OLLAMA_API = "http://ollama:11399/api/generate"
MODEL = "tinyllama"

def send_to_ollama(prompt):
    response = requests.post(OLLAMA_API, json={"model": MODEL, "prompt": prompt, "stream": "false"})
    print("\n💬 Resposta da IA:\n")
    print(response.json()["response"])

def summarize(file, name):
    with open(file) as f:
        content = f.read()
    prompt = f"""
Analise o output do {name} abaixo, identifique vulnerabilidades e sugira correções:

{content[:4000]}
"""
    send_to_ollama(prompt)

if __name__ == "__main__":
    summarize("bandit.json", "Bandit")
    summarize("trivy-results.sarif", "Trivy")