# ============================================================
#  Project 1: Rule-Based AI Chatbot
#  Architecture: IPO Model  ->  Input | Process | Output
# ============================================================

# ── KNOWLEDGE BASE (O(1) Dictionary Lookup) ─────────────────
RESPONSES = {
    # Greetings
    "hello":        "Hey there! How can I help you today?",
    "hi":           "Hi! What is on your mind?",
    "hey":          "Hey! What do you need?",

    # Identity
    "who are you":  "I am a rule-based AI chatbot built on pure logic.",
    "what are you": "I am a deterministic chatbot running on if-else logic. No hallucinations here.",

    # Wellbeing
    "how are you":  "Running at 100% uptime. Thanks for asking!",
    "how r u":      "All systems operational! How about you?",

    # AI topics
    "what is ai":   "Artificial Intelligence is the simulation of human intelligence by machines through logic, learning, and decision-making.",
    "what is ml":   "Machine Learning is a subset of AI where systems learn patterns from data instead of following explicit rules.",
    "what is nlp":  "Natural Language Processing lets computers understand and generate human language.",
    "rule based ai":"Rule-based AI uses explicit if-else logic to make decisions. It is deterministic, traceable, and has zero hallucination risk.",

    # Help
    "help":         "You can ask me about AI, ML, or NLP. Type 'exit' to quit.",
    "what can you do": "I can answer questions about AI concepts. Try asking 'what is AI' or 'who are you'.",

    # Farewells
    "bye":          "Goodbye!",
    "goodbye":      "See you next time!",
    "see you":      "Later! Keep learning.",

    # Easter egg
    "are you smart":"I am as smart as my rules allow. Expand my dictionary and I will get smarter.",
}

# Fallback for unrecognised input
FALLBACK = "I do not understand that yet. Try asking about AI, ML, or type 'help' for options."

# Exit commands
EXIT_COMMANDS = {"exit", "quit", "q", "stop", "end"}


# ── PHASE 1: INPUT & SANITIZATION ───────────────────────────
def sanitize(raw: str) -> str:
    return raw.lower().strip()


# ── PHASE 2: PROCESS (Intent Matching) ──────────────────────
def get_response(clean_input: str) -> str:
    return RESPONSES.get(clean_input, FALLBACK)


# ── PHASE 3: OUTPUT (Response Generation) ───────────────────
def display(message: str) -> None:
    print(f"\n  Bot: {message}\n")


# ── HEARTBEAT: THE INFINITE LOOP ────────────────────────────
def main():
    print("=" * 50)
    print("  Rule-Based AI Chatbot  |  Project 1")
    print("  Type 'help' for options  |  Type 'exit' to quit")
    print("=" * 50)

    while True:
        try:
            raw_input_text = input("\n  You: ")
        except (EOFError, KeyboardInterrupt):
            display("Session interrupted. Goodbye!")
            break

        clean_input = sanitize(raw_input_text)

        if not clean_input:
            continue

        if clean_input in EXIT_COMMANDS:
            display("Goodbye!")
            break

        response = get_response(clean_input)
        display(response)


if __name__ == "__main__":
    main()