from brain import think
from memory import save_memory, recall_memory
from tools import decide_tool, open_app, get_time
from voice import listen, speak

while True:
    user_input = input("You: ")


    past_memory = recall_memory(user_input)
    response = think(user_input, past_memory)

    tool = decide_tool(user_input)

    if tool == "open_app":
        result = open_app("Safari")
        speak(result)

    elif tool == "get_time":
        speak(get_time())

    else:
        speak(response)

    save_memory(user_input)
