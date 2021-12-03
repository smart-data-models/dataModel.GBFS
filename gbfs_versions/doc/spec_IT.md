Entità: gbfs_versions  
=====================  
[Licenza aperta](https://github.com/smart-data-models//dataModel.GBFS/blob/master/gbfs_versions/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: ** Elenca tutti gli endpoint di alimentazione pubblicati secondo la versione sof della documentazione GBFS. (aggiunto nella v1.1) Secondo lo standard GBFS 2.2**  
versione: 0.0.1  

## Elenco delle proprietà  

- `data`: Dati di risposta sotto forma di coppie nome:valore.  - `id`: Identificatore unico dell'entità  - `last_updated`: L'ultima volta che i dati nel feed sono stati aggiornati in tempo POSIX.  - `ttl`: Numero di secondi prima che i dati nel feed vengano aggiornati di nuovo (0 se i dati devono essere sempre aggiornati).  - `type`: Tipo di entità NGSI. Deve essere gbfs_versions  - `version`: Numero di versione GBFS a cui il feed è conforme, secondo il framework di versioning.    
Proprietà richieste  
- `data`  - `id`  - `last_updated`  - `ttl`  - `type`  - `version`    
Mappatura della norma [GBFS 2.2](https://github.com/NABSA/gbfs/blob/v2.2/gbfs.md)  
## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
gbfs_versions:    
  description: 'Lists all feed endpoints published according to version sof the GBFS documentation. (added in v1.1) According to the Standard GBFS 2.2'    
  properties:    
    data:    
      additionalProperties: false    
      description: 'Response data in the form of name:value pairs.'    
      properties:    
        versions:    
          description: 'Contains one object, as defined below, for each of the available versions of a feed. The array must be sorted by increasing MAJOR and MINOR version number.'    
          items:    
            properties:    
              url:    
                description: 'URL of the corresponding gbfs.json endpoint'    
                format: uri    
                type: string    
              version:    
                description: 'The semantic version of the feed in the form X.Y'    
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
            required:    
              - version    
              - url    
            type: object    
          type: array    
      required:    
        - versions    
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
      description: 'NGSI entity type. It has to be gbfs_versions'    
      enum:    
        - gbfs_versions    
      type: string    
      x-ngsi:    
        type: Property    
    version:    
      description: 'GBFS version number to which the feed conforms, according to the versioning framework.'    
      enum:    
        - 1.1-RC    
        - 1.1    
        - 2.0-RC    
        - 2.0    
        - 2.1-RC    
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
#### gbfs_versions Valori chiave NGSI-v2 Esempio  
Ecco un esempio di gbfs_versions in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:gbfs_versions:id:BZXQ:05985472",  
  "type": "gbfs_versions",  
  "last_updated": 1450156427,  
  "ttl": 576,  
  "version": "2.0",  
  "data": {  
    "versions": [  
      {  
        "version": "3.0-RC",  
        "url": "urn:ngsi-ld:gbfs_versions:url:OOKT:50451777"  
      },  
      {  
        "version": "1.1-RC",  
        "url": "urn:ngsi-ld:gbfs_versions:url:ZPWS:72960398"  
      }  
    ]  
  }  
}  
```  
#### gbfs_versions NGSI-v2 normalizzato Esempio  
Ecco un esempio di gbfs_versions in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:gbfs_versions:id:BZXQ:05985472",  
  "type": "gbfs_versions",  
  "last_updated": {  
    "type": "Number",  
    "value": 1450156427  
  },  
  "ttl": {  
    "type": "Number",  
    "value": 576  
  },  
  "version": {  
    "type": "Text",  
    "value": "2.0"  
  },  
  "data": {  
    "type": "StructuredValue",  
    "value": {  
      "versions": [  
        {  
          "version": "3.0-RC",  
          "url": "urn:ngsi-ld:gbfs_versions:url:OOKT:50451777"  
        },  
        {  
          "version": "1.1-RC",  
          "url": "urn:ngsi-ld:gbfs_versions:url:ZPWS:72960398"  
        }  
      ]  
    }  
  }  
}  
```  
#### gbfs_versions Valori chiave NGSI-LD Esempio  
Ecco un esempio di gbfs_versions in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:gbfs_versions:id:BZXQ:05985472",  
  "type": "gbfs_versions",  
  "last_updated": 1450156427,  
  "ttl": 576,  
  "version": "2.0",  
  "data": {  
    "versions": [  
      {  
        "version": "3.0-RC",  
        "url": "urn:ngsi-ld:gbfs_versions:url:OOKT:50451777"  
      },  
      {  
        "version": "1.1-RC",  
        "url": "urn:ngsi-ld:gbfs_versions:url:ZPWS:72960398"  
      }  
    ]  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### gbfs_versions NGSI-LD normalizzato Esempio  
Ecco un esempio di gbfs_versions in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:gbfs_versions:id:BZXQ:05985472",  
  "type": "gbfs_versions",  
  "last_updated": {  
    "type": "Property",  
    "value": 1450156427  
  },  
  "ttl": {  
    "type": "Property",  
    "value": 576  
  },  
  "version": {  
    "type": "Property",  
    "value": "2.0"  
  },  
  "data": {  
    "type": "Property",  
    "value": {  
      "versions": [  
        {  
          "version": "3.0-RC",  
          "url": "urn:ngsi-ld:gbfs_versions:url:OOKT:50451777"  
        },  
        {  
          "version": "1.1-RC",  
          "url": "urn:ngsi-ld:gbfs_versions:url:ZPWS:72960398"  
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