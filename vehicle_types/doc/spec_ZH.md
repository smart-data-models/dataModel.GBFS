<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体: 车辆_类型  
=========<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.GBFS/blob/master/vehicle_types/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述。**描述系统运营商可供出租的车辆类型（在V2.1-RC版中添加）。根据标准GBFS 2.2**的规定  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `data[object]`: 响应数据的形式为名称：值对。  - `id[*]`: 实体的唯一标识符  - `last_updated[integer]`: 饲料中的数据最后一次在POSIX时间内被更新。  - `ttl[integer]`: 饲料中的数据将被再次更新之前的秒数（如果数据应始终被刷新，则为0）。  - `type[string]`: NGSI实体类型。它必须是 vehicle_types  - `version[string]`: 根据版本框架，该饲料符合的GBFS版本号。  <!-- /30-PropertiesList -->  
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
vehicle_types:    
  description: 'Describes the types of vehicles that System operator has available for rent (added in v2.1-RC). According to the Standard GBFS 2.2'    
  properties:    
    data:    
      description: 'Response data in the form of name:value pairs.'    
      properties:    
        vehicle_types:    
          description: 'Array that contains one object per vehicle type in the system as defined below.'    
          if:    
            properties:    
              propulsion_type:    
                const:    
                  - electric    
                  - electric_assist    
                  - combustion    
          items:    
            properties:    
              form_factor:    
                description: 'The vehicle''s general form factor.'    
                enum:    
                  - bicycle    
                  - car    
                  - moped    
                  - other    
                  - scooter    
                type: string    
              max_range_meters:    
                description: 'The furthest distance in meters that the vehicle can travel without recharging or refueling when it has the maximum amount of energy potential.'    
                minimum: 0    
                type: number    
              name:    
                description: 'The public name of this vehicle type.'    
                type: string    
              propulsion_type:    
                description: 'The primary propulsion type of the vehicle.'    
                enum:    
                  - human    
                  - electric_assist    
                  - electric    
                  - combustion    
                type: string    
              vehicle_type_id:    
                description: 'Unique identifier of a vehicle type.'    
                type: string    
            required:    
              - vehicle_type_id    
              - form_factor    
              - propulsion_type    
            type: object    
          then:    
            properties:    
              max_range_meters:    
                required:    
                  - max_range_meters    
          type: array    
      required:    
        - vehicle_types    
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
      description: 'NGSI entity type. It has to be vehicle_types'    
      enum:    
        - vehicle_types    
      type: string    
      x-ngsi:    
        type: Property    
    version:    
      description: 'GBFS version number to which the feed conforms, according to the versioning framework.'    
      enum:    
        - 2.1-RC    
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
  x-license-url: https://github.com/smart-data-models/dataModel.GBFS/blob/master/vehicle_types/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.GBFS/vehicle_types/schema.json    
  x-model-tags: GBFS    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
#### vehicle_types NGSI-v2 key-values 示例  
这里是一个以JSON-LD格式作为key-values的vehicle_types的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:vehicle_types:id:FNNO:60592292",  
  "type": "vehicle_types",  
  "last_updated": 1609866247,  
  "ttl": 0,  
  "version": "3.0",  
  "data": {  
    "vehicle_types": [  
      {  
        "vehicle_type_id": "abc123",  
        "form_factor": "bicycle",  
        "propulsion_type": "human",  
        "name": "Example Basic Bike",  
        "default_reserve_time": 30,  
        "return_type": [  
          "any_station",  
          "free_floating"  
        ],  
        "vehicle_assets": {  
          "icon_url": "https://www.example.com/assets/icon_bicycle.svg",  
          "icon_url_dark": "https://www.example.com/assets/icon_bicycle_dark.svg",  
          "icon_last_modified": "2021-06-15"  
        },  
        "default_pricing_plan_id": "bike_plan_1",  
        "pricing_plan_ids": [  
          "bike_plan_1",  
          "bike_plan_2",  
          "bike_plan_3"  
        ]  
      },  
      {  
        "vehicle_type_id": "def456",  
        "form_factor": "scooter",  
        "propulsion_type": "electric",  
        "name": "Example E-scooter V2",  
        "default_reserve_time": 30,  
        "max_range_meters": 12345,  
        "return_type": [  
          "free_floating"  
        ],  
        "vehicle_assets": {  
          "icon_url": "https://www.example.com/assets/icon_escooter.svg",  
          "icon_url_dark": "https://www.example.com/assets/icon_escooter_dark.svg",  
          "icon_last_modified": "2021-06-15"  
        },  
        "default_pricing_plan_id": "scooter_plan_1"  
      },  
      {  
        "vehicle_type_id": "car1",  
        "form_factor": "car",  
        "propulsion_type": "combustion",  
        "name": "Four-door Sedan",  
        "default_reserve_time": 0,  
        "max_range_meters": 523992,  
        "return_type": [  
          "roundtrip_station"  
        ],  
        "vehicle_assets": {  
          "icon_url": "https://www.example.com/assets/icon_car.svg",  
          "icon_url_dark": "https://www.example.com/assets/icon_car_dark.svg",  
          "icon_last_modified": "2021-06-15"  
        },  
        "default_pricing_plan_id": "car_plan_1"  
      }  
    ]  
  }  
}  
```  
</details>  
#### vehicle_types NGSI-v2 normalized 示例  
下面是一个规范化的JSON-LD格式的vehicle_types的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:vehicle_types:id:FNNO:60592292",  
  "type": "vehicle_types",  
  "last_updated": {  
    "type": "Number",  
    "value": 1609866247  
  },  
  "ttl": {  
    "type": "Number",  
    "value": 0  
  },  
  "version": {  
    "type": "Text",  
    "value": "3.0"  
  },  
  "data": {  
    "type": "StructuredValue",  
    "value": {  
      "vehicle_types": [  
        {  
          "vehicle_type_id": "abc123",  
          "form_factor": "bicycle",  
          "propulsion_type": "human",  
          "name": "Example Basic Bike",  
          "default_reserve_time": 30,  
          "return_type": [  
            "any_station",  
            "free_floating"  
          ],  
          "vehicle_assets": {  
            "icon_url": "https://www.example.com/assets/icon_bicycle.svg",  
            "icon_url_dark": "https://www.example.com/assets/icon_bicycle_dark.svg",  
            "icon_last_modified": "2021-06-15"  
          },  
          "default_pricing_plan_id": "bike_plan_1",  
          "pricing_plan_ids": [  
            "bike_plan_1",  
            "bike_plan_2",  
            "bike_plan_3"  
          ]  
        },  
        {  
          "vehicle_type_id": "def456",  
          "form_factor": "scooter",  
          "propulsion_type": "electric",  
          "name": "Example E-scooter V2",  
          "default_reserve_time": 30,  
          "max_range_meters": 12345,  
          "return_type": [  
            "free_floating"  
          ],  
          "vehicle_assets": {  
            "icon_url": "https://www.example.com/assets/icon_escooter.svg",  
            "icon_url_dark": "https://www.example.com/assets/icon_escooter_dark.svg",  
            "icon_last_modified": "2021-06-15"  
          },  
          "default_pricing_plan_id": "scooter_plan_1"  
        },  
        {  
          "vehicle_type_id": "car1",  
          "form_factor": "car",  
          "propulsion_type": "combustion",  
          "name": "Four-door Sedan",  
          "default_reserve_time": 0,  
          "max_range_meters": 523992,  
          "return_type": [  
            "roundtrip_station"  
          ],  
          "vehicle_assets": {  
            "icon_url": "https://www.example.com/assets/icon_car.svg",  
            "icon_url_dark": "https://www.example.com/assets/icon_car_dark.svg",  
            "icon_last_modified": "2021-06-15"  
          },  
          "default_pricing_plan_id": "car_plan_1"  
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
#### vehicle_types NGSI-LD key-values 示例  
这里是一个以JSON-LD格式作为key-values的 vehicle_types的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:vehicle_types:id:FNNO:60592292",  
    "type": "vehicle_types",  
    "last_updated": 1609866247,  
    "ttl": 0,  
    "version": "3.0",  
    "data": {  
        "vehicle_types": [  
            {  
                "vehicle_type_id": "abc123",  
                "form_factor": "bicycle",  
                "propulsion_type": "human",  
                "name": "Example Basic Bike",  
                "default_reserve_time": 30,  
                "return_type": [  
                    "any_station",  
                    "free_floating"  
                ],  
                "vehicle_assets": {  
                    "icon_url": "https://www.example.com/assets/icon_bicycle.svg",  
                    "icon_url_dark": "https://www.example.com/assets/icon_bicycle_dark.svg",  
                    "icon_last_modified": "2021-06-15"  
                },  
                "default_pricing_plan_id": "bike_plan_1",  
                "pricing_plan_ids": [  
                    "bike_plan_1",  
                    "bike_plan_2",  
                    "bike_plan_3"  
                ]  
            },  
            {  
                "vehicle_type_id": "def456",  
                "form_factor": "scooter",  
                "propulsion_type": "electric",  
                "name": "Example E-scooter V2",  
                "default_reserve_time": 30,  
                "max_range_meters": 12345,  
                "return_type": [  
                    "free_floating"  
                ],  
                "vehicle_assets": {  
                    "icon_url": "https://www.example.com/assets/icon_escooter.svg",  
                    "icon_url_dark": "https://www.example.com/assets/icon_escooter_dark.svg",  
                    "icon_last_modified": "2021-06-15"  
                },  
                "default_pricing_plan_id": "scooter_plan_1"  
            },  
            {  
                "vehicle_type_id": "car1",  
                "form_factor": "car",  
                "propulsion_type": "combustion",  
                "name": "Four-door Sedan",  
                "default_reserve_time": 0,  
                "max_range_meters": 523992,  
                "return_type": [  
                    "roundtrip_station"  
                ],  
                "vehicle_assets": {  
                    "icon_url": "https://www.example.com/assets/icon_car.svg",  
                    "icon_url_dark": "https://www.example.com/assets/icon_car_dark.svg",  
                    "icon_last_modified": "2021-06-15"  
                },  
                "default_pricing_plan_id": "car_plan_1"  
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
#### vehicle_types NGSI-LD归一化实例  
下面是一个规范化的JSON-LD格式的vehicle_types的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:vehicle_types:id:FNNO:60592292",  
    "type": "vehicle_types",  
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
            "vehicle_types": [  
                {  
                    "vehicle_type_id": "abc123",  
                    "form_factor": "bicycle",  
                    "propulsion_type": "human",  
                    "name": "Example Basic Bike",  
                    "default_reserve_time": 30,  
                    "return_type": [  
                        "any_station",  
                        "free_floating"  
                    ],  
                    "vehicle_assets": {  
                        "icon_url": "https://www.example.com/assets/icon_bicycle.svg",  
                        "icon_url_dark": "https://www.example.com/assets/icon_bicycle_dark.svg",  
                        "icon_last_modified": "2021-06-15"  
                    },  
                    "default_pricing_plan_id": "bike_plan_1",  
                    "pricing_plan_ids": [  
                        "bike_plan_1",  
                        "bike_plan_2",  
                        "bike_plan_3"  
                    ]  
                },  
                {  
                    "vehicle_type_id": "def456",  
                    "form_factor": "scooter",  
                    "propulsion_type": "electric",  
                    "name": "Example E-scooter V2",  
                    "default_reserve_time": 30,  
                    "max_range_meters": 12345,  
                    "return_type": [  
                        "free_floating"  
                    ],  
                    "vehicle_assets": {  
                        "icon_url": "https://www.example.com/assets/icon_escooter.svg",  
                        "icon_url_dark": "https://www.example.com/assets/icon_escooter_dark.svg",  
                        "icon_last_modified": "2021-06-15"  
                    },  
                    "default_pricing_plan_id": "scooter_plan_1"  
                },  
                {  
                    "vehicle_type_id": "car1",  
                    "form_factor": "car",  
                    "propulsion_type": "combustion",  
                    "name": "Four-door Sedan",  
                    "default_reserve_time": 0,  
                    "max_range_meters": 523992,  
                    "return_type": [  
                        "roundtrip_station"  
                    ],  
                    "vehicle_assets": {  
                        "icon_url": "https://www.example.com/assets/icon_car.svg",  
                        "icon_url_dark": "https://www.example.com/assets/icon_car_dark.svg",  
                        "icon_last_modified": "2021-06-15"  
                    },  
                    "default_pricing_plan_id": "car_plan_1"  
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
