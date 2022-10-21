<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: station_status  
======================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.GBFS/blob/master/station_status/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **Describes the capacity and rental availability of the station According to the Standard GBFS 2.2**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `data[object]`: Array that contains one object per station as defined below.  - `id[*]`: Unique identifier of the entity  - `last_updated[integer]`: Last time the data in the feed was updated in POSIX time.  - `ttl[integer]`: Number of seconds before the data in the feed will be updated again (0 if the data should always be refreshed).  - `type[string]`: NGSI entity type. It has to be station_status  - `version[string]`: GBFS version number to which the feed conforms, according to the versioning framework (added in v1.1).  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `data`  - `id`  - `last_updated`  - `ttl`  - `type`  - `version`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Mapping of the Standard [GBFS 2.2](https://github.com/NABSA/gbfs/blob/v2.2/gbfs.md)  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
station_status:    
  description: 'Describes the capacity and rental availability of the station According to the Standard GBFS 2.2'    
  properties:    
    data:    
      description: 'Array that contains one object per station as defined below.'    
      properties:    
        stations:    
          items:    
            properties:    
              is_installed:    
                description: 'Is the station currently on the street?'    
                type: boolean    
              is_renting:    
                description: 'Is the station currently renting vehicles?'    
                type: boolean    
              is_returning:    
                description: 'Is the station accepting vehicle returns?'    
                type: boolean    
              last_reported:    
                description: 'The last time this station reported its status to the operator''s backend in POSIX time.'    
                minimum: 1450155600    
                type: number    
              num_bikes_available:    
                description: 'Number of vehicles of any type physically available for rental at the station.'    
                minimum: 0    
                type: number    
              num_bikes_disabled:    
                description: 'Number of disabled vehicles of any type at the station.'    
                minimum: 0    
                type: number    
              num_docks_available:    
                description: 'Number of functional docks physically at the station.'    
                minimum: 0    
                type: number    
              num_docks_disabled:    
                description: 'Number of empty but disabled docks at the station.'    
                minimum: 0    
                type: number    
              station_id:    
                description: 'Identifier of a station.'    
                type: string    
              vehicle_docks_available:    
                dependencies:    
                  vehicle_docks_available:    
                    - vehicle_type_ids    
                    - count    
                description: 'Object displaying available docks by vehicle type (added in v2.1-RC).'    
                items:    
                  properties:    
                    count:    
                      description: 'A number representing the total number of available docks for the defined vehicle type (added in v2.1-RC).'    
                      minimum: 0    
                      type: number    
                    vehicle_type_ids:    
                      description: 'An array of strings where each string represents a vehicle_type_id that is able to use a particular type of dock at the station (added in v2.1-RC).'    
                      items:    
                        type: string    
                      type: array    
                  type: object    
                type: array    
              vehicles:    
                description: 'Array of objects containing data about a specific vehicle that is present at the docking station (added in v2.1-RC).'    
                items:    
                  properties:    
                    bike_id:    
                      description: 'Rotated identifier of a vehicle (added in v2.1-RC).'    
                      type: string    
                    current_range_meters:    
                      description: 'The furthest distance in meters that the vehicle can travel without recharging or refueling with the vehicle''s current charge or fuel (added in v2.1-RC).'    
                      minimum: 0    
                      type: number    
                    is_disabled:    
                      description: 'Is the vehicle currently disabled (broken)? (added in v2.1-RC)'    
                      type: boolean    
                    is_reserved:    
                      description: 'Is the vehicle currently reserved for someone else? (added in v2.1-RC)'    
                      type: boolean    
                    vehicle_type_id:    
                      description: 'The vehicle_type_id of this vehicle as described in vehicle_types.json (added in v2.1-RC).'    
                      type: string    
                  type: object    
                required:    
                  - bike_id    
                  - is_reserved    
                  - is_disabled    
                  - vehicle_type_id    
                type: array    
              vehicles_types_available:    
                description: 'Array of objects displaying the total number of each vehicle type at the station (added in v2.1-RC).'    
                items:    
                  properties:    
                    count:    
                      description: 'A number representing the total amount of this vehicle type at the station (added in v2.1-RC).'    
                      minimum: 0    
                      type: number    
                    vehicle_type_id:    
                      description: 'The vehicle_type_id of vehicle at the station (added in v2.1-RC).'    
                      type: string    
                  type: object    
                type: array    
            type: object    
          required:    
            - station_id    
            - num_bikes_available    
            - is_installed    
            - is_renting    
            - is_returning    
            - last_reported    
          type: array    
      required:    
        - stations    
      type: object    
      x-ngsi:    
        type: Property    
    id:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    last_updated:    
      description: 'Last time the data in the feed was updated in POSIX time.'    
      minimum: 1450155600    
      type: integer    
      x-ngsi:    
        type: Property    
    ttl:    
      description: 'Number of seconds before the data in the feed will be updated again (0 if the data should always be refreshed).'    
      minimum: 0    
      type: integer    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI entity type. It has to be station_status'    
      enum:    
        - station_status    
      type: string    
      x-ngsi:    
        type: Property    
    version:    
      description: 'GBFS version number to which the feed conforms, according to the versioning framework (added in v1.1).'    
      enum:    
        - 2.1-RC2    
        - 2.1    
        - 2.2    
        - 3.0    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - data    
    - id    
    - last_updated    
    - ttl    
    - type    
    - version    
  type: object    
  x-derived-from: https://github.com/NABSA/gbfs/blob/v2.2/gbfs.md    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.GBFS/blob/master/station_status/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.GBFS/station_status/schema.json    
  x-model-tags: GBFS    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
#### station_status NGSI-v2 key-values Example    
Here is an example of a station_status in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:station_status:id:FNNO:60592292",  
  "type": "station_status",  
  "last_updated": 1609866247,  
  "ttl": 0,  
  "version": "3.0",  
  "data": {  
    "stations": [  
      {  
        "station_id": "station1",  
        "is_installed": true,  
        "is_renting": true,  
        "is_returning": true,  
        "last_reported": 1609866125,  
        "num_docks_available": 3,  
        "vehicle_docks_available": [  
          {  
            "vehicle_type_ids": [  
              "abc123"  
            ],  
            "count": 2  
          },  
          {  
            "vehicle_type_ids": [  
              "def456"  
            ],  
            "count": 1  
          }  
        ],  
        "num_bikes_available": 1,  
        "vehicle_types_available": [  
          {  
            "vehicle_type_id": "abc123",  
            "count": 1  
          },  
          {  
            "vehicle_type_id": "def456",  
            "count": 0  
          }  
        ]  
      },  
      {  
        "station_id": "station2",  
        "is_installed": true,  
        "is_renting": true,  
        "is_returning": true,  
        "last_reported": 1609866106,  
        "num_docks_available": 8,  
        "vehicle_docks_available": [  
          {  
            "vehicle_type_ids": [  
              "abc123"  
            ],  
            "count": 6  
          },  
          {  
            "vehicle_type_ids": [  
              "def456"  
            ],  
            "count": 2  
          }  
        ],  
        "num_bikes_available": 6,  
        "vehicle_types_available": [  
          {  
            "vehicle_type_id": "abc123",  
            "count": 2  
          },  
          {  
            "vehicle_type_id": "def456",  
            "count": 4  
          }  
        ]  
      }  
    ]  
  }  
}  
```  
</details>  
#### station_status NGSI-v2 normalized Example    
Here is an example of a station_status in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:station_status:id:FNNO:60592292",  
  "type": "station_status",  
  "last_updated": {  
    "type": "Number",  
    "value": 1609866247  
  },  
  "ttl": {  
    "type": "Number",  
    "value": 0  
  },  
  "version": {  
    "type": "Text",  
    "value": "3.0"  
  },  
  "data": {  
    "type": "StructuredValue",  
    "value": {  
      "stations": [  
        {  
          "station_id": "station1",  
          "is_installed": true,  
          "is_renting": true,  
          "is_returning": true,  
          "last_reported": 1609866125,  
          "num_docks_available": 3,  
          "vehicle_docks_available": [  
            {  
              "vehicle_type_ids": [  
                "abc123"  
              ],  
              "count": 2  
            },  
            {  
              "vehicle_type_ids": [  
                "def456"  
              ],  
              "count": 1  
            }  
          ],  
          "num_bikes_available": 1,  
          "vehicle_types_available": [  
            {  
              "vehicle_type_id": "abc123",  
              "count": 1  
            },  
            {  
              "vehicle_type_id": "def456",  
              "count": 0  
            }  
          ]  
        },  
        {  
          "station_id": "station2",  
          "is_installed": true,  
          "is_renting": true,  
          "is_returning": true,  
          "last_reported": 1609866106,  
          "num_docks_available": 8,  
          "vehicle_docks_available": [  
            {  
              "vehicle_type_ids": [  
                "abc123"  
              ],  
              "count": 6  
            },  
            {  
              "vehicle_type_ids": [  
                "def456"  
              ],  
              "count": 2  
            }  
          ],  
          "num_bikes_available": 6,  
          "vehicle_types_available": [  
            {  
              "vehicle_type_id": "abc123",  
              "count": 2  
            },  
            {  
              "vehicle_type_id": "def456",  
              "count": 4  
            }  
          ]  
        }  
      ]  
    }  
  }  
}  
```  
</details>  
#### station_status NGSI-LD key-values Example    
Here is an example of a station_status in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:station_status:id:FNNO:60592292",  
    "type": "station_status",  
    "last_updated": 1609866247,  
    "ttl": 0,  
    "version": "3.0",  
    "data": {  
        "stations": [  
            {  
                "station_id": "station1",  
                "is_installed": true,  
                "is_renting": true,  
                "is_returning": true,  
                "last_reported": 1609866125,  
                "num_docks_available": 3,  
                "vehicle_docks_available": [  
                    {  
                        "vehicle_type_ids": [  
                            "abc123"  
                        ],  
                        "count": 2  
                    },  
                    {  
                        "vehicle_type_ids": [  
                            "def456"  
                        ],  
                        "count": 1  
                    }  
                ],  
                "num_bikes_available": 1,  
                "vehicle_types_available": [  
                    {  
                        "vehicle_type_id": "abc123",  
                        "count": 1  
                    },  
                    {  
                        "vehicle_type_id": "def456",  
                        "count": 0  
                    }  
                ]  
            },  
            {  
                "station_id": "station2",  
                "is_installed": true,  
                "is_renting": true,  
                "is_returning": true,  
                "last_reported": 1609866106,  
                "num_docks_available": 8,  
                "vehicle_docks_available": [  
                    {  
                        "vehicle_type_ids": [  
                            "abc123"  
                        ],  
                        "count": 6  
                    },  
                    {  
                        "vehicle_type_ids": [  
                            "def456"  
                        ],  
                        "count": 2  
                    }  
                ],  
                "num_bikes_available": 6,  
                "vehicle_types_available": [  
                    {  
                        "vehicle_type_id": "abc123",  
                        "count": 2  
                    },  
                    {  
                        "vehicle_type_id": "def456",  
                        "count": 4  
                    }  
                ]  
            }  
        ]  
    },  
    "@context": [  
        "https://smartdatamodels.org/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.GBFS/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### station_status NGSI-LD normalized Example    
Here is an example of a station_status in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:station_status:id:FNNO:60592292",  
    "type": "station_status",  
    "last_updated": {  
        "type": "Property",  
        "value": 1609866247  
    },  
    "ttl": {  
        "type": "Property",  
        "value": 0  
    },  
    "version": {  
        "type": "Property",  
        "value": "3.0"  
    },  
    "data": {  
        "type": "Property",  
        "value": {  
            "stations": [  
                {  
                    "station_id": "station1",  
                    "is_installed": true,  
                    "is_renting": true,  
                    "is_returning": true,  
                    "last_reported": 1609866125,  
                    "num_docks_available": 3,  
                    "vehicle_docks_available": [  
                        {  
                            "vehicle_type_ids": [  
                                "abc123"  
                            ],  
                            "count": 2  
                        },  
                        {  
                            "vehicle_type_ids": [  
                                "def456"  
                            ],  
                            "count": 1  
                        }  
                    ],  
                    "num_bikes_available": 1,  
                    "vehicle_types_available": [  
                        {  
                            "vehicle_type_id": "abc123",  
                            "count": 1  
                        },  
                        {  
                            "vehicle_type_id": "def456",  
                            "count": 0  
                        }  
                    ]  
                },  
                {  
                    "station_id": "station2",  
                    "is_installed": true,  
                    "is_renting": true,  
                    "is_returning": true,  
                    "last_reported": 1609866106,  
                    "num_docks_available": 8,  
                    "vehicle_docks_available": [  
                        {  
                            "vehicle_type_ids": [  
                                "abc123"  
                            ],  
                            "count": 6  
                        },  
                        {  
                            "vehicle_type_ids": [  
                                "def456"  
                            ],  
                            "count": 2  
                        }  
                    ],  
                    "num_bikes_available": 6,  
                    "vehicle_types_available": [  
                        {  
                            "vehicle_type_id": "abc123",  
                            "count": 2  
                        },  
                        {  
                            "vehicle_type_id": "def456",  
                            "count": 4  
                        }  
                    ]  
                }  
            ]  
        }  
    },  
    "@context": [  
        "https://smartdatamodels.org/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.GBFS/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
