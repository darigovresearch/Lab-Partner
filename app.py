# app.py is code that runs a flask web app for the user interface

from flask import Flask, render_template, request
import scheduler as s

app = Flask(__name__)
# line to prevent cache from not updating static files
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/', methods=['POST', 'GET'])
def home():

    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        form_data = request.form
        print(form_data)

        if form_data["enabled"] == "enabled-no":
            s.reset_all()
            return render_template('index.html', enabled="No")
        else:
            if form_data["frequency"] == "freq-1":
                s.every_minute()
                return render_template(
                                        'index.html',
                                        enabled="Yes",
                                        frequency="Every minute"
                                      )
            elif form_data["frequency"] == "freq-5":
                s.every_five_minutes()
                return render_template(
                                        'index.html',
                                        enabled="Yes",
                                        frequency="Every 5 minutes"
                                       )
            elif form_data["frequency"] == "freq-10":
                s.every_ten_minutes()
                return render_template(
                                        'index.html',
                                        enabled="Yes",
                                        frequency="Every 10 minutes"
                                      )
            elif form_data["frequency"] == "freq-15":
                s.every_fifteen_minutes()
                return render_template(
                                        'index.html',
                                        enabled="Yes",
                                        frequency="Every 15 minutes"
                                      )
            elif form_data["frequency"] == "freq-30":
                s.every_thirty_minutes()
                return render_template(
                                        'index.html',
                                        enabled="Yes",
                                        frequency="Every 30 minutes"
                                      )
            elif form_data["frequency"] == "freq-60":
                s.every_sixty_minutes()
                return render_template(
                                        'index.html',
                                        enabled="Yes",
                                        frequency="Every 60 minutes"
                                      )
            else:
                print("Incorrect selection")
        return render_template('index.html')

    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8765", debug=True)
