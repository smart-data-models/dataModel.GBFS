<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティ：Geofencing_zones  
=======================<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.GBFS/blob/master/geofencing_zones/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述。**ジオフェンシングゾーンとそれに関連するルールや属性を記述する（v2.1-RC で追加）。標準GBFS2.2による**。  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性にタイプがない場合、複数のタイプまたは異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `data[object]`: システムのジオフェンシング情報を含む配列。  - `id[*]`: エンティティの一意な識別子  - `last_updated[integer]`: フィードのデータが POSIX 時間で最後に更新された時刻。  - `ttl[integer]`: フィードのデータが再び更新されるまでの秒数（常にデータを更新する場合は0）。  - `type[string]`: NGSIエンティティタイプ。geofencing_zones である必要があります。  - `version[string]`: フィードが準拠しているGBFSのバージョン番号（バージョン管理フレームワークによる。  <!-- /30-PropertiesList -->  
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
geofencing_zones:    
  description: 'Describes geofencing zones and their associated rules and attributes (added in v2.1-RC). According to the Standard GBFS 2.2'    
  properties:    
    data:    
      description: 'Array that contains geofencing information for the system.'    
      properties:    
        geofencing_zones:    
          description: 'Each geofenced zone and its associated rules and attributes is described as an object within the array of features.'    
          properties:    
            features:    
              description: 'Array of objects.'    
              items:    
                properties:    
                  geometry:    
                    description: 'A polygon that describes where rides might not be able to start, end, go through, or have otehr limitations. Must follow the right-hand rule.'    
                    properties:    
                      coordinates:    
                        items:    
                          items:    
                            items:    
                              items:    
                                type: number    
                              minItems: 2    
                              type: array    
                            minItems: 4    
                            type: array    
                          type: array    
                        type: array    
                      type:    
                        enum:    
                          - MultiPolygon    
                        type: string    
                    required:    
                      - type    
                      - coordinates    
                    title: 'GeoJSON MultiPolygon'    
                    type: object    
                  properties:    
                    description: 'Describing travel allowances and limitations.'    
                    properties:    
                      end:    
                        description: 'End time of the geofencing zone in POSIX time.'    
                        minimum: 1450155600    
                        type: number    
                      name:    
                        description: 'Public name of the geofencing zone.'    
                        type: string    
                      rules:    
                        description: 'Array that contains one object per rule.'    
                        items:    
                          properties:    
                            maximum_speed_kph:    
                              description: 'What is the maximum speed allowed, in kilometers per hour?'    
                              minimum: 0    
                              type: number    
                            ride_allowed:    
                              description: 'Is the undocked ride allowed to stat and end in this zone?'    
                              type: boolean    
                            ride_through_allowed:    
                              description: 'Is the ride allowed to travel through this zone?'    
                              type: boolean    
                            vehicle_type_id:    
                              description: 'Array of vehicle type IDs for which these restrictions apply.'    
                              items:    
                                type: string    
                              type: array    
                          required:    
                            - ride_allowed    
                            - ride_through_allowed    
                          type: object    
                        type: array    
                      start:    
                        description: 'Start time of the geofencing zone in POSIX time.'    
                        minimum: 1450155600    
                        type: number    
                    type: object    
                  type:    
                    enum:    
                      - Feature    
                    type: string    
                required:    
                  - type    
                  - geometry    
                  - properties    
                title: 'GeoJSON Feature'    
                type: object    
              type: array    
            type:    
              description: 'FeatureCollection as per IETF RFC 7946.'    
              enum:    
                - FeatureCollection    
              type: string    
          required:    
            - type    
            - features    
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
      description: 'NGSI entity type. It has to be geofencing_zones'    
      enum:    
        - geofencing_zones    
      type: string    
      x-ngsi:    
        type: Property    
    version:    
      description: 'GBFS version number to which the feed conforms, according to the versioning framework.'    
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
    - id    
    - data    
    - last_updated    
    - ttl    
    - type    
    - version    
  type: object    
  x-derived-from: https://github.com/NABSA/gbfs/blob/v2.2/gbfs.md    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.GBFS/blob/master/geofencing_zones/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.GBFS/geofencing_zones/schema.json    
  x-model-tags: GBFS    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### geofencing_zones NGSI-v2 key-value 例  
以下は、geofencing_zones を JSON-LD 形式で key-value にした例です。これは `options=keyValues` を使用した場合に NGSI-v2 と互換性があり、個々のエンティティのコンテキストデータが返されます。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:geofencing_zones:id:FNNO:60592292",  
  "type": "geofencing_zones",  
  "last_updated": 1604198100,  
  "ttl": 60,  
  "version": "3.0",  
  "data": {  
    "geofencing_zones": {  
      "type": "FeatureCollection",  
      "features": [  
        {  
          "type": "Feature",  
          "geometry": {  
            "type": "MultiPolygon",  
            "coordinates": [  
              [  
                [  
                  [  
                    -122.578067,  
                    45.562982  
                  ],  
                  [  
                    -122.661838,  
                    45.562741  
                  ],  
                  [  
                    -122.661151,  
                    45.504542  
                  ],  
                  [  
                    -122.578926,  
                    45.5046625  
                  ],  
                  [  
                    -122.578067,  
                    45.562982  
                  ]  
                ]  
              ],  
              [  
                [  
                  [  
                    -122.650680,  
                    45.548197  
                  ],  
                  [  
                    -122.650852,  
                    45.534731  
                  ],  
                  [  
                    -122.630939,  
                    45.535212  
                  ],  
                  [  
                    -122.630424,  
                    45.548197  
                  ],  
                  [  
                    -122.650680,  
                    45.548197  
                  ]  
                ]  
              ]  
            ]  
          },  
          "properties": {  
            "name": "NE 24th/NE Knott",  
            "start": 1593878400,  
            "end": 1593907260,  
            "rules": [  
              {  
                "vehicle_type_id": [  
                  "moped1",  
                  "car1"  
                ],  
                "ride_allowed": false,  
                "ride_through_allowed": true,  
                "maximum_speed_kph": 10  
              }  
            ]  
          }  
        }  
      ]  
    }  
  }  
}  
```  
</details>  
#### geofencing_zones NGSI-v2 正規化例  
以下は、JSON-LD 形式で正規化された geofencing_zones の例です。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:geofencing_zones:id:FNNO:60592292",  
  "type": "geofencing_zones",  
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
      "geofencing_zones": {  
        "type": "FeatureCollection",  
        "features": [  
          {  
            "type": "Feature",  
            "geometry": {  
              "type": "MultiPolygon",  
              "coordinates": [  
                [  
                  [  
                    [  
                      -122.578067,  
                      45.562982  
                    ],  
                    [  
                      -122.661838,  
                      45.562741  
                    ],  
                    [  
                      -122.661151,  
                      45.504542  
                    ],  
                    [  
                      -122.578926,  
                      45.5046625  
                    ],  
                    [  
                      -122.578067,  
                      45.562982  
                    ]  
                  ]  
                ],  
                [  
                  [  
                    [  
                      -122.650680,  
                      45.548197  
                    ],  
                    [  
                      -122.650852,  
                      45.534731  
                    ],  
                    [  
                      -122.630939,  
                      45.535212  
                    ],  
                    [  
                      -122.630424,  
                      45.548197  
                    ],  
                    [  
                      -122.650680,  
                      45.548197  
                    ]  
                  ]  
                ]  
              ]  
            },  
            "properties": {  
              "name": "NE 24th/NE Knott",  
              "start": 1593878400,  
              "end": 1593907260,  
              "rules": [  
                {  
                  "vehicle_type_id": [  
                    "moped1",  
                    "car1"  
                  ],  
                  "ride_allowed": false,  
                  "ride_through_allowed": true,  
                  "maximum_speed_kph": 10  
                }  
              ]  
            }  
          }  
        ]  
      }  
    }  
  }  
}  
```  
</details>  
#### geofencing_zones NGSI-LD キー値例  
ここでは、geofencing_zonesをJSON-LD形式でkey-valuesとした例を示します。これは `options=keyValues` を使用した場合に NGSI-LD と互換性があり、個々のエンティティのコンテキストデータが返されます。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:geofencing_zones:id:FNNO:60592292",  
    "type": "geofencing_zones",  
    "last_updated": 1604198100,  
    "ttl": 60,  
    "version": "3.0",  
    "data": {  
        "geofencing_zones": {  
            "type": "FeatureCollection",  
            "features": [  
                {  
                    "type": "Feature",  
                    "geometry": {  
                        "type": "MultiPolygon",  
                        "coordinates": [  
                            [  
                                [  
                                    [  
                                        -122.578067,  
                                        45.562982  
                                    ],  
                                    [  
                                        -122.661838,  
                                        45.562741  
                                    ],  
                                    [  
                                        -122.661151,  
                                        45.504542  
                                    ],  
                                    [  
                                        -122.578926,  
                                        45.5046625  
                                    ],  
                                    [  
                                        -122.578067,  
                                        45.562982  
                                    ]  
                                ]  
                            ],  
                            [  
                                [  
                                    [  
                                        -122.65068,  
                                        45.548197  
                                    ],  
                                    [  
                                        -122.650852,  
                                        45.534731  
                                    ],  
                                    [  
                                        -122.630939,  
                                        45.535212  
                                    ],  
                                    [  
                                        -122.630424,  
                                        45.548197  
                                    ],  
                                    [  
                                        -122.65068,  
                                        45.548197  
                                    ]  
                                ]  
                            ]  
                        ]  
                    },  
                    "properties": {  
                        "name": "NE 24th/NE Knott",  
                        "start": 1593878400,  
                        "end": 1593907260,  
                        "rules": [  
                            {  
                                "vehicle_type_id": [  
                                    "moped1",  
                                    "car1"  
                                ],  
                                "ride_allowed": false,  
                                "ride_through_allowed": true,  
                                "maximum_speed_kph": 10  
                            }  
                        ]  
                    }  
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
</details>  
#### geofencing_zones NGSI-LD 正規化例  
以下は、JSON-LD 形式の geofencing_zones を正規化した例です。これはオプションを使用しない場合、NGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:geofencing_zones:id:FNNO:60592292",  
    "type": "geofencing_zones",  
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
            "geofencing_zones": {  
                "type": "FeatureCollection",  
                "features": [  
                    {  
                        "type": "Feature",  
                        "geometry": {  
                            "type": "MultiPolygon",  
                            "coordinates": [  
                                [  
                                    [  
                                        [  
                                            -122.578067,  
                                            45.562982  
                                        ],  
                                        [  
                                            -122.661838,  
                                            45.562741  
                                        ],  
                                        [  
                                            -122.661151,  
                                            45.504542  
                                        ],  
                                        [  
                                            -122.578926,  
                                            45.5046625  
                                        ],  
                                        [  
                                            -122.578067,  
                                            45.562982  
                                        ]  
                                    ]  
                                ],  
                                [  
                                    [  
                                        [  
                                            -122.65068,  
                                            45.548197  
                                        ],  
                                        [  
                                            -122.650852,  
                                            45.534731  
                                        ],  
                                        [  
                                            -122.630939,  
                                            45.535212  
                                        ],  
                                        [  
                                            -122.630424,  
                                            45.548197  
                                        ],  
                                        [  
                                            -122.65068,  
                                            45.548197  
                                        ]  
                                    ]  
                                ]  
                            ]  
                        },  
                        "properties": {  
                            "name": "NE 24th/NE Knott",  
                            "start": 1593878400,  
                            "end": 1593907260,  
                            "rules": [  
                                {  
                                    "vehicle_type_id": [  
                                        "moped1",  
                                        "car1"  
                                    ],  
                                    "ride_allowed": false,  
                                    "ride_through_allowed": true,  
                                    "maximum_speed_kph": 10  
                                }  
                            ]  
                        }  
                    }  
                ]  
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
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
