from flask import Flask, render_template, redirect, request
from vsearch import search4letters
from markupsafe import escape

app = Flask(__name__)

"""@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'
    """

"""@app.route('/')
def hello() -> '302':
    return redirect('/entry')"""

@app.route('/')
@app.route('/entry')
def entry_page():
    """Returns the entry page to browser."""
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')

@app.route('/search5', methods=['POST'])
def do_search5() -> str:
    return str(search4letters('life, the universe, and everything', 'eiru,!'))

def log_request(req, res: str) -> None:
    """Log details of the web request and the results."""
    with open('vsearch.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')

@app.route('/search4', methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    #return phrase +"    " +letters +"    "+ results
    log_request(request, results)
    log_request2(request, results)
    return render_template('results.html',
                           the_title='Here are your results!',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results)

"""@app.route('/viewlog')
def view_the_log() -> 'str':
    with open('vsearch.log') as log:
        contents = log.read()
    # return contents
    return escape(contents)"""

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

def log_request2(req, res: str) -> None:
    """Log details of the web request and the results."""
    dbconfig = {'host': '127.0.0.1',
                'user': 'root',
                'password': 'banjalukA1%',
                'database': 'vsearchlogDB', 
                'port' : 3306}

    import mysql.connector

    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    print(req.form['phrase'],
                          req.form['letters'],
                          req.remote_addr,
                          req.user_agent,
                          res,)
    _SQL = """insert into log
    (phrase, letters, ip, browser_string, results)
    values
    (%s, %s, %s, %s, %s)"""
    cursor.execute(_SQL, (req.form['phrase'],
                          req.form['letters'],
                          req.remote_addr,
                          str(req.user_agent), # req.user_agent.browser,
                          res,))
    conn.commit()
    cursor.close()
    conn.close()


app.run(debug=True)
