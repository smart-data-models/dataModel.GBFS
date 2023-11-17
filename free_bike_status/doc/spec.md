<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entity: free_bike_status    
========================<!-- /10-Header -->    
<!-- 15-License -->    
[Open License](https://github.com/smart-data-models//dataModel.GBFS/blob/master/free_bike_status/LICENSE.md)    
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Global description: **Describes the vehicles that are available for rent (as of v2.1-RC2). According to the Standard GBFS 2.2**    
version: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## List of properties    
<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>    
- `data[object]`: Array that contains one object per bike as defined below.  	    
- `id[*]`: Unique identifier of the entity  - `last_updated[integer]`: Last time the data in the feed was updated in POSIX time.  - `ttl[integer]`: Number of seconds before the data in the feed will be updated again (0 if the data should always be refreshed).  - `type[string]`: NGSI entity type. It has to be free_bike_status  - `version[string]`: GBFS version number to which the feed conforms, according to the versioning framework (added in v1.1).  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Required properties    
- `id`  - `last_updated`  - `type`  <!-- /35-RequiredProperties -->    
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
free_bike_status:      
  description: Describes the vehicles that are available for rent (as of v2.1-RC2). According to the Standard GBFS 2.2      
  properties:      
    data:      
      description: Array that contains one object per bike as defined below.      
      properties:      
        bikes:      
          items:      
            properties:      
              bike_id:      
                description: Rotating (as of v2.0) identifier of a vehicle.      
                type: string      
              current_range_meters:      
                description: The furthest distance in meters that the vehicle can travel without recharging or refueling with the vehicle's current charge or fuel (added in v2.1-RC).      
                minimum: 0      
                type: number      
              is_disabled:      
                description: 'Is the vehicle currently disabled (broken)?'      
                type: boolean      
              is_reserved:      
                description: 'Is the vehicle currently reserved?'      
                type: boolean      
              last_reported:      
                description: The last time this vehicle reported its status to the operator's backend in POSIX time (added in v2.1-RC).      
                minimum: 1450155600      
                type: number      
              lat:      
                description: The latitude of the vehicle.      
                maximum: 90      
                minimum: -90      
                type: number      
              lon:      
                description: The longitude of the vehicle.      
                maximum: 180      
                minimum: -180      
                type: number      
              pricing_plan_id:      
                description: The plan_id of the pricing plan this vehicle is eligible for (added in v2.1-RC2).      
                type: string      
              rental_uris:      
                description: 'Contains rental uris for Android, iOS, and web in the android, ios, and web fields (added in v1.1).'      
                properties:      
                  android:      
                    description: URI that can be passed to an Android app with an intent (added in v1.1).      
                    format: uri      
                    type: string      
                  ios:      
                    description: URI that can be used on iOS to launch the rental app for this vehicle (added in v1.1).      
                    format: uri      
                    type: string      
                  web:      
                    description: URL that can be used by a web browser to show more information about renting this vehicle (added in v1.1).      
                    format: uri      
                    type: string      
                type: object      
              station_id:      
                description: Identifier referencing the station_id if the vehicle is currently at a station (added in v2.1-RC2).      
                type: string      
              vehicle_type_id:      
                description: The vehicle_type_id of this vehicle (added in v2.1-RC).      
                type: string      
            required:      
              - bike_id      
              - is_reserved      
              - is_disabled      
            type: object      
          required:      
            - bikes      
          type: array      
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
      description: NGSI entity type. It has to be free_bike_status      
      enum:      
        - free_bike_status      
      type: string      
      x-ngsi:      
        type: Property      
    version:      
      description: 'GBFS version number to which the feed conforms, according to the versioning framework (added in v1.1).'      
      enum:      
        - 2.2      
        - 3.0-RC      
        - 3.0      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - last_updated      
    - type      
  type: object      
  x-derived-from: https://github.com/NABSA/gbfs/blob/v2.2/gbfs.md      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.GBFS/blob/master/free_bike_status/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.GBFS/free_bike_status/schema.json      
  x-model-tags: GBFS      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Example payloads      
#### free_bike_status NGSI-v2 key-values Example      
Here is an example of a free_bike_status in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:free_bike_status:id:ZMAW:94046191",  
  "type": "free_bike_status",  
  "last_updated": 1450156464,  
  "ttl": 864,  
  "version": "3.0-RC",  
  "data": {  
    "bikes": [  
      {  
        "bike_id": "bike:001:0023",  
        "lat": 9.6,  
        "lon": 18.6,  
        "is_reserved": true,  
        "is_disabled": false,  
        "rental_uris": {  
          "android": "urn:ngsi-ld:free_bike_status:android:DDCU:76475938",  
          "ios": "urn:ngsi-ld:free_bike_status:ios:OJIQ:89241157",  
          "web": "urn:ngsi-ld:free_bike_status:web:XCVS:38778408"  
        },  
        "vehicle_type_id": "regular bike",  
        "last_reported": 1450156464,  
        "current_range_meters": 864.6,  
        "station_id": "Madrid puerta del sol",  
        "pricing_plan_id": "Tourist 1 day"  
      },  
      {  
        "bike_id": "bike:001:0024",  
        "lat": 9.6,  
        "lon": 18.6,  
        "is_reserved": true,  
        "is_disabled": false,  
        "rental_uris": {  
          "android": "urn:ngsi-ld:free_bike_status:android:DDCU:76475938",  
          "ios": "urn:ngsi-ld:free_bike_status:ios:OJIQ:89241157",  
          "web": "urn:ngsi-ld:free_bike_status:web:XCVS:38778408"  
        },  
        "vehicle_type_id": "regular bike",  
        "last_reported": 1450156464,  
        "current_range_meters": 864.6,  
        "station_id": "Madrid puerta del sol",  
        "pricing_plan_id": "Tourist 1 day"  
      }  
    ]  
  }  
}  
```  
</details>    
#### free_bike_status NGSI-v2 normalized Example      
Here is an example of a free_bike_status in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:free_bike_status:id:ZMAW:94046191",  
  "type": "free_bike_status",  
  "last_updated": {  
    "type": "Number",  
    "value": 1450156464  
  },  
  "ttl": {  
    "type": "Number",  
    "value": 864  
  },  
  "version": {  
    "type": "Text",  
    "value": "3.0-RC"  
  },  
  "data": {  
    "type": "StructuredValue",  
    "value": {  
      "bikes": [  
        {  
          "bike_id": "bike:001:0023",  
          "lat": 9.6,  
          "lon": 18.6,  
          "is_reserved": true,  
          "is_disabled": false,  
          "rental_uris": {  
            "android": "urn:ngsi-ld:free_bike_status:android:DDCU:76475938",  
            "ios": "urn:ngsi-ld:free_bike_status:ios:OJIQ:89241157",  
            "web": "urn:ngsi-ld:free_bike_status:web:XCVS:38778408"  
          },  
          "vehicle_type_id": "regular bike",  
          "last_reported": 1450156464,  
          "current_range_meters": 864.6,  
          "station_id": "Madrid puerta del sol",  
          "pricing_plan_id": "Tourist 1 day"  
        },  
        {  
          "bike_id": "bike:001:0024",  
          "lat": 9.6,  
          "lon": 18.6,  
          "is_reserved": true,  
          "is_disabled": false,  
          "rental_uris": {  
            "android": "urn:ngsi-ld:free_bike_status:android:DDCU:76475938",  
            "ios": "urn:ngsi-ld:free_bike_status:ios:OJIQ:89241157",  
            "web": "urn:ngsi-ld:free_bike_status:web:XCVS:38778408"  
          },  
          "vehicle_type_id": "regular bike",  
          "last_reported": 1450156464,  
          "current_range_meters": 864.6,  
          "station_id": "Madrid puerta del sol",  
          "pricing_plan_id": "Tourist 1 day"  
        }  
      ]  
    }  
  }  
}  
```  
</details>    
#### free_bike_status NGSI-LD key-values Example      
Here is an example of a free_bike_status in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:free_bike_status:id:ZMAW:94046191",  
  "type": "free_bike_status",  
  "last_updated": 1450156464,  
  "ttl": 864,  
  "version": "3.0-RC",  
  "data": {  
    "bikes": [  
      {  
        "bike_id": "bike:001:0023",  
        "lat": 9.6,  
        "lon": 18.6,  
        "is_reserved": true,  
        "is_disabled": false,  
        "rental_uris": {  
          "android": "urn:ngsi-ld:free_bike_status:android:DDCU:76475938",  
          "ios": "urn:ngsi-ld:free_bike_status:ios:OJIQ:89241157",  
          "web": "urn:ngsi-ld:free_bike_status:web:XCVS:38778408"  
        },  
        "vehicle_type_id": "regular bike",  
        "last_reported": 1450156464,  
        "current_range_meters": 864.6,  
        "station_id": "Madrid puerta del sol",  
        "pricing_plan_id": "Tourist 1 day"  
      },  
      {  
        "bike_id": "bike:001:0024",  
        "lat": 9.6,  
        "lon": 18.6,  
        "is_reserved": true,  
        "is_disabled": false,  
        "rental_uris": {  
          "android": "urn:ngsi-ld:free_bike_status:android:DDCU:76475938",  
          "ios": "urn:ngsi-ld:free_bike_status:ios:OJIQ:89241157",  
          "web": "urn:ngsi-ld:free_bike_status:web:XCVS:38778408"  
        },  
        "vehicle_type_id": "regular bike",  
        "last_reported": 1450156464,  
        "current_range_meters": 864.6,  
        "station_id": "Madrid puerta del sol",  
        "pricing_plan_id": "Tourist 1 day"  
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
#### free_bike_status NGSI-LD normalized Example      
Here is an example of a free_bike_status in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:free_bike_status:id:ZMAW:94046191",  
    "type": "free_bike_status",  
    "last_updated": {  
        "type": "Property",  
        "value": 1450156464  
    },  
    "ttl": {  
        "type": "Property",  
        "value": 864  
    },  
    "version": {  
        "type": "Property",  
        "value": "3.0-RC"  
    },  
    "data": {  
        "type": "Property",  
        "value": {  
            "bikes": [  
                {  
                    "bike_id": "bike:001:0023",  
                    "lat": 9.6,  
                    "lon": 18.6,  
                    "is_reserved": true,  
                    "is_disabled": false,  
                    "rental_uris": {  
                        "android": "urn:ngsi-ld:free_bike_status:android:DDCU:76475938",  
                        "ios": "urn:ngsi-ld:free_bike_status:ios:OJIQ:89241157",  
                        "web": "urn:ngsi-ld:free_bike_status:web:XCVS:38778408"  
                    },  
                    "vehicle_type_id": "regular bike",  
                    "last_reported": 1450156464,  
                    "current_range_meters": 864.6,  
                    "station_id": "Madrid puerta del sol",  
                    "pricing_plan_id": "Tourist 1 day"  
                },  
                {  
                    "bike_id": "bike:001:0024",  
                    "lat": 9.6,  
                    "lon": 18.6,  
                    "is_reserved": true,  
                    "is_disabled": false,  
                    "rental_uris": {  
                        "android": "urn:ngsi-ld:free_bike_status:android:DDCU:76475938",  
                        "ios": "urn:ngsi-ld:free_bike_status:ios:OJIQ:89241157",  
                        "web": "urn:ngsi-ld:free_bike_status:web:XCVS:38778408"  
                    },  
                    "vehicle_type_id": "regular bike",  
                    "last_reported": 1450156464,  
                    "current_range_meters": 864.6,  
                    "station_id": "Madrid puerta del sol",  
                    "pricing_plan_id": "Tourist 1 day"  
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
