<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
엔티티: 시스템_경고    
===========<!-- /10-Header -->    
<!-- 15-License -->    
[오픈 라이선스](https://github.com/smart-data-models//dataModel.GBFS/blob/master/system_alerts/LICENSE.md)    
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
전역 설명: **시스템에 대한 임시 변경 사항을 설명합니다. 표준 GBFS 2.2**에 따르면    
버전: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 속성 목록    
<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.    
- `data[object]`: 시스템에 대한 임시 알림을 포함하는 배열입니다.  	- `alerts`:       
- `id[*]`: 엔티티의 고유 식별자  - `last_updated[integer]`: 피드의 데이터가 마지막으로 업데이트된 시간은 POSIX 시간입니다.  - `ttl[integer]`: 피드의 데이터가 다시 업데이트되기까지의 시간(초)(데이터를 항상 새로 고쳐야 하는 경우 0)입니다.  - `type[string]`: NGSI 엔티티 유형입니다. system_alerts여야 합니다.  - `version[string]`: 버전 관리 프레임워크에 따라 피드가 준수하는 GBFS 버전 번호(v1.1에 추가됨).  <!-- /30-PropertiesList -->    
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
## 페이로드 예시    
#### system_alerts NGSI-v2 키-값 예시    
다음은 키-값으로 JSON-LD 형식의 system_alerts의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
#### system_alerts NGSI-v2 정규화 예제    
다음은 정규화된 JSON-LD 형식의 system_alerts의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
  }  
}  
```  
</details>    
#### system_alerts NGSI-LD 키-값 예시    
다음은 키-값으로 JSON-LD 형식의 system_alerts의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
#### system_alerts NGSI-LD 정규화 예제    
다음은 정규화된 JSON-LD 형식의 system_alerts의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
