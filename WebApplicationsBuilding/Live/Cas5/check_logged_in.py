from flask import session
 
 
def check_logged_in() -> bool:
    if 'logged_in' in session:
        return True
    return False