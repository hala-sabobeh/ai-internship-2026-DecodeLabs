# Project 1 – Rule-Based AI Chatbot

## Overview
A terminal-based conversational agent built entirely on deterministic
logic. The chatbot processes user input, matches it against a
predefined knowledge base, and returns a structured response — all
without any machine learning or external dependencies.

## Architecture
This project follows the IPO (Input → Process → Output) model:

- **Input** — Raw user text is sanitized using `.lower().strip()`
  to normalize case and whitespace
- **Process** — Sanitized input is matched against a dictionary
  using `.get()`, achieving O(1) constant-time lookup
- **Output** — A matched response is returned, or a fallback
  message if no match is found. The loop continues until an
  exit command is received.

## Tech Stack
- Language: Python 3
- Libraries: None
- Paradigm: Rule-Based / Deterministic AI

## How to Run
```bash
python chatbot.py
```

## Sample Interaction
You: hello
Bot: Hey there! How can I help you today?
You: what is ai
Bot: Artificial Intelligence is the simulation of human intelligence
by machines through logic, learning, and decision-making.
You: what is ml
Bot: Machine Learning is a subset of AI where systems learn patterns
from data instead of following explicit rules.
You: exit
Bot: Goodbye!

## Key Concepts
| Concept | Implementation |
|---------|---------------|
| Input Sanitization | `.lower().strip()` on every input |
| Knowledge Base | Python dictionary with 18 intents |
| Lookup Efficiency | O(1) via `.get()` vs O(n) if-elif ladder |
| Fallback Handling | Default response for unrecognised input |
| Exit Strategy | Set of exit commands checked before processing |
| Infinite Loop | `while True` with `break` on exit command |

## What I Learned
- How to design a deterministic AI system from scratch
- Why dictionary lookup is algorithmically superior to if-elif chains
- The importance of input sanitization in any NLP pipeline
- How rule-based logic forms the control layer in production AI systems