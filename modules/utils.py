from datetime import datetime
from rich.console import Console
from rich.markdown import Markdown

console = Console()
HISTORY_FILE = "chat_history.txt"

def save_to_history(user_input, bot_response):
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        f.write(f"{timestamp} You: {user_input}\n")
        f.write(f"{timestamp} Astra: {bot_response}\n\n")

def print_logo():
    logo = r"""
     █████╗ ███████╗████████╗██████╗  █████╗     
    ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗ ██╔══██╗    
    ███████║███████╗   ██║   ██████╔╝ ███████║    
    ██╔══██║╚════██║   ██║   ██╔═ ██╝ ██╔══██║    
    ██║  ██║███████║   ██║   ██║ ╚██╗ ██║  ██║    
    ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═╝  ╚═╝    
         Your AI Terminal Companion 🤖         
    """
    console.print(logo, style="bold magenta")


def print_intro():
    console.clear()
    print_logo()
    console.print("[bold yellow]Commands:[/] [green]exit[/], [green]clear[/], [green]reset[/]\n")

def clear_screen():
    console.clear()
    print_intro()

def reset_history():
    open(HISTORY_FILE, "w").close()
    console.print("🔄 [yellow]Chat history cleared.[/]\n")
