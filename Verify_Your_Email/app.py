from flask import Flask,render_template,request,flash,redirect,url_for,session
import os,random
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from sendgrid.helpers.mail import To

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(16)

def send_mail(recepient,mail_object,body):
    message = Mail(
    from_email=("bulkmailer69@gmail.com", "Verifier"),
    to_emails=recepient,
    subject=mail_object,
    html_content=body)
    sg = SendGridAPIClient(
    "YOUR API KEY")
    sg.send(message)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/otp_form')
def otp_form():
    return render_template("otp.html")

@app.route('/send',methods=['POST'])
def send():
    if request.method == "POST":
        email = request.form['mail']
        otp = random.randint(000000,999999)
        session['otp'] = otp
        subject = "OTP"
        message = "Dear User, your verification code is: " + str(otp)
        try:
            send_mail(email,subject,message)
            flash("OTP sent","success")
            return redirect(url_for("otp_form"))
        except:
            flash("Mail was not sent.Please try again later","error")
            return redirect(url_for("home"))

@app.route('/verify',methods=['POST'])
def verify():
    if request.method == "POST":
        user_otp = request.form['otp']
        if session['otp'] == int(user_otp):
            flash("Email verified successfully","success")
            return redirect(url_for("home"))
        else:
            flash("Wrong OTP. Please try again","error")
            return redirect(url_for("otp_form"))

if __name__ == "__main__":
    app.run(debug=True)