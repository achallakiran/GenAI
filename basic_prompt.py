import os
import openai

openai.api_type = "azure"
openai.api_base = os.getenv("OPENAI_ENV")
openai.api_version = "2023-07-01-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")

message_text = [{"role":"user","content":"Can you tell me the capital of France?"}]

completion = openai.ChatCompletion.create(
  engine="gpt-35-turbo-test",
  messages = message_text,
  temperature=0.7,
  max_tokens=800,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None
)

print(completion['choices'][0]['message']['content'])