<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entité : station_information    
============================<!-- /10-Header -->    
<!-- 15-License -->    
[Licence ouverte] (https://github.com/smart-data-models//dataModel.GBFS/blob/master/station_information/LICENSE.md)    
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Description globale : **Détails comprenant l'opérateur du système, l'emplacement du système, l'année de mise en œuvre, l'URL, les informations de contact, le fuseau horaire. Selon la norme GBFS 2.2**    
version : 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste des propriétés    
<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il pourrait avoir plusieurs types ou différents formats/modèles</sub></sup>.    
- `data[object]`: Tableau qui contient un objet par station comme défini ci-dessous.  - `id[*]`: Identifiant unique de l'entité  - `last_updated[integer]`: Dernière fois que les données du flux ont été mises à jour en temps POSIX.  - `ttl[integer]`: Nombre de secondes avant que les données du flux ne soient à nouveau mises à jour (0 si les données doivent toujours être rafraîchies).  - `type[string]`: Type d'entité NGSI. Il doit s'agir de station_information  - `version[string]`: Numéro de version du GBFS auquel le flux est conforme, selon le cadre de versionnage (ajouté dans la v1.1).  <!-- /30-PropertiesList -->    
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
station_information:      
  description: 'Details including system operator, system location, year implemented, URL, contact info, time zone. According to the Standard GBFS 2.2'      
  properties:      
    data:      
      description: 'Array that contains one object per station as defined below.'      
      properties:      
        stations:      
          items:      
            properties:      
              address:      
                description: 'Address where station is located.'      
                type: string      
              capacity:      
                description: 'Number of total docking points installed at this station, both available and unavailable.'      
                minimum: 0      
                type: number      
              cross_street:      
                description: 'Cross street or landmark where the station is located.'      
                type: string      
              is_valet_station:      
                description: 'Are valet services provided at this station? (added in v2.1-RC)'      
                type: boolean      
              is_virtual_station:      
                description: 'Is this station a location with or without physical infrastructure? (added in v2.1-RC)'      
                type: boolean      
              lat:      
                description: 'The latitude of the station.'      
                maximum: 90      
                minimum: -90      
                type: number      
              lon:      
                description: 'The longitude fo the station.'      
                maximum: 180      
                minimum: -180      
                type: number      
              name:      
                description: 'Public name of the station.'      
                type: string      
              post_code:      
                description: 'Postal code where station is located.'      
                type: string      
              region_id:      
                description: 'Identifier of the region where the station is located.'      
                type: string      
              rental_methods:      
                description: 'Payment methods accepted at this station.'      
                items:      
                  enum:      
                    - key      
                    - creditcard      
                    - paypass      
                    - applepay      
                    - androidpay      
                    - transitcard      
                    - accountnumber      
                    - phone      
                  type: string      
                minItems: 1      
                type: array      
              rental_uris:      
                description: 'Contains rental uris for Android, iOS, and web in the android, ios, and web fields (added in v1.1).'      
                properties:      
                  android:      
                    description: 'URI that can be passed to an Android app with an intent (added in v1.1).'      
                    format: uri      
                    type: string      
                  ios:      
                    description: 'URI that can be used on iOS to launch the rental app for this station (added in v1.1).'      
                    format: uri      
                    type: string      
                  web:      
                    description: 'URL that can be used by a web browser to show more information about renting a vehicle at this station (added in v1.1).'      
                    format: uri      
                    type: string      
                type: object      
              short_name:      
                description: 'Short name or other type of identifier.'      
                type: string      
              station_area:      
                description: 'A multipolygon that describes the area of a virtual station (added in v2.1-RC).'      
                properties:      
                  coordinates:      
                    items:      
                      items:      
                        items:      
                          items:      
                            type: number      
                          minItems: 2      
                          type: array      
                        minItems: 4      
                        type: array      
                      type: array      
                    type: array      
                  type:      
                    enum:      
                      - Multipolygon      
                    type: string      
                required:      
                  - type      
                  - coordinates      
                type: object      
              station_id:      
                description: 'Identifier of a station.'      
                type: string      
              vehicle_capacity:      
                additionalProperties:      
                  type: number      
                description: 'An object where each key is a vehicle_type_id and the value is a number presenting the total number of vehicles of this type that can park within the station_area (added in v2.1-RC).'      
                type: object      
              vehicle_type_capacity:      
                additionalProperties:      
                  type: number      
                description: 'An object where each key is a vehicle_type_id and the value is a number representing the total docking points installed at this station for each vehicle type (added in v2.1-RC).'      
                type: object      
            required:      
              - station_id      
              - name      
              - lat      
              - lon      
            type: object      
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
      description: 'NGSI entity type. It has to be station_information'      
      enum:      
        - station_information      
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
    - last_updated      
    - ttl      
    - version      
    - data      
    - id      
    - type      
  type: object      
  x-derived-from: https://github.com/NABSA/gbfs/blob/v2.2/gbfs.md      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.GBFS/blob/master/station_information/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.GBFS/station_information/schema.json      
  x-model-tags: GBFS      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Exemples de charges utiles    
#### station_information NGSI-v2 key-values Exemple    
Voici un exemple de station_information au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 quand on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:station_information:id:FNNO:60592292",  
  "type": "station_information",  
  "last_updated": 1609866247,  
  "ttl": 0,  
  "version": "3.0",  
  "data": {  
    "stations": [  
      {  
        "station_id": "station12",  
        "name": "SE Belmont & SE 10 th",  
        "lat": -82.655775,  
        "lon": 45.516445,  
        "is_valet_station": false,  
        "is_virtual_station": true,  
        "station_area": {  
          "type": "Multipolygon",  
          "coordinates": [  
            [  
              [  
                [  
                  -122.655775,  
                  45.516445  
                ],  
                [  
                  -122.655705,  
                  45.516445  
                ],  
                [  
                  -122.655705,  
                  45.516495  
                ],  
                [  
                  -122.655775,  
                  45.516495  
                ],  
                [  
                  -122.655775,  
                  45.516445  
                ]  
              ]  
            ]  
          ]  
        },  
        "capacity": 16,  
        "vehicle_capacity": {  
          "abc123": 8,  
          "def456": 8,  
          "ghi789": 16  
        }  
      }  
    ]  
  }  
}  
```  
</details>    
#### station_information NGSI-v2 normalisé Exemple    
Voici un exemple de station_information au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:station_information:id:FNNO:60592292",  
  "type": "station_information",  
  "last_updated": {  
    "type": "Number",  
    "value": 1609866247  
  },  
  "ttl": {  
    "type": "Boolean",  
    "value": false  
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
          "station_id": "station12",  
          "name": "SE Belmont & SE 10 th",  
          "lat": -82.655775,  
          "lon": 45.516445,  
          "is_valet_station": false,  
          "is_virtual_station": true,  
          "station_area": {  
            "type": "Multipolygon",  
            "coordinates": [  
              [  
                [  
                  [  
                    -122.655775,  
                    45.516445  
                  ],  
                  [  
                    -122.655705,  
                    45.516445  
                  ],  
                  [  
                    -122.655705,  
                    45.516495  
                  ],  
                  [  
                    -122.655775,  
                    45.516495  
                  ],  
                  [  
                    -122.655775,  
                    45.516445  
                  ]  
                ]  
              ]  
            ]  
          },  
          "capacity": 16,  
          "vehicle_capacity": {  
            "abc123": 8,  
            "def456": 8,  
            "ghi789": 16  
          }  
        }  
      ]  
    }  
  }  
}  
```  
</details>    
#### station_information NGSI-LD key-values Exemple    
Voici un exemple de station_information au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD quand on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:station_information:id:FNNO:60592292",  
  "type": "station_information",  
  "last_updated": 1609866247,  
  "ttl": 0,  
  "version": "3.0",  
  "data": {  
    "stations": [  
      {  
        "station_id": "station12",  
        "name": "SE Belmont & SE 10 th",  
        "lat": -82.655775,  
        "lon": 45.516445,  
        "is_valet_station": false,  
        "is_virtual_station": true,  
        "station_area": {  
          "type": "Multipolygon",  
          "coordinates": [  
            [  
              [  
                [  
                  -122.655775,  
                  45.516445  
                ],  
                [  
                  -122.655705,  
                  45.516445  
                ],  
                [  
                  -122.655705,  
                  45.516495  
                ],  
                [  
                  -122.655775,  
                  45.516495  
                ],  
                [  
                  -122.655775,  
                  45.516445  
                ]  
              ]  
            ]  
          ]  
        },  
        "capacity": 16,  
        "vehicle_capacity": {  
          "abc123": 8,  
          "def456": 8,  
          "ghi789": 16  
        }  
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
#### station_information NGSI-LD normalisé Exemple    
Voici un exemple de station_information au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:station_information:id:FNNO:60592292",  
    "type": "station_information",  
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
                    "station_id": "station12",  
                    "name": "SE Belmont & SE 10 th",  
                    "lat": -82.655775,  
                    "lon": 45.516445,  
                    "is_valet_station": false,  
                    "is_virtual_station": true,  
                    "station_area": {  
                        "type": "Multipolygon",  
                        "coordinates": [  
                            [  
                                [  
                                    [  
                                        -122.655775,  
                                        45.516445  
                                    ],  
                                    [  
                                        -122.655705,  
                                        45.516445  
                                    ],  
                                    [  
                                        -122.655705,  
                                        45.516495  
                                    ],  
                                    [  
                                        -122.655775,  
                                        45.516495  
                                    ],  
                                    [  
                                        -122.655775,  
                                        45.516445  
                                    ]  
                                ]  
                            ]  
                        ]  
                    },  
                    "capacity": 16,  
                    "vehicle_capacity": {  
                        "abc123": 8,  
                        "def456": 8,  
                        "ghi789": 16  
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
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
