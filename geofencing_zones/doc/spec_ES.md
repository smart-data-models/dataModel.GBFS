Entidad: geofencing_zones  
=========================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.GBFS/blob/master/geofencing_zones/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **Describe las zonas de geofencing y sus reglas y atributos asociados (añadidos en la v2.1-RC). Según la norma GBFS 2.2**  
versión: 0.0.1  

## Lista de propiedades  

- `data`: Matriz que contiene información de geofencing para el sistema.  - `id`: Identificador único de la entidad  - `last_updated`: Última vez que se actualizaron los datos del feed en tiempo POSIX.  - `ttl`: Número de segundos antes de que los datos del feed se actualicen de nuevo (0 si los datos deben actualizarse siempre).  - `type`: Tipo de entidad NGSI. Tiene que ser geofencing_zones  - `version`: Número de la versión de GBFS a la que se ajusta la alimentación, según el marco de versiones.    
Propiedades requeridas  
- `data`  - `id`  - `last_updated`  - `ttl`  - `type`  - `version`    
Asignación de la norma [GBFS 2.2](https://github.com/NABSA/gbfs/blob/v2.2/gbfs.md)  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
geofencing_zones:    
  description: 'Describes geofencing zones and their associated rules and attributes (added in v2.1-RC). According to the Standard GBFS 2.2'    
  properties:    
    data:    
      description: 'Array that contains geofencing information for the system.'    
      properties:    
        geofencing_zones:    
          description: 'Each geofenced zone and its associated rules and attributes is described as an object within the array of features.'    
          properties:    
            features:    
              description: 'Array of objects.'    
              items:    
                properties:    
                  geometry:    
                    description: 'A polygon that describes where rides might not be able to start, end, go through, or have otehr limitations. Must follow the right-hand rule.'    
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
                          - MultiPolygon    
                        type: string    
                    required:    
                      - type    
                      - coordinates    
                    title: 'GeoJSON MultiPolygon'    
                    type: object    
                  properties:    
                    description: 'Describing travel allowances and limitations.'    
                    properties:    
                      end:    
                        description: 'End time of the geofencing zone in POSIX time.'    
                        minimum: 1450155600    
                        type: number    
                      name:    
                        description: 'Public name of the geofencing zone.'    
                        type: string    
                      rules:    
                        description: 'Array that contains one object per rule.'    
                        items:    
                          properties:    
                            maximum_speed_kph:    
                              description: 'What is the maximum speed allowed, in kilometers per hour?'    
                              minimum: 0    
                              type: number    
                            ride_allowed:    
                              description: 'Is the undocked ride allowed to stat and end in this zone?'    
                              type: boolean    
                            ride_through_allowed:    
                              description: 'Is the ride allowed to travel through this zone?'    
                              type: boolean    
                            vehicle_type_id:    
                              description: 'Array of vehicle type IDs for which these restrictions apply.'    
                              items:    
                                type: string    
                              type: array    
                          required:    
                            - ride_allowed    
                            - ride_through_allowed    
                          type: object    
                        type: array    
                      start:    
                        description: 'Start time of the geofencing zone in POSIX time.'    
                        minimum: 1450155600    
                        type: number    
                    type: object    
                  type:    
                    enum:    
                      - Feature    
                    type: string    
                required:    
                  - type    
                  - geometry    
                  - properties    
                title: 'GeoJSON Feature'    
                type: object    
              type: array    
            type:    
              description: 'FeatureCollection as per IETF RFC 7946.'    
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
      description: 'NGSI entity type. It has to be geofencing_zones'    
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
  version: 0.0.1    
```  
</details>    
## Ejemplo de carga útil  
#### geofencing_zones NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de geofencing_zones en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### geofencing_zones NGSI-v2 normalizado Ejemplo  
He aquí un ejemplo de geofencing_zones en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
#### geofencing_zones NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de geofencing_zones en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### geofencing_zones NGSI-LD normalizado Ejemplo  
He aquí un ejemplo de geofencing_zones en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud