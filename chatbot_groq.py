import os
from groq import Groq
from session_manager import generate_prompt, update_session

def chat_loop():
    client = Groq()
    session = {
        "journey": None,
        "topic": None,
        "subtopic": None,
    }

    print("🤖 Bot siap ngobrol. Ketik 'exit' untuk keluar.\n")

    while True:
        user_input = input("👤 Kamu: ").strip()
        if user_input.lower() in ["exit", "keluar"]:
            print("\n🤖 Bot: Sampai jumpa!")
            break

        session = update_session(session, user_input)
        prompt = generate_prompt(session)

        # Kirim user input + system prompt ke Groq API
        completion = client.chat.completions.create(
            model="qwen-qwq-32b",
            messages=[
                {"role": "user", "content": user_input},
                {"role": "system", "content": prompt},
            ],
            temperature=0.6,
            max_completion_tokens=4096,
            top_p=0.95,
            stream=True,
        )

        print("🤖 Bot:", end=" ", flush=True)
        for chunk in completion:
            delta = chunk.choices[0].delta
            if hasattr(delta, "content") and delta.content:
                print(delta.content, end="", flush=True)
        print()

if __name__ == "__main__":
    chat_loop()
