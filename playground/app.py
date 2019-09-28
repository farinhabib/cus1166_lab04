from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/layout")
def layout():
    return render_template("layout.html")

@app.route("/roster/<string:grade_view>")
def roster(grade_view):
    s1 = ('Freshmen',,'Farin', 'B')
    s2 = ('Freshmen',, 'Arna', 'B')
    s3 = ('Senior', 'Afry', 'C-')
    s4 = ('Senior', 'Aayushi', 'A')
    s5 = ('Junior', 'Mary', 'B+')
    s6 = ('Senior', 'Sumaia', 'F')
    s7 = ('Junior', 'Peter', 'C')
    class_roster = [s1, s2, s3, s4, s5, s6, s7]
    return render_template("roster.html", grade_view = grade_view, class_roster =class_roster)

@app.route("/welcome/<string:student_name>")
def welcome(student_name):
    #student_name = student_name
    return render_template("welcome.html", student_name = student_name)

if __name__ == "__main__":
    app.run()
