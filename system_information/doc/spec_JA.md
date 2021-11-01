エンティティ：System_information  
=========================  
[オープンライセンス](https://github.com/smart-data-models//dataModel.GBFS/blob/master/system_information/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述。**システムオペレーター、システムの所在地、導入年、URL、連絡先、タイムゾーンなどの詳細情報。規格GBFS2.2による。  
バージョン: 0.0.1  

## プロパティのリスト  

- `data`: 名前：値のペアの形で応答データ。  - `id`: エンティティのユニークな識別子  - `last_updated`: フィードのデータがPOSIX時間で更新された最後の時間。  - `ttl`: フィードのデータが再び更新されるまでの秒数（常にデータを更新する場合は0）。  - `type`: NGSIエンティティタイプ。それはsystem_informationでなければならない。  - `version`: フィードが準拠している GBFS のバージョン番号 (v1.1 で追加)。    
必須項目  
- `data`  - `id`  - `last_updated`  - `ttl`  - `type`  - `version`    
規格のマッピング [GBFS 2.2](https://github.com/NABSA/gbfs/blob/v2.2/gbfs.md)  
## データモデルによるプロパティの記述  
アルファベット順（クリックすると詳細が表示されます  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
system_information:    
  description: 'Details including system operator, system location, year implemented, URL, contact info, time zone. According to the Standard GBFS 2.2'    
  properties:    
    data:    
      description: 'Response data in the form of name:value pairs.'    
      properties:    
        email:    
          description: 'Email address actively monitored by the operator''s customer service department.'    
          format: email    
          type: string    
        feed_contact_email:    
          description: 'A single contact email address for consumers of this feed to report technical issues (added in v1.1).'    
          format: email    
          type: string    
        language:    
          description: 'The language that will be used throughout the rest of the files. It must match the value in the gbfs.json file.'    
          pattern: ^[a-z]{2,3}(-[A-Z]{2})?$    
          type: string    
        license_url:    
          description: 'A fully qualified URL of a page that defines the license terms for the GBFS data for this system.'    
          format: uri    
          type: string    
        name:    
          description: 'Name of the system to be displayed to customers.'    
          type: string    
        operator:    
          description: 'Name of the operator'    
          type: string    
        phone_number:    
          description: 'A single voice telephone number for the specified system that presents the telephone number as typical for the system''s service area.'    
          type: string    
        purchase_url:    
          description: 'URL where a customer can purchase a membership.'    
          format: uri    
          type: string    
        rental_apps:    
          description: 'Contains rental app information in the android and ios JSON objects (added in v1.1).'    
          properties:    
            android:    
              dependencies:    
                android:    
                  - store_uri    
                  - discovery_uri    
              description: 'Contains rental app download and app discovery information for the Android platform. (added in v1.1)'    
              properties:    
                discovery_uri:    
                  description: 'URI that can be used to discover if the rental Android app is installed on the device (added in v1.1).'    
                  format: uri    
                  type: string    
                store_uri:    
                  description: 'URI where the rental Android app can be downloaded from (added in v1.1).'    
                  format: uri    
                  type: string    
              type: object    
            ios:    
              dependencies:    
                ios:    
                  - store_uri    
                  - discovery_uri    
              description: 'Contains rental information for the iOS platform (added in v1.1).'    
              properties:    
                discovery_uri:    
                  description: 'URI that can be used to discover if the rental iOS app is installed on the device (added in v1.1).'    
                  format: uri    
                  type: string    
                store_uri:    
                  description: 'URI where the rental iOS app can be downloaded from (added in v1.1).'    
                  format: uri    
                  type: string    
              type: object    
          type: object    
        short_name:    
          description: 'Optional abbreviation for a system.'    
          type: string    
        start_date:    
          description: 'Date that the system began operations.'    
          pattern: ^[0-9]{4}-[0-9]{2}-[0-9]{2}$    
          type: string    
        system_id:    
          description: 'Identifier for this vehicle share system. This should be globally unique (even between different systems).'    
          type: string    
        timezone:    
          description: 'The time zone where the system is located.'    
          type: string    
        url:    
          description: 'The URL of the vehicle share system.'    
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
      description: 'NGSI entity type. It has to be system_information'    
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
  version: 0.0.1    
```  
</details>    
## ペイロードの例  
#### system_information NGSI-v2 key-values の例。  
system_informationをkey-valuesとしてJSON-LD形式で出力した例です。これは`options=keyValues`を使った場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### system_information NGSI-v2 正規化例  
ここでは、JSON-LD形式のsystem_informationを正規化した例を示します。これは、オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### system_information NGSI-LD key-values の例。  
ここでは、system_informationをkey-valuesとしてJSON-LD形式で記述した例を紹介します。これは`options=keyValues`を使った場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
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
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### system_information NGSI-LD 正規化例  
ここでは、JSON-LD形式のsystem_informationを正規化した例を示します。これはオプションを使用しない場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
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
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
