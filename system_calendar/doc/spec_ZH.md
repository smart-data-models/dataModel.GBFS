<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：System_calendar  
==================<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.GBFS/blob/master/system_calendar/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述。**描述了一个系统的操作日历。根据标准GBFS 2.2**的规定  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `data[object]`: 包含系统操作日历的数组。  - `id[*]`: 实体的唯一标识符  - `last_updated[integer]`: 饲料中的数据最后一次在POSIX时间内被更新。  - `ttl[integer]`: 饲料中的数据将被再次更新之前的秒数（如果数据应始终被刷新，则为0）。  - `type[string]`: NGSI实体类型。它必须是system_calendar  - `version[string]`: 根据版本框架，饲料符合的GBFS版本号（在v1.1版中添加）。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `data`  - `id`  - `last_updated`  - `ttl`  - `type`  - `version`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
标准的映射[GBFS 2.2](https://github.com/NABSA/gbfs/blob/v2.2/gbfs.md)  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
system_calendar:    
  description: 'Describes the operating calendar for a system. According to the Standard GBFS 2.2'    
  properties:    
    data:    
      description: 'Array that contains opertions calendar for the system.'    
      properties:    
        calendars:    
          items:    
            properties:    
              end_day:    
                description: 'End day for the system operations.'    
                maximum: 31    
                minimum: 1    
                type: number    
              end_month:    
                description: 'End month for the system operations.'    
                maximum: 12    
                minimum: 1    
                type: number    
              end_year:    
                description: 'End year for the system operations.'    
                pattern: ^\d{4}$    
                type: number    
              start_day:    
                description: 'Starting day for the system operations.'    
                maximum: 31    
                minimum: 1    
                type: number    
              start_month:    
                description: 'Starting month for the system operations.'    
                maximum: 12    
                minimum: 1    
                type: number    
              start_year:    
                description: 'Starting year for the system operations.'    
                pattern: ^\d{4}$    
                type: number    
            required:    
              - start_month    
              - start_day    
              - end_month    
              - end_day    
            type: object    
          type: array    
      required:    
        - calendars    
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
      description: 'NGSI entity type. It has to be system_calendar'    
      enum:    
        - system_calendar    
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
  x-license-url: https://github.com/smart-data-models/dataModel.GBFS/blob/master/system_calendar/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.GBFS/system_calendar/schema.json    
  x-model-tags: GBFS    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
#### system_calendar NGSI-v2 key-values 示例  
这里是一个以JSON-LD格式作为key-values的system_calendar的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:system_calendar:id:FNNO:60592292",  
  "type": "system_calendar",  
  "last_updated": 1604333830,  
  "ttl": 86400,  
  "version": "3.0",  
  "data": {  
    "calendars": [  
      {  
        "start_month": 4,  
        "start_day": 1,  
        "start_year": 2020,  
        "end_month": 11,  
        "end_day": 5,  
        "end_year": 2020  
      }  
    ]  
  }  
}  
```  
</details>  
#### system_calendar NGSI-v2 normalized 示例  
下面是一个以JSON-LD格式规范化的system_calendar的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:system_calendar:id:FNNO:60592292",  
  "type": "system_calendar",  
  "last_updated": {  
    "type": "Number",  
    "value": 1604333830  
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
      "calendars": [  
        {  
          "start_month": 4,  
          "start_day": 1,  
          "start_year": 2020,  
          "end_month": 11,  
          "end_day": 5,  
          "end_year": 2020  
        }  
      ]  
    }  
  }  
}  
```  
</details>  
#### system_calendar NGSI-LD key-values 示例  
这里是一个以JSON-LD格式作为key-values的system_calendar的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:system_calendar:id:FNNO:60592292",  
    "type": "system_calendar",  
    "last_updated": 1604333830,  
    "ttl": 86400,  
    "version": "3.0",  
    "data": {  
        "calendars": [  
            {  
                "start_month": 4,  
                "start_day": 1,  
                "start_year": 2020,  
                "end_month": 11,  
                "end_day": 5,  
                "end_year": 2020  
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
#### system_calendar NGSI-LD规范化示例  
下面是一个以JSON-LD格式规范化的system_calendar的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:system_calendar:id:FNNO:60592292",  
    "type": "system_calendar",  
    "last_updated": {  
        "type": "Property",  
        "value": 1604333830  
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
            "calendars": [  
                {  
                    "start_month": 4,  
                    "start_day": 1,  
                    "start_year": 2020,  
                    "end_month": 11,  
                    "end_day": 5,  
                    "end_year": 2020  
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
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
