Entity: system_hours  
====================









- `data`  



<details><summary><strong>full yaml details</strong></summary>    

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