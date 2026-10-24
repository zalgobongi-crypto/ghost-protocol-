import os
from openai import OpenAI

BOT_NAME = "OFENTSE AI CORE"

SYSTEM_PROMPT = """
You are OFENTSE AI CORE, a programming and technology assistant.

Your specialties include:
- Python, C#, JavaScript, HTML, and CSS
- Linux, Termux, Git, and GitHub
- Debugging and explaining code
- Software development and automation
- Cybersecurity education and authorized testing

Explain concepts clearly to beginners.
Provide useful code examples when appropriate.
Be honest about your limitations.
"""

def main():
    api_key = os.environ.get("OPENAI_API_KEY")

    if not api_key:
        print("API key not configured.")
        print("Set the OPENAI_API_KEY environment variable.")
        return

    client = OpenAI(api_key=api_key)
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    print(f"\n{BOT_NAME}")
    print("Programming and Technology Assistant")
    print("Type 'exit' to quit.\n")

    while True:
        try:
            user_input = input("You > ").strip()

            if user_input.lower() in ("exit", "quit"):
                print("Goodbye!")
                break

            if not user_input:
                continue

            messages.append({
                "role": "user",
                "content": user_input
            })

            response = client.responses.create(
                model="gpt-4.1-mini",
                input=messages
            )

            answer = response.output_text
            print(f"\n{BOT_NAME} > {answer}\n")

            messages.append({
                "role": "assistant",
                "content": answer
            })

            # Keep recent conversation context manageable.
            if len(messages) > 21:
                messages = [messages[0]] + messages[-20:]

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as error:
            print(f"Request failed: {error}")

if __name__ == "__main__":
    main()
