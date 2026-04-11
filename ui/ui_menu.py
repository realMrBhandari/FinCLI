from rich.console import Console, Group
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich import box

console = Console()


def rich_fincli_menu():
    def create_option(index, text, is_exit=False):
        style = "bold red" if is_exit else "bold cyan"
        content = Text()
        content.append(f"{index}. ", style="bold bright_yellow")
        content.append(text, style=style)

        return Panel(
            Align.left(content),
            box=box.ROUNDED,
            border_style="dim yellow",
            padding=(0, 2),
        )

    options = [
        "Record Income Transaction",
        "Record Expense Transaction",
        "View Transactions",
        "Balance Overview",
        "Monthly Spending Summary",
        "Exit",
    ]

    option_panels = [
        create_option(i, opt, is_exit=(i == 6)) for i, opt in enumerate(options, 1)
    ]

    menu_group = Group(*option_panels)

    main_panel = Panel(
        menu_group,
        title=Text("FinCLI Finance Menu", style="bold bright_yellow"),
        title_align="center",
        border_style="bright_yellow",
        box=box.DOUBLE,
        width=70,
        padding=(1, 2),
    )

    console.print("\n")
    console.print(main_panel)
    console.print("\n")
