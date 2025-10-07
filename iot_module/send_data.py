import requests, random, time

url = 'http://127.0.0.1:5000/submit_health_data'

while True:
    sample = {
        'village':'TestVillage',
        'temperature': random.randint(36,40),
        'diarrhea_cases': random.randint(0,5)
    }
    try:
        r = requests.post(url,json=sample)
        print(r.json())
    except:
        print('Backend not running')
    time.sleep(10)
