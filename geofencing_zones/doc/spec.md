<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: geofencing_zones  
========================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.GBFS/blob/master/geofencing_zones/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **Describes geofencing zones and their associated rules and attributes (added in v2.1-RC). According to the Standard GBFS 2.2**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `data[object]`: Array that contains geofencing information for the system.  	  
- `id[*]`: Unique identifier of the entity  - `last_updated[integer]`: Last time the data in the feed was updated in POSIX time.  - `ttl[integer]`: Number of seconds before the data in the feed will be updated again (0 if the data should always be refreshed).  - `type[string]`: NGSI entity type. It has to be geofencing_zones  - `version[string]`: GBFS version number to which the feed conforms, according to the versioning framework.  <!-- /30-PropertiesList -->  
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
geofencing_zones:    
  description: Describes geofencing zones and their associated rules and attributes (added in v2.1-RC). According to the Standard GBFS 2.2    
  properties:    
    data:    
      description: Array that contains geofencing information for the system.    
      properties:    
        geofencing_zones:    
          description: Each geofenced zone and its associated rules and attributes is described as an object within the array of features.    
          properties:    
            features:    
              description: Array of objects.    
              items:    
                properties:    
                  geometry:    
                    description: 'A polygon that describes where rides might not be able to start, end, go through, or have otehr limitations. Must follow the right-hand rule.'    
                    properties:    
                      coordinates:    
                      type:    
                    required:    
                      - type    
                      - coordinates    
                    title: GeoJSON MultiPolygon    
                    type: object    
                  properties:    
                    description: Describing travel allowances and limitations.    
                    properties:    
                      end:    
                      name:    
                      rules:    
                      start:    
                    type: object    
                  type:    
                    enum:    
                      - Feature    
                    type: string    
                required:    
                  - type    
                  - geometry    
                  - properties    
                title: GeoJSON Feature    
                type: object    
              type: array    
            type:    
              description: FeatureCollection as per IETF RFC 7946.    
              enum:    
                - FeatureCollection    
              type: string    
          required:    
            - type    
            - features    
          type: object    
      type: object    
      x-ngsi:    
        type: Property    
    id:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    last_updated:    
      description: Last time the data in the feed was updated in POSIX time.    
      minimum: 1450155600    
      type: integer    
      x-ngsi:    
        type: Property    
    ttl:    
      description: Number of seconds before the data in the feed will be updated again (0 if the data should always be refreshed).    
      minimum: 0    
      type: integer    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI entity type. It has to be geofencing_zones    
      enum:    
        - geofencing_zones    
      type: string    
      x-ngsi:    
        type: Property    
    version:    
      description: 'GBFS version number to which the feed conforms, according to the versioning framework.'    
      enum:    
        - 2.1-RC    
        - 2.1-RC2    
        - 2.1    
        - 2.2    
        - 3.0-RC    
        - 3.0    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - data    
    - last_updated    
    - ttl    
    - type    
    - version    
  type: object    
  x-derived-from: https://github.com/NABSA/gbfs/blob/v2.2/gbfs.md    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.GBFS/blob/master/geofencing_zones/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.GBFS/geofencing_zones/schema.json    
  x-model-tags: GBFS    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
#### geofencing_zones NGSI-v2 key-values Example    
Here is an example of a geofencing_zones in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:geofencing_zones:id:FNNO:60592292",  
  "type": "geofencing_zones",  
  "last_updated": 1604198100,  
  "ttl": 60,  
  "version": "3.0",  
  "data": {  
    "geofencing_zones": {  
      "type": "FeatureCollection",  
      "features": [  
        {  
          "type": "Feature",  
          "geometry": {  
            "type": "MultiPolygon",  
            "coordinates": [  
              [  
                [  
                  [  
                    -122.578067,  
                    45.562982  
                  ],  
                  [  
                    -122.661838,  
                    45.562741  
                  ],  
                  [  
                    -122.661151,  
                    45.504542  
                  ],  
                  [  
                    -122.578926,  
                    45.5046625  
                  ],  
                  [  
                    -122.578067,  
                    45.562982  
                  ]  
                ]  
              ],  
              [  
                [  
                  [  
                    -122.650680,  
                    45.548197  
                  ],  
                  [  
                    -122.650852,  
                    45.534731  
                  ],  
                  [  
                    -122.630939,  
                    45.535212  
                  ],  
                  [  
                    -122.630424,  
                    45.548197  
                  ],  
                  [  
                    -122.650680,  
                    45.548197  
                  ]  
                ]  
              ]  
            ]  
          },  
          "properties": {  
            "name": "NE 24th/NE Knott",  
            "start": 1593878400,  
            "end": 1593907260,  
            "rules": [  
              {  
                "vehicle_type_id": [  
                  "moped1",  
                  "car1"  
                ],  
                "ride_allowed": false,  
                "ride_through_allowed": true,  
                "maximum_speed_kph": 10  
              }  
            ]  
          }  
        }  
      ]  
    }  
  }  
}  
```  
</details>  
#### geofencing_zones NGSI-v2 normalized Example    
Here is an example of a geofencing_zones in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:geofencing_zones:id:FNNO:60592292",  
  "type": "geofencing_zones",  
  "last_updated": {  
    "type": "Number",  
    "value": 1604198100  
  },  
  "ttl": {  
    "type": "Number",  
    "value": 60  
  },  
  "version": {  
    "type": "Text",  
    "value": "3.0"  
  },  
  "data": {  
    "type": "StructuredValue",  
    "value": {  
      "geofencing_zones": {  
        "type": "FeatureCollection",  
        "features": [  
          {  
            "type": "Feature",  
            "geometry": {  
              "type": "MultiPolygon",  
              "coordinates": [  
                [  
                  [  
                    [  
                      -122.578067,  
                      45.562982  
                    ],  
                    [  
                      -122.661838,  
                      45.562741  
                    ],  
                    [  
                      -122.661151,  
                      45.504542  
                    ],  
                    [  
                      -122.578926,  
                      45.5046625  
                    ],  
                    [  
                      -122.578067,  
                      45.562982  
                    ]  
                  ]  
                ],  
                [  
                  [  
                    [  
                      -122.650680,  
                      45.548197  
                    ],  
                    [  
                      -122.650852,  
                      45.534731  
                    ],  
                    [  
                      -122.630939,  
                      45.535212  
                    ],  
                    [  
                      -122.630424,  
                      45.548197  
                    ],  
                    [  
                      -122.650680,  
                      45.548197  
                    ]  
                  ]  
                ]  
              ]  
            },  
            "properties": {  
              "name": "NE 24th/NE Knott",  
              "start": 1593878400,  
              "end": 1593907260,  
              "rules": [  
                {  
                  "vehicle_type_id": [  
                    "moped1",  
                    "car1"  
                  ],  
                  "ride_allowed": false,  
                  "ride_through_allowed": true,  
                  "maximum_speed_kph": 10  
                }  
              ]  
            }  
          }  
        ]  
      }  
    }  
  }  
}  
```  
</details>  
#### geofencing_zones NGSI-LD key-values Example    
Here is an example of a geofencing_zones in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:geofencing_zones:id:FNNO:60592292",  
    "type": "geofencing_zones",  
    "last_updated": 1604198100,  
    "ttl": 60,  
    "version": "3.0",  
    "data": {  
        "geofencing_zones": {  
            "type": "FeatureCollection",  
            "features": [  
                {  
                    "type": "Feature",  
                    "geometry": {  
                        "type": "MultiPolygon",  
                        "coordinates": [  
                            [  
                                [  
                                    [  
                                        -122.578067,  
                                        45.562982  
                                    ],  
                                    [  
                                        -122.661838,  
                                        45.562741  
                                    ],  
                                    [  
                                        -122.661151,  
                                        45.504542  
                                    ],  
                                    [  
                                        -122.578926,  
                                        45.5046625  
                                    ],  
                                    [  
                                        -122.578067,  
                                        45.562982  
                                    ]  
                                ]  
                            ],  
                            [  
                                [  
                                    [  
                                        -122.65068,  
                                        45.548197  
                                    ],  
                                    [  
                                        -122.650852,  
                                        45.534731  
                                    ],  
                                    [  
                                        -122.630939,  
                                        45.535212  
                                    ],  
                                    [  
                                        -122.630424,  
                                        45.548197  
                                    ],  
                                    [  
                                        -122.65068,  
                                        45.548197  
                                    ]  
                                ]  
                            ]  
                        ]  
                    },  
                    "properties": {  
                        "name": "NE 24th/NE Knott",  
                        "start": 1593878400,  
                        "end": 1593907260,  
                        "rules": [  
                            {  
                                "vehicle_type_id": [  
                                    "moped1",  
                                    "car1"  
                                ],  
                                "ride_allowed": false,  
                                "ride_through_allowed": true,  
                                "maximum_speed_kph": 10  
                            }  
                        ]  
                    }  
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
</details>  
#### geofencing_zones NGSI-LD normalized Example    
Here is an example of a geofencing_zones in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:geofencing_zones:id:FNNO:60592292",  
    "type": "geofencing_zones",  
    "last_updated": {  
        "type": "Property",  
        "value": 1604198100  
    },  
    "ttl": {  
        "type": "Property",  
        "value": 60  
    },  
    "version": {  
        "type": "Property",  
        "value": "3.0"  
    },  
    "data": {  
        "type": "Property",  
        "value": {  
            "geofencing_zones": {  
                "type": "FeatureCollection",  
                "features": [  
                    {  
                        "type": "Feature",  
                        "geometry": {  
                            "type": "MultiPolygon",  
                            "coordinates": [  
                                [  
                                    [  
                                        [  
                                            -122.578067,  
                                            45.562982  
                                        ],  
                                        [  
                                            -122.661838,  
                                            45.562741  
                                        ],  
                                        [  
                                            -122.661151,  
                                            45.504542  
                                        ],  
                                        [  
                                            -122.578926,  
                                            45.5046625  
                                        ],  
                                        [  
                                            -122.578067,  
                                            45.562982  
                                        ]  
                                    ]  
                                ],  
                                [  
                                    [  
                                        [  
                                            -122.65068,  
                                            45.548197  
                                        ],  
                                        [  
                                            -122.650852,  
                                            45.534731  
                                        ],  
                                        [  
                                            -122.630939,  
                                            45.535212  
                                        ],  
                                        [  
                                            -122.630424,  
                                            45.548197  
                                        ],  
                                        [  
                                            -122.65068,  
                                            45.548197  
                                        ]  
                                    ]  
                                ]  
                            ]  
                        },  
                        "properties": {  
                            "name": "NE 24th/NE Knott",  
                            "start": 1593878400,  
                            "end": 1593907260,  
                            "rules": [  
                                {  
                                    "vehicle_type_id": [  
                                        "moped1",  
                                        "car1"  
                                    ],  
                                    "ride_allowed": false,  
                                    "ride_through_allowed": true,  
                                    "maximum_speed_kph": 10  
                                }  
                            ]  
                        }  
                    }  
                ]  
            }  
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
