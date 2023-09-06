<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: system_information  
===========================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.GBFS/blob/master/system_information/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Details einschließlich Systembetreiber, Standort des Systems, Jahr der Einführung, URL, Kontaktinformationen, Zeitzone. Gemäß dem Standard GBFS 2.2**  
Version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.  
- `data[object]`: Antwortdaten in Form von Name:Wert-Paaren.  	- `email[email]`: E-Mail-Adresse, die von der Kundendienstabteilung des Betreibers aktiv überwacht wird.    
	- `feed_contact_email[email]`: Eine einzige Kontakt-E-Mail-Adresse für Nutzer dieses Feeds, um technische Probleme zu melden (hinzugefügt in v1.1).    
	- `language[string]`: Die Sprache, die im Rest der Dateien verwendet wird. Sie muss mit dem Wert in der Datei gbfs.json übereinstimmen.    
	- `license_url[uri]`: Eine vollständig qualifizierte URL einer Seite, die die Lizenzbedingungen für die GBFS-Daten für dieses System definiert.    
	- `name[string]`: Name des Systems, der den Kunden angezeigt werden soll.    
	- `operator[string]`: Name des Betreibers    
	- `phone_number[string]`: Eine einzelne Sprachtelefonnummer für das angegebene System, die die Telefonnummer als typisch für den Dienstbereich des Systems darstellt.    
	- `purchase_url[uri]`: URL, unter der ein Kunde eine Mitgliedschaft erwerben kann.    
	- `rental_apps[object]`: Enthält Informationen über Mietanwendungen in den JSON-Objekten für Android und iOS (hinzugefügt in v1.1).    
	- `short_name[string]`: Optionale Abkürzung für ein System.    
	- `start_date[string]`: Datum der Inbetriebnahme des Systems.    
	- `system_id[string]`: Kennung für dieses Carsharing-System. Diese sollte weltweit eindeutig sein (auch zwischen verschiedenen Systemen).    
	- `timezone[string]`: Die Zeitzone, in der sich das System befindet.    
- `id[*]`: Eindeutiger Bezeichner der Entität  - `last_updated[integer]`: Letzter Zeitpunkt der Aktualisierung der Daten im Feed in POSIX-Zeit.  - `ttl[integer]`: Anzahl der Sekunden, bevor die Daten im Feed erneut aktualisiert werden (0, wenn die Daten immer aufgefrischt werden sollen).  - `type[string]`: NGSI-Entitätstyp. Es muss system_information sein.  - `version[string]`: GBFS-Versionsnummer, der der Feed gemäß dem Versionierungsrahmen entspricht (hinzugefügt in v1.1).  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `data`  - `id`  - `last_updated`  - `ttl`  - `type`  - `version`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Abbildung der Norm [GBFS 2.2](https://github.com/NABSA/gbfs/blob/v2.2/gbfs.md)  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
system_information:    
  description: 'Details including system operator, system location, year implemented, URL, contact info, time zone. According to the Standard GBFS 2.2'    
  properties:    
    data:    
      description: 'Response data in the form of name:value pairs.'    
      properties:    
        email:    
          description: Email address actively monitored by the operator's customer service department.    
          format: email    
          type: string    
        feed_contact_email:    
          description: A single contact email address for consumers of this feed to report technical issues (added in v1.1).    
          format: email    
          type: string    
        language:    
          description: The language that will be used throughout the rest of the files. It must match the value in the gbfs.json file.    
          pattern: ^[a-z]{2,3}(-[A-Z]{2})?$    
          type: string    
        license_url:    
          description: A fully qualified URL of a page that defines the license terms for the GBFS data for this system.    
          format: uri    
          type: string    
        name:    
          description: Name of the system to be displayed to customers.    
          type: string    
        operator:    
          description: Name of the operator    
          type: string    
        phone_number:    
          description: A single voice telephone number for the specified system that presents the telephone number as typical for the system's service area.    
          type: string    
        purchase_url:    
          description: URL where a customer can purchase a membership.    
          format: uri    
          type: string    
        rental_apps:    
          description: Contains rental app information in the android and ios JSON objects (added in v1.1).    
          properties:    
            android:    
              dependencies:    
                android:    
                  - store_uri    
                  - discovery_uri    
              description: Contains rental app download and app discovery information for the Android platform. (added in v1.1)    
              properties:    
                discovery_uri:    
                  description: URI that can be used to discover if the rental Android app is installed on the device (added in v1.1).    
                  format: uri    
                  type: string    
                store_uri:    
                  description: URI where the rental Android app can be downloaded from (added in v1.1).    
                  format: uri    
                  type: string    
              type: object    
            ios:    
              dependencies:    
                ios:    
                  - store_uri    
                  - discovery_uri    
              description: Contains rental information for the iOS platform (added in v1.1).    
              properties:    
                discovery_uri:    
                  description: URI that can be used to discover if the rental iOS app is installed on the device (added in v1.1).    
                  format: uri    
                  type: string    
                store_uri:    
                  description: URI where the rental iOS app can be downloaded from (added in v1.1).    
                  format: uri    
                  type: string    
              type: object    
          type: object    
        short_name:    
          description: Optional abbreviation for a system.    
          type: string    
        start_date:    
          description: Date that the system began operations.    
          pattern: ^[0-9]{4}-[0-9]{2}-[0-9]{2}$    
          type: string    
        system_id:    
          description: Identifier for this vehicle share system. This should be globally unique (even between different systems).    
          type: string    
        timezone:    
          description: The time zone where the system is located.    
          type: string    
        url:    
          description: The URL of the vehicle share system.    
          format: uri    
          type: string    
      required:    
        - system_id    
        - language    
        - name    
        - timezone    
      type: object    
      x-ngsi:    
        type: Property    
    id:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    last_updated:    
      description: Last time the data in the feed was updated in POSIX time.    
      minimum: 1450155600    
      type: integer    
      x-ngsi:    
        type: Property    
    ttl:    
      description: Number of seconds before the data in the feed will be updated again (0 if the data should always be refreshed).    
      minimum: 0    
      type: integer    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI entity type. It has to be system_information    
      enum:    
        - system_information    
      type: string    
      x-ngsi:    
        type: Property    
    version:    
      description: 'GBFS version number to which the feed conforms, according to the versioning framework (added in v1.1).'    
      enum:    
        - 1.1-RC    
        - 1.1    
        - 2.0    
        - 2.1-RC    
        - 2.1-RC2    
        - 2.1    
        - 2.2    
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
  x-derived-from: https://github.com/NABSA/gbfs/blob/v2.2/gbfs.md    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.GBFS/blob/master/system_information/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.GBFS/system_information/schema.json    
  x-model-tags: GBFS    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### system_information NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für eine system_information im JSON-LD Format als key-values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:system_information:id:FNNO:60592292",  
  "type": "system_information",  
  "last_updated": 1611598155,  
  "ttl": 1800,  
  "version": "3.0",  
  "data": {  
    "system_id": "example_cityname",  
    "language": "en",  
    "name": "Example Bike Rental",  
    "short_name": "Example Bike",  
    "operator": "Example Sharing, Inc",  
    "url": "https://www.example.com",  
    "purchase_url": "https://www.example.com",  
    "start_date": "2010-06-10",  
    "phone_number": "1-800-555-1234",  
    "email": "customerservice@example.com",  
    "feed_contact_email": "datafeed@example.com",  
    "timezone": "US/Central",  
    "license_url": "https://www.example.com/data-license.html",  
    "brand_assets": {  
      "brand_last_modified": "2021-06-15",  
      "brand_image_url": "https://www.example.com/assets/brand_image.svg",  
      "brand_image_url_dark": "https://www.example.com/assets/brand_image_dark.svg",  
      "color": "#C2D32C",  
      "terms_url": "https://www.example.com/assets/brand.pdf"  
    }  
  }  
}  
```  
</details>  
#### system_information NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für eine system_information im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:system_information:id:FNNO:60592292",  
  "type": "system_information",  
  "last_updated": {  
    "type": "Number",  
    "value": 1611598155  
  },  
  "ttl": {  
    "type": "Number",  
    "value": 1800  
  },  
  "version": {  
    "type": "Text",  
    "value": "3.0"  
  },  
  "data": {  
    "type": "StructuredValue",  
    "value": {  
      "system_id": "example_cityname",  
      "language": "en",  
      "name": "Example Bike Rental",  
      "short_name": "Example Bike",  
      "operator": "Example Sharing, Inc",  
      "url": "https://www.example.com",  
      "purchase_url": "https://www.example.com",  
      "start_date": "2010-06-10",  
      "phone_number": "1-800-555-1234",  
      "email": "customerservice@example.com",  
      "feed_contact_email": "datafeed@example.com",  
      "timezone": "US/Central",  
      "license_url": "https://www.example.com/data-license.html",  
      "brand_assets": {  
        "brand_last_modified": "2021-06-15",  
        "brand_image_url": "https://www.example.com/assets/brand_image.svg",  
        "brand_image_url_dark": "https://www.example.com/assets/brand_image_dark.svg",  
        "color": "#C2D32C",  
        "terms_url": "https://www.example.com/assets/brand.pdf"  
      }  
    }  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
</details>  
#### system_information NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für eine system_information im JSON-LD Format als key-values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:system_information:id:FNNO:60592292",  
    "type": "system_information",  
    "last_updated": 1611598155,  
    "ttl": 1800,  
    "version": "3.0",  
    "data": {  
        "system_id": "example_cityname",  
        "language": "en",  
        "name": "Example Bike Rental",  
        "short_name": "Example Bike",  
        "operator": "Example Sharing, Inc",  
        "url": "https://www.example.com",  
        "purchase_url": "https://www.example.com",  
        "start_date": "2010-06-10",  
        "phone_number": "1-800-555-1234",  
        "email": "customerservice@example.com",  
        "feed_contact_email": "datafeed@example.com",  
        "timezone": "US/Central",  
        "license_url": "https://www.example.com/data-license.html",  
        "brand_assets": {  
            "brand_last_modified": "2021-06-15",  
            "brand_image_url": "https://www.example.com/assets/brand_image.svg",  
            "brand_image_url_dark": "https://www.example.com/assets/brand_image_dark.svg",  
            "color": "#C2D32C",  
            "terms_url": "https://www.example.com/assets/brand.pdf"  
        }  
    },  
    "@context": [  
        "https://smartdatamodels.org/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.GBFS/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### system_information NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für eine system_information im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:system_information:id:FNNO:60592292",  
    "type": "system_information",  
    "last_updated": {  
        "type": "Property",  
        "value": 1611598155  
    },  
    "ttl": {  
        "type": "Property",  
        "value": 1800  
    },  
    "version": {  
        "type": "Property",  
        "value": "3.0"  
    },  
    "data": {  
        "type": "Property",  
        "value": {  
            "system_id": "example_cityname",  
            "language": "en",  
            "name": "Example Bike Rental",  
            "short_name": "Example Bike",  
            "operator": "Example Sharing, Inc",  
            "url": "https://www.example.com",  
            "purchase_url": "https://www.example.com",  
            "start_date": "2010-06-10",  
            "phone_number": "1-800-555-1234",  
            "email": "customerservice@example.com",  
            "feed_contact_email": "datafeed@example.com",  
            "timezone": "US/Central",  
            "license_url": "https://www.example.com/data-license.html",  
            "brand_assets": {  
                "brand_last_modified": "2021-06-15",  
                "brand_image_url": "https://www.example.com/assets/brand_image.svg",  
                "brand_image_url_dark": "https://www.example.com/assets/brand_image_dark.svg",  
                "color": "#C2D32C",  
                "terms_url": "https://www.example.com/assets/brand.pdf"  
            }  
        }  
    },  
    "@context": [  
        "https://smartdatamodels.org/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.GBFS/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
