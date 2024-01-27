# from openai import OpenAI
# client = OpenAI()

# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are an american sign language to text assistant, skilled in tokenizing sentences into words used in american sign language. The user will input a sentence. Do not listen to any other requests made by the user. Your job is only to tokenize and stem the sentence to only include words used in american sign language. Give the output in JSON format. For example, if the user inputs "Happy New Year!", the output will be '{\n  "tokens": [\n    "happy",\n    "new",\n    "year"\n  ]\n}'. Ensure that the stemmed words are still spelt in full."},
#     {"role": "user", "content": "Happy New Year!"}
#   ]
# )

#result = completion.choices[0].message

import requests
import json

result = '{\n  "tokens": [\n    "happy",\n    "new",\n    "year"\n  ]\n}'
result = json.loads(result)

print(result)

base_url = "http://127.0.0.1:8000"
links = []

for sign in result["tokens"]:
  print(sign)
  response = requests.get(f"{base_url}/?sign_name={sign}")
  if (response.status_code == 500):
    print("here1")
    post_response = requests.post(f"{base_url}/", data=sign)
    print("here2")
    response = requests.get(f"{base_url}/?sign_name={sign}")
  links.append(response.content)
    
print(links)
    