# FinCLI - A Python based CLI application for tracking personal expenses

**FinCLI** is a cross-platform personal finance tracking application that runs entirely in the terminal. Written in Python, it allows users to record and track where their money comes from and where it goes, helping them make informed financial decisions and plan their finances more effectively.

**FinCLI** enables users to record and categorize financial transactions while attaching useful metadata such as the **source account**, **transaction date**, and **notes**. This makes it easier to remember the context behind every transaction and maintain a clear financial history.

**FinCLI** is intentionally designed as a **terminal-based application**. Unlike graphical applications that often introduce visual clutter, notifications, and multiple layers of interaction, a CLI keeps the workflow direct and distraction-free.

Because everything happens on a single, simple screen, the process of recording transactions becomes **fast, focused, and deliberate**.

Even without a graphical interface, **FinCLI** still prioritizes **user experience and clear visual hierarchy**. Output is structured and readable so users can quickly understand prompts, inputs, and recorded data without confusion.

In a world of increasingly complex interfaces, **FinCLI** embraces simplicity. It is designed for focus: **open the terminal, record the transaction, move on.**

To ensure reliable financial records, **FinCLI** performs **input validation at every step**, preserving data integrity and preventing incorrect entries from affecting financial tracking and planning.

You can track the development progress of **FinCLI** on the [**Trello page**](https://trello.com/b/JP2u5w9J)

## User Manual

Detailed usage instructions for FinCLI can be found here:

[FinCLI User Manual](docs/manual.md)

## Current Features:

- Recording a valid transaction amount
- Categorize income sources (Business, Freelancing, Salary, etc.) to analyze your income streams.
- Record additional transaction metadata for better tracking:
  - Transaction date
  - Bank account where the transaction occurred (helps track account-level balances)
  - Transaction **notes** for future reference
- JSON-based transaction storage

## Planned Features:

- Expense recording functionality
- Transaction history viewer
- SQL database integration
- Monthly spending summaries
- Net-worth and balance calculation across accounts
- Terminal User Interface (TUI)

## Tech Stack:

- Python
- JSON _(for data storage)_
- SQL _(planned for database support)_
