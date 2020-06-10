
print("REQUESTING SOME DATA FROM THE INTERNET...")

import requests
import json
import statistics

request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products/2.json"
response = requests.get(request_url)

response_data = json.loads(response.text)
print(response_data["name"])

print("             ")

request_url2 = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.json"
response2 = requests.get(request_url2)
response_data2 = json.loads(response2.text)
for item in response_data2:
    name = item["name"]
    iden = item["id"]
    print(f"Name is {name} and ID is {iden}.")

print("             ")

request_url3 = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/gradebook.json"
response3 = requests.get(request_url3)
response_data3 = json.loads(response3.text)
grades = [grade['finalGrade'] for grade in response_data3["students"]]
mean = statistics.mean(grades)
minimum_grade = min(grades)
maximum_grade = max(grades)
print(f"Mean is {mean}.")
print(f"The max grade is {maximum_grade} and the min grade is {minimum_grade}.")
