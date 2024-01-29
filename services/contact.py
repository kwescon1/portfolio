from flask import request

def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            
            # connect to db here
        except:
            # data was not saved.
            # throw exception
            pass
        
        return data
    else:
        return 'somthing went wrong'
    