from flask import Flask
from datetime import date

app = Flask(__name__)

# Получаем текущую дату
today = date.today()

@app.route('/')
def current_date():
    return f"<p>Текущая дата: {today}</p>"

if __name__ == '__main__':
    app.run()
