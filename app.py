from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# In-memory storage (for demo/teaching purposes)
todos = []  # each item: {"id": int, "text": str, "done": bool, "created_at": str}

def next_id():
    return (max([t["id"] for t in todos]) + 1) if todos else 1

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add():
    text = request.form.get("text", "").strip()
    if text:
        todos.append({
            "id": next_id(),
            "text": text,
            "done": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    return redirect(url_for("index"))

@app.route("/toggle/<int:todo_id>", methods=["POST"])
def toggle(todo_id):
    for t in todos:
        if t["id"] == todo_id:
            t["done"] = not t["done"]
            break
    return redirect(url_for("index"))

@app.route("/delete/<int:todo_id>", methods=["POST"])
def delete(todo_id):
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    return redirect(url_for("index"))

if __name__ == "__main__":
    # For local dev only. In Docker, use the default below.
    app.run(host="0.0.0.0", port=5000, debug=True)
