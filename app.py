from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from groq import Groq
from config import journeys

app = Flask(__name__)
app.secret_key = "secret-key"  # ganti dengan yang aman

client = Groq()

@app.route("/")
def index():
    return render_template("index.html", journeys=journeys)

@app.route("/start_chat", methods=["POST"])
def start_chat():
    data = request.json
    journey = data.get("journey")
    topic = data.get("topic")
    subtopic = data.get("subtopic")

    # Save ke session supaya dipakai saat chat
    session["journey"] = journey
    session["topic"] = topic
    session["subtopic"] = subtopic
    return jsonify({"success": True})

@app.route("/chat", methods=["GET"])
def chat_page():
    if not session.get("journey"):
        return redirect(url_for("index"))
    return render_template("chat.html")

@app.route("/send_message", methods=["POST"])
def send_message():
    data = request.json
    user_input = data.get("message")
    journey = session.get("journey")
    topic = session.get("topic")
    subtopic = session.get("subtopic")

    # Ambil response statis dari config.py berdasarkan pilihan
    response_static = "Maaf, saya tidak mengerti."  # default fallback

    try:
        response_static = journeys[journey]["topics"][topic]["subtopics"][subtopic]
    except Exception:
        try:
            response_static = journeys[journey]["topics"][topic].get("default_response", response_static)
        except Exception:
            response_static = "Halo, ada yang bisa saya bantu?"

    # Kirim ke Groq API dengan tambahan konteks static itu supaya model tetap di jalur
    messages = [
        {"role": "system", "content": f"Topik pembicaraan: {journey} > {topic} > {subtopic}"},
        {"role": "system", "content": response_static},
        {"role": "user", "content": user_input},
    ]

    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=messages,
        temperature=0.6,
        max_completion_tokens=1024,
        top_p=0.95,
        stream=False,
    )
    answer = completion.choices[0].message.content

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
