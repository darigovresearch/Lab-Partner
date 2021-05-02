# app.py is code that runs a flask web app for the user interface

from flask import Flask, render_template, request
import scheduler as s
import pandas as pd

app = Flask(__name__)
# line to prevent cache from not updating static files
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/', methods=['POST', 'GET'])
def home():

    parsed_data = "No data yet available"

    df = pd.read_csv("Data//data.csv")
    parsed_data = df.to_html()

    if request.method == 'GET':
        return render_template('index.html', data=parsed_data)
    if request.method == 'POST':
        form_data = request.form
        print(form_data)

        enabled_status = form_data["enabled"]
        frequecy_status = form_data["frequency"]

        if enabled_status == "enabled-no":
            s.reset_all()
            return render_template(
                                    'index.html',
                                    enabled="No",
                                    data=parsed_data
                                  )
        elif enabled_status == "enabled-yes":
            if frequecy_status == "freq-1":
                s.every_minute()
                return render_template(
                                        'index.html',
                                        enabled="Yes",
                                        frequency="Every minute",
                                        data=parsed_data
                                      )
            elif frequecy_status == "freq-5":
                s.every_five_minutes()
                return render_template(
                                        'index.html',
                                        enabled="Yes",
                                        frequency="Every 5 minutes",
                                        data=parsed_data
                                       )
            elif frequecy_status == "freq-10":
                s.every_ten_minutes()
                return render_template(
                                        'index.html',
                                        enabled="Yes",
                                        frequency="Every 10 minutes",
                                        data=parsed_data
                                      )
            elif frequecy_status == "freq-15":
                s.every_fifteen_minutes()
                return render_template(
                                        'index.html',
                                        enabled="Yes",
                                        frequency="Every 15 minutes",
                                        data=parsed_data
                                      )
            elif frequecy_status == "freq-30":
                s.every_thirty_minutes()
                return render_template(
                                        'index.html',
                                        enabled="Yes",
                                        frequency="Every 30 minutes",
                                        data=parsed_data
                                      )
            elif frequecy_status == "freq-60":
                s.every_sixty_minutes()
                return render_template(
                                        'index.html',
                                        enabled="Yes",
                                        frequency="Every 60 minutes",
                                        data=parsed_data
                                      )
            else:
                print("Incorrect selection")

        else:
            print("Enabled has not been set")
        return render_template('index.html', data=parsed_data)

    else:
        return render_template('index.html', data=parsed_data)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8765", debug=True)
