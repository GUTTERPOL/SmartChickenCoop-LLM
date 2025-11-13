import ollama

model_name = "qwen3:4b"
prompt = "Why do cows produce milk?"

print(f"🚀 Loading model: {model_name}")
print("🧩 Generating response...\n")

response = ollama.generate(
    model=model_name,
    prompt=prompt,
    options={
        "temperature": 0.7,
        "top_p": 0.9,
        "num_predict": 256
    }
)

# Qwen3 puts the REAL answer in 'thinking', not 'response'
answer = ""

if hasattr(response, "response") and response.response:
    answer = response.response
else:
    answer = response.thinking    # ← THIS is where your model is generating text

print("=============================")
print("🧠 Model says:\n")
print(answer)
print("=============================")

