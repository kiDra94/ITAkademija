import html
from flask import Flask, redirect,  render_template, request
from vsearch import search4letters
from markupsafe import escape

app = Flask(__name__)

'''@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'
#stara root putanja'''


'''
@app.route('/')
def hello() -> '302': #302 je poruka o redirekciji
    return redirect('/entry')'''

@app.route('/') #dodatni dekorater da ne moramo da pravimo def hello!
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')
#render_template perusmjerava

@app.route('/entry2')
def entry2_page() -> 'html':
    return render_template('entry2.html')

@app.route('/abc')
def hello_abc() -> str:
    return 'Hello abc!'

@app.route('/search4', methods=['POST']) #POST zato sto je u entry.html isto post!!!
def do_search() -> str:
    phrase = request.form['phrase'] #zato sto je u entry.html name phrase
    letters = request.form['letters'] #zato sto je u entry.html name letters
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',\
                            the_title = 'This are the results',\
                            the_phrase = phrase,\
                            the_letters = letters,\
                            the_results = results)

def log_request(req, res: str) -> None:
    """Log details of the web request and the results."""
    with open('vsearch.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')

@app.route('/search5', methods=['POST']) 
def do_search5() -> str:
    return str(search4letters('life, the universe, and everything', 'earbj,!'))

'''@app.route('/viewlog')
def view_the_log() -> 'str':
    with open('vsearch.log') as log:
        contents = log.read()
    # return contents
    return escape(contents)'''
 
@app.route('/viewlog')
def view_the_log():
    """Display the contents of the log file as a HTML table."""
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents,)


app.run(debug=True) #debuge=True znaci da ne moramo da restart server kad hocemo promjene
