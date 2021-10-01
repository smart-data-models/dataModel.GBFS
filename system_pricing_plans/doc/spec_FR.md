Entité : system_pricing_plans  
=============================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.GBFS/blob/master/system_pricing_plans/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Décrit les systèmes de tarification du système. Selon la norme GBFS 2.2**  
version : 0.0.1  

## Liste des propriétés  

- `data`: Tableau qui contient un objet par plan tel que défini ci-dessous.  - `id`: Identifiant unique de l'entité  - `last_updated`: Dernière fois que les données du flux ont été mises à jour en temps POSIX.  - `ttl`: Nombre de secondes avant que les données du flux ne soient à nouveau mises à jour (0 si les données doivent toujours être rafraîchies).  - `type`: Type d'entité NGSI. Il doit s'agir de system_pricing_plans.  - `version`: Numéro de version du GBFS auquel le flux est conforme, selon le cadre de versionnage (ajouté dans la v1.1).    
Propriétés requises  
- `data`  - `id`  - `last_updated`  - `ttl`  - `type`  - `version`    
Cartographie de la norme [GBFS 2.2] (https://github.com/NABSA/gbfs/blob/v2.2/gbfs.md)  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
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
  version: 0.0.1    
```  
</details>    
## Exemples de charges utiles  
#### system_pricing_plans NGSI-v2 key-values Exemple  
Voici un exemple de plans de tarification du système au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### système_pricing_plans NGSI-v2 normalisé Exemple  
Voici un exemple de system_pricing_plans au format JSON-LD tel que normalisé. Ceci est compatible avec la NGSI-v2 lorsqu'elle n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### plan_de_tarification_système Valeurs-clés NGSI-LD Exemple  
Voici un exemple de plans de tarification du système au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD lorsque vous utilisez `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### système_pricing_plans NGSI-LD normalisé Exemple  
Voici un exemple de system_pricing_plans au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
