from flask_mail import Mail, Message

mail = Mail()

def send_result(email, score, total):

    msg = Message(
        subject="Quiz Result",
        sender="your_email@gmail.com",
        recipients=[email]
    )

    msg.body = f"""
    Your Quiz Result

    Score : {score}/{total}

    Thank you for taking the test.
    """

    mail.send(msg)