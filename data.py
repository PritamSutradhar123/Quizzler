import requests



params ={
    "amount":10,
    "category":11,
    "type":"boolean"

}
def question_data():
    response = requests.get(url="https://opentdb.com/api.php",params=params)
    response.raise_for_status()
    return response.json()['results']