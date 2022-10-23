<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティ：system_regions  
=====================<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.GBFS/blob/master/system_regions/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述です。**地理的または政治的な地域によって分割されたシステムの地域を記述する。標準GBFS2.2による**。  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性にタイプがない場合、複数のタイプまたは異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `data[object]`: 地域に関するグローバルデータ  - `id[*]`: エンティティの一意な識別子  - `last_updated[integer]`: フィードのデータが POSIX 時間で最後に更新された時刻。  - `ttl[integer]`: フィードのデータが再び更新されるまでの秒数（常にデータを更新する場合は0）。  - `type[string]`: NGSIエンティティタイプ。system_regionsでなければならない。  - `version[string]`: フィードが準拠しているGBFSのバージョン番号（バージョン管理の枠組みによる）（v1.1で追加）。  <!-- /30-PropertiesList -->  
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
system_regions:    
  description: 'Describes regions for a system that is broken up by geographic or political region. According to the Standard GBFS 2.2'    
  properties:    
    data:    
      description: 'Global data about the regions'    
      properties:    
        regions:    
          description: 'Array of regions.'    
          items:    
            properties:    
              name:    
                description: 'Public name for this region.'    
                type: string    
              region_id:    
                description: 'identifier of the region.'    
                type: string    
            required:    
              - region_id    
              - name    
            type: object    
          type: array    
      required:    
        - regions    
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
      description: 'NGSI entity type. It has to be system_regions'    
      enum:    
        - system_regions    
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
  x-derived-from: https://github.com/NABSA/gbfs/blob/v2.2/gbfs.md    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.GBFS/blob/master/system_regions/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.GBFS/system_regions/schema.json    
  x-model-tags: GBFS    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### system_regions NGSI-v2 key-value 例．  
以下は、system_regionsをJSON-LD形式でkey-valuesにした例である。これは `options=keyValues` を使用した場合に NGSI-v2 と互換性があり、個々のエンティティのコンテキストデータが返される。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:system_regions:id:FNNO:60592292",  
  "type": "system_regions",  
  "last_updated": 1604332380,  
  "ttl": 86400,  
  "version": "3.0",  
  "data": {  
    "regions": [  
      {  
        "name": "North",  
        "region_id": "3"  
      },  
      {  
        "name": "East",  
        "region_id": "4"  
      },  
      {  
        "name": "South",  
        "region_id": "5"  
      },  
      {  
        "name": "West",  
        "region_id": "6"  
      }  
    ]  
  }  
}  
```  
</details>  
#### system_regions NGSI-v2 正規化例  
以下は、system_regions を JSON-LD 形式で正規化した例である。これはオプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:system_regions:id:FNNO:60592292",  
  "type": "system_regions",  
  "last_updated": {  
    "type": "Number",  
    "value": 1604332380  
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
      "regions": [  
        {  
          "name": "North",  
          "region_id": "3"  
        },  
        {  
          "name": "East",  
          "region_id": "4"  
        },  
        {  
          "name": "South",  
          "region_id": "5"  
        },  
        {  
          "name": "West",  
          "region_id": "6"  
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
#### system_regions NGSI-LD key-value 例  
ここでは、system_regionsをJSON-LD形式でkey-valuesにした例を示す。これは `options=keyValues` を利用した場合に NGSI-LD と互換性があり、個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:system_regions:id:FNNO:60592292",  
    "type": "system_regions",  
    "last_updated": 1604332380,  
    "ttl": 86400,  
    "version": "3.0",  
    "data": {  
        "regions": [  
            {  
                "name": "North",  
                "region_id": "3"  
            },  
            {  
                "name": "East",  
                "region_id": "4"  
            },  
            {  
                "name": "South",  
                "region_id": "5"  
            },  
            {  
                "name": "West",  
                "region_id": "6"  
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
#### system_regions NGSI-LD 正規化例  
以下は、system_regions を JSON-LD 形式で正規化した例である。これはオプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:system_regions:id:FNNO:60592292",  
    "type": "system_regions",  
    "last_updated": {  
        "type": "Property",  
        "value": 1604332380  
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
            "regions": [  
                {  
                    "name": "North",  
                    "region_id": "3"  
                },  
                {  
                    "name": "East",  
                    "region_id": "4"  
                },  
                {  
                    "name": "South",  
                    "region_id": "5"  
                },  
                {  
                    "name": "West",  
                    "region_id": "6"  
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
