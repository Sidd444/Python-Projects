#importing
from flask import Flask,render_template,request

#interaction
web=Flask(__name__)

#mapping
@web.route('/')
#inputs
def home():
    return render_template('home.html')

@web.route('/register')
def register():
    return render_template('register.html')

@web.route('/confirmation', methods=['POST','GET'])
def confirmation():
    if request.method=='POST':
        get_name=request.form.get('name')
        get_city=request.form.get('city')
        get_phoneNo=request.form.get('phone-number')
    return render_template('confirmation.html', name=get_name, city=get_city,phoneNo=get_phoneNo)


#main
if __name__ == '__main__':
    web.run(debug=True)