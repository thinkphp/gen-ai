from openai import OpenAI

client = OpenAI(api_key='___')

messages = [ {"role": "system", "content":
              "You are a intelligent assistant."} ]
while True:

    message = input("IronMam@adonix.cs.unibuc.ro>>> : ")
    
    if message:
    
        messages.append(
        
            {"role": "user", "content": message},
        )
        
        chat = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
        
    reply = chat.choices[0].message.content
    
    print(f"ChatGPT: {reply}")
    
    messages.append({"role": "assistant", "content": reply})
