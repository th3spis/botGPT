#! /usr/bin/env python3


import telebot
import openai

# Enter your bot token here
bot = telebot.TeleBot('')

# Define the group ID
group_id = 


# Set your OpenAI API key
openai.api_key = ""


# Set the name of the GPT model to use for generating the response
model = "gpt-3.5-turbo"
model = "davinci"

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

# Thanks to https://levelup.gitconnected.com/interfacing-chatgpt-with-python-824be63dfa2f
messages = []   

# Define a function to handle messages
@bot.message_handler(func=lambda message: message.chat.id == group_id)
def get_message(message):
    #message.chat.id == group_id

    #bot.reply_to(message, "ok")
    # Print the message text
    print("[%s]: %s" % (message.from_user.username, message.text))

    # Set the prompt for ChatGPT to complete
    prompt = message.text

    messages.append(
        {
            'role':'user',
            'content':prompt
        }) 

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = messages)
    
    response = completion['choices'][0]['message']['content']
    print(response)    
    messages.append(
        {
            'role':'assistant',
            'content':response
        })
    
    bot.send_message(message.chat.id, response)


# Start the bot
bot.polling(none_stop=True, timeout=10)
