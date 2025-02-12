import requests
import datetime as dt
import smtplib
import time

MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"

MY_LAT = 51.507
MY_LNG = -0.1277

def currently_dark():
    # sunrise/sunset
    parameters = {
        "lat":MY_LAT,
        "lng": MY_LNG,
        "formatted":0
    }


    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    print(sunrise)
    print(sunset)

    time_now =dt.datetime.now().hour

    if time_now < sunset or time_now > sunrise:
        return True


def within_position( ):
    #ISS position
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    # if response.status_code == 404:
    #     raise Exception ("Resource does not exist")

    data = response.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    iss_position = (iss_longitude,iss_latitude)
    print(iss_position)

    if MY_LAT-5<= iss_longitude <= MY_LAT+5 and MY_LNG-5<=iss_latitude<=MY_LNG:
        return True

while True:
    time.sleep(200)
    if currently_dark and within_position:
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs="YOUR ADDRESS", msg="LOOK UP! ISS IS ABOVE YOU")
        
        connection.close()
