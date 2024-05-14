
#         # This code allows you to install a orion-ld broker in a linux system
#         # The manuals are here https://github.com/FIWARE/context.Orion-LD/tree/develop/doc/manuals-ld
#         
#         # INSTALL NGSI LD broker (OrionLD)
#         sudo docker pull mongo:3.6
#         sudo docker pull fiware/orion-ld
#         sudo docker network create fiware_default
#         sudo docker run -d --name=mongo-db --network=fiware_default --expose=27017 mongo:3.6 --bind_ip_all --smallfiles
#         sudo docker run -d --name fiware-orionld -h orion --network=fiware_default -p 1026:1026  fiware/orion-ld -dbhost mongo-db
#         
#         # TO RELAUNCH (only if you have already installed a broker in the same machine)
#         sudo docker stop fiware-orionld
#         sudo docker rm fiware-orionld
#         sudo docker stop mongo-db
#         sudo docker rm mongo-db
#         sudo docker network rm fiware_default
#         
#         # CHECK INSTANCES
#         # Check the broker is running
#         curl -X GET 'http://localhost:1026/version'
#         
#         # Check what entities are in the broker
#         curl -X GET http://localhost:1026/ngsi-ld/v1/entities?local=true&limit=1000
#         
#         # now the python code you can use to insert some value in the context broker according to the data model
#         
from pysmartdatamodels import pysmartdatamodels as sdm
import subprocess
serverUrl = "http://localhost:1026" # supposed that your broker is installed in localhost. Edit to match your configuration
dataModel = "vehicle_types"
subject = "dataModel.GBFS"
last_updated = {'type': 'Property', 'value': 1609866247}
attribute = "last_updated"
value = last_updated
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

ttl = {'type': 'Property', 'value': 0}
attribute = "ttl"
value = ttl
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

version = "{'type': 'Property', 'value': '3.0'}"
attribute = "version"
value = version
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

data = {'type': 'Property', 'value': {'vehicle_types': [{'vehicle_type_id': 'abc123', 'form_factor': 'bicycle', 'propulsion_type': 'human', 'name': 'Example Basic Bike', 'default_reserve_time': 30, 'return_type': ['any_station', 'free_floating'], 'vehicle_assets': {'icon_url': 'https://www.example.com/assets/icon_bicycle.svg', 'icon_url_dark': 'https://www.example.com/assets/icon_bicycle_dark.svg', 'icon_last_modified': '2021-06-15'}, 'default_pricing_plan_id': 'bike_plan_1', 'pricing_plan_ids': ['bike_plan_1', 'bike_plan_2', 'bike_plan_3']}, {'vehicle_type_id': 'def456', 'form_factor': 'scooter', 'propulsion_type': 'electric', 'name': 'Example E-scooter V2', 'default_reserve_time': 30, 'max_range_meters': 12345, 'return_type': ['free_floating'], 'vehicle_assets': {'icon_url': 'https://www.example.com/assets/icon_escooter.svg', 'icon_url_dark': 'https://www.example.com/assets/icon_escooter_dark.svg', 'icon_last_modified': '2021-06-15'}, 'default_pricing_plan_id': 'scooter_plan_1'}, {'vehicle_type_id': 'car1', 'form_factor': 'car', 'propulsion_type': 'combustion', 'name': 'Four-door Sedan', 'default_reserve_time': 0, 'max_range_meters': 523992, 'return_type': ['roundtrip_station'], 'vehicle_assets': {'icon_url': 'https://www.example.com/assets/icon_car.svg', 'icon_url_dark': 'https://www.example.com/assets/icon_car_dark.svg', 'icon_last_modified': '2021-06-15'}, 'default_pricing_plan_id': 'car_plan_1'}]}}
attribute = "data"
value = data
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

print(" In case you have installed the orion-ld broker (see comments on the header of this program)")
print(" Execute this instruction to check that the entities has been inserted")
command = ['curl', '-X', 'GET', 'http://localhost:1026/ngsi-ld/v1/entities?local=true&limit=1000']
result = subprocess.run(command, capture_output=True, text=True)
print(result.stdout)
