import os
from datetime import datetime

BOT_NAME = "OFENTSE AI CORE"
VERSION = "1.0.0"

SYSTEM_PROMPT = """
You are OFENTSE AI CORE, a programming and technology assistant.

Your specialties include:
- Python and C# programming
- Git and GitHub
- Linux and Termux
- Debugging and software development
- Automation and cybersecurity education

Explain concepts clearly, especially to beginners.
When providing code, explain how to run and test it.
Be honest about limitations and untested code.
"""

def show_banner():
    print("=" * 48)
    print(f"  {BOT_NAME} v{VERSION}")
    print("  PROGRAMMING & TECHNOLOGY ASSISTANT")
    print("=" * 48)
    print("Commands: help, time, clear, exit")
    print("AI connection: not configured yet")
    print()

def show_help():
    print("""
Available commands:
  help   - Show available commands
  time   - Display the current time
  clear  - Clear the terminal
  exit   - Close the assistant

Ask programming and technology questions normally.
""")

def main():
    show_banner()

    while True:
        try:
            message = input("You > ").strip()

            if not message:
                continue

            command = message.lower()

            if command in ("exit", "quit"):
                print(f"{BOT_NAME}: Goodbye!")
                break

            elif command == "help":
                show_help()

            elif command == "time":
                print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

            elif command == "clear":
                os.system("clear")

            else:
                print(
                    f"\n{BOT_NAME}: You asked: {message}"
                )
                print(
                    "The online AI engine will be connected "
                    "in the next development step.\n"
                )

        except (KeyboardInterrupt, EOFError):
            print(f"\n{BOT_NAME}: Session ended.")
            break

if __name__ == "__main__":
    main()
