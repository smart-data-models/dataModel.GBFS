<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entität: system_calendar    
========================<!-- /10-Header -->    
<!-- 15-License -->    
[Offene Lizenz](https://github.com/smart-data-models//dataModel.GBFS/blob/master/system_calendar/LICENSE.md)    
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Globale Beschreibung: **Beschreibt den Betriebskalender für ein System. Gemäß dem Standard GBFS 2.2**    
Version: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste der Eigenschaften    
<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.    
- `data[object]`: Array, das Operationskalender für das System enthält.  	    
- `id[*]`: Eindeutiger Bezeichner der Entität  - `last_updated[integer]`: Letzter Zeitpunkt der Aktualisierung der Daten im Feed in POSIX-Zeit.  - `ttl[integer]`: Anzahl der Sekunden, bevor die Daten im Feed erneut aktualisiert werden (0, wenn die Daten immer aufgefrischt werden sollen).  - `type[string]`: NGSI-Entitätstyp. Es muss system_calendar sein.  - `version[string]`: GBFS-Versionsnummer, der der Feed gemäß dem Versionierungsrahmen entspricht (hinzugefügt in v1.1).  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Erforderliche Eigenschaften    
- `data`  - `id`  - `last_updated`  - `ttl`  - `type`  - `version`  <!-- /35-RequiredProperties -->    
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
system_calendar:      
  description: Describes the operating calendar for a system. According to the Standard GBFS 2.2      
  properties:      
    data:      
      description: Array that contains opertions calendar for the system.      
      properties:      
        calendars:      
          items:      
            properties:      
              end_day:      
                description: End day for the system operations.      
                maximum: 31      
                minimum: 1      
                type: number      
              end_month:      
                description: End month for the system operations.      
                maximum: 12      
                minimum: 1      
                type: number      
              end_year:      
                description: End year for the system operations.      
                pattern: ^\d{4}$      
                type: number      
              start_day:      
                description: Starting day for the system operations.      
                maximum: 31      
                minimum: 1      
                type: number      
              start_month:      
                description: Starting month for the system operations.      
                maximum: 12      
                minimum: 1      
                type: number      
              start_year:      
                description: Starting year for the system operations.      
                pattern: ^\d{4}$      
                type: number      
            required:      
              - start_month      
              - start_day      
              - end_month      
              - end_day      
            type: object      
          type: array      
      required:      
        - calendars      
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
      description: NGSI entity type. It has to be system_calendar      
      enum:      
        - system_calendar      
      type: string      
      x-ngsi:      
        type: Property      
    version:      
      description: 'GBFS version number to which the feed conforms, according to the versioning framework (added in v1.1).'      
      enum:      
        - 1.1-RC      
        - 1.1      
        - 2.0-RC      
        - 2.0      
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
    - last_updated      
    - ttl      
    - version      
    - data      
    - id      
    - type      
  type: object      
  x-derived-from: https://github.com/NABSA/gbfs/blob/v2.2/gbfs.md      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.GBFS/blob/master/system_calendar/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.GBFS/system_calendar/schema.json      
  x-model-tags: GBFS      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Beispiel-Nutzlasten    
#### system_calendar NGSI-v2 key-values Beispiel    
Hier ist ein Beispiel für einen system_calendar im JSON-LD Format als key-values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:system_calendar:id:FNNO:60592292",  
  "type": "system_calendar",  
  "last_updated": 1604333830,  
  "ttl": 86400,  
  "version": "3.0",  
  "data": {  
    "calendars": [  
      {  
        "start_month": 4,  
        "start_day": 1,  
        "start_year": 2020,  
        "end_month": 11,  
        "end_day": 5,  
        "end_year": 2020  
      }  
    ]  
  }  
}  
```  
</details>    
#### system_calendar NGSI-v2 normalized Beispiel    
Hier ist ein Beispiel für einen system_calendar im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:system_calendar:id:FNNO:60592292",  
  "type": "system_calendar",  
  "last_updated": {  
    "type": "Number",  
    "value": 1604333830  
  },  
  "ttl": {  
    "type": "Number",  
    "value": 86400  
  },  
  "version": {  
    "type": "Text",  
    "value": "3.0"  
  },  
  "data": {  
    "type": "StructuredValue",  
    "value": {  
      "calendars": [  
        {  
          "start_month": 4,  
          "start_day": 1,  
          "start_year": 2020,  
          "end_month": 11,  
          "end_day": 5,  
          "end_year": 2020  
        }  
      ]  
    }  
  }  
}  
```  
</details>    
#### system_calendar NGSI-LD key-values Beispiel    
Hier ist ein Beispiel für einen system_calendar im JSON-LD Format als key-values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:system_calendar:id:FNNO:60592292",  
  "type": "system_calendar",  
  "last_updated": 1604333830,  
  "ttl": 86400,  
  "version": "3.0",  
  "data": {  
    "calendars": [  
      {  
        "start_month": 4,  
        "start_day": 1,  
        "start_year": 2020,  
        "end_month": 11,  
        "end_day": 5,  
        "end_year": 2020  
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
#### system_calendar NGSI-LD normalized Beispiel    
Hier ist ein Beispiel für einen system_calendar im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:system_calendar:id:FNNO:60592292",  
    "type": "system_calendar",  
    "last_updated": {  
        "type": "Property",  
        "value": 1604333830  
    },  
    "ttl": {  
        "type": "Property",  
        "value": 86400  
    },  
    "version": {  
        "type": "Property",  
        "value": "3.0"  
    },  
    "data": {  
        "type": "Property",  
        "value": {  
            "calendars": [  
                {  
                    "start_month": 4,  
                    "start_day": 1,  
                    "start_year": 2020,  
                    "end_month": 11,  
                    "end_day": 5,  
                    "end_year": 2020  
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
