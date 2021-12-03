Entità: gbfs  
============  
[Licenza aperta](https://github.com/smart-data-models//dataModel.GBFS/blob/master/gbfs/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **File di scoperta automatica che si collega a tutti gli altri file pubblicati dal sistema. Secondo lo standard GBFS 2.2**  
versione: 0.0.1  

## Elenco delle proprietà  

- `data`: Dati di risposta sotto forma di coppie nome:valore.  - `id`: Identificatore unico dell'entità  - `last_updated`: L'ultima volta che i dati nel feed sono stati aggiornati in tempo POSIX.  - `ttl`: Numero di secondi prima che i dati nel feed vengano aggiornati di nuovo (0 se i dati devono essere sempre aggiornati).  - `type`: Tipo di entità NGSI. Deve essere gbfs  - `version`: Numero di versione GBFS a cui il feed è conforme, secondo il framework di versioning (aggiunto nella v1.1).    
Proprietà richieste  
- `data`  - `id`  - `last_updated`  - `ttl`  - `type`  - `version`    
Mappatura della norma [GBFS 2.2](https://github.com/NABSA/gbfs/blob/v2.2/gbfs.md)  
## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
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
  version: 0.0.1    
```  
</details>    
## Esempio di payloads  
#### gbfs NGSI-v2 valori chiave Esempio  
Ecco un esempio di un gbfs in formato JSON-LD come key-values. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### gbfs NGSI-v2 normalizzato Esempio  
Ecco un esempio di un gbfs in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
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
#### gbfs NGSI-LD valori-chiave Esempio  
Ecco un esempio di un gbfs in formato JSON-LD come key-values. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### gbfs NGSI-LD normalizzato Esempio  
Ecco un esempio di un gbfs in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
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
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per avere una risposta su come trattare le unità di grandezza