import os

BOT_NAME = "OFENTSE AI"
VERSION = "1.0"

SYSTEM_PROMPT = """
You are Ofentse AI, a helpful personal AI assistant.
You help with programming, learning, research,
problem-solving, and everyday questions.
Be friendly, clear, and honest.
"""

def show_banner():
    print("=" * 40)
    print(f"       {BOT_NAME} v{VERSION}")
    print("       ONLINE AI ASSISTANT")
    print("=" * 40)
    print("Type 'exit' to close the assistant.")
    print()

def main():
    show_banner()

    while True:
        message = input("You: ").strip()

        if message.lower() in ("exit", "quit"):
            print(f"{BOT_NAME}: Goodbye!")
            break

        if not message:
            continue

        print(f"\n{BOT_NAME}: Your message was received.")
        print("Online AI connection will be added next.\n")

if __name__ == "__main__":
    main()
