Entité : system_calendar  
========================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.GBFS/blob/master/system_calendar/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Décrit le calendrier d'exploitation d'un système. Selon la norme GBFS 2.2**  
version : 0.0.1  

## Liste des propriétés  

- `data`: Tableau qui contient le calendrier des opérations pour le système.  - `id`: Identifiant unique de l'entité  - `last_updated`: Dernière fois que les données du flux ont été mises à jour en temps POSIX.  - `ttl`: Nombre de secondes avant que les données du flux ne soient à nouveau mises à jour (0 si les données doivent toujours être rafraîchies).  - `type`: Type d'entité NGSI. Il doit s'agir de system_calendar  - `version`: Numéro de version du GBFS auquel le flux est conforme, selon le cadre de versionnage (ajouté dans la v1.1).    
Propriétés requises  
- `data`  - `id`  - `last_updated`  - `ttl`  - `type`  - `version`    
Cartographie de la norme [GBFS 2.2] (https://github.com/NABSA/gbfs/blob/v2.2/gbfs.md)  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
system_calendar:    
  description: 'Describes the operating calendar for a system. According to the Standard GBFS 2.2'    
  properties:    
    data:    
      description: 'Array that contains opertions calendar for the system.'    
      properties:    
        calendars:    
          items:    
            properties:    
              end_day:    
                description: 'End day for the system operations.'    
                maximum: 31    
                minimum: 1    
                type: number    
              end_month:    
                description: 'End month for the system operations.'    
                maximum: 12    
                minimum: 1    
                type: number    
              end_year:    
                description: 'End year for the system operations.'    
                pattern: ^\d{4}$    
                type: number    
              start_day:    
                description: 'Starting day for the system operations.'    
                maximum: 31    
                minimum: 1    
                type: number    
              start_month:    
                description: 'Starting month for the system operations.'    
                maximum: 12    
                minimum: 1    
                type: number    
              start_year:    
                description: 'Starting year for the system operations.'    
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
      description: 'NGSI entity type. It has to be system_calendar'    
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
  version: 0.0.1    
```  
</details>    
## Exemples de charges utiles  
#### system_calendar Valeurs-clés NGSI-v2 Exemple  
Voici un exemple de calendrier système au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### system_calendar NGSI-v2 normalisé Exemple  
Voici un exemple d'un system_calendar au format JSON-LD tel que normalisé. Il est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### system_calendar valeurs-clés NGSI-LD Exemple  
Voici un exemple de calendrier système au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### system_calendar NGSI-LD normalisé Exemple  
Voici un exemple d'un system_calendar au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude