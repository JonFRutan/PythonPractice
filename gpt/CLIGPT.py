import sys, os, platform
import openai 

def validate_key(api_key):
    try:
        client = openai.OpenAI(api_key=api_key)
        client.models.list()
        return client
    except openai.BadRequestError:
        print("Invalid API key.")
        return False
    except Exception as e:
        print("API Issue. Try reentering your API key.")
        return False

def generate_response(client, prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[
        {"role": "system", "content": "Be brief."},
        {"role": "user", "content": f"{prompt}"}],
        stream=True
    )
    return response

def save_environment_variable(api_key):
    platform_type = platform.system()
    if platform_type in ["Linux", "Darwin"]: #POSIX systems; Linux, and Darwin for MAC
       shell = os.path.expanduser("~/.bashrc")
       if os.path.exists(os.path.expanduser("~/.zshrc")):
           shell = os.path.expanduser("~/.zshrc")
       with open(shell, "a") as console:
            console.write(f'\nexport OPENAI_API_KEY="{api_key}"\n')
            print(f"API key saved. Restart your terminal to update it.")

    elif platform_type == "Windows":
        os.system(f'setx OPENAI_API_KEY "{api_key}"')

        print(f"API key saved. Restart your terminal to update it.")
    else:
        print(f"Unsupported OS: {platform_type}. Try setting the env variable manually.\nCreate an issue or message me if you see this!")

ready = True
key = os.getenv("OPENAI_API_KEY")
if key:
    client = validate_key(key)   
if not key:
    ready = False
    
while not ready:
    api_key = input("Please provide your OpenAI API key (? for help, x for exit.): ")
    if api_key == "?":
        print("Navigate to platform.openai.com, sign in, under PROJECT is an API key section.")
    elif api_key == 'x':
        exit()
    else:
        client = validate_key(api_key)
        if client:
            ready = True
            save = input("Would you like to save the key to your system environment? (y/n)")
            if save == 'y':
                save_environment_variable(api_key)
        

print("CLI-GPT\nType 'exit' or hit Ctrl+C to exit the program.")
while True:    
    prompt = input("\n> ")
    if prompt == "exit":
        exit()
    response = generate_response(client, prompt)
    for chunk in response:
        buffer = chunk.choices[0].delta.content
        if buffer:
            print(buffer, end="")
