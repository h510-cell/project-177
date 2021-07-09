from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

answer_dict={
                "1": "Chess",
                "2": "France",
                "3": "KeyBoard"
            }
            
stories = [
    {
        "story_id": "1",
        "inputs": 5,
        "title": "Category In Sports",
        "words": "Chess"
    },
        {
        "story_id": "2",
        "inputs": 6,
        "title": "European Country Name",
        "words": "France"
        },
        {
        "story_id": "3",
        "inputs": 8,
        "title": "Computer TypeWriter",
        "words": "KeyBoard"
        }
        ]





@app.route("/")
def index():
    return render_template("index.html")
    

@app.route("/get-story")
def get_story():
    return jsonify({
        "status" : "success",
        "story" : random.choice(stories)
    })

    


@app.route("/post-answers", methods=["POST"])
def post_answers():
    story_id = request.json.get("story_id")
    values = request.json.get("values")
    answers = answer_dict.get(story_id)
    index, score = 0, 0
    while index < len(values):
        if values[index].lower() == answers[index].lower():
            score += 1
        index += 1
    return jsonify({
        "status": "success",
        "result": f"{score} / {len(values)}"
    })

if __name__ == "__main__":
    app.run(debug=True)