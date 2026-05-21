from flask import Flask, render_template

app = Flask(__name__)

notes = [
    {
        "id": 1,
        "title": "Python变量",
        "content": "变量用于存储数据"
    },
    {
        "id": 2,
        "title": "Python循环",
        "content": "for循环和while循环"
    }
]

@app.route('/')
def home():
    return render_template("index.html", notes=notes)

@app.route('/note/<int:id>')
def note(id):

    for n in notes:
        if n["id"] == id:
            return render_template("note.html", note=n)

    return "笔记不存在"

if __name__ == '__main__':
    app.run(debug=True)