import requests
import time
import datetime
import threading


url = "http://127.0.0.1:8000/upload/"
payload={}
headers = {}

files = [
  [('1', ('1.txt', open('./data_to_upload/1.txt', 'rb'), 'text/plain'))],
  [('2', ('2.txt', open('./data_to_upload/2.txt', 'rb'), 'text/plain'))],
  [('3', ('3.txt', open('./data_to_upload/3.txt', 'rb'), 'text/plain'))],
  [('4', ('4.txt', open('./data_to_upload/4.txt', 'rb'), 'text/plain'))],
  [('5', ('5.txt', open('./data_to_upload/5.txt', 'rb'), 'text/plain'))],
]

# BIG FILES
files = [
  [('1', ('1.txt', open('./big_data_to_upload/1.txt', 'rb'), 'text/plain'))],
  [('2', ('2.txt', open('./big_data_to_upload/2.txt', 'rb'), 'text/plain'))],
  [('3', ('3.txt', open('./big_data_to_upload/3.txt', 'rb'), 'text/plain'))],
  [('4', ('4.txt', open('./big_data_to_upload/4.txt', 'rb'), 'text/plain'))],
  [('5', ('5.txt', open('./big_data_to_upload/5.txt', 'rb'), 'text/plain'))],
]


def make_request(file):
    start_time = time.time()
    print('')
    response = requests.request("POST", url, headers=headers, data=payload, files=file)
    end_time = time.time()
    print(f"RESPONSE: {response.text} \n->\n came at: {datetime.datetime.now()}, sending took: ~{end_time - start_time:.2f} seconds\n")


threads = []
for file in files:
    # make_request(file)
    t = threading.Thread(target=make_request, args=(file,))
    threads.append(t)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()




