Entity: vehicle_types  
=====================  
[Open License](https://github.com/smart-data-models//dataModel.GBFS/blob/master/vehicle_types/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Global description: **Describes the types of vehicles that System operator has available for rent (added in v2.1-RC). According to the Standard GBFS 2.2**  
version: 0.0.1  

## List of properties  

- `data`: Response data in the form of name:value pairs.  - `id`: Unique identifier of the entity  - `last_updated`: Last time the data in the feed was updated in POSIX time.  - `ttl`: Number of seconds before the data in the feed will be updated again (0 if the data should always be refreshed).  - `type`: NGSI entity type. It has to be vehicle_types  - `version`: GBFS version number to which the feed conforms, according to the versioning framework.    
Required properties  
- `data`  - `id`  - `last_updated`  - `ttl`  - `type`  - `version`    
Mapping of the Standard [GBFS 2.2](https://github.com/NABSA/gbfs/blob/v2.2/gbfs.md)  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
vehicle_types:    
  description: 'Describes the types of vehicles that System operator has available for rent (added in v2.1-RC). According to the Standard GBFS 2.2'    
  properties:    
    data:    
      description: 'Response data in the form of name:value pairs.'    
      properties:    
        vehicle_types:    
          description: 'Array that contains one object per vehicle type in the system as defined below.'    
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
                description: 'The vehicle''s general form factor.'    
                enum:    
                  - bicycle    
                  - car    
                  - moped    
                  - other    
                  - scooter    
                type: string    
              max_range_meters:    
                description: 'The furthest distance in meters that the vehicle can travel without recharging or refueling when it has the maximum amount of energy potential.'    
                minimum: 0    
                type: number    
              name:    
                description: 'The public name of this vehicle type.'    
                type: string    
              propulsion_type:    
                description: 'The primary propulsion type of the vehicle.'    
                enum:    
                  - human    
                  - electric_assist    
                  - electric    
                  - combustion    
                type: string    
              vehicle_type_id:    
                description: 'Unique identifier of a vehicle type.'    
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
      description: 'NGSI entity type. It has to be vehicle_types'    
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
  version: 0.0.1    
```  
</details>    
## Example payloads    
#### vehicle_types NGSI-v2 key-values Example    
Here is an example of a vehicle_types in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### vehicle_types NGSI-v2 normalized Example    
Here is an example of a vehicle_types in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
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
#### vehicle_types NGSI-LD key-values Example    
Here is an example of a vehicle_types in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
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
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### vehicle_types NGSI-LD normalized Example    
Here is an example of a vehicle_types in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
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
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units