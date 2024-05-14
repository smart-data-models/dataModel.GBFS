
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
dataModel = "station_status"
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

data = {'type': 'Property', 'value': {'stations': [{'station_id': 'station1', 'is_installed': True, 'is_renting': True, 'is_returning': True, 'last_reported': 1609866125, 'num_docks_available': 3, 'vehicle_docks_available': [{'vehicle_type_ids': ['abc123'], 'count': 2}, {'vehicle_type_ids': ['def456'], 'count': 1}], 'num_bikes_available': 1, 'vehicle_types_available': [{'vehicle_type_id': 'abc123', 'count': 1}, {'vehicle_type_id': 'def456', 'count': 0}]}, {'station_id': 'station2', 'is_installed': True, 'is_renting': True, 'is_returning': True, 'last_reported': 1609866106, 'num_docks_available': 8, 'vehicle_docks_available': [{'vehicle_type_ids': ['abc123'], 'count': 6}, {'vehicle_type_ids': ['def456'], 'count': 2}], 'num_bikes_available': 6, 'vehicle_types_available': [{'vehicle_type_id': 'abc123', 'count': 2}, {'vehicle_type_id': 'def456', 'count': 4}]}]}}
attribute = "data"
value = data
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

print(" In case you have installed the orion-ld broker (see comments on the header of this program)")
print(" Execute this instruction to check that the entities has been inserted")
command = ['curl', '-X', 'GET', 'http://localhost:1026/ngsi-ld/v1/entities?local=true&limit=1000']
result = subprocess.run(command, capture_output=True, text=True)
print(result.stdout)