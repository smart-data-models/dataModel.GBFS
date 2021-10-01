Entité : system_hours  
=====================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.GBFS/blob/master/system_hours/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Décrit les heures de fonctionnement du système. Selon la norme GBFS 2.2**  
version : 0.0.1  

## Liste des propriétés  

- `data`: Tableau qui contient les heures de fonctionnement du système.  - `id`: Identifiant unique de l'entité  - `last_updated`: Dernière fois que les données du flux ont été mises à jour en temps POSIX.  - `ttl`: Nombre de secondes avant que les données du flux ne soient à nouveau mises à jour (0 si les données doivent toujours être rafraîchies).  - `type`: Type d'entité NGSI. Il doit s'agir de system_hours  - `version`: Numéro de version du GBFS auquel le flux est conforme, selon le cadre de versionnage (ajouté dans la v1.1).    
Propriétés requises  
- `data`  - `id`  - `last_updated`  - `ttl`  - `type`  - `version`    
Cartographie de la norme [GBFS 2.2] (https://github.com/NABSA/gbfs/blob/v2.2/gbfs.md)  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
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
## Exemples de charges utiles  
#### system_hours NGSI-v2 key-values Exemple  
Voici un exemple de system_hours au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### system_hours NGSI-v2 normalisé Exemple  
Voici un exemple de system_hours au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### system_hours NGSI-LD key-values Exemple  
Voici un exemple de system_hours au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### system_hours NGSI-LD normalisé Exemple  
Voici un exemple de system_hours au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
