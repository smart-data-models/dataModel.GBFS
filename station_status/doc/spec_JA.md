<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
エンティティ：station_status    
=====================<!-- /10-Header -->    
<!-- 15-License -->    
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.GBFS/blob/master/station_status/LICENSE.md)    
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
グローバルな記述：**標準 GBFS 2.2 に従い、ステーションのキャパシティとレンタル可用性を記述する。    
バージョン: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## プロパティのリスト    
<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。    
- `data[object]`: 以下に定義するように、ステーションごとに1つのオブジェクトを含む配列。  	    
- `id[*]`: エンティティの一意識別子  - `last_updated[integer]`: フィードのデータが POSIX 時間で最後に更新された時刻。  - `ttl[integer]`: フィードのデータが更新されるまでの秒数 (常に更新される場合は 0)。  - `type[string]`: NGSI エンティティタイプ。station_status でなければならない。  - `version[string]`: バージョニングフレームワーク (v1.1 で追加) に従った、フィードが準拠している GBFS のバージョン番号。  <!-- /30-PropertiesList -->    
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
station_status:      
  description: Describes the capacity and rental availability of the station According to the Standard GBFS 2.2      
  properties:      
    data:      
      description: Array that contains one object per station as defined below.      
      properties:      
        stations:      
          items:      
            properties:      
              is_installed:      
                description: 'Is the station currently on the street?'      
                type: boolean      
              is_renting:      
                description: 'Is the station currently renting vehicles?'      
                type: boolean      
              is_returning:      
                description: 'Is the station accepting vehicle returns?'      
                type: boolean      
              last_reported:      
                description: The last time this station reported its status to the operator's backend in POSIX time.      
                minimum: 1450155600      
                type: number      
              num_bikes_available:      
                description: Number of vehicles of any type physically available for rental at the station.      
                minimum: 0      
                type: number      
              num_bikes_disabled:      
                description: Number of disabled vehicles of any type at the station.      
                minimum: 0      
                type: number      
              num_docks_available:      
                description: Number of functional docks physically at the station.      
                minimum: 0      
                type: number      
              num_docks_disabled:      
                description: Number of empty but disabled docks at the station.      
                minimum: 0      
                type: number      
              station_id:      
                description: Identifier of a station.      
                type: string      
              vehicle_docks_available:      
                dependencies:      
                  vehicle_docks_available:      
                    - vehicle_type_ids      
                    - count      
                description: Object displaying available docks by vehicle type (added in v2.1-RC).      
                items:      
                  properties:      
                    count:      
                      description: A number representing the total number of available docks for the defined vehicle type (added in v2.1-RC).      
                      minimum: 0      
                      type: number      
                    vehicle_type_ids:      
                      description: An array of strings where each string represents a vehicle_type_id that is able to use a particular type of dock at the station (added in v2.1-RC).      
                      items:      
                        type: string      
                      type: array      
                  type: object      
                type: array      
              vehicles:      
                description: Array of objects containing data about a specific vehicle that is present at the docking station (added in v2.1-RC).      
                items:      
                  properties:      
                    bike_id:      
                      description: Rotated identifier of a vehicle (added in v2.1-RC).      
                      type: string      
                    current_range_meters:      
                      description: The furthest distance in meters that the vehicle can travel without recharging or refueling with the vehicle's current charge or fuel (added in v2.1-RC).      
                      minimum: 0      
                      type: number      
                    is_disabled:      
                      description: 'Is the vehicle currently disabled (broken)? (added in v2.1-RC)'      
                      type: boolean      
                    is_reserved:      
                      description: 'Is the vehicle currently reserved for someone else? (added in v2.1-RC)'      
                      type: boolean      
                    vehicle_type_id:      
                      description: The vehicle_type_id of this vehicle as described in vehicle_types.json (added in v2.1-RC).      
                      type: string      
                  type: object      
                required:      
                  - bike_id      
                  - is_reserved      
                  - is_disabled      
                  - vehicle_type_id      
                type: array      
              vehicles_types_available:      
                description: Array of objects displaying the total number of each vehicle type at the station (added in v2.1-RC).      
                items:      
                  properties:      
                    count:      
                      description: A number representing the total amount of this vehicle type at the station (added in v2.1-RC).      
                      minimum: 0      
                      type: number      
                    vehicle_type_id:      
                      description: The vehicle_type_id of vehicle at the station (added in v2.1-RC).      
                      type: string      
                  type: object      
                type: array      
            type: object      
          required:      
            - station_id      
            - num_bikes_available      
            - is_installed      
            - is_renting      
            - is_returning      
            - last_reported      
          type: array      
      required:      
        - stations      
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
      description: NGSI entity type. It has to be station_status      
      enum:      
        - station_status      
      type: string      
      x-ngsi:      
        type: Property      
    version:      
      description: 'GBFS version number to which the feed conforms, according to the versioning framework (added in v1.1).'      
      enum:      
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
  x-license-url: https://github.com/smart-data-models/dataModel.GBFS/blob/master/station_status/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.GBFS/station_status/schema.json      
  x-model-tags: GBFS      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## ペイロードの例    
#### station_status NGSI-v2 キー値の例    
以下はstation_statusをJSON-LD形式でkey-valuesとした例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると、個々のエンティティのコンテキストデータを返す。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:station_status:id:FNNO:60592292",  
  "type": "station_status",  
  "last_updated": 1609866247,  
  "ttl": 0,  
  "version": "3.0",  
  "data": {  
    "stations": [  
      {  
        "station_id": "station1",  
        "is_installed": true,  
        "is_renting": true,  
        "is_returning": true,  
        "last_reported": 1609866125,  
        "num_docks_available": 3,  
        "vehicle_docks_available": [  
          {  
            "vehicle_type_ids": [  
              "abc123"  
            ],  
            "count": 2  
          },  
          {  
            "vehicle_type_ids": [  
              "def456"  
            ],  
            "count": 1  
          }  
        ],  
        "num_bikes_available": 1,  
        "vehicle_types_available": [  
          {  
            "vehicle_type_id": "abc123",  
            "count": 1  
          },  
          {  
            "vehicle_type_id": "def456",  
            "count": 0  
          }  
        ]  
      },  
      {  
        "station_id": "station2",  
        "is_installed": true,  
        "is_renting": true,  
        "is_returning": true,  
        "last_reported": 1609866106,  
        "num_docks_available": 8,  
        "vehicle_docks_available": [  
          {  
            "vehicle_type_ids": [  
              "abc123"  
            ],  
            "count": 6  
          },  
          {  
            "vehicle_type_ids": [  
              "def456"  
            ],  
            "count": 2  
          }  
        ],  
        "num_bikes_available": 6,  
        "vehicle_types_available": [  
          {  
            "vehicle_type_id": "abc123",  
            "count": 2  
          },  
          {  
            "vehicle_type_id": "def456",  
            "count": 4  
          }  
        ]  
      }  
    ]  
  }  
}  
```  
</details>    
#### station_status NGSI-v2 正規化例    
以下は、正規化された JSON-LD 形式の station_status の例である。これはNGSI-v2と互換性があり、オプションを使用せず、個々のエンティティのコンテキストデータを返す。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:station_status:id:FNNO:60592292",  
  "type": "station_status",  
  "last_updated": {  
    "type": "Number",  
    "value": 1609866247  
  },  
  "ttl": {  
    "type": "Boolean",  
    "value": false  
  },  
  "version": {  
    "type": "Text",  
    "value": "3.0"  
  },  
  "data": {  
    "type": "StructuredValue",  
    "value": {  
      "stations": [  
        {  
          "station_id": "station1",  
          "is_installed": true,  
          "is_renting": true,  
          "is_returning": true,  
          "last_reported": 1609866125,  
          "num_docks_available": 3,  
          "vehicle_docks_available": [  
            {  
              "vehicle_type_ids": [  
                "abc123"  
              ],  
              "count": 2  
            },  
            {  
              "vehicle_type_ids": [  
                "def456"  
              ],  
              "count": 1  
            }  
          ],  
          "num_bikes_available": 1,  
          "vehicle_types_available": [  
            {  
              "vehicle_type_id": "abc123",  
              "count": 1  
            },  
            {  
              "vehicle_type_id": "def456",  
              "count": 0  
            }  
          ]  
        },  
        {  
          "station_id": "station2",  
          "is_installed": true,  
          "is_renting": true,  
          "is_returning": true,  
          "last_reported": 1609866106,  
          "num_docks_available": 8,  
          "vehicle_docks_available": [  
            {  
              "vehicle_type_ids": [  
                "abc123"  
              ],  
              "count": 6  
            },  
            {  
              "vehicle_type_ids": [  
                "def456"  
              ],  
              "count": 2  
            }  
          ],  
          "num_bikes_available": 6,  
          "vehicle_types_available": [  
            {  
              "vehicle_type_id": "abc123",  
              "count": 2  
            },  
            {  
              "vehicle_type_id": "def456",  
              "count": 4  
            }  
          ]  
        }  
      ]  
    }  
  }  
}  
```  
</details>    
#### station_status NGSI-LD キー値の例    
以下はstation_statusをJSON-LD形式でkey-valuesとした例である。これは NGSI-LD と互換性があり、`options=keyValues` を使うと個々のエンティティのコンテキストデータを返す。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:station_status:id:FNNO:60592292",  
  "type": "station_status",  
  "last_updated": 1609866247,  
  "ttl": 0,  
  "version": "3.0",  
  "data": {  
    "stations": [  
      {  
        "station_id": "station1",  
        "is_installed": true,  
        "is_renting": true,  
        "is_returning": true,  
        "last_reported": 1609866125,  
        "num_docks_available": 3,  
        "vehicle_docks_available": [  
          {  
            "vehicle_type_ids": [  
              "abc123"  
            ],  
            "count": 2  
          },  
          {  
            "vehicle_type_ids": [  
              "def456"  
            ],  
            "count": 1  
          }  
        ],  
        "num_bikes_available": 1,  
        "vehicle_types_available": [  
          {  
            "vehicle_type_id": "abc123",  
            "count": 1  
          },  
          {  
            "vehicle_type_id": "def456",  
            "count": 0  
          }  
        ]  
      },  
      {  
        "station_id": "station2",  
        "is_installed": true,  
        "is_renting": true,  
        "is_returning": true,  
        "last_reported": 1609866106,  
        "num_docks_available": 8,  
        "vehicle_docks_available": [  
          {  
            "vehicle_type_ids": [  
              "abc123"  
            ],  
            "count": 6  
          },  
          {  
            "vehicle_type_ids": [  
              "def456"  
            ],  
            "count": 2  
          }  
        ],  
        "num_bikes_available": 6,  
        "vehicle_types_available": [  
          {  
            "vehicle_type_id": "abc123",  
            "count": 2  
          },  
          {  
            "vehicle_type_id": "def456",  
            "count": 4  
          }  
        ]  
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
#### station_status NGSI-LD 正規化例    
以下は、正規化された JSON-LD 形式の station_status の例である。これは、オプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:station_status:id:FNNO:60592292",  
    "type": "station_status",  
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
            "stations": [  
                {  
                    "station_id": "station1",  
                    "is_installed": true,  
                    "is_renting": true,  
                    "is_returning": true,  
                    "last_reported": 1609866125,  
                    "num_docks_available": 3,  
                    "vehicle_docks_available": [  
                        {  
                            "vehicle_type_ids": [  
                                "abc123"  
                            ],  
                            "count": 2  
                        },  
                        {  
                            "vehicle_type_ids": [  
                                "def456"  
                            ],  
                            "count": 1  
                        }  
                    ],  
                    "num_bikes_available": 1,  
                    "vehicle_types_available": [  
                        {  
                            "vehicle_type_id": "abc123",  
                            "count": 1  
                        },  
                        {  
                            "vehicle_type_id": "def456",  
                            "count": 0  
                        }  
                    ]  
                },  
                {  
                    "station_id": "station2",  
                    "is_installed": true,  
                    "is_renting": true,  
                    "is_returning": true,  
                    "last_reported": 1609866106,  
                    "num_docks_available": 8,  
                    "vehicle_docks_available": [  
                        {  
                            "vehicle_type_ids": [  
                                "abc123"  
                            ],  
                            "count": 6  
                        },  
                        {  
                            "vehicle_type_ids": [  
                                "def456"  
                            ],  
                            "count": 2  
                        }  
                    ],  
                    "num_bikes_available": 6,  
                    "vehicle_types_available": [  
                        {  
                            "vehicle_type_id": "abc123",  
                            "count": 2  
                        },  
                        {  
                            "vehicle_type_id": "def456",  
                            "count": 4  
                        }  
                    ]  
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
