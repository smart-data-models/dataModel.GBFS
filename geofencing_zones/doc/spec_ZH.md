<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
实体：地理围栏区    
========<!-- /10-Header -->    
<!-- 15-License -->    
[开放许可](https://github.com/smart-data-models//dataModel.GBFS/blob/master/geofencing_zones/LICENSE.md)    
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
全局描述：**描述地理围栏区域及其相关规则和属性（在 v2.1-RC 中添加）。根据 GBFS 2.2 标准**    
版本： 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 属性列表    
<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。    
- `data[object]`: 包含系统地理围栏信息的数组。  	    
- `id[*]`: 实体的唯一标识符  - `last_updated[integer]`: 在 POSIX 时间内，Feed 中数据的最后一次更新时间。  - `ttl[integer]`: 数据源中的数据再次更新前的秒数（如果数据应始终刷新，则为 0）。  - `type[string]`: NGSI 实体类型。必须是 geofencing_zones  - `version[string]`: 根据版本框架，馈送符合的 GBFS 版本号。  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
所需属性    
- `data`  - `id`  - `last_updated`  - `ttl`  - `type`  - `version`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
标准的映射[GBFS 2.2](https://github.com/NABSA/gbfs/blob/v2.2/gbfs.md)    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 属性的数据模型描述    
按字母顺序排列（点击查看详情）    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
geofencing_zones:      
  description: Describes geofencing zones and their associated rules and attributes (added in v2.1-RC). According to the Standard GBFS 2.2      
  properties:      
    data:      
      description: Array that contains geofencing information for the system.      
      properties:      
        geofencing_zones:      
          description: Each geofenced zone and its associated rules and attributes is described as an object within the array of features.      
          properties:      
            features:      
              description: Array of objects.      
              items:      
                properties:      
                  geometry:      
                    description: 'A polygon that describes where rides might not be able to start, end, go through, or have otehr limitations. Must follow the right-hand rule.'      
                    properties:      
                      coordinates:      
                      type:      
                    required:      
                      - type      
                      - coordinates      
                    title: GeoJSON MultiPolygon      
                    type: object      
                  properties:      
                    description: Describing travel allowances and limitations.      
                    properties:      
                      end:      
                      name:      
                      rules:      
                      start:      
                    type: object      
                  type:      
                    enum:      
                      - Feature      
                    type: string      
                required:      
                  - type      
                  - geometry      
                  - properties      
                title: GeoJSON Feature      
                type: object      
              type: array      
            type:      
              description: FeatureCollection as per IETF RFC 7946.      
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
      description: NGSI entity type. It has to be geofencing_zones      
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
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
## 有效载荷示例    
#### geofencing_zones NGSI-v2 键值示例    
下面是一个以 JSON-LD 格式作为键值的 geofencing_zones 示例。当使用 `options=keyValues` 时，这与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
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
  }  
}  
```  
</details>    
#### geofencing_zones NGSI-v2 标准化示例    
下面是一个规范化 JSON-LD 格式的 geofencing_zones 示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
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
  }  
}  
```  
</details>    
#### geofencing_zones NGSI-LD 键值示例    
下面是一个以 JSON-LD 格式作为键值的 geofencing_zones 示例。当使用 `options=keyValues` 时，这与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
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
#### geofencing_zones NGSI-LD 归一化示例    
下面是一个规范化 JSON-LD 格式的 geofencing_zones 示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
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
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
