# app.py is code that runs a flask web app for the user interface

from flask import Flask, render_template, request
import scheduler as s
import pandas as pd
import data_processing as dp

app = Flask(__name__)
# line to prevent cache from not updating static files
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# generate folder & placeholder db on load
dp.generate_initial_db()

@app.route('/', methods=['POST', 'GET'])
def home():

    parsed_data = "No data yet available"
    parsed_images = "No images yet available"

    df = pd.read_csv("static//Data//data.csv")
    parsed_data = df.to_html()

    list_of_images = []
    for i in range(0, len(list(df.index))):
        temp_image = df.iat[i, 0]
        # temp_image = '<img src="{{url_for(\'static\', filename=\'Data/'+ temp_image +'\')}}" alt="">'
        temp_image = '<img src="/static/Data/' + temp_image + '\" alt="">'
        list_of_images.append(temp_image)

    parsed_images = "\n<br>\n".join(list_of_images)

    if request.method == 'GET':
        return render_template(
                                'index.html',
                                data=parsed_data,
                                images=parsed_images
                              )
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
                                    data=parsed_data,
                                    images=parsed_data
                                  )
        elif enabled_status == "enabled-yes":
            if frequecy_status == "freq-1":
                s.every_minute()
                return render_template(
                                        'index.html',
                                        enabled="Yes",
                                        frequency="Every minute",
                                        data=parsed_data,
                                        images=parsed_data
                                      )
            elif frequecy_status == "freq-5":
                s.every_five_minutes()
                return render_template(
                                        'index.html',
                                        enabled="Yes",
                                        frequency="Every 5 minutes",
                                        data=parsed_data,
                                        images=parsed_data
                                       )
            elif frequecy_status == "freq-10":
                s.every_ten_minutes()
                return render_template(
                                        'index.html',
                                        enabled="Yes",
                                        frequency="Every 10 minutes",
                                        data=parsed_data,
                                        images=parsed_data
                                      )
            elif frequecy_status == "freq-15":
                s.every_fifteen_minutes()
                return render_template(
                                        'index.html',
                                        enabled="Yes",
                                        frequency="Every 15 minutes",
                                        data=parsed_data,
                                        images=parsed_data
                                      )
            elif frequecy_status == "freq-30":
                s.every_thirty_minutes()
                return render_template(
                                        'index.html',
                                        enabled="Yes",
                                        frequency="Every 30 minutes",
                                        data=parsed_data,
                                        images=parsed_images
                                      )
            elif frequecy_status == "freq-60":
                s.every_sixty_minutes()
                return render_template(
                                        'index.html',
                                        enabled="Yes",
                                        frequency="Every 60 minutes",
                                        data=parsed_data,
                                        images=parsed_data
                                      )
            else:
                print("Incorrect selection")

        else:
            print("Enabled has not been set")
        return render_template(
                                'index.html',
                                data=parsed_data,
                                images=parsed_images
                              )

    else:
        return render_template(
                                'index.html',
                                data=parsed_data,
                                images=parsed_images
                              )


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8765", debug=True)
