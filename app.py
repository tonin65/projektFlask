from flask import Flask, render_template, request
###############################################
#          Import some packages               #
###############################################
from flask_mail import Mail, Message
from form_contact import ContactForm, csrf


mail = Mail()

app = Flask(__name__)

app.config['SECRET_KEY'] = "000d88cd9d90036ebdd237eb6b0db000"
csrf.init_app(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'tonin89@gmail.com'
app.config['MAIL_PASSWORD'] = 'testnaLozinka'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail.init_app(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/o-nama')
def onama():
    return render_template('onama.html')
    
@app.route('/jelovnik')
def jelovnik():
    return render_template('jelovnik.html')

@app.route('/galerija')
def galerija():
    return render_template('galerija.html')

###############################################
#       Render Contact page                   #
###############################################
@app.route('/kontakt', methods=['POST', 'GET'])
def kontakt():
    form = ContactForm()
    if form.validate_on_submit():        
        print('-------------------------')
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['subject'])
        print(request.form['message'])       
        print('-------------------------')
        send_message(request.form)
        return redirect('/success')    

    return render_template('kontakt.html', form=form)

@app.route('/success')
def success():
    return render_template('index.html')

def send_message(message):
    print(message.get('name'))

    msg = Message(message.get('subject'), sender = message.get('email'),
            recipients = ['id1@gmail.com'],
            body= message.get('message')
    )  
    mail.send(msg)

if __name__ == '__main__':
    app.run()