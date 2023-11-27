from flask import Flask, redirect, render_template, request, url_for
import re

app = Flask(__name__)
emojis = {
    ":)": "😀", 
    ":(": "😞", 
    ":D": "😃", 
    ";)": "😉", 
    ":P": "😛", 
    "xD": "🤣", 
    ":-)": "😀", 
    ":-(": "☹️", 
    "(y)":"👍",
    "(n)":"👎",
    "<3": "❤️",
    "\\m/": "🤘",
    ":-O": "😮",
    ":O": "😮",
    ":-|": "😐",
    ":|": "😐",
    ":-*": "😗",
    ":*": "😗",
    ">:-(": "😠",
    ">:(": "😠",
    "^^": "😊",
    ":-]": "😊",
    ":3":"🐶", 
}

def lexicographic_analyzer(string):
    words = new_string = string
    num_emojis, num_spanish_words = 0, 0
    
    for key in emojis.keys():
        pattern = re.compile(re.escape(key) + "|[?¿¡!.,]")
        words = re.sub(pattern, " ", words)

    num_spanish_words = len(words.split())

    for key in emojis.keys():
        pattern = re.compile(re.escape(key))
        matches = re.findall(pattern, new_string)
        num_emojis += len(matches)
        new_string = re.sub(pattern, emojis[key], new_string)

    return [new_string, num_emojis, num_spanish_words]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form_text = request.form['text']
        emojis_string, num_emojis, num_spanish_words = lexicographic_analyzer(form_text)
        return render_template('index.html', tokens=[("Emojis", num_emojis), ("Spanish Words", num_spanish_words)], result_string=emojis_string)
    
    return render_template('index.html', tokens=None, result_string=None)

if(__name__=="__main__"): 
    app.run() 