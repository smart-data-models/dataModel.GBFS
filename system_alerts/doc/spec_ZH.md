<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：系统警报  
=======<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.GBFS/blob/master/system_alerts/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述：**描述对系统的临时更改。根据 GBFS 2.2 标准**  
版本： 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 属性列表  

<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。  
- `data[object]`: 包含系统临时警报的阵列。  	  
- `id[*]`: 实体的唯一标识符  - `last_updated[integer]`: 在 POSIX 时间内，Feed 中数据的最后一次更新时间。  - `ttl[integer]`: 数据源中的数据再次更新前的秒数（如果数据应始终刷新，则为 0）。  - `type[string]`: NGSI 实体类型。必须是 system_alerts  - `version[string]`: 根据版本框架（在版本 1.1 中添加），馈送符合的 GBFS 版本号。  <!-- /30-PropertiesList -->  
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
system_alerts:    
  description: Describes ad-hoc changes to the system. According to the Standard GBFS 2.2    
  properties:    
    data:    
      description: Array that contains ad-hoc alerts for the system.    
      properties:    
        alerts:    
          items:    
            properties:    
              alert_id:    
                description: Identifier for this alert.    
                type: string    
              description:    
                description: Detailed description of the alert.    
                type: string    
              last_updated:    
                description: Indicates the last time the info for the alert was updated.    
                minimum: 1450155600    
                type: number    
              region_ids:    
                description: Array of identifiers of the regions for which this alert applies.    
                items:    
                  type: string    
                type: array    
              station_ids:    
                description: Array of identifiers of the stations for which this alert applies.    
                items:    
                  type: string    
                type: array    
              summary:    
                description: A short summary of this alert to be displayed to the customer.    
                type: string    
              times:    
                additionalItems: false    
                description: Array of objects indicating when the alert is in effect.    
                items:    
                  properties:    
                    end:    
                      description: End time of the alert.    
                      minimum: 1450155600    
                      type: number    
                    start:    
                      description: Start time of the alert.    
                      minimum: 1450155600    
                      type: number    
                  type: object    
                required:    
                  - start    
                type: array    
              type:    
                description: Type of alert.    
                enum:    
                  - system_closure    
                  - station_closure    
                  - station_move    
                  - other    
                type: string    
              url:    
                description: URL where the customer can learn more information about this alert.    
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
      description: NGSI entity type. It has to be system_alerts    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
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
## 有效载荷示例  
#### system_alerts NGSI-v2 key-values 示例  
下面是一个以 JSON-LD 格式作为键值的 system_alerts 实例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
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
#### system_alerts NGSI-v2 标准化示例  
下面是一个以 JSON-LD 格式规范化的 system_alerts 实例。当不使用选项时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
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
#### system_alerts NGSI-LD 关键值 示例  
下面是一个以 JSON-LD 格式作为键值的 system_alerts 实例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
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
#### system_alerts NGSI-LD 标准化示例  
下面是一个规范化 JSON-LD 格式的 system_alerts 示例。当不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
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
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
