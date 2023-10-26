<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: 시스템_정보  
===========<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.GBFS/blob/master/system_information/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **시스템 운영자, 시스템 위치, 구현 연도, URL, 연락처 정보, 시간대를 포함한 세부 정보입니다. 표준 GBFS 2.2**에 따르면  
버전: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `data[object]`: 이름:값 쌍 형식의 응답 데이터.  	- `email[email]`: 운영자의 고객 서비스 부서에서 적극적으로 모니터링하는 이메일 주소입니다.    
	- `feed_contact_email[email]`: 이 피드의 소비자가 기술 문제를 신고할 수 있는 단일 연락처 이메일 주소(v1.1에 추가됨).    
	- `language[string]`: 나머지 파일 전체에서 사용할 언어입니다. gbfs.json 파일의 값과 일치해야 합니다.    
	- `license_url[uri]`: 이 시스템의 GBFS 데이터에 대한 라이선스 조건을 정의하는 페이지의 정규화된 URL입니다.    
	- `name[string]`: 고객에게 표시할 시스템 이름입니다.    
	- `operator[string]`: 운영자 이름    
	- `phone_number[string]`: 지정된 시스템에 대한 단일 음성 전화 번호로, 해당 시스템의 서비스 지역에서 일반적으로 사용되는 전화 번호를 나타냅니다.    
	- `purchase_url[uri]`: 고객이 멤버십을 구매할 수 있는 URL입니다.    
	- `rental_apps[object]`: Android 및 iOS JSON 객체에 렌탈 앱 정보를 포함합니다(v1.1에 추가됨).    
	- `short_name[string]`: 시스템의 선택적 약어입니다.    
	- `start_date[string]`: 시스템 운영을 시작한 날짜입니다.    
	- `system_id[string]`: 이 차량 공유 시스템의 식별자입니다. 이 식별자는 전 세계적으로 고유해야 합니다(다른 시스템 간에도 동일).    
	- `timezone[string]`: 시스템이 위치한 표준 시간대입니다.    
	- `url[uri]`: 차량 공유 시스템의 URL입니다.    
- `id[*]`: 엔티티의 고유 식별자  - `last_updated[integer]`: 피드의 데이터가 마지막으로 업데이트된 시간은 POSIX 시간입니다.  - `ttl[integer]`: 피드의 데이터가 다시 업데이트되기까지의 시간(초)(데이터를 항상 새로 고쳐야 하는 경우 0)입니다.  - `type[string]`: NGSI 엔티티 유형입니다. 시스템_정보여야 합니다.  - `version[string]`: 버전 관리 프레임워크에 따라 피드가 준수하는 GBFS 버전 번호(v1.1에 추가됨).  <!-- /30-PropertiesList -->  
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
system_information:    
  description: 'Details including system operator, system location, year implemented, URL, contact info, time zone. According to the Standard GBFS 2.2'    
  properties:    
    data:    
      description: 'Response data in the form of name:value pairs.'    
      properties:    
        email:    
          description: Email address actively monitored by the operator's customer service department.    
          format: email    
          type: string    
        feed_contact_email:    
          description: A single contact email address for consumers of this feed to report technical issues (added in v1.1).    
          format: email    
          type: string    
        language:    
          description: The language that will be used throughout the rest of the files. It must match the value in the gbfs.json file.    
          pattern: ^[a-z]{2,3}(-[A-Z]{2})?$    
          type: string    
        license_url:    
          description: A fully qualified URL of a page that defines the license terms for the GBFS data for this system.    
          format: uri    
          type: string    
        name:    
          description: Name of the system to be displayed to customers.    
          type: string    
        operator:    
          description: Name of the operator    
          type: string    
        phone_number:    
          description: A single voice telephone number for the specified system that presents the telephone number as typical for the system's service area.    
          type: string    
        purchase_url:    
          description: URL where a customer can purchase a membership.    
          format: uri    
          type: string    
        rental_apps:    
          description: Contains rental app information in the android and ios JSON objects (added in v1.1).    
          properties:    
            android:    
              dependencies:    
                android:    
                  - store_uri    
                  - discovery_uri    
              description: Contains rental app download and app discovery information for the Android platform. (added in v1.1)    
              properties:    
                discovery_uri:    
                  description: URI that can be used to discover if the rental Android app is installed on the device (added in v1.1).    
                  format: uri    
                  type: string    
                store_uri:    
                  description: URI where the rental Android app can be downloaded from (added in v1.1).    
                  format: uri    
                  type: string    
              type: object    
            ios:    
              dependencies:    
                ios:    
                  - store_uri    
                  - discovery_uri    
              description: Contains rental information for the iOS platform (added in v1.1).    
              properties:    
                discovery_uri:    
                  description: URI that can be used to discover if the rental iOS app is installed on the device (added in v1.1).    
                  format: uri    
                  type: string    
                store_uri:    
                  description: URI where the rental iOS app can be downloaded from (added in v1.1).    
                  format: uri    
                  type: string    
              type: object    
          type: object    
        short_name:    
          description: Optional abbreviation for a system.    
          type: string    
        start_date:    
          description: Date that the system began operations.    
          pattern: ^[0-9]{4}-[0-9]{2}-[0-9]{2}$    
          type: string    
        system_id:    
          description: Identifier for this vehicle share system. This should be globally unique (even between different systems).    
          type: string    
        timezone:    
          description: The time zone where the system is located.    
          type: string    
        url:    
          description: The URL of the vehicle share system.    
          format: uri    
          type: string    
      required:    
        - system_id    
        - language    
        - name    
        - timezone    
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
      description: NGSI entity type. It has to be system_information    
      enum:    
        - system_information    
      type: string    
      x-ngsi:    
        type: Property    
    version:    
      description: 'GBFS version number to which the feed conforms, according to the versioning framework (added in v1.1).'    
      enum:    
        - 1.1-RC    
        - 1.1    
        - 2.0    
        - 2.1-RC    
        - 2.1-RC2    
        - 2.1    
        - 2.2    
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
  x-license-url: https://github.com/smart-data-models/dataModel.GBFS/blob/master/system_information/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.GBFS/system_information/schema.json    
  x-model-tags: GBFS    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
#### system_정보 NGSI-v2 키 값 예시  
다음은 JSON-LD 형식의 시스템 정보를 키값으로 사용하는 예제입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:system_information:id:FNNO:60592292",  
  "type": "system_information",  
  "last_updated": 1611598155,  
  "ttl": 1800,  
  "version": "3.0",  
  "data": {  
    "system_id": "example_cityname",  
    "language": "en",  
    "name": "Example Bike Rental",  
    "short_name": "Example Bike",  
    "operator": "Example Sharing, Inc",  
    "url": "https://www.example.com",  
    "purchase_url": "https://www.example.com",  
    "start_date": "2010-06-10",  
    "phone_number": "1-800-555-1234",  
    "email": "customerservice@example.com",  
    "feed_contact_email": "datafeed@example.com",  
    "timezone": "US/Central",  
    "license_url": "https://www.example.com/data-license.html",  
    "brand_assets": {  
      "brand_last_modified": "2021-06-15",  
      "brand_image_url": "https://www.example.com/assets/brand_image.svg",  
      "brand_image_url_dark": "https://www.example.com/assets/brand_image_dark.svg",  
      "color": "#C2D32C",  
      "terms_url": "https://www.example.com/assets/brand.pdf"  
    }  
  }  
}  
```  
</details>  
#### system_info NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 시스템_정보의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:system_information:id:FNNO:60592292",  
  "type": "system_information",  
  "last_updated": {  
    "type": "Number",  
    "value": 1611598155  
  },  
  "ttl": {  
    "type": "Number",  
    "value": 1800  
  },  
  "version": {  
    "type": "Text",  
    "value": "3.0"  
  },  
  "data": {  
    "type": "StructuredValue",  
    "value": {  
      "system_id": "example_cityname",  
      "language": "en",  
      "name": "Example Bike Rental",  
      "short_name": "Example Bike",  
      "operator": "Example Sharing, Inc",  
      "url": "https://www.example.com",  
      "purchase_url": "https://www.example.com",  
      "start_date": "2010-06-10",  
      "phone_number": "1-800-555-1234",  
      "email": "customerservice@example.com",  
      "feed_contact_email": "datafeed@example.com",  
      "timezone": "US/Central",  
      "license_url": "https://www.example.com/data-license.html",  
      "brand_assets": {  
        "brand_last_modified": "2021-06-15",  
        "brand_image_url": "https://www.example.com/assets/brand_image.svg",  
        "brand_image_url_dark": "https://www.example.com/assets/brand_image_dark.svg",  
        "color": "#C2D32C",  
        "terms_url": "https://www.example.com/assets/brand.pdf"  
      }  
    }  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
</details>  
#### system_info NGSI-LD 키-값 예시  
다음은 JSON-LD 형식의 시스템 정보를 키-값으로 사용하는 예제입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:system_information:id:FNNO:60592292",  
    "type": "system_information",  
    "last_updated": 1611598155,  
    "ttl": 1800,  
    "version": "3.0",  
    "data": {  
        "system_id": "example_cityname",  
        "language": "en",  
        "name": "Example Bike Rental",  
        "short_name": "Example Bike",  
        "operator": "Example Sharing, Inc",  
        "url": "https://www.example.com",  
        "purchase_url": "https://www.example.com",  
        "start_date": "2010-06-10",  
        "phone_number": "1-800-555-1234",  
        "email": "customerservice@example.com",  
        "feed_contact_email": "datafeed@example.com",  
        "timezone": "US/Central",  
        "license_url": "https://www.example.com/data-license.html",  
        "brand_assets": {  
            "brand_last_modified": "2021-06-15",  
            "brand_image_url": "https://www.example.com/assets/brand_image.svg",  
            "brand_image_url_dark": "https://www.example.com/assets/brand_image_dark.svg",  
            "color": "#C2D32C",  
            "terms_url": "https://www.example.com/assets/brand.pdf"  
        }  
    },  
    "@context": [  
        "https://smartdatamodels.org/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.GBFS/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### system_info NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 시스템_정보의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:system_information:id:FNNO:60592292",  
    "type": "system_information",  
    "last_updated": {  
        "type": "Property",  
        "value": 1611598155  
    },  
    "ttl": {  
        "type": "Property",  
        "value": 1800  
    },  
    "version": {  
        "type": "Property",  
        "value": "3.0"  
    },  
    "data": {  
        "type": "Property",  
        "value": {  
            "system_id": "example_cityname",  
            "language": "en",  
            "name": "Example Bike Rental",  
            "short_name": "Example Bike",  
            "operator": "Example Sharing, Inc",  
            "url": "https://www.example.com",  
            "purchase_url": "https://www.example.com",  
            "start_date": "2010-06-10",  
            "phone_number": "1-800-555-1234",  
            "email": "customerservice@example.com",  
            "feed_contact_email": "datafeed@example.com",  
            "timezone": "US/Central",  
            "license_url": "https://www.example.com/data-license.html",  
            "brand_assets": {  
                "brand_last_modified": "2021-06-15",  
                "brand_image_url": "https://www.example.com/assets/brand_image.svg",  
                "brand_image_url_dark": "https://www.example.com/assets/brand_image_dark.svg",  
                "color": "#C2D32C",  
                "terms_url": "https://www.example.com/assets/brand.pdf"  
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
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
