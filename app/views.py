from django.shortcuts import render
import openai, os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_KEY", None)

def home(request):
    chatbot_response = None
    if request.method == 'POST' and api_key != None:
        openai.api_key = api_key
        user_input = request.POST['user_input']
        prompt = user_input

        response = openai.Completion.create(
            engine = 'text-davinci-003',
            prompt = prompt,
            max_tokens = 256,
        )
        print(response)
        chatbot_response = response['choices'][0]['text']
        print("chatgpt response:", chatbot_response)
    return render(request, 'home.html', {"response":chatbot_response})
