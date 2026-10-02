# AI SQL Data Analyst Agent

An AI-powered SQL Data Analyst Agent that will help users explore structured data and answer business questions using natural language.

## Current Progress

**Phase 1: Project Foundation and Database**

* Created a SQLite database for e-commerce analytics.
* Designed tables for customers, products, orders, and order items.
* Added synthetic sample data for testing.
* Enabled foreign-key constraints.
* Added automated tests for record counts, data integrity, and revenue calculations.

The natural-language SQL agent and LangChain integration are planned for later phases.

## Database Schema

| Table         | Purpose                                         |
| ------------- | ----------------------------------------------- |
| `customers`   | Customer information                            |
| `products`    | Product names, categories, and prices           |
| `orders`      | Order dates and statuses                        |
| `order_items` | Products, quantities, and prices for each order |

## Setup

Python 3.12 or a compatible version is recommended.

Activate the project's virtual environment in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Initialize the database and insert the sample data:

```powershell
python -m src.seed_data
```

## Run Tests

```powershell
python -m unittest discover -s tests -v
```

The tests check expected record counts, foreign-key integrity, and total revenue from completed orders.

## Technology Stack

* Python
* SQLite
* SQL
* unittest

## Project Goal

Build the foundation for an AI agent that can translate business questions into SQL queries, execute them safely, and explain analytical results.
