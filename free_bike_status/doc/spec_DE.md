<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entität: free_bike_status    
=========================<!-- /10-Header -->    
<!-- 15-License -->    
[Offene Lizenz](https://github.com/smart-data-models//dataModel.GBFS/blob/master/free_bike_status/LICENSE.md)    
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Globale Beschreibung: **Beschreibt die Fahrzeuge, die zur Vermietung zur Verfügung stehen (ab v2.1-RC2). Gemäß dem Standard GBFS 2.2**    
Version: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste der Eigenschaften    
<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.    
- `data[object]`: Array, das ein Objekt pro Fahrrad enthält, wie unten definiert.  	    
- `id[*]`: Eindeutiger Bezeichner der Entität  - `last_updated[integer]`: Letzter Zeitpunkt der Aktualisierung der Daten im Feed in POSIX-Zeit.  - `ttl[integer]`: Anzahl der Sekunden, bevor die Daten im Feed erneut aktualisiert werden (0, wenn die Daten immer aufgefrischt werden sollen).  - `type[string]`: NGSI-Entitätstyp. Er muss free_bike_status sein.  - `version[string]`: GBFS-Versionsnummer, der der Feed gemäß dem Versionierungsrahmen entspricht (hinzugefügt in v1.1).  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Erforderliche Eigenschaften    
- `id`  - `last_updated`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
Abbildung der Norm [GBFS 2.2](https://github.com/NABSA/gbfs/blob/v2.2/gbfs.md)    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Datenmodell Beschreibung der Eigenschaften    
Alphabetisch sortiert (für Details anklicken)    
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
## Beispiel-Nutzlasten    
#### free_bike_status NGSI-v2 key-values Beispiel    
Hier ist ein Beispiel für einen free_bike_status im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
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
#### free_bike_status NGSI-v2 normalisiert Beispiel    
Hier ist ein Beispiel für einen free_bike_status im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
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
#### free_bike_status NGSI-LD key-values Beispiel    
Hier ist ein Beispiel für einen free_bike_status im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
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
#### free_bike_status NGSI-LD normalisiert Beispiel    
Hier ist ein Beispiel für einen free_bike_status im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
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
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
