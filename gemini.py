import google.generativeai as genai
import textwrap
from IPython.display import display, Markdown
from PIL import Image


# Setup your API key
with open('api.txt', 'r') as file:
    api_key = file.read().strip()

GOOGLE_API_KEY = api_key
genai.configure(api_key=GOOGLE_API_KEY)


def GenAI(user_input):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(user_input, stream=True)
    response.resolve()


    def to_markdown(text):
        text = text.replace('•', '  *')
        return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
    
    formatted_response = to_markdown(response.text)

    return  response.text


user = input('Select [1], or [2]:- ')

if user == '1': 
    while True:
        print('')
        multi_input = input('Gemini-Pro:- ')
        print('')
        if multi_input.lower() != 'exit':
            model_response = GenAI(multi_input)
            print('------------------------response start-----------------')
            print('')
            print(model_response)
            print('')
            print('--------------------------response end-------------------')
        else:
            break



















