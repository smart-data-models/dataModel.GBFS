<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティ：system_alerts  
====================<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.GBFS/blob/master/system_alerts/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述です。**システムに対するアドホックな変更点を記述します。標準GBFS2.2による**。  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性にタイプがない場合、複数のタイプまたは異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `data[object]`: システムのアドホックアラートを含むアレイ。  - `id[*]`: エンティティの一意な識別子  - `last_updated[integer]`: フィードのデータが POSIX 時間で最後に更新された時刻。  - `ttl[integer]`: フィードのデータが再び更新されるまでの秒数（常にデータを更新する場合は0）。  - `type[string]`: NGSIエンティティタイプ。system_alertsでなければならない。  - `version[string]`: バージョン管理の枠組みによる、フィードが準拠するGBFSのバージョン番号（v1.1で追加）。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必要なプロパティ  
- `data`  - `id`  - `last_updated`  - `ttl`  - `type`  - `version`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
規格のマッピング[GBFS 2.2](https://github.com/NABSA/gbfs/blob/v2.2/gbfs.md)  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
system_alerts:    
  description: 'Describes ad-hoc changes to the system. According to the Standard GBFS 2.2'    
  properties:    
    data:    
      description: 'Array that contains ad-hoc alerts for the system.'    
      properties:    
        alerts:    
          items:    
            properties:    
              alert_id:    
                description: 'Identifier for this alert.'    
                type: string    
              description:    
                description: 'Detailed description of the alert.'    
                type: string    
              last_updated:    
                description: 'Indicates the last time the info for the alert was updated.'    
                minimum: 1450155600    
                type: number    
              region_ids:    
                description: 'Array of identifiers of the regions for which this alert applies.'    
                items:    
                  type: string    
                type: array    
              station_ids:    
                description: 'Array of identifiers of the stations for which this alert applies.'    
                items:    
                  type: string    
                type: array    
              summary:    
                description: 'A short summary of this alert to be displayed to the customer.'    
                type: string    
              times:    
                additionalItems: false    
                description: 'Array of objects indicating when the alert is in effect.'    
                items:    
                  properties:    
                    end:    
                      description: 'End time of the alert.'    
                      minimum: 1450155600    
                      type: number    
                    start:    
                      description: 'Start time of the alert.'    
                      minimum: 1450155600    
                      type: number    
                  type: object    
                required:    
                  - start    
                type: array    
              type:    
                description: 'Type of alert.'    
                enum:    
                  - system_closure    
                  - station_closure    
                  - station_move    
                  - other    
                type: string    
              url:    
                description: 'URL where the customer can learn more information about this alert.'    
                format: uri    
                type: string    
            required:    
              - alert_id    
              - type    
              - summary    
            type: object    
          type: array    
      required:    
        - alerts    
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
      description: 'NGSI entity type. It has to be system_alerts'    
      enum:    
        - system_alerts    
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
  x-derived-from: https://github.com/NABSA/gbfs/blob/v2.2/gbfs.md    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.GBFS/blob/master/system_alerts/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.GBFS/system_alerts/schema.json    
  x-model-tags: GBFS    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### system_alerts NGSI-v2 key-value 例  
以下は、system_alertsをJSON-LD形式でkey-valuesにした例である。これは、`options=keyValues`を使用した場合にNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:system_alerts:id:FNNO:60592292",  
  "type": "system_alerts",  
  "last_updated": 1604198100,  
  "ttl": 60,  
  "version": "3.0",  
  "data": {  
    "alerts": [  
      {  
        "alert_id": "21",  
        "type": "station_closure",  
        "station_ids": [  
          "123",  
          "456",  
          "789"  
        ],  
        "times": [  
          {  
            "start": 1604448000,  
            "end": 1604674800  
          }  
        ],  
        "url": "https://example.com/more-info",  
        "summary": "Disruption of Service",  
        "description": "The three stations on Broadway will be out of service from 12:00am Nov 3 to 3:00pm Nov 6th to accommodate road work",  
        "last_updated": 1604519393  
      }  
    ]  
  }  
}  
```  
</details>  
#### system_alerts NGSI-v2 正規化例  
以下は、system_alerts を JSON-LD 形式で正規化した例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:system_alerts:id:FNNO:60592292",  
  "type": "system_alerts",  
  "last_updated": {  
    "type": "Number",  
    "value": 1604198100  
  },  
  "ttl": {  
    "type": "Number",  
    "value": 60  
  },  
  "version": {  
    "type": "Text",  
    "value": "3.0"  
  },  
  "data": {  
    "type": "StructuredValue",  
    "value": {  
      "alerts": [  
        {  
          "alert_id": "21",  
          "type": "station_closure",  
          "station_ids": [  
            "123",  
            "456",  
            "789"  
          ],  
          "times": [  
            {  
              "start": 1604448000,  
              "end": 1604674800  
            }  
          ],  
          "url": "https://example.com/more-info",  
          "summary": "Disruption of Service",  
          "description": "The three stations on Broadway will be out of service from 12:00am Nov 3 to 3:00pm Nov 6th to accommodate road work",  
          "last_updated": 1604519393  
        }  
      ]  
    }  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
</details>  
#### system_alerts NGSI-LD key-value 例  
ここでは、system_alertsをJSON-LD形式でkey-valuesにした例を示す。これは `options=keyValues` を使用した場合に NGSI-LD と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:system_alerts:id:FNNO:60592292",  
    "type": "system_alerts",  
    "last_updated": 1604198100,  
    "ttl": 60,  
    "version": "3.0",  
    "data": {  
        "alerts": [  
            {  
                "alert_id": "21",  
                "type": "station_closure",  
                "station_ids": [  
                    "123",  
                    "456",  
                    "789"  
                ],  
                "times": [  
                    {  
                        "start": 1604448000,  
                        "end": 1604674800  
                    }  
                ],  
                "url": "https://example.com/more-info",  
                "summary": "Disruption of Service",  
                "description": "The three stations on Broadway will be out of service from 12:00am Nov 3 to 3:00pm Nov 6th to accommodate road work",  
                "last_updated": 1604519393  
            }  
        ]  
    },  
    "@context": [  
        "https://smartdatamodels.org/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.GBFS/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### system_alerts NGSI-LD 正規化例  
以下は、system_alerts を JSON-LD 形式で正規化した例である。これはオプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:system_alerts:id:FNNO:60592292",  
    "type": "system_alerts",  
    "last_updated": {  
        "type": "Property",  
        "value": 1604198100  
    },  
    "ttl": {  
        "type": "Property",  
        "value": 60  
    },  
    "version": {  
        "type": "Property",  
        "value": "3.0"  
    },  
    "data": {  
        "type": "Property",  
        "value": {  
            "alerts": [  
                {  
                    "alert_id": "21",  
                    "type": "station_closure",  
                    "station_ids": [  
                        "123",  
                        "456",  
                        "789"  
                    ],  
                    "times": [  
                        {  
                            "start": 1604448000,  
                            "end": 1604674800  
                        }  
                    ],  
                    "url": "https://example.com/more-info",  
                    "summary": "Disruption of Service",  
                    "description": "The three stations on Broadway will be out of service from 12:00am Nov 3 to 3:00pm Nov 6th to accommodate road work",  
                    "last_updated": 1604519393  
                }  
            ]  
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
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
