from flask import Flask
from .randomly_close import randomly_close, mobile, desktop

app = Flask(__name__)

@app.route('/<layout>/<int:length>')
def get_random_code(layout='mobile', length=5):
    if layout == 'mobile':
        layout = mobile
    else:
        layout = desktop
    return ''.join([str(num) for num in randomly_close(layout, length)])
