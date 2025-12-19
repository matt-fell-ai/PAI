import os
import sys
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.progress import BarColumn, Progress, TextColumn
from rich.box import ROUNDED, DOUBLE_EDGE
from rich.markdown import Markdown

console = Console()

class PAI_UI:
    @staticmethod
    def print_logo():
        logo = Text("""
    ██████╗  █████╗ ██╗
    ██╔══██╗██╔══██╗██║
    ██████╔╝███████║██║
    ██╔═══╝ ██╔══██║██║
    ██║     ██║  ██║██║
    ╚═╝     ╚═╝  ╚═╝╚═╝""", style="bold cyan")
        subtitle = Text("    Universal Infrastructure 2.0", style="bold blue")
        console.print(logo)
        console.print(subtitle)
        console.print("")

    @staticmethod
    def panel(content, title=None, subtitle=None, style="cyan"):
        p = Panel(
            content,
            title=f"[bold]{title}[/bold]" if title else None,
            subtitle=subtitle,
            border_style=style,
            box=ROUNDED,
            expand=False
        )
        console.print(p)

    @staticmethod
    def table(title, columns, rows, style="green"):
        table = Table(title=title, box=ROUNDED, border_style=style, header_style="bold magenta")
        for col in columns:
            table.add_column(col)
        for row in rows:
            table.add_row(*row)
        console.print(table)

    @staticmethod
    def essence_bars(essence_data):
        console.print(f"\n[bold underline yellow]--- {essence_data['name']} Executive Essence (PXE) ---[/bold underline yellow]")
        console.print(f"Mode: [bold green]{essence_data['operational_mode']}[/bold green] (Calibrated: {essence_data.get('last_calibration', 'N/A')})\n")
        
        for attr, val in essence_data["essence"].items():
            # Determine color based on value
            color = "blue"
            if val > 15: color = "red"
            elif val > 10: color = "yellow"
            
            # Simple manual bar for maximum compatibility, or use Rich progress
            bar_len = val
            bar = "█" * bar_len + "░" * (20 - bar_len)
            console.print(f" {attr.capitalize():<15} [bold {color}]{bar}[/bold {color}] {val}/20")
        console.print("\n[dim]--- End Tablet Transmission ---[/dim]\n")

    @staticmethod
    def error(msg):
        console.print(Panel(f"[bold red]ERROR:[/bold red] {msg}", border_style="red", box=ROUNDED))

    @staticmethod
    def tip(msg):
        console.print(f"\n[bold yellow]💡 TIP:[/bold yellow] {msg}")

    @staticmethod
    def markdown(content):
        console.print(Markdown(content))
