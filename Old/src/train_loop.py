import requests
import time
import train


def data_loop(next_train):

    API_KEY = '610fdb33f19f4ae6bf2a1c8429838600'

    while True:

        try:
            session = requests.Session()
            session.headers['api_key'] = API_KEY
            adapter = requests.adapters.HTTPAdapter(max_retries=0)
            session.mount('http://', adapter)
            response = session.get("https://api.wmata.com/StationPrediction.svc/json/GetPrediction/K04",
                                   timeout=2.5)
            print("Data Received")
        except requests.exceptions.Timeout:
            print("*************TIMEOUT**************")
        except requests.exceptions.RequestException:
            print("*************DNS ERROR**************")

        if response is not None:
            try:
                trains_data = response.json()['Trains']
                next_train.clear()
            except KeyError:
                break

        for train_data in trains_data:
            if (train_data['DestinationName'] == "New Carrollton" or train_data['DestinationName'] == "Largo Town Center"):
                t = train.Train()
                t.time = train_data['Min']
                t.set_line(train_data['Line'])
                t.dest = train_data['DestinationName']
                next_train.append(t)

        time.sleep(20)
