<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
엔티티: 시스템_시간    
===========<!-- /10-Header -->    
<!-- 15-License -->    
[오픈 라이선스](https://github.com/smart-data-models//dataModel.GBFS/blob/master/system_hours/LICENSE.md)    
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
글로벌 설명: **시스템 운영 시간을 설명합니다. 표준 GBFS 2.2**에 따름.    
버전: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 속성 목록    
<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.    
- `data[object]`: 시스템 운영 시간이 포함된 배열입니다.  	- `rental_hours`:       
- `id[*]`: 엔티티의 고유 식별자  - `last_updated[integer]`: 피드의 데이터가 마지막으로 업데이트된 시간은 POSIX 시간입니다.  - `ttl[integer]`: 피드의 데이터가 다시 업데이트되기까지의 시간(초)(데이터를 항상 새로 고쳐야 하는 경우 0)입니다.  - `type[string]`: NGSI 엔티티 유형입니다. 시스템_시간이어야 합니다.  - `version[string]`: 버전 관리 프레임워크에 따라 피드가 준수하는 GBFS 버전 번호(v1.1에 추가됨).  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
필수 속성    
- `data`  - `id`  - `last_updated`  - `ttl`  - `type`  - `version`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
표준 매핑 [GBFS 2.2](https://github.com/NABSA/gbfs/blob/v2.2/gbfs.md)    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 속성에 대한 데이터 모델 설명    
알파벳순으로 정렬(자세한 내용을 보려면 클릭)    
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
## 페이로드 예시    
#### system_hours NGSI-v2 키 값 예제    
다음은 JSON-LD 형식의 시스템_시간을 키값으로 사용하는 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
#### system_hours NGSI-v2 정규화 예제    
다음은 정규화된 JSON-LD 형식의 시스템_시간의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
#### system_hours NGSI-LD 키-값 예시    
다음은 JSON-LD 형식의 시스템_시간을 키-값으로 사용하는 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
#### system_hours NGSI-LD 정규화 예제    
다음은 정규화된 JSON-LD 형식의 시스템_시간의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
