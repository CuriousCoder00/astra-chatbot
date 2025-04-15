from modules.chat_engine import get_chatbot_response
from modules.logger import setup_logger
from modules.utils import save_to_history, print_intro, clear_screen, reset_history
from rich.console import Console
from rich.markdown import Markdown
from rich.spinner import Spinner
from rich.live import Live
from datetime import datetime
import logging

console = Console()

def auto_reply():
    user_input = console.input("[bold green]🧑 You:[/] ").strip()

    if user_input.lower() in ["exit", "quit"]:
        console.print("\n👋 [bold red]Goodbye from Astra![/]\n")
        exit()
    elif user_input.lower() == "clear":
        clear_screen()
        return
    elif user_input.lower() == "reset":
        reset_history()
        return

    timestamp = datetime.now().strftime("[dim]%H:%M[/]")

    with Live(Spinner("dots", text="Astra is thinking...", style="magenta"), refresh_per_second=12):
        response = get_chatbot_response(user_input)

    console.print(f"{timestamp} 🤖 [bold magenta]Astra:[/] {response}\n")
    save_to_history(user_input, response)
    logging.info(f"User: {user_input}")
    logging.info(f"Astra: {response}")

if __name__ == "__main__":
    setup_logger()
    print_intro()
    while True:
        auto_reply()
