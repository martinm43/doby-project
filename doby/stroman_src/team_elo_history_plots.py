"""
Short sample script that plots the moving SRS for a given team over their 
available history in the SRS database.

Inputs: None
    
Outputs: Bitmap images of the SRS rating history of all 30 teams

"""
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
import io
import base64
from doby.stroman_src.mlb_database.queries import team_abbreviation


rolling_average = 41

from pathlib import Path
base_path = Path(__file__).parent
file_path = (base_path / "mlb_data.sqlite").resolve()
#file_path = "/Users/martin/Documents/doby-project/doby/stroman_src/mlb_data.sqlite"
#print(file_path)

def team_plot_function(team_id):
    print(file_path)
    conn = sqlite3.connect(file_path)
    query = "SELECT epochtime,elo_rating FROM ratings where team_id = " + str(
        team_id)+ " order by epochtime desc"
    

    df = pd.read_sql_query(query, conn)

    df["epochtime"] = pd.to_datetime(df["epochtime"], unit="s")

    # get the appropriate colours
    cursor = conn.cursor()
    cursor.execute(
        "SELECT primary_color from teams where team_id=" + str(team_id)
    )
    s = cursor.fetchall()
    plt.figure(figsize=(6, 6))
    plt.plot(
        df["epochtime"],
        df["elo_rating"].rolling(rolling_average).mean(),
        label=team_abbreviation(team_id),
        color=s[0][0],
    )
    plt.xticks(rotation=45)
    plt.legend()
    plt.title("Elo rating history")
    img_stream = io.BytesIO()
    plt.savefig(img_stream, format='png')
    img_stream.seek(0)
    img_base64 = base64.b64encode(img_stream.read()).decode()
    return img_base64

if __name__=="__main__":
    for team_id in range(30, 0, -1):
        img_base64 = team_plot_function(team_id)

        # Decode the Base64 string to bytes
        img_data = base64.b64decode(img_base64)

        # Create a BytesIO object to read the image data
        img_stream = io.BytesIO(img_data)

        # Read and plot the image using Matplotlib
        img = plt.imread(img_stream)
        plt.imshow(img)
        #plt.axis('off')  # Optionally, turn off axis labels

        plt.show(block=False)
        plt.pause(1)
        plt.close()