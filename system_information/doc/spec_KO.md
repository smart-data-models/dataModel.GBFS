<!-- 10-Header -->
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

===========
<!-- 15-License -->


<!-- /15-License -->
<!-- 20-Description -->


<!-- /20-Description -->
<!-- 30-PropertiesList -->




- `data[object]`: 이름:값 쌍 형식의 응답 데이터.  
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
- `id[*]`: 엔티티의 고유 식별자  
<!-- 35-RequiredProperties -->

- `data`  
<!-- 40-RequiredProperties -->

<!-- /40-RequiredProperties -->
<!-- 50-DataModelHeader -->


<!-- /50-DataModelHeader -->
<!-- 60-ModelYaml -->
<details><summary><strong>full yaml details</strong></summary>    

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



<details><summary><strong>show/hide example</strong></summary>    


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


<details><summary><strong>show/hide example</strong></summary>    


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


<details><summary><strong>show/hide example</strong></summary>    


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


<details><summary><strong>show/hide example</strong></summary>    


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

<!-- /95-Units -->
<!-- 97-LastFooter -->
---  
