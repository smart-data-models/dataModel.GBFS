<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: vehicle_types  
=====================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.GBFS/blob/master/vehicle_types/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **Describes the types of vehicles that System operator has available for rent (added in v2.1-RC). According to the Standard GBFS 2.2**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `data[object]`: Response data in the form of name:value pairs.  	  
- `id[*]`: Unique identifier of the entity  - `last_updated[integer]`: Last time the data in the feed was updated in POSIX time.  - `ttl[integer]`: Number of seconds before the data in the feed will be updated again (0 if the data should always be refreshed).  - `type[string]`: NGSI entity type. It has to be vehicle_types  - `version[string]`: GBFS version number to which the feed conforms, according to the versioning framework.  <!-- /30-PropertiesList -->  
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
vehicle_types:    
  description: Describes the types of vehicles that System operator has available for rent (added in v2.1-RC). According to the Standard GBFS 2.2    
  properties:    
    data:    
      description: 'Response data in the form of name:value pairs.'    
      properties:    
        vehicle_types:    
          description: Array that contains one object per vehicle type in the system as defined below.    
          if:    
            properties:    
              propulsion_type:    
                const:    
                  - electric    
                  - electric_assist    
                  - combustion    
          items:    
            properties:    
              form_factor:    
                description: The vehicle's general form factor.    
                enum:    
                  - bicycle    
                  - car    
                  - moped    
                  - other    
                  - scooter    
                type: string    
              max_range_meters:    
                description: The furthest distance in meters that the vehicle can travel without recharging or refueling when it has the maximum amount of energy potential.    
                minimum: 0    
                type: number    
              name:    
                description: The public name of this vehicle type.    
                type: string    
              propulsion_type:    
                description: The primary propulsion type of the vehicle.    
                enum:    
                  - human    
                  - electric_assist    
                  - electric    
                  - combustion    
                type: string    
              vehicle_type_id:    
                description: Unique identifier of a vehicle type.    
                type: string    
            required:    
              - vehicle_type_id    
              - form_factor    
              - propulsion_type    
            type: object    
          then:    
            properties:    
              max_range_meters:    
                required:    
                  - max_range_meters    
          type: array    
      required:    
        - vehicle_types    
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
      description: NGSI entity type. It has to be vehicle_types    
      enum:    
        - vehicle_types    
      type: string    
      x-ngsi:    
        type: Property    
    version:    
      description: 'GBFS version number to which the feed conforms, according to the versioning framework.'    
      enum:    
        - 2.1-RC    
        - 2.1    
        - 2.2    
        - 3.0-RC    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.GBFS/blob/master/vehicle_types/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.GBFS/vehicle_types/schema.json    
  x-model-tags: GBFS    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
#### vehicle_types NGSI-v2 key-values Example    
Here is an example of a vehicle_types in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:vehicle_types:id:FNNO:60592292",  
  "type": "vehicle_types",  
  "last_updated": 1609866247,  
  "ttl": 0,  
  "version": "3.0",  
  "data": {  
    "vehicle_types": [  
      {  
        "vehicle_type_id": "abc123",  
        "form_factor": "bicycle",  
        "propulsion_type": "human",  
        "name": "Example Basic Bike",  
        "default_reserve_time": 30,  
        "return_type": [  
          "any_station",  
          "free_floating"  
        ],  
        "vehicle_assets": {  
          "icon_url": "https://www.example.com/assets/icon_bicycle.svg",  
          "icon_url_dark": "https://www.example.com/assets/icon_bicycle_dark.svg",  
          "icon_last_modified": "2021-06-15"  
        },  
        "default_pricing_plan_id": "bike_plan_1",  
        "pricing_plan_ids": [  
          "bike_plan_1",  
          "bike_plan_2",  
          "bike_plan_3"  
        ]  
      },  
      {  
        "vehicle_type_id": "def456",  
        "form_factor": "scooter",  
        "propulsion_type": "electric",  
        "name": "Example E-scooter V2",  
        "default_reserve_time": 30,  
        "max_range_meters": 12345,  
        "return_type": [  
          "free_floating"  
        ],  
        "vehicle_assets": {  
          "icon_url": "https://www.example.com/assets/icon_escooter.svg",  
          "icon_url_dark": "https://www.example.com/assets/icon_escooter_dark.svg",  
          "icon_last_modified": "2021-06-15"  
        },  
        "default_pricing_plan_id": "scooter_plan_1"  
      },  
      {  
        "vehicle_type_id": "car1",  
        "form_factor": "car",  
        "propulsion_type": "combustion",  
        "name": "Four-door Sedan",  
        "default_reserve_time": 0,  
        "max_range_meters": 523992,  
        "return_type": [  
          "roundtrip_station"  
        ],  
        "vehicle_assets": {  
          "icon_url": "https://www.example.com/assets/icon_car.svg",  
          "icon_url_dark": "https://www.example.com/assets/icon_car_dark.svg",  
          "icon_last_modified": "2021-06-15"  
        },  
        "default_pricing_plan_id": "car_plan_1"  
      }  
    ]  
  }  
}  
```  
</details>  
#### vehicle_types NGSI-v2 normalized Example    
Here is an example of a vehicle_types in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:vehicle_types:id:FNNO:60592292",  
  "type": "vehicle_types",  
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
      "vehicle_types": [  
        {  
          "vehicle_type_id": "abc123",  
          "form_factor": "bicycle",  
          "propulsion_type": "human",  
          "name": "Example Basic Bike",  
          "default_reserve_time": 30,  
          "return_type": [  
            "any_station",  
            "free_floating"  
          ],  
          "vehicle_assets": {  
            "icon_url": "https://www.example.com/assets/icon_bicycle.svg",  
            "icon_url_dark": "https://www.example.com/assets/icon_bicycle_dark.svg",  
            "icon_last_modified": "2021-06-15"  
          },  
          "default_pricing_plan_id": "bike_plan_1",  
          "pricing_plan_ids": [  
            "bike_plan_1",  
            "bike_plan_2",  
            "bike_plan_3"  
          ]  
        },  
        {  
          "vehicle_type_id": "def456",  
          "form_factor": "scooter",  
          "propulsion_type": "electric",  
          "name": "Example E-scooter V2",  
          "default_reserve_time": 30,  
          "max_range_meters": 12345,  
          "return_type": [  
            "free_floating"  
          ],  
          "vehicle_assets": {  
            "icon_url": "https://www.example.com/assets/icon_escooter.svg",  
            "icon_url_dark": "https://www.example.com/assets/icon_escooter_dark.svg",  
            "icon_last_modified": "2021-06-15"  
          },  
          "default_pricing_plan_id": "scooter_plan_1"  
        },  
        {  
          "vehicle_type_id": "car1",  
          "form_factor": "car",  
          "propulsion_type": "combustion",  
          "name": "Four-door Sedan",  
          "default_reserve_time": 0,  
          "max_range_meters": 523992,  
          "return_type": [  
            "roundtrip_station"  
          ],  
          "vehicle_assets": {  
            "icon_url": "https://www.example.com/assets/icon_car.svg",  
            "icon_url_dark": "https://www.example.com/assets/icon_car_dark.svg",  
            "icon_last_modified": "2021-06-15"  
          },  
          "default_pricing_plan_id": "car_plan_1"  
        }  
      ]  
    }  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
</details>  
#### vehicle_types NGSI-LD key-values Example    
Here is an example of a vehicle_types in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:vehicle_types:id:FNNO:60592292",  
    "type": "vehicle_types",  
    "last_updated": 1609866247,  
    "ttl": 0,  
    "version": "3.0",  
    "data": {  
        "vehicle_types": [  
            {  
                "vehicle_type_id": "abc123",  
                "form_factor": "bicycle",  
                "propulsion_type": "human",  
                "name": "Example Basic Bike",  
                "default_reserve_time": 30,  
                "return_type": [  
                    "any_station",  
                    "free_floating"  
                ],  
                "vehicle_assets": {  
                    "icon_url": "https://www.example.com/assets/icon_bicycle.svg",  
                    "icon_url_dark": "https://www.example.com/assets/icon_bicycle_dark.svg",  
                    "icon_last_modified": "2021-06-15"  
                },  
                "default_pricing_plan_id": "bike_plan_1",  
                "pricing_plan_ids": [  
                    "bike_plan_1",  
                    "bike_plan_2",  
                    "bike_plan_3"  
                ]  
            },  
            {  
                "vehicle_type_id": "def456",  
                "form_factor": "scooter",  
                "propulsion_type": "electric",  
                "name": "Example E-scooter V2",  
                "default_reserve_time": 30,  
                "max_range_meters": 12345,  
                "return_type": [  
                    "free_floating"  
                ],  
                "vehicle_assets": {  
                    "icon_url": "https://www.example.com/assets/icon_escooter.svg",  
                    "icon_url_dark": "https://www.example.com/assets/icon_escooter_dark.svg",  
                    "icon_last_modified": "2021-06-15"  
                },  
                "default_pricing_plan_id": "scooter_plan_1"  
            },  
            {  
                "vehicle_type_id": "car1",  
                "form_factor": "car",  
                "propulsion_type": "combustion",  
                "name": "Four-door Sedan",  
                "default_reserve_time": 0,  
                "max_range_meters": 523992,  
                "return_type": [  
                    "roundtrip_station"  
                ],  
                "vehicle_assets": {  
                    "icon_url": "https://www.example.com/assets/icon_car.svg",  
                    "icon_url_dark": "https://www.example.com/assets/icon_car_dark.svg",  
                    "icon_last_modified": "2021-06-15"  
                },  
                "default_pricing_plan_id": "car_plan_1"  
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
#### vehicle_types NGSI-LD normalized Example    
Here is an example of a vehicle_types in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:vehicle_types:id:FNNO:60592292",  
    "type": "vehicle_types",  
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
            "vehicle_types": [  
                {  
                    "vehicle_type_id": "abc123",  
                    "form_factor": "bicycle",  
                    "propulsion_type": "human",  
                    "name": "Example Basic Bike",  
                    "default_reserve_time": 30,  
                    "return_type": [  
                        "any_station",  
                        "free_floating"  
                    ],  
                    "vehicle_assets": {  
                        "icon_url": "https://www.example.com/assets/icon_bicycle.svg",  
                        "icon_url_dark": "https://www.example.com/assets/icon_bicycle_dark.svg",  
                        "icon_last_modified": "2021-06-15"  
                    },  
                    "default_pricing_plan_id": "bike_plan_1",  
                    "pricing_plan_ids": [  
                        "bike_plan_1",  
                        "bike_plan_2",  
                        "bike_plan_3"  
                    ]  
                },  
                {  
                    "vehicle_type_id": "def456",  
                    "form_factor": "scooter",  
                    "propulsion_type": "electric",  
                    "name": "Example E-scooter V2",  
                    "default_reserve_time": 30,  
                    "max_range_meters": 12345,  
                    "return_type": [  
                        "free_floating"  
                    ],  
                    "vehicle_assets": {  
                        "icon_url": "https://www.example.com/assets/icon_escooter.svg",  
                        "icon_url_dark": "https://www.example.com/assets/icon_escooter_dark.svg",  
                        "icon_last_modified": "2021-06-15"  
                    },  
                    "default_pricing_plan_id": "scooter_plan_1"  
                },  
                {  
                    "vehicle_type_id": "car1",  
                    "form_factor": "car",  
                    "propulsion_type": "combustion",  
                    "name": "Four-door Sedan",  
                    "default_reserve_time": 0,  
                    "max_range_meters": 523992,  
                    "return_type": [  
                        "roundtrip_station"  
                    ],  
                    "vehicle_assets": {  
                        "icon_url": "https://www.example.com/assets/icon_car.svg",  
                        "icon_url_dark": "https://www.example.com/assets/icon_car_dark.svg",  
                        "icon_last_modified": "2021-06-15"  
                    },  
                    "default_pricing_plan_id": "car_plan_1"  
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
