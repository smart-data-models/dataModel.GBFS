<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: gbfs  
=========<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.GBFS/blob/master/gbfs/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: 시스템에서 게시한 다른 모든 파일에 연결되는 **자동 검색 파일입니다. 표준 GBFS 2.2**에 따르면  
버전: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `data[object]`: 이름:값 쌍 형식의 응답 데이터.  - `id[*]`: 엔티티의 고유 식별자  - `last_updated[integer]`: 피드의 데이터가 마지막으로 업데이트된 시간은 POSIX 시간입니다.  - `ttl[integer]`: 피드의 데이터가 다시 업데이트되기까지의 시간(초)(데이터를 항상 새로 고쳐야 하는 경우 0)입니다.  - `type[string]`: NGSI 엔티티 유형. gbfs여야 합니다.  - `version[string]`: 버전 관리 프레임워크에 따라 피드가 준수하는 GBFS 버전 번호(v1.1에 추가됨).  <!-- /30-PropertiesList -->  
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
gbfs:    
  description: Auto-discovery file that links to all of the other files published by the system. According to the Standard GBFS 2.2    
  properties:    
    data:    
      description: 'Response data in the form of name:value pairs.'    
      patternProperties:    
        ^[a-z]{2,3}(-[A-Z]{2})?$:    
          properties:    
            feeds:    
              description: An array of all of the feeds that are published by the auto-discovery file. Each element in the array is an object with the keys below.    
              items:    
                properties:    
                  name:    
                    description: Key identifying the type of feed this is. The key must be the base file name defined in the spec for the corresponding feed type.    
                    enum:    
                      - gbfs    
                      - gbfs_versions    
                      - system_information    
                      - vehicle_types    
                      - station_information    
                      - station_status    
                      - free_bike_status    
                      - system_hours    
                      - system_alerts    
                      - system_calendar    
                      - system_regions    
                      - system_pricing_plans    
                      - geofencing_zones    
                    type: string    
                  url:    
                    description: URL for the feed.    
                    format: uri    
                    type: string    
                required:    
                  - name    
                  - url    
                type: object    
              type: array    
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
      description: NGSI entity type. It has to be gbfs    
      enum:    
        - gbfs    
      type: string    
      x-ngsi:    
        type: Property    
    version:    
      description: 'GBFS version number to which the feed conforms, according to the versioning framework (added in v1.1).'    
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
    - data    
    - id    
    - last_updated    
    - ttl    
    - type    
    - version    
  type: object    
  x-derived-from: https://github.com/NABSA/gbfs/blob/v2.2/gbfs.md    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.GBFS/blob/master/gbfs/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.GBFS/gbfs/schema.json    
  x-model-tags: GBFS    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
#### gbfs NGSI-v2 키-값 예제  
다음은 키-값으로 JSON-LD 형식의 gbfs의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:gbfs:id:UKBQ:60920452",  
  "type": "gbfs",  
  "last_updated": 1450156395,  
  "ttl": 566,  
  "version": "2.1",  
  "data": {  
    "feeds": [  
      {  
        "name": "station_information",  
        "url": "urn:ngsi-ld:gbfs:url:EPHA:59077032"  
      },  
      {  
        "name": "system_hours",  
        "url": "urn:ngsi-ld:gbfs:url:GDPS:83970346"  
      }  
    ]  
  }  
}  
```  
</details>  
#### gbfs NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 gbfs의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:gbfs:id:UKBQ:60920452",  
  "type": "gbfs",  
  "last_updated": {  
    "type": "Number",  
    "value": 1450156395  
  },  
  "ttl": {  
    "type": "Number",  
    "value": 566  
  },  
  "version": {  
    "type": "Text",  
    "value": "2.1"  
  },  
  "data": {  
    "type": "StructuredValue",  
    "value": {  
      "feeds": [  
        {  
          "name": "station_information",  
          "url": "urn:ngsi-ld:gbfs:url:EPHA:59077032"  
        },  
        {  
          "name": "system_hours",  
          "url": "urn:ngsi-ld:gbfs:url:GDPS:83970346"  
        }  
      ]  
    }  
  }  
}  
```  
</details>  
#### gbfs NGSI-LD 키-값 예제  
다음은 키-값으로 JSON-LD 형식의 gbfs의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:gbfs:id:UKBQ:60920452",  
    "type": "gbfs",  
    "last_updated": 1450156395,  
    "ttl": 566,  
    "version": "2.1",  
    "data": {  
        "feeds": [  
            {  
                "name": "station_information",  
                "url": "urn:ngsi-ld:gbfs:url:EPHA:59077032"  
            },  
            {  
                "name": "system_hours",  
                "url": "urn:ngsi-ld:gbfs:url:GDPS:83970346"  
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
#### gbfs NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 gbfs의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:gbfs:id:UKBQ:60920452",  
    "type": "gbfs",  
    "last_updated": {  
        "type": "Property",  
        "value": 1450156395  
    },  
    "ttl": {  
        "type": "Property",  
        "value": 566  
    },  
    "version": {  
        "type": "Property",  
        "value": "2.1"  
    },  
    "data": {  
        "type": "Property",  
        "value": {  
            "feeds": [  
                {  
                    "name": "station_information",  
                    "url": "urn:ngsi-ld:gbfs:url:EPHA:59077032"  
                },  
                {  
                    "name": "system_hours",  
                    "url": "urn:ngsi-ld:gbfs:url:GDPS:83970346"  
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
