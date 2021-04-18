
import os
import datetime
import pandas as pd


def generate_initial_db():
    """ generate_initial_db is code to make a data.csv file given that the
    Data/ folder already exists and contains images taken on a schedule
    """

    full_data = []
    list_of_files = os.listdir("Data")
    print(list_of_files)

    for i in range(0, len(list_of_files)):
        if list_of_files[i].endswith(".png"):
            temp_value = list_of_files[i]
            start_string = temp_value[:19]
            print(start_string)
            try:
                date_time = datetime.datetime.strptime(
                                                            start_string,
                                                            '%Y_%m_%d-%H_%M_%S'
                                                            )
                print("\t" + str(date_time))

                temp_list = []
                temp_list.append(list_of_files[i])
                temp_list.append(date_time)
                temp_list.append("TODO")
                full_data.append(temp_list)
            except Exception as e:
                pass

    print(len(list_of_files))
    print(full_data)
    print(len(full_data))

    # generating dataFrame
    columns = ["Image name", "Date stamp", "Value"]
    df = pd.DataFrame(columns=columns, data=full_data)

    # testing dataframe
    print(df)
    print(df.columns)

    # exporting dataset
    df.to_csv("Data//data.csv", index=False)


if __name__ == '__main__':
    generate_initial_db()
