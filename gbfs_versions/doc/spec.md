<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: gbfs_versions  
=====================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.GBFS/blob/master/gbfs_versions/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **Lists all feed endpoints published according to version sof the GBFS documentation. (added in v1.1) According to the Standard GBFS 2.2**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `data[object]`: Response data in the form of name:value pairs.  - `id[*]`: Unique identifier of the entity  - `last_updated[integer]`: Last time the data in the feed was updated in POSIX time.  - `ttl[integer]`: Number of seconds before the data in the feed will be updated again (0 if the data should always be refreshed).  - `type[string]`: NGSI entity type. It has to be gbfs_versions  - `version[string]`: GBFS version number to which the feed conforms, according to the versioning framework.  <!-- /30-PropertiesList -->  
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
gbfs_versions:    
  description: 'Lists all feed endpoints published according to version sof the GBFS documentation. (added in v1.1) According to the Standard GBFS 2.2'    
  properties:    
    data:    
      additionalProperties: false    
      description: 'Response data in the form of name:value pairs.'    
      properties:    
        versions:    
          description: 'Contains one object, as defined below, for each of the available versions of a feed. The array must be sorted by increasing MAJOR and MINOR version number.'    
          items:    
            properties:    
              url:    
                description: 'URL of the corresponding gbfs.json endpoint'    
                format: uri    
                type: string    
              version:    
                description: 'The semantic version of the feed in the form X.Y'    
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
            required:    
              - version    
              - url    
            type: object    
          type: array    
      required:    
        - versions    
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
      description: 'NGSI entity type. It has to be gbfs_versions'    
      enum:    
        - gbfs_versions    
      type: string    
      x-ngsi:    
        type: Property    
    version:    
      description: 'GBFS version number to which the feed conforms, according to the versioning framework.'    
      enum:    
        - 1.1-RC    
        - 1.1    
        - 2.0-RC    
        - 2.0    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.GBFS/blob/master/gbfs_versions/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.GBFS/gbfs_versions/schema.json    
  x-model-tags: GBFS    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
#### gbfs_versions NGSI-v2 key-values Example    
Here is an example of a gbfs_versions in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:gbfs_versions:id:BZXQ:05985472",  
  "type": "gbfs_versions",  
  "last_updated": 1450156427,  
  "ttl": 576,  
  "version": "2.0",  
  "data": {  
    "versions": [  
      {  
        "version": "3.0-RC",  
        "url": "urn:ngsi-ld:gbfs_versions:url:OOKT:50451777"  
      },  
      {  
        "version": "1.1-RC",  
        "url": "urn:ngsi-ld:gbfs_versions:url:ZPWS:72960398"  
      }  
    ]  
  }  
}  
```  
</details>  
#### gbfs_versions NGSI-v2 normalized Example    
Here is an example of a gbfs_versions in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:gbfs_versions:id:BZXQ:05985472",  
  "type": "gbfs_versions",  
  "last_updated": {  
    "type": "Number",  
    "value": 1450156427  
  },  
  "ttl": {  
    "type": "Number",  
    "value": 576  
  },  
  "version": {  
    "type": "Text",  
    "value": "2.0"  
  },  
  "data": {  
    "type": "StructuredValue",  
    "value": {  
      "versions": [  
        {  
          "version": "3.0-RC",  
          "url": "urn:ngsi-ld:gbfs_versions:url:OOKT:50451777"  
        },  
        {  
          "version": "1.1-RC",  
          "url": "urn:ngsi-ld:gbfs_versions:url:ZPWS:72960398"  
        }  
      ]  
    }  
  }  
}  
```  
</details>  
#### gbfs_versions NGSI-LD key-values Example    
Here is an example of a gbfs_versions in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:gbfs_versions:id:BZXQ:05985472",  
    "type": "gbfs_versions",  
    "last_updated": 1450156427,  
    "ttl": 576,  
    "version": "2.0",  
    "data": {  
        "versions": [  
            {  
                "version": "3.0-RC",  
                "url": "urn:ngsi-ld:gbfs_versions:url:OOKT:50451777"  
            },  
            {  
                "version": "1.1-RC",  
                "url": "urn:ngsi-ld:gbfs_versions:url:ZPWS:72960398"  
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
#### gbfs_versions NGSI-LD normalized Example    
Here is an example of a gbfs_versions in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:gbfs_versions:id:BZXQ:05985472",  
    "type": "gbfs_versions",  
    "last_updated": {  
        "type": "Property",  
        "value": 1450156427  
    },  
    "ttl": {  
        "type": "Property",  
        "value": 576  
    },  
    "version": {  
        "type": "Property",  
        "value": "2.0"  
    },  
    "data": {  
        "type": "Property",  
        "value": {  
            "versions": [  
                {  
                    "version": "3.0-RC",  
                    "url": "urn:ngsi-ld:gbfs_versions:url:OOKT:50451777"  
                },  
                {  
                    "version": "1.1-RC",  
                    "url": "urn:ngsi-ld:gbfs_versions:url:ZPWS:72960398"  
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
