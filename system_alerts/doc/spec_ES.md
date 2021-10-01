Entidad: system_alerts  
======================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.GBFS/blob/master/system_alerts/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **Describe los cambios ad-hoc en el sistema. Según la norma GBFS 2.2**  
versión: 0.0.1  

## Lista de propiedades  

- `data`: Matriz que contiene alertas ad-hoc para el sistema.  - `id`: Identificador único de la entidad  - `last_updated`: Última vez que se actualizaron los datos del feed en tiempo POSIX.  - `ttl`: Número de segundos antes de que los datos del feed se actualicen de nuevo (0 si los datos deben actualizarse siempre).  - `type`: Tipo de entidad NGSI. Tiene que ser system_alerts  - `version`: Número de versión de GBFS al que se ajusta el feed, según el marco de versiones (añadido en la v1.1).    
Propiedades requeridas  
- `data`  - `id`  - `last_updated`  - `ttl`  - `type`  - `version`    
Asignación de la norma [GBFS 2.2](https://github.com/NABSA/gbfs/blob/v2.2/gbfs.md)  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
system_alerts:    
  description: 'Describes ad-hoc changes to the system. According to the Standard GBFS 2.2'    
  properties:    
    data:    
      description: 'Array that contains ad-hoc alerts for the system.'    
      properties:    
        alerts:    
          items:    
            properties:    
              alert_id:    
                description: 'Identifier for this alert.'    
                type: string    
              description:    
                description: 'Detailed description of the alert.'    
                type: string    
              last_updated:    
                description: 'Indicates the last time the info for the alert was updated.'    
                minimum: 1450155600    
                type: number    
              region_ids:    
                description: 'Array of identifiers of the regions for which this alert applies.'    
                items:    
                  type: string    
                type: array    
              station_ids:    
                description: 'Array of identifiers of the stations for which this alert applies.'    
                items:    
                  type: string    
                type: array    
              summary:    
                description: 'A short summary of this alert to be displayed to the customer.'    
                type: string    
              times:    
                additionalItems: false    
                description: 'Array of objects indicating when the alert is in effect.'    
                items:    
                  properties:    
                    end:    
                      description: 'End time of the alert.'    
                      minimum: 1450155600    
                      type: number    
                    start:    
                      description: 'Start time of the alert.'    
                      minimum: 1450155600    
                      type: number    
                  type: object    
                required:    
                  - start    
                type: array    
              type:    
                description: 'Type of alert.'    
                enum:    
                  - system_closure    
                  - station_closure    
                  - station_move    
                  - other    
                type: string    
              url:    
                description: 'URL where the customer can learn more information about this alert.'    
                format: uri    
                type: string    
            required:    
              - alert_id    
              - type    
              - summary    
            type: object    
          type: array    
      required:    
        - alerts    
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
      description: 'NGSI entity type. It has to be system_alerts'    
      enum:    
        - system_alerts    
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
  version: 0.0.1    
```  
</details>    
## Ejemplo de carga útil  
#### system_alerts NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de system_alerts en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:system_alerts:id:FNNO:60592292",  
  "type": "system_alerts",  
  "last_updated": 1604198100,  
  "ttl": 60,  
  "version": "3.0",  
  "data": {  
    "alerts": [  
      {  
        "alert_id": "21",  
        "type": "station_closure",  
        "station_ids": [  
          "123",  
          "456",  
          "789"  
        ],  
        "times": [  
          {  
            "start": 1604448000,  
            "end": 1604674800  
          }  
        ],  
        "url": "https://example.com/more-info",  
        "summary": "Disruption of Service",  
        "description": "The three stations on Broadway will be out of service from 12:00am Nov 3 to 3:00pm Nov 6th to accommodate road work",  
        "last_updated": 1604519393  
      }  
    ]  
  }  
}  
```  
#### system_alerts NGSI-v2 normalized Ejemplo  
He aquí un ejemplo de system_alerts en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:system_alerts:id:FNNO:60592292",  
  "type": "system_alerts",  
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
      "alerts": [  
        {  
          "alert_id": "21",  
          "type": "station_closure",  
          "station_ids": [  
            "123",  
            "456",  
            "789"  
          ],  
          "times": [  
            {  
              "start": 1604448000,  
              "end": 1604674800  
            }  
          ],  
          "url": "https://example.com/more-info",  
          "summary": "Disruption of Service",  
          "description": "The three stations on Broadway will be out of service from 12:00am Nov 3 to 3:00pm Nov 6th to accommodate road work",  
          "last_updated": 1604519393  
        }  
      ]  
    }  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### system_alerts NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de system_alerts en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:system_alerts:id:FNNO:60592292",  
  "type": "system_alerts",  
  "last_updated": 1604198100,  
  "ttl": 60,  
  "version": "3.0",  
  "data": {  
    "alerts": [  
      {  
        "alert_id": "21",  
        "type": "station_closure",  
        "station_ids": [  
          "123",  
          "456",  
          "789"  
        ],  
        "times": [  
          {  
            "start": 1604448000,  
            "end": 1604674800  
          }  
        ],  
        "url": "https://example.com/more-info",  
        "summary": "Disruption of Service",  
        "description": "The three stations on Broadway will be out of service from 12:00am Nov 3 to 3:00pm Nov 6th to accommodate road work",  
        "last_updated": 1604519393  
      }  
    ]  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### system_alerts NGSI-LD normalizado Ejemplo  
Este es un ejemplo de system_alerts en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:system_alerts:id:FNNO:60592292",  
  "type": "system_alerts",  
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
      "alerts": [  
        {  
          "alert_id": "21",  
          "type": "station_closure",  
          "station_ids": [  
            "123",  
            "456",  
            "789"  
          ],  
          "times": [  
            {  
              "start": 1604448000,  
              "end": 1604674800  
            }  
          ],  
          "url": "https://example.com/more-info",  
          "summary": "Disruption of Service",  
          "description": "The three stations on Broadway will be out of service from 12:00am Nov 3 to 3:00pm Nov 6th to accommodate road work",  
          "last_updated": 1604519393  
        }  
      ]  
    }  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
