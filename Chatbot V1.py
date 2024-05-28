import openai

openai.api_key = "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"

messages = []
system_msg = input("What kind of chatbot would you like to create?\n") #Vraagt om input van de user en slaat deze op in de system_msg variable.
messages.append({"role": "system", "content": system_msg}) #voeg de input van de user toe aan de messages list.

print ("Say hello to your new assistent!")
while input != "quit": #Zorgt ervoor dat je vragen kan blijven stellen aan de chatbot.
    message = input("")
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", #Welk model er word gebruikt.
        messages=messages) #Chatbot krijgt de alle eerste message en de gestelde vraag.
    reply = response["choices"] [0] ["message"] ["content"] #Sla de response op van de chatbot in de reply variable.
    messages.append({"role": "assistant", "content": reply}) #De chatbot herinnert ook de vorige gesprekken omdat ik de reply toe voeg aan de list.
    print("\n" + reply + "\n") #Print de reply.