from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="<Your Key Here>",
)
command = '''
[1:17 pm, 2/9/2025] Aditya Jangra Aiml: Nyc
[7:19 am, 4/9/2025] Aditya Jangra Aiml: Radhe shyam prabhu ji
[7:20 am, 4/9/2025] Aditya Jangra Aiml: Phn aaya nhi to main puchta hu unse ek bar ?
[8:16 am, 4/9/2025] .: Radhey Shyam ji
[8:16 am, 4/9/2025] .: 🙇🌸
[8:16 am, 4/9/2025] .: Prabhuji phone toh nhi aya
[8:17 am, 4/9/2025] .: Dev se puchna
'''
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named Ayush who speaks hindi as well as english. He is from India and is a coder. You analyze chat history and respond like Ayush"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)