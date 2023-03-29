import openai
from dynaconf import settings
openai.api_key = settings.APIKEY

name = "GUSTAVOOLIVEIRAKANNO"
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role":"user",
               "content": f"Separe all names and/or surnames in this text: {name}. Label with 'name' and 'surnames' "}]
)

print(response)