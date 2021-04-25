from flask import Flask, render_template, request, redirect, url_for
import smtplib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/more/')
def more():

    return render_template('more.html')

@app.route('/form', methods=['POST'])
def form():
    name = request.form.get('name')
    email = request.form.get('email')
    text = request.form.get('text')

    SendmMailTO = ""
    SenderMail = ""
    SenderPassword = ""
    DataToSend = name + email + text


    message = "Your message has been sent"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(SenderMail, SenderPassword)
    server.sendmail(SenderMail, SendmMailTO, DataToSend)

    if not name or not email or not text:
        error = "All field must be filled"
        return render_template('error.html', error=error)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
