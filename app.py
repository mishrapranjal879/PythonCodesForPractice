from flask import Flask, render_template, request, redirect, session, url_for
from config import Config
from models.user import db, User
from models.quiz import Quiz, Question
from email_services import mail, send_result
from ai_generator import generate_mcq

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
mail.init_app(app)

# -----------------------------
# Create Database Tables
# -----------------------------
with app.app_context():
    db.create_all()


# -----------------------------
# Home Page
# -----------------------------
@app.route('/')
def home():
    return render_template("index.html")


# -----------------------------
# Register User
# -----------------------------
@app.route('/register', methods=['GET','POST'])
def register():

    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']

        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()

        session['user_email'] = email

        return redirect(url_for('generate_quiz'))

    return render_template("register.html")


# -----------------------------
# Generate Quiz Using AI
# -----------------------------
@app.route('/generate_quiz')
def generate_quiz():

    questions = generate_mcq()

    quiz = Quiz()
    db.session.add(quiz)
    db.session.commit()

    for q in questions:
        question = Question(
            quiz_id=quiz.id,
            question=q['question'],
            option1=q['options'][0],
            option2=q['options'][1],
            option3=q['options'][2],
            option4=q['options'][3],
            answer=q['answer']
        )
        db.session.add(question)

    db.session.commit()

    return redirect(url_for('quiz', quiz_id=quiz.id))


# -----------------------------
# Show Quiz
# -----------------------------
@app.route('/quiz/<int:quiz_id>')
def quiz(quiz_id):

    questions = Question.query.filter_by(quiz_id=quiz_id).all()

    return render_template(
        "quiz.html",
        questions=questions,
        quiz_id=quiz_id
    )


# -----------------------------
# Submit Quiz
# -----------------------------
@app.route('/submit/<int:quiz_id>', methods=['POST'])
def submit(quiz_id):

    questions = Question.query.filter_by(quiz_id=quiz_id).all()

    score = 0

    for q in questions:
        selected = request.form.get(str(q.id))

        if selected == q.answer:
            score += 1

    email = session.get('user_email')

    # send email result
    send_result(email, score, len(questions))

    return render_template(
        "result.html",
        score=score,
        total=len(questions)
    )


# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)