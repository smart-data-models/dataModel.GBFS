Entidad: system_hours  
=====================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.GBFS/blob/master/system_hours/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **Describe el horario de funcionamiento del sistema. Según la norma GBFS 2.2**  
versión: 0.0.1  

## Lista de propiedades  

- `data`: Matriz que contiene las horas de funcionamiento del sistema.  - `id`: Identificador único de la entidad  - `last_updated`: Última vez que se actualizaron los datos del feed en tiempo POSIX.  - `ttl`: Número de segundos antes de que los datos del feed se actualicen de nuevo (0 si los datos deben actualizarse siempre).  - `type`: Tipo de entidad NGSI. Tiene que ser system_hours  - `version`: Número de versión de GBFS al que se ajusta el feed, según el marco de versiones (añadido en la v1.1).    
Propiedades requeridas  
- `data`  - `id`  - `last_updated`  - `ttl`  - `type`  - `version`    
Asignación de la norma [GBFS 2.2](https://github.com/NABSA/gbfs/blob/v2.2/gbfs.md)  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
system_hours:    
  description: 'Describes the system hours of operation. According to the Standard GBFS 2.2'    
  properties:    
    data:    
      description: 'Array that contains system hours of operations.'    
      properties:    
        rental_hours:    
          items:    
            properties:    
              days:    
                description: 'An array of abbreviations (first 3 letters) of English names of the days of the week for which this object applies.'    
                items:    
                  enum:    
                    - sun    
                    - mon    
                    - tue    
                    - wed    
                    - thu    
                    - fri    
                    - sat    
                  type: string    
                maxItems: 7    
                minItems: 1    
                type: array    
              end_time:    
                description: 'End time for the hours of operation of the system.'    
                pattern: ^([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$    
                type: string    
              start_time:    
                description: 'Start time for the hours of operation of the system.'    
                pattern: ^([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$    
                type: string    
              user_types:    
                description: 'Array of member and nonmember value(s) indicating that this set of rental hours applies to either members or non-members only.'    
                items:    
                  enum:    
                    - member    
                    - nonmember    
                  type: string    
                maxItems: 2    
                minItems: 1    
                type: array    
            required:    
              - user_types    
              - days    
              - start_time    
              - end_time    
            type: object    
          type: array    
      required:    
        - rental_hours    
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
      description: 'NGSI entity type. It has to be system_hours'    
      enum:    
        - system_hours    
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
## Ejemplo de carga útil  
#### system_hours NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de system_hours en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:system_hours:id:FNNO:60592292",  
  "type": "system_hours",  
  "last_updated": 1609866247,  
  "ttl": 86400,  
  "version": "3.0",  
  "data": {  
    "rental_hours": [  
      {  
        "user_types": [  
          "member"  
        ],  
        "days": [  
          "sat",  
          "sun"  
        ],  
        "start_time": "00:00:00",  
        "end_time": "23:59:59"  
      },  
      {  
        "user_types": [  
          "nonmember"  
        ],  
        "days": [  
          "sat",  
          "sun"  
        ],  
        "start_time": "05:00:00",  
        "end_time": "23:59:59"  
      },  
      {  
        "user_types": [  
          "member",  
          "nonmember"  
        ],  
        "days": [  
          "mon",  
          "tue",  
          "wed",  
          "thu",  
          "fri"  
        ],  
        "start_time": "00:00:00",  
        "end_time": "23:59:59"  
      }  
    ]  
  }  
}  
```  
#### sistema_horas NGSI-v2 normalizado Ejemplo  
Este es un ejemplo de system_hours en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:system_hours:id:FNNO:60592292",  
  "type": "system_hours",  
  "last_updated": {  
    "type": "Number",  
    "value": 1609866247  
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
      "rental_hours": [  
        {  
          "user_types": [  
            "member"  
          ],  
          "days": [  
            "sat",  
            "sun"  
          ],  
          "start_time": "00:00:00",  
          "end_time": "23:59:59"  
        },  
        {  
          "user_types": [  
            "nonmember"  
          ],  
          "days": [  
            "sat",  
            "sun"  
          ],  
          "start_time": "05:00:00",  
          "end_time": "23:59:59"  
        },  
        {  
          "user_types": [  
            "member",  
            "nonmember"  
          ],  
          "days": [  
            "mon",  
            "tue",  
            "wed",  
            "thu",  
            "fri"  
          ],  
          "start_time": "00:00:00",  
          "end_time": "23:59:59"  
        }  
      ]  
    }  
  }  
}  
```  
#### system_hours NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de system_hours en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:system_hours:id:FNNO:60592292",  
  "type": "system_hours",  
  "last_updated": 1609866247,  
  "ttl": 86400,  
  "version": "3.0",  
  "data": {  
    "rental_hours": [  
      {  
        "user_types": [  
          "member"  
        ],  
        "days": [  
          "sat",  
          "sun"  
        ],  
        "start_time": "00:00:00",  
        "end_time": "23:59:59"  
      },  
      {  
        "user_types": [  
          "nonmember"  
        ],  
        "days": [  
          "sat",  
          "sun"  
        ],  
        "start_time": "05:00:00",  
        "end_time": "23:59:59"  
      },  
      {  
        "user_types": [  
          "member",  
          "nonmember"  
        ],  
        "days": [  
          "mon",  
          "tue",  
          "wed",  
          "thu",  
          "fri"  
        ],  
        "start_time": "00:00:00",  
        "end_time": "23:59:59"  
      }  
    ]  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### sistema_horas NGSI-LD normalizado Ejemplo  
Este es un ejemplo de system_hours en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:system_hours:id:FNNO:60592292",  
  "type": "system_hours",  
  "last_updated": {  
    "type": "Property",  
    "value": 1609866247  
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
      "rental_hours": [  
        {  
          "user_types": [  
            "member"  
          ],  
          "days": [  
            "sat",  
            "sun"  
          ],  
          "start_time": "00:00:00",  
          "end_time": "23:59:59"  
        },  
        {  
          "user_types": [  
            "nonmember"  
          ],  
          "days": [  
            "sat",  
            "sun"  
          ],  
          "start_time": "05:00:00",  
          "end_time": "23:59:59"  
        },  
        {  
          "user_types": [  
            "member",  
            "nonmember"  
          ],  
          "days": [  
            "mon",  
            "tue",  
            "wed",  
            "thu",  
            "fri"  
          ],  
          "start_time": "00:00:00",  
          "end_time": "23:59:59"  
        }  
      ]  
    }  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud