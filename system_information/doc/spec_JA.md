<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
エンティティ：システム情報    
=============<!-- /10-Header -->    
<!-- 15-License -->    
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.GBFS/blob/master/system_information/LICENSE.md)    
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
グローバルな説明**システム運営者、システム所在地、実施年、URL、連絡先、タイムゾーンなどの詳細。標準GBFS 2.2**による。    
バージョン: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## プロパティのリスト    
<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。    
- `data[object]`: 名前と値のペアの形式のレスポンスデータ。  	- `email[email]`: オペレーターのカスタマーサービス部門が積極的に監視している電子メールアドレス。      
	- `feed_contact_email[email]`: このフィードの利用者が技術的な問題を報告するための単一の連絡先メールアドレス (v1.1 で追加)。      
	- `language[string]`: 残りのファイルで使用される言語。gbfs.jsonファイルの値と一致しなければならない。      
	- `license_url[uri]`: このシステムのGBFSデータのライセンス条件を定義するページの完全修飾URL。      
	- `name[string]`: 顧客に表示するシステム名。      
	- `operator[string]`: 運営者名      
	- `phone_number[string]`: 指定されたシステムの単一音声電話番号で、そのシステムのサービスエリアの典型的な電話番号を示す。      
	- `purchase_url[uri]`: 顧客がメンバーシップを購入できるURL。      
	- `rental_apps[object]`: レンタルアプリの情報をandroidとiosのJSONオブジェクトに格納（v1.1で追加）。      
	- `short_name[string]`: システムの省略形。      
	- `start_date[string]`: システムの運用開始日。      
	- `system_id[string]`: 車両共有システムの識別子。これはグローバルに一意でなければならない（異なるシステム間であっても）。      
	- `timezone[string]`: システムが置かれているタイムゾーン。      
- `id[*]`: エンティティの一意識別子  - `last_updated[integer]`: フィードのデータが POSIX 時間で最後に更新された時刻。  - `ttl[integer]`: フィードのデータが更新されるまでの秒数 (常に更新される場合は 0)。  - `type[string]`: NGSIエンティティタイプ。system_informationでなければならない。  - `version[string]`: バージョニングフレームワーク (v1.1 で追加) に従った、フィードが準拠している GBFS のバージョン番号。  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
必須プロパティ    
- `data`  - `id`  - `last_updated`  - `ttl`  - `type`  - `version`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
規格のマッピング [GBFS 2.2](https://github.com/NABSA/gbfs/blob/v2.2/gbfs.md)    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## プロパティのデータモデル記述    
アルファベット順（クリックで詳細表示）    
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
## ペイロードの例    
#### システム情報 NGSI-v2 キー値の例    
以下は、JSON-LD形式のsystem_informationのkey-valuesの例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると個々のエンティティのコンテキストデータを返す。    
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
#### システム情報 NGSI-v2 正規化例    
以下は、正規化されたJSON-LD形式のsystem_informationの例である。これはNGSI-v2と互換性があり、オプションを使用しない場合、個々のエンティティのコンテキストデータを返します。    
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
  }  
}  
```  
</details>    
#### システム情報 NGSI-LD キー値の例    
以下は、JSON-LD形式のsystem_informationのkey-valuesの例である。options=keyValues`を使うとNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返す。    
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
#### システム情報 NGSI-LD 正規化例    
以下は、正規化された JSON-LD 形式の system_information の例である。これは、オプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。    
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
