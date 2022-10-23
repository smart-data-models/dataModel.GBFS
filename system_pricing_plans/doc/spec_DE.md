<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: system_pricing_plans  
=============================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.GBFS/blob/master/system_pricing_plans/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Beschreibt die Preisschemata des Systems. Gemäß dem Standard GBFS 2.2**  
Version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, liegt das daran, dass es mehrere Typen oder unterschiedliche Formate/Muster haben kann</sub></sup>.  
- `data[object]`: Array, das ein Objekt pro Plan wie unten definiert enthält.  - `id[*]`: Eindeutiger Bezeichner der Entität  - `last_updated[integer]`: Letzter Zeitpunkt der Aktualisierung der Daten im Feed in POSIX-Zeit.  - `ttl[integer]`: Anzahl der Sekunden, bevor die Daten im Feed erneut aktualisiert werden (0, wenn die Daten immer aufgefrischt werden sollen).  - `type[string]`: NGSI-Entitätstyp. Es muss system_pricing_plans sein.  - `version[string]`: GBFS-Versionsnummer, der der Feed gemäß dem Versionierungsrahmen entspricht (hinzugefügt in v1.1).  <!-- /30-PropertiesList -->  
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
system_pricing_plans:    
  description: 'Describes the pricing schemes of the system. According to the Standard GBFS 2.2'    
  properties:    
    data:    
      description: 'Array that contains one object per plan as defined below.'    
      properties:    
        plans:    
          items:    
            properties:    
              currency:    
                description: 'Currency used to pay the fare in ISO 4217 code.'    
                pattern: ^\w{3}$    
                type: string    
              description:    
                description: 'Customer-readable description of the pricing plan.'    
                type: string    
              is_taxable:    
                description: 'Will additional tax be added to the base price?'    
                type: boolean    
              name:    
                description: 'Name of this pricing plan.'    
                type: string    
              per_km_pricing:    
                dependencies:    
                  per_km_pricing:    
                    - start    
                    - rate    
                    - interval    
                description: 'Array of segments when the price is a function of distance travelled, displayed in kilometers (added in v2.1-RC2).'    
                items:    
                  properties:    
                    end:    
                      description: 'The kilometer at which the rate will no longer apply (added in v2.1-RC2).'    
                      minimum: 0    
                      type: number    
                    interval:    
                      description: 'Interval in kilometers at which the rate of this segment is either reapplied indefinitely, or if defined, up until (but not including) end kilometer (added in v2.1-RC2).'    
                      minimum: 0    
                      type: number    
                    rate:    
                      description: 'Rate that is charged for each kilometer interval after the start (added in v2.1-RC2).'    
                      type: number    
                    start:    
                      description: 'Number of kilometers that have to elapse before this segment starts applying (added in v2.1-RC2).'    
                      minimum: 0    
                      type: number    
                  type: object    
                type: array    
              per_min_pricing:    
                dependencies:    
                  per_min_pricing:    
                    - start    
                    - rate    
                    - interval    
                description: 'Array of segments when the price is a function of time travelled, displayed in minutes (added in v2.1-RC2).'    
                items:    
                  properties:    
                    end:    
                      description: 'The minute at which the rate will no longer apply (added in v2.1-RC2).'    
                      minimum: 0    
                      type: number    
                    interval:    
                      description: 'Interval in minutes at which the rate of this segment is either reapplied (added in v2.1-RC2).'    
                      minimum: 0    
                      type: number    
                    rate:    
                      description: 'Rate that is charged for each minute interval after the start (added in v2.1-RC2).'    
                      type: number    
                    start:    
                      description: 'Number of minutes that have to elapse before this segment starts applying (added in v2.1-RC2).'    
                      minimum: 0    
                      type: number    
                  type: object    
                type: array    
              plan_id:    
                description: 'Identifier of a pricing plan in the system.'    
                type: string    
              price:    
                description: 'Fare price.'    
                minimum: 0    
                type: number    
              surge_pricing:    
                description: 'Is there currently an increase in price in response to increased demand in this pricing plan? (added in v2.1-RC2)'    
                type: boolean    
              url:    
                description: 'URL where the customer can learn more about this pricing plan.'    
                format: uri    
                type: string    
            type: object    
          required:    
            - plan_id    
            - name    
            - currency    
            - price    
            - is_taxable    
            - description    
          type: array    
      required:    
        - plans    
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
      description: 'NGSI entity type. It has to be system_pricing_plans'    
      enum:    
        - system_pricing_plans    
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
    - last_updated    
    - ttl    
    - version    
    - data    
    - id    
    - type    
  type: object    
  x-derived-from: https://github.com/NABSA/gbfs/blob/v2.2/gbfs.md    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.GBFS/blob/master/system_pricing_plans/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.GBFS/system_pricing_plans/schema.json    
  x-model-tags: GBFS    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### system_pricing_plans NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für einen system_pricing_plans im JSON-LD Format als key-values. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:system_pricing_plans:id:FNNO:60592292",  
  "type": "system_pricing_plans",  
  "last_updated": 1609866247,  
  "ttl": 0,  
  "version": "3.0",  
  "data": {  
    "plans": [  
      {  
        "plan_id": "plan3",  
        "name": "Simple Rate",  
        "currency": "CAD",  
        "price": 3,  
        "is_taxable": true,  
        "description": "$3 unlock fee, $0.25 per kilometer and 0.50 per minute.",  
        "per_km_pricing": [  
          {  
            "start": 0,  
            "rate": 0.25,  
            "interval": 1  
          }  
        ],  
        "per_min_pricing": [  
          {  
            "start": 0,  
            "rate": 0.50,  
            "interval": 1  
          }  
        ]  
      }  
    ]  
  }  
}  
```  
</details>  
#### system_pricing_plans NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen system_pricing_plans im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:system_pricing_plans:id:FNNO:60592292",  
  "type": "system_pricing_plans",  
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
      "plans": [  
        {  
          "plan_id": "plan3",  
          "name": "Simple Rate",  
          "currency": "CAD",  
          "price": 3,  
          "is_taxable": true,  
          "description": "$3 unlock fee, $0.25 per kilometer and 0.50 per minute.",  
          "per_km_pricing": [  
            {  
              "start": 0,  
              "rate": 0.25,  
              "interval": 1  
            }  
          ],  
          "per_min_pricing": [  
            {  
              "start": 0,  
              "rate": 0.50,  
              "interval": 1  
            }  
          ]  
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
#### system_pricing_plans NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für einen system_pricing_plans im JSON-LD Format als key-values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:system_pricing_plans:id:FNNO:60592292",  
    "type": "system_pricing_plans",  
    "last_updated": 1609866247,  
    "ttl": 0,  
    "version": "3.0",  
    "data": {  
        "plans": [  
            {  
                "plan_id": "plan3",  
                "name": "Simple Rate",  
                "currency": "CAD",  
                "price": 3,  
                "is_taxable": true,  
                "description": "$3 unlock fee, $0.25 per kilometer and 0.50 per minute.",  
                "per_km_pricing": [  
                    {  
                        "start": 0,  
                        "rate": 0.25,  
                        "interval": 1  
                    }  
                ],  
                "per_min_pricing": [  
                    {  
                        "start": 0,  
                        "rate": 0.5,  
                        "interval": 1  
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
#### system_pricing_plans NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen system_pricing_plans im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:system_pricing_plans:id:FNNO:60592292",  
    "type": "system_pricing_plans",  
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
            "plans": [  
                {  
                    "plan_id": "plan3",  
                    "name": "Simple Rate",  
                    "currency": "CAD",  
                    "price": 3,  
                    "is_taxable": true,  
                    "description": "$3 unlock fee, $0.25 per kilometer and 0.50 per minute.",  
                    "per_km_pricing": [  
                        {  
                            "start": 0,  
                            "rate": 0.25,  
                            "interval": 1  
                        }  
                    ],  
                    "per_min_pricing": [  
                        {  
                            "start": 0,  
                            "rate": 0.5,  
                            "interval": 1  
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
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
