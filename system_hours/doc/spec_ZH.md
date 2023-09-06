<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：系统小时  
=======<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.GBFS/blob/master/system_hours/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述：**描述系统运行时间。根据 GBFS 2.2 标准**  
版本： 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 属性列表  

<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。  
- `data[object]`: 包含系统运行小时数的数组。  	  
- `id[*]`: 实体的唯一标识符  - `last_updated[integer]`: 在 POSIX 时间内，Feed 中数据的最后一次更新时间。  - `ttl[integer]`: 数据源中的数据再次更新前的秒数（如果数据应始终刷新，则为 0）。  - `type[string]`: NGSI 实体类型。必须是 system_hours  - `version[string]`: 根据版本框架（在版本 1.1 中添加），馈送符合的 GBFS 版本号。  <!-- /30-PropertiesList -->  
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
system_hours:    
  description: Describes the system hours of operation. According to the Standard GBFS 2.2    
  properties:    
    data:    
      description: Array that contains system hours of operations.    
      properties:    
        rental_hours:    
          items:    
            properties:    
              days:    
                description: An array of abbreviations (first 3 letters) of English names of the days of the week for which this object applies.    
                items:    
                  enum:    
                    - sun    
                    - mon    
                    - tue    
                    - wed    
                    - thu    
                    - fri    
                    - sat    
                  type: string    
                maxItems: 7    
                minItems: 1    
                type: array    
              end_time:    
                description: End time for the hours of operation of the system.    
                pattern: ^([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$    
                type: string    
              start_time:    
                description: Start time for the hours of operation of the system.    
                pattern: ^([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$    
                type: string    
              user_types:    
                description: Array of member and nonmember value(s) indicating that this set of rental hours applies to either members or non-members only.    
                items:    
                  enum:    
                    - member    
                    - nonmember    
                  type: string    
                maxItems: 2    
                minItems: 1    
                type: array    
            required:    
              - user_types    
              - days    
              - start_time    
              - end_time    
            type: object    
          type: array    
      required:    
        - rental_hours    
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
      description: NGSI entity type. It has to be system_hours    
      enum:    
        - system_hours    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.GBFS/blob/master/system_hours/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.GBFS/system_hours/schema.json    
  x-model-tags: GBFS    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 有效载荷示例  
#### system_hours NGSI-v2 关键值 示例  
下面是一个以 JSON-LD 格式作为键值的 system_hours 示例。当使用 `options=keyValues` 时，这与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:system_hours:id:FNNO:60592292",  
  "type": "system_hours",  
  "last_updated": 1609866247,  
  "ttl": 86400,  
  "version": "3.0",  
  "data": {  
    "rental_hours": [  
      {  
        "user_types": [  
          "member"  
        ],  
        "days": [  
          "sat",  
          "sun"  
        ],  
        "start_time": "00:00:00",  
        "end_time": "23:59:59"  
      },  
      {  
        "user_types": [  
          "nonmember"  
        ],  
        "days": [  
          "sat",  
          "sun"  
        ],  
        "start_time": "05:00:00",  
        "end_time": "23:59:59"  
      },  
      {  
        "user_types": [  
          "member",  
          "nonmember"  
        ],  
        "days": [  
          "mon",  
          "tue",  
          "wed",  
          "thu",  
          "fri"  
        ],  
        "start_time": "00:00:00",  
        "end_time": "23:59:59"  
      }  
    ]  
  }  
}  
```  
</details>  
#### system_hours NGSI-v2 归一化示例  
下面是一个规范化 JSON-LD 格式的 system_hours 示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:system_hours:id:FNNO:60592292",  
  "type": "system_hours",  
  "last_updated": {  
    "type": "Number",  
    "value": 1609866247  
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
      "rental_hours": [  
        {  
          "user_types": [  
            "member"  
          ],  
          "days": [  
            "sat",  
            "sun"  
          ],  
          "start_time": "00:00:00",  
          "end_time": "23:59:59"  
        },  
        {  
          "user_types": [  
            "nonmember"  
          ],  
          "days": [  
            "sat",  
            "sun"  
          ],  
          "start_time": "05:00:00",  
          "end_time": "23:59:59"  
        },  
        {  
          "user_types": [  
            "member",  
            "nonmember"  
          ],  
          "days": [  
            "mon",  
            "tue",  
            "wed",  
            "thu",  
            "fri"  
          ],  
          "start_time": "00:00:00",  
          "end_time": "23:59:59"  
        }  
      ]  
    }  
  }  
}  
```  
</details>  
#### system_hours NGSI-LD 关键值 示例  
下面是一个以 JSON-LD 格式作为键值的 system_hours 示例。当使用 `options=keyValues` 时，这与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:system_hours:id:FNNO:60592292",  
    "type": "system_hours",  
    "last_updated": 1609866247,  
    "ttl": 86400,  
    "version": "3.0",  
    "data": {  
        "rental_hours": [  
            {  
                "user_types": [  
                    "member"  
                ],  
                "days": [  
                    "sat",  
                    "sun"  
                ],  
                "start_time": "00:00:00",  
                "end_time": "23:59:59"  
            },  
            {  
                "user_types": [  
                    "nonmember"  
                ],  
                "days": [  
                    "sat",  
                    "sun"  
                ],  
                "start_time": "05:00:00",  
                "end_time": "23:59:59"  
            },  
            {  
                "user_types": [  
                    "member",  
                    "nonmember"  
                ],  
                "days": [  
                    "mon",  
                    "tue",  
                    "wed",  
                    "thu",  
                    "fri"  
                ],  
                "start_time": "00:00:00",  
                "end_time": "23:59:59"  
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
#### system_hours NGSI-LD 归一化示例  
下面是一个规范化 JSON-LD 格式的 system_hours 示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:system_hours:id:FNNO:60592292",  
    "type": "system_hours",  
    "last_updated": {  
        "type": "Property",  
        "value": 1609866247  
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
            "rental_hours": [  
                {  
                    "user_types": [  
                        "member"  
                    ],  
                    "days": [  
                        "sat",  
                        "sun"  
                    ],  
                    "start_time": "00:00:00",  
                    "end_time": "23:59:59"  
                },  
                {  
                    "user_types": [  
                        "nonmember"  
                    ],  
                    "days": [  
                        "sat",  
                        "sun"  
                    ],  
                    "start_time": "05:00:00",  
                    "end_time": "23:59:59"  
                },  
                {  
                    "user_types": [  
                        "member",  
                        "nonmember"  
                    ],  
                    "days": [  
                        "mon",  
                        "tue",  
                        "wed",  
                        "thu",  
                        "fri"  
                    ],  
                    "start_time": "00:00:00",  
                    "end_time": "23:59:59"  
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
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
