from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def root():  # put application's code here
    courses = ['PHP', 'Python', 'Java', 'Javascript']
    data = {
        'title': 'Home page',
        'message': 'Hello, world',
        'courses': courses,
        'courses_amount': len(courses)
    }
    return render_template('index.jinja', data=data)

@app.route('/contact/<name>')
def contact(name):
    data = {
        'title': 'Contact', 
        'name': name
    }
    return render_template('contact.jinja', data=data)
    

if __name__ == '__main__':
    app.run(debug=True, port=5000)
