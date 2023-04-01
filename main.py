from flask import Flask, render_template, request, redirect
from generate import readMETAR, formatData, warnings, opacities

app = Flask(__name__)

null = [None, '', ' ']

@app.route('/')
def home():
    values = formatData()
    return render_template('clearskies.html', contentTo=values['contentTo'], contentFrom=values['contentFrom'], warnings=values['warnings'], opacities=values['opacities'])

@app.route("/how")
def how():
    return render_template('clearskieshowtouse.html')

@app.route("/search")
def search():
    radio = request.args.get('radio')
    searchTo = request.args.get('q1')
    searchFrom = request.args.get('q2')
    deicing = request.args.get('deicing')
    print(f"RADIO= {radio}, SEARCH= {search} SWITCH= {deicing}")
    if searchTo not in null and searchFrom not in null:
        values = formatData(radio=radio, searchTo=searchTo, searchFrom=searchFrom, deicing=deicing)
        if not values:
            return render_template('clearskieserror.html')
    else:
        return render_template('clearskieserror.html')
    return render_template('clearskies.html', contentTo=values['contentTo'], contentFrom=values['contentFrom'], warnings=values['warnings'], opacities=values['opacities'])


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)