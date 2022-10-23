<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : gbfs  
=============<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.GBFS/blob/master/gbfs/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Fichier de découverte automatique qui renvoie à tous les autres fichiers publiés par le système. Selon la norme GBFS 2.2**  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il pourrait avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `data[object]`: Données de réponse sous la forme de paires nom:valeur.  - `id[*]`: Identifiant unique de l'entité  - `last_updated[integer]`: Dernière fois que les données du flux ont été mises à jour en temps POSIX.  - `ttl[integer]`: Nombre de secondes avant que les données du flux ne soient à nouveau mises à jour (0 si les données doivent toujours être rafraîchies).  - `type[string]`: Type d'entité NGSI. Il doit être gbfs  - `version[string]`: Numéro de version du GBFS auquel le flux est conforme, selon le cadre de versionnage (ajouté dans la v1.1).  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `data`  - `id`  - `last_updated`  - `ttl`  - `type`  - `version`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Cartographie de la norme [GBFS 2.2] (https://github.com/NABSA/gbfs/blob/v2.2/gbfs.md)  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
gbfs:    
  description: 'Auto-discovery file that links to all of the other files published by the system. According to the Standard GBFS 2.2'    
  properties:    
    data:    
      description: 'Response data in the form of name:value pairs.'    
      patternProperties:    
        ^[a-z]{2,3}(-[A-Z]{2})?$:    
          properties:    
            feeds:    
              description: 'An array of all of the feeds that are published by the auto-discovery file. Each element in the array is an object with the keys below.'    
              items:    
                properties:    
                  name:    
                    description: 'Key identifying the type of feed this is. The key must be the base file name defined in the spec for the corresponding feed type.'    
                    enum:    
                      - gbfs    
                      - gbfs_versions    
                      - system_information    
                      - vehicle_types    
                      - station_information    
                      - station_status    
                      - free_bike_status    
                      - system_hours    
                      - system_alerts    
                      - system_calendar    
                      - system_regions    
                      - system_pricing_plans    
                      - geofencing_zones    
                    type: string    
                  url:    
                    description: 'URL for the feed.'    
                    format: uri    
                    type: string    
                required:    
                  - name    
                  - url    
                type: object    
              type: array    
          type: object    
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
      description: 'NGSI entity type. It has to be gbfs'    
      enum:    
        - gbfs    
      type: string    
      x-ngsi:    
        type: Property    
    version:    
      description: 'GBFS version number to which the feed conforms, according to the versioning framework (added in v1.1).'    
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
    - data    
    - id    
    - last_updated    
    - ttl    
    - type    
    - version    
  type: object    
  x-derived-from: https://github.com/NABSA/gbfs/blob/v2.2/gbfs.md    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.GBFS/blob/master/gbfs/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.GBFS/gbfs/schema.json    
  x-model-tags: GBFS    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### gbfs NGSI-v2 key-values Exemple  
Voici un exemple d'un gbfs au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 en utilisant `options=keyValues` et retourne les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:gbfs:id:UKBQ:60920452",  
  "type": "gbfs",  
  "last_updated": 1450156395,  
  "ttl": 566,  
  "version": "2.1",  
  "data": {  
    "feeds": [  
      {  
        "name": "station_information",  
        "url": "urn:ngsi-ld:gbfs:url:EPHA:59077032"  
      },  
      {  
        "name": "system_hours",  
        "url": "urn:ngsi-ld:gbfs:url:GDPS:83970346"  
      }  
    ]  
  }  
}  
```  
</details>  
#### gbfs NGSI-v2 normalisé Exemple  
Voici un exemple d'un gbfs au format JSON-LD tel que normalisé. Ceci est compatible avec NGSI-v2 lorsqu'on n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:gbfs:id:UKBQ:60920452",  
  "type": "gbfs",  
  "last_updated": {  
    "type": "Number",  
    "value": 1450156395  
  },  
  "ttl": {  
    "type": "Number",  
    "value": 566  
  },  
  "version": {  
    "type": "Text",  
    "value": "2.1"  
  },  
  "data": {  
    "type": "StructuredValue",  
    "value": {  
      "feeds": [  
        {  
          "name": "station_information",  
          "url": "urn:ngsi-ld:gbfs:url:EPHA:59077032"  
        },  
        {  
          "name": "system_hours",  
          "url": "urn:ngsi-ld:gbfs:url:GDPS:83970346"  
        }  
      ]  
    }  
  }  
}  
```  
</details>  
#### gbfs NGSI-LD key-values Exemple  
Voici un exemple d'un gbfs au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:gbfs:id:UKBQ:60920452",  
    "type": "gbfs",  
    "last_updated": 1450156395,  
    "ttl": 566,  
    "version": "2.1",  
    "data": {  
        "feeds": [  
            {  
                "name": "station_information",  
                "url": "urn:ngsi-ld:gbfs:url:EPHA:59077032"  
            },  
            {  
                "name": "system_hours",  
                "url": "urn:ngsi-ld:gbfs:url:GDPS:83970346"  
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
#### gbfs NGSI-LD normalisé Exemple  
Voici un exemple d'un gbfs au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:gbfs:id:UKBQ:60920452",  
    "type": "gbfs",  
    "last_updated": {  
        "type": "Property",  
        "value": 1450156395  
    },  
    "ttl": {  
        "type": "Property",  
        "value": 566  
    },  
    "version": {  
        "type": "Property",  
        "value": "2.1"  
    },  
    "data": {  
        "type": "Property",  
        "value": {  
            "feeds": [  
                {  
                    "name": "station_information",  
                    "url": "urn:ngsi-ld:gbfs:url:EPHA:59077032"  
                },  
                {  
                    "name": "system_hours",  
                    "url": "urn:ngsi-ld:gbfs:url:GDPS:83970346"  
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
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
