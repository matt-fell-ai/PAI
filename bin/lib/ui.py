import os
import sys
from typing import List, Dict, Any, Optional, Union
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.progress import BarColumn, Progress, TextColumn
from rich.box import ROUNDED, DOUBLE_EDGE
from rich.markdown import Markdown

# Initialize Rich Console
console = Console()

class PAI_UI:
    """
    PAI_UI: The centralized presentation engine for the PAI CLI.
    
    Uses the Rich library to provide a high-fidelity, cyber-obsidian 
    visual experience across all system outputs.
    """
    
    @staticmethod
    def print_logo() -> None:
        """Renders the Neon-Cyber PAI logo to the console."""
        logo = Text("""
    ██████╗  █████╗ ██╗
    ██╔══██╗██╔══██╗██║
    ██████╔╝███████║██║
    ██╔═══╝ ██╔══██║██║
    ██║     ██║  ██║██║
    ╚═╝     ╚═╝  ╚═╝╚═╝""", style="bold cyan")
        subtitle = Text("    Universal Infrastructure 2030", style="bold blue")
        console.print(logo)
        console.print(subtitle)
        console.print("")

    @staticmethod
    def panel(content: Any, title: Optional[str] = None, subtitle: Optional[str] = None, style: str = "cyan") -> None:
        """
        Wraps content in a standardized Rich Panel.
        
        Args:
            content: The text or Rich object to display.
            title: Optional header text.
            subtitle: Optional footer text.
            style: Border and title color.
        """
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
    def table(title: str, columns: List[str], rows: List[List[str]], style: str = "green") -> None:
        """
        Renders a data table with standardized formatting.
        
        Args:
            title: The table header.
            columns: List of column names.
            rows: List of row data (list of lists).
            style: Border color.
        """
        table = Table(title=title, box=ROUNDED, border_style=style, header_style="bold magenta")
        for col in columns:
            table.add_column(col)
        for row in rows:
            table.add_row(*row)
        console.print(table)

    @staticmethod
    def essence_bars(essence_data: Dict[str, Any]) -> None:
        """
        Renders the Executive Essence (PXE) bars for identity monitoring.
        
        Args:
            essence_data: Dict containing 'essence' attributes and values.
        """
        console.print(f"\n[bold underline yellow]--- {essence_data['name']} Executive Essence (PXE) ---[/bold underline yellow]")
        console.print(f"Mode: [bold green]{essence_data['operational_mode']}[/bold green] (Calibrated: {essence_data.get('last_calibration', 'N/A')})\n")
        
        for attr, val in essence_data["essence"].items():
            color = "blue"
            if val > 15: color = "red"
            elif val > 10: color = "yellow"
            
            bar_len = int(val)
            bar = "█" * bar_len + "░" * (20 - bar_len)
            console.print(f" {attr.capitalize():<15} [bold {color}]{bar}[/bold {color}] {val}/20")
        console.print("\n[dim]--- End Tablet Transmission ---[/dim]\n")

    @staticmethod
    def error(msg: str) -> None:
        """Renders a high-visibility error panel."""
        console.print(Panel(f"[bold red]ERROR:[/bold red] {msg}", border_style="red", box=ROUNDED))

    @staticmethod
    def tip(msg: str) -> None:
        """Renders a helpful tip with an icon."""
        console.print(f"\n[bold yellow]💡 TIP:[/bold yellow] {msg}")

    @staticmethod
    def markdown(content: str) -> None:
        """Renders markdown content with Rich formatting."""
        console.print(Markdown(content))
