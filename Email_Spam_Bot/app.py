from flask import Flask,render_template,request,flash,redirect,url_for
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from sendgrid.helpers.mail import To

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(16)

def send_mail(recepient,mail_object,body):
    message = Mail(
    from_email=("bulkmailer69@gmail.com", "Spammer"),
    to_emails=recepient,
    subject=mail_object,
    html_content=body)
    sg = SendGridAPIClient(
    "YOUR API KEY")
    sg.send(message)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/send_message',methods=['POST'])
def send_message():
    if request.method == "POST":
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["msg"]
        N = int(request.form["numberof"])
        try:
            for _ in range(1,N):
                send_mail(email,subject,message)
            flash("Spammed","success")
            return redirect(url_for("home"))
        except:
            flash("Spammed failed.Please try again later","error")
            return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)

