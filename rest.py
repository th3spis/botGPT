#! /usr/bin/env python3


import telebot
import requests

# Enter your bot token here
bot = telebot.TeleBot('')

# Define the group ID
group_id = 


# Set the API endpoint URL
url = "https://api.openai.com/v1/engines/davinci-codex-beta/completions"
url = "https://api.openai.com/v1/chat/completions"
# Set your OpenAI API key
api_key = ""


# Set the name of the GPT model to use for generating the response
model = "gpt-3.5-turbo"
# Set the number of responses to generate
num_responses = 1
# Set the maximum length of each response
max_length = 100
# Set the temperature of the response (higher values = more creative, lower values = more predictable)
temperature = 0.7
# Set the top_p value for the response (higher values = more conservative, lower values = more creative)
top_p = 1
# Set the frequency penalty value (higher values = discourage repetition in the response)
frequency_penalty = 0.5
# Set the presence penalty value (higher values = discourage responses that contradict the given context)
presence_penalty = 0


#str(uuid.uuid4())
convo_id = '9339df02-749a-4514-9fae-9206e2d35e14'


# Define a function to handle messages
@bot.message_handler(func=lambda message: True)
def get_message(message):
    #message.chat.id == group_id

    #bot.reply_to(message, "ok")
    # Print the message text
    print("[%s]: %s" % (message.from_user.username, message.text))

    # Set the prompt for ChatGPT to complete
    prompt = message.text

    # Set the data for the request
    data = {
        "messages": [{"role": "user", "content": prompt}],
        "model": model,
        #"engine": model,
        "max_tokens": max_length,
        "temperature": temperature,
        "top_p": top_p,
        "n": num_responses,
        "frequency_penalty": frequency_penalty,
        "presence_penalty": presence_penalty
    }

    # Set the headers for the request (including the API key)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    # Send the request to the API endpoint and get the response
    response = requests.post(url, json=data, headers=headers)

    gptmsg = response.json()
    print(gptmsg)
    gptext = gptmsg['choices'][0]['message']['content']
    print(gptext)
    bot.send_message(message.chat.id, gptext)




# Start the bot
bot.polling(none_stop=True, timeout=10)
