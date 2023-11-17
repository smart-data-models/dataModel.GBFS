<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
엔티티: 시스템_가격 책정_플랜    
=================<!-- /10-Header -->    
<!-- 15-License -->    
[오픈 라이선스](https://github.com/smart-data-models//dataModel.GBFS/blob/master/system_pricing_plans/LICENSE.md)    
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
글로벌 설명: **시스템의 가격 책정 방식을 설명합니다. 표준 GBFS 2.2**에 따름.    
버전: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 속성 목록    
<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.    
- `data[object]`: 아래 정의된 대로 플랜당 하나의 객체를 포함하는 배열입니다.  	- `plans`:       
- `id[*]`: 엔티티의 고유 식별자  - `last_updated[integer]`: 피드의 데이터가 마지막으로 업데이트된 시간은 POSIX 시간입니다.  - `ttl[integer]`: 피드의 데이터가 다시 업데이트되기까지의 시간(초)(데이터를 항상 새로 고쳐야 하는 경우 0)입니다.  - `type[string]`: NGSI 엔티티 유형. 시스템_가격 책정_플랜이어야 합니다.  - `version[string]`: 버전 관리 프레임워크에 따라 피드가 준수하는 GBFS 버전 번호(v1.1에 추가됨).  <!-- /30-PropertiesList -->    
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
system_pricing_plans:      
  description: Describes the pricing schemes of the system. According to the Standard GBFS 2.2      
  properties:      
    data:      
      description: Array that contains one object per plan as defined below.      
      properties:      
        plans:      
          items:      
            properties:      
              currency:      
                description: Currency used to pay the fare in ISO 4217 code.      
                pattern: ^\w{3}$      
                type: string      
              description:      
                description: Customer-readable description of the pricing plan.      
                type: string      
              is_taxable:      
                description: 'Will additional tax be added to the base price?'      
                type: boolean      
              name:      
                description: Name of this pricing plan.      
                type: string      
              per_km_pricing:      
                dependencies:      
                  per_km_pricing:      
                    - start      
                    - rate      
                    - interval      
                description: 'Array of segments when the price is a function of distance travelled, displayed in kilometers (added in v2.1-RC2).'      
                items:      
                  properties:      
                    end:      
                      description: The kilometer at which the rate will no longer apply (added in v2.1-RC2).      
                      minimum: 0      
                      type: number      
                    interval:      
                      description: 'Interval in kilometers at which the rate of this segment is either reapplied indefinitely, or if defined, up until (but not including) end kilometer (added in v2.1-RC2).'      
                      minimum: 0      
                      type: number      
                    rate:      
                      description: Rate that is charged for each kilometer interval after the start (added in v2.1-RC2).      
                      type: number      
                    start:      
                      description: Number of kilometers that have to elapse before this segment starts applying (added in v2.1-RC2).      
                      minimum: 0      
                      type: number      
                  type: object      
                type: array      
              per_min_pricing:      
                dependencies:      
                  per_min_pricing:      
                    - start      
                    - rate      
                    - interval      
                description: 'Array of segments when the price is a function of time travelled, displayed in minutes (added in v2.1-RC2).'      
                items:      
                  properties:      
                    end:      
                      description: The minute at which the rate will no longer apply (added in v2.1-RC2).      
                      minimum: 0      
                      type: number      
                    interval:      
                      description: Interval in minutes at which the rate of this segment is either reapplied (added in v2.1-RC2).      
                      minimum: 0      
                      type: number      
                    rate:      
                      description: Rate that is charged for each minute interval after the start (added in v2.1-RC2).      
                      type: number      
                    start:      
                      description: Number of minutes that have to elapse before this segment starts applying (added in v2.1-RC2).      
                      minimum: 0      
                      type: number      
                  type: object      
                type: array      
              plan_id:      
                description: Identifier of a pricing plan in the system.      
                type: string      
              price:      
                description: Fare price.      
                minimum: 0      
                type: number      
              surge_pricing:      
                description: 'Is there currently an increase in price in response to increased demand in this pricing plan? (added in v2.1-RC2)'      
                type: boolean      
              url:      
                description: URL where the customer can learn more about this pricing plan.      
                format: uri      
                type: string      
            type: object      
          required:      
            - plan_id      
            - name      
            - currency      
            - price      
            - is_taxable      
            - description      
          type: array      
      required:      
        - plans      
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
      description: NGSI entity type. It has to be system_pricing_plans      
      enum:      
        - system_pricing_plans      
      type: string      
      x-ngsi:      
        type: Property      
    version:      
      description: 'GBFS version number to which the feed conforms, according to the versioning framework (added in v1.1).'      
      enum:      
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
  x-license-url: https://github.com/smart-data-models/dataModel.GBFS/blob/master/system_pricing_plans/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.GBFS/system_pricing_plans/schema.json      
  x-model-tags: GBFS      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 페이로드 예시    
#### system_pricing_plans NGSI-v2 키값 예시    
다음은 JSON-LD 형식의 시스템_가격 책정_플랜을 키값으로 사용하는 예제입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:system_pricing_plans:id:FNNO:60592292",  
  "type": "system_pricing_plans",  
  "last_updated": 1609866247,  
  "ttl": 0,  
  "version": "3.0",  
  "data": {  
    "plans": [  
      {  
        "plan_id": "plan3",  
        "name": "Simple Rate",  
        "currency": "CAD",  
        "price": 3,  
        "is_taxable": true,  
        "description": "$3 unlock fee, $0.25 per kilometer and 0.50 per minute.",  
        "per_km_pricing": [  
          {  
            "start": 0,  
            "rate": 0.25,  
            "interval": 1  
          }  
        ],  
        "per_min_pricing": [  
          {  
            "start": 0,  
            "rate": 0.5,  
            "interval": 1  
          }  
        ]  
      }  
    ]  
  }  
}  
```  
</details>    
#### system_pricing_plans NGSI-v2 정규화 예제    
다음은 정규화된 JSON-LD 형식의 시스템 가격 책정 계획의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:system_pricing_plans:id:FNNO:60592292",  
  "type": "system_pricing_plans",  
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
      "plans": [  
        {  
          "plan_id": "plan3",  
          "name": "Simple Rate",  
          "currency": "CAD",  
          "price": 3,  
          "is_taxable": true,  
          "description": "$3 unlock fee, $0.25 per kilometer and 0.50 per minute.",  
          "per_km_pricing": [  
            {  
              "start": 0,  
              "rate": 0.25,  
              "interval": 1  
            }  
          ],  
          "per_min_pricing": [  
            {  
              "start": 0,  
              "rate": 0.5,  
              "interval": 1  
            }  
          ]  
        }  
      ]  
    }  
  }  
}  
```  
</details>    
#### system_pricing_plans NGSI-LD 키 값 예시    
다음은 JSON-LD 형식의 시스템_가격 책정_플랜을 키값으로 사용하는 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:system_pricing_plans:id:FNNO:60592292",  
  "type": "system_pricing_plans",  
  "last_updated": 1609866247,  
  "ttl": 0,  
  "version": "3.0",  
  "data": {  
    "plans": [  
      {  
        "plan_id": "plan3",  
        "name": "Simple Rate",  
        "currency": "CAD",  
        "price": 3,  
        "is_taxable": true,  
        "description": "$3 unlock fee, $0.25 per kilometer and 0.50 per minute.",  
        "per_km_pricing": [  
          {  
            "start": 0,  
            "rate": 0.25,  
            "interval": 1  
          }  
        ],  
        "per_min_pricing": [  
          {  
            "start": 0,  
            "rate": 0.5,  
            "interval": 1  
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
#### system_pricing_plans NGSI-LD 정규화 예제    
다음은 정규화된 JSON-LD 형식의 시스템 가격 책정 계획의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:system_pricing_plans:id:FNNO:60592292",  
    "type": "system_pricing_plans",  
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
            "plans": [  
                {  
                    "plan_id": "plan3",  
                    "name": "Simple Rate",  
                    "currency": "CAD",  
                    "price": 3,  
                    "is_taxable": true,  
                    "description": "$3 unlock fee, $0.25 per kilometer and 0.50 per minute.",  
                    "per_km_pricing": [  
                        {  
                            "start": 0,  
                            "rate": 0.25,  
                            "interval": 1  
                        }  
                    ],  
                    "per_min_pricing": [  
                        {  
                            "start": 0,  
                            "rate": 0.5,  
                            "interval": 1  
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
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
