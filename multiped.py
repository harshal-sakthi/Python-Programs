l = [
    {"trip_id": "UB12345", "pickup": "Namakkal", "drop": "Airport", "fare" : 560},
    {"trip_id": "UB1002", "pickup": "Chennai", "drop":"Kerala", "fare" : 130},
    {"trip_id": "UB1001", "pickup": "Kanyakumari", "fare" : 450}
]

for i in l:
    print(i["trip_id"])