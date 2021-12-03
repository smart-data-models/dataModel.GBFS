Entità: system_calendar  
=======================  
[Licenza aperta](https://github.com/smart-data-models//dataModel.GBFS/blob/master/system_calendar/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Descrive il calendario operativo di un sistema. Secondo lo standard GBFS 2.2**  
versione: 0.0.1  

## Elenco delle proprietà  

- `data`: Array che contiene il calendario delle operazioni per il sistema.  - `id`: Identificatore unico dell'entità  - `last_updated`: L'ultima volta che i dati nel feed sono stati aggiornati in tempo POSIX.  - `ttl`: Numero di secondi prima che i dati nel feed vengano aggiornati di nuovo (0 se i dati devono essere sempre aggiornati).  - `type`: Tipo di entità NGSI. Deve essere system_calendar  - `version`: Numero di versione GBFS a cui il feed è conforme, secondo il framework di versioning (aggiunto nella v1.1).    
Proprietà richieste  
- `data`  - `id`  - `last_updated`  - `ttl`  - `type`  - `version`    
Mappatura della norma [GBFS 2.2](https://github.com/NABSA/gbfs/blob/v2.2/gbfs.md)  
## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
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
## Esempio di payloads  
#### system_calendar Valori chiave NGSI-v2 Esempio  
Ecco un esempio di un system_calendar in formato JSON-LD come key-values. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### system_calendar NGSI-v2 normalizzato Esempio  
Ecco un esempio di un system_calendar in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
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
#### system_calendar Valori chiave NGSI-LD Esempio  
Ecco un esempio di un system_calendar in formato JSON-LD come key-values. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### system_calendar NGSI-LD normalizzato Esempio  
Ecco un esempio di un system_calendar in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per avere una risposta su come trattare le unità di grandezza