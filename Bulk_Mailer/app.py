from flask import Flask,render_template,request,flash,redirect,url_for
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from sendgrid.helpers.mail import To

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(16)

def send_mail(recepient,mail_object,body):
    message = Mail(
    from_email=("bulkmailer69@gmail.com", "Pranith's Newsletter"),
    to_emails=recepient,
    subject=mail_object,
    html_content=body)
    sg = SendGridAPIClient(
    "YOUR API KEY")
    sg.send(message)


myFile = "subscribers.txt"
subscribers = []
with open(myFile) as f:
    subscribers = f.readlines()
subscribers = [email.strip() for email in subscribers]

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/admin')
def admin():
    return render_template("admin.html")

@app.route('/sub_form')
def sub_form():
    return render_template("subscribe.html")

@app.route('/thankyou')
def thankyou():
    return render_template("thankyou.html")

@app.route('/unsub_form')
def unsub_form():
    return render_template("unsubscribe.html")

@app.route("/reload")
def reload():
    myFile = "subscribers.txt"
    subscribers = []
    with open(myFile) as f:
        subscribers = f.readlines()
    subscribers = [email.strip() for email in subscribers]
    return redirect(url_for("sub_form"))

@app.route('/subscribe',methods=['POST'])
def subscribe():
    if request.method == "POST":
        email = request.form['mail']
        myFile = "subscribers.txt"
        subscribers = []
        with open(myFile) as f:
            subscribers = f.readlines()
        subscribers = [email.strip() for email in subscribers]
        if email in subscribers:
            flash("Already Subscribed","warning")
            return redirect(url_for("home"))
        else:
            listofsubscribers = open("subscribers.txt","a+")
            listofsubscribers.write(email)
            listofsubscribers.write("\n")
            listofsubscribers.close()
            flash("Subscribed successfully")
            return render_template("thankyou.html")

@app.route('/send_message',methods=['POST'])
def send_message():
    if request.method == "POST":
        subject_from_form = request.form["subject"]
        message_from_form = request.form["msg"]
        try:
            for email in subscribers:
                print('hai')
                message = message_from_form
                subject = subject_from_form
                send_mail(email,subject,message)
            flash("Message Sent","success")
            return redirect(url_for("home"))
        except:
            flash("Broadcast failed.Please try again later","error")
            return redirect(url_for("home"))

@app.route('/unsubscribe',methods=['POST'])
def unsubscribe():
    if request.method == "POST":
        email = request.form['mail']
        with open("subscribers.txt","r") as f:
            subscribers = f.readlines()
        with open("subscribers.txt","w") as f:
            for emails in subscribers:
                if emails.strip("\n") != email:
                    f.write(emails)
        flash("Unsubscribed Successfully","success")
        return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)