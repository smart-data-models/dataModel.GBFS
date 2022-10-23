<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティ：free_bike_status  
=======================<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.GBFS/blob/master/free_bike_status/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述です。**レンタル可能な車両を記述する（v2.1-RC2 時点）。標準GBFS2.2による**。  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性にタイプがない場合、複数のタイプまたは異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `data[object]`: 以下に定義する、1 台の自転車につき 1 つのオブジェクトを含む配列。  - `id[*]`: エンティティの一意な識別子  - `last_updated[integer]`: フィードのデータが POSIX 時間で最後に更新された時刻。  - `ttl[integer]`: フィードのデータが再び更新されるまでの秒数（常にデータを更新する場合は0）。  - `type[string]`: NGSIエンティティタイプ。free_bike_status である必要があります。  - `version[string]`: バージョン管理の枠組みによる、フィードが準拠するGBFSのバージョン番号（v1.1で追加）。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必要なプロパティ  
- `id`  - `last_updated`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
規格のマッピング[GBFS 2.2](https://github.com/NABSA/gbfs/blob/v2.2/gbfs.md)  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
free_bike_status:    
  description: 'Describes the vehicles that are available for rent (as of v2.1-RC2). According to the Standard GBFS 2.2'    
  properties:    
    data:    
      description: 'Array that contains one object per bike as defined below.'    
      properties:    
        bikes:    
          items:    
            properties:    
              bike_id:    
                description: 'Rotating (as of v2.0) identifier of a vehicle.'    
                type: string    
              current_range_meters:    
                description: 'The furthest distance in meters that the vehicle can travel without recharging or refueling with the vehicle''s current charge or fuel (added in v2.1-RC).'    
                minimum: 0    
                type: number    
              is_disabled:    
                description: 'Is the vehicle currently disabled (broken)?'    
                type: boolean    
              is_reserved:    
                description: 'Is the vehicle currently reserved?'    
                type: boolean    
              last_reported:    
                description: 'The last time this vehicle reported its status to the operator''s backend in POSIX time (added in v2.1-RC).'    
                minimum: 1450155600    
                type: number    
              lat:    
                description: 'The latitude of the vehicle.'    
                maximum: 90    
                minimum: -90    
                type: number    
              lon:    
                description: 'The longitude of the vehicle.'    
                maximum: 180    
                minimum: -180    
                type: number    
              pricing_plan_id:    
                description: 'The plan_id of the pricing plan this vehicle is eligible for (added in v2.1-RC2).'    
                type: string    
              rental_uris:    
                description: 'Contains rental uris for Android, iOS, and web in the android, ios, and web fields (added in v1.1).'    
                properties:    
                  android:    
                    description: 'URI that can be passed to an Android app with an intent (added in v1.1).'    
                    format: uri    
                    type: string    
                  ios:    
                    description: 'URI that can be used on iOS to launch the rental app for this vehicle (added in v1.1).'    
                    format: uri    
                    type: string    
                  web:    
                    description: 'URL that can be used by a web browser to show more information about renting this vehicle (added in v1.1).'    
                    format: uri    
                    type: string    
                type: object    
              station_id:    
                description: 'Identifier referencing the station_id if the vehicle is currently at a station (added in v2.1-RC2).'    
                type: string    
              vehicle_type_id:    
                description: 'The vehicle_type_id of this vehicle (added in v2.1-RC).'    
                type: string    
            required:    
              - bike_id    
              - is_reserved    
              - is_disabled    
            type: object    
          required:    
            - bikes    
          type: array    
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
      description: 'NGSI entity type. It has to be free_bike_status'    
      enum:    
        - free_bike_status    
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
    - id    
    - last_updated    
    - type    
  type: object    
  x-derived-from: https://github.com/NABSA/gbfs/blob/v2.2/gbfs.md    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.GBFS/blob/master/free_bike_status/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.GBFS/free_bike_status/schema.json    
  x-model-tags: GBFS    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### Free_bike_status NGSI-v2 key-value 例．  
以下は、free_bike_statusをJSON-LD形式でkey-valuesとした例である。これは `options=keyValues` を使用したときに NGSI-v2 と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:free_bike_status:id:ZMAW:94046191",  
    "type": "free_bike_status",  
    "last_updated": 1450156464,  
    "ttl": 864,  
    "version": "3.0-RC",  
    "data": {  
        "bikes": [  
            {  
                "bike_id": "bike:001:0023",  
                "lat": 9.6,  
                "lon": 18.6,  
                "is_reserved": true,  
                "is_disabled": false,  
                "rental_uris": {  
                    "android": "urn:ngsi-ld:free_bike_status:android:DDCU:76475938",  
                    "ios": "urn:ngsi-ld:free_bike_status:ios:OJIQ:89241157",  
                    "web": "urn:ngsi-ld:free_bike_status:web:XCVS:38778408"  
                },  
                "vehicle_type_id": "regular bike",  
                "last_reported": 1450156464,  
                "current_range_meters": 864.6,  
                "station_id": "Madrid puerta del sol",  
                "pricing_plan_id": "Tourist 1 day"  
            },  
            {  
                "bike_id": "bike:001:0024",  
                "lat": 9.6,  
                "lon": 18.6,  
                "is_reserved": true,  
                "is_disabled": false,  
                "rental_uris": {  
                    "android": "urn:ngsi-ld:free_bike_status:android:DDCU:76475938",  
                    "ios": "urn:ngsi-ld:free_bike_status:ios:OJIQ:89241157",  
                    "web": "urn:ngsi-ld:free_bike_status:web:XCVS:38778408"  
                },  
                "vehicle_type_id": "regular bike",  
                "last_reported": 1450156464,  
                "current_range_meters": 864.6,  
                "station_id": "Madrid puerta del sol",  
                "pricing_plan_id": "Tourist 1 day"  
            }  
        ]  
    }  
}  
```  
</details>  
#### Free_bike_status NGSI-v2 正規化例  
以下は、正規化された JSON-LD 形式の free_bike_status の例である。これはオプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:free_bike_status:id:ZMAW:94046191",  
  "type": "free_bike_status",  
  "last_updated": {  
    "type": "number",  
    "value": 1450156464  
  },  
  "ttl": {  
    "type": "number",  
    "value": 864  
  },  
  "version": {  
    "type": "string",  
    "value": "3.0-RC"  
  },  
  "data": {  
    "type": "object",  
    "value": {  
      "bikes": [  
        {  
          "bike_id": "bike:001:0023",  
          "lat": 9.6,  
          "lon": 18.6,  
          "is_reserved": true,  
          "is_disabled": false,  
          "rental_uris": {  
            "android": "urn:ngsi-ld:free_bike_status:android:DDCU:76475938",  
            "ios": "urn:ngsi-ld:free_bike_status:ios:OJIQ:89241157",  
            "web": "urn:ngsi-ld:free_bike_status:web:XCVS:38778408"  
          },  
          "vehicle_type_id": "regular bike",  
          "last_reported": 1450156464,  
          "current_range_meters": 864.6,  
          "station_id": "Madrid puerta del sol",  
          "pricing_plan_id": "Tourist 1 day"  
        },  
        {  
          "bike_id": "bike:001:0024",  
          "lat": 9.6,  
          "lon": 18.6,  
          "is_reserved": true,  
          "is_disabled": false,  
          "rental_uris": {  
            "android": "urn:ngsi-ld:free_bike_status:android:DDCU:76475938",  
            "ios": "urn:ngsi-ld:free_bike_status:ios:OJIQ:89241157",  
            "web": "urn:ngsi-ld:free_bike_status:web:XCVS:38778408"  
          },  
          "vehicle_type_id": "regular bike",  
          "last_reported": 1450156464,  
          "current_range_meters": 864.6,  
          "station_id": "Madrid puerta del sol",  
          "pricing_plan_id": "Tourist 1 day"  
        }  
      ]  
    }  
  }  
}  
```  
</details>  
#### Free_bike_status NGSI-LD キー値例  
以下は、free_bike_statusをJSON-LD形式でkey-valuesとした例である。これは `options=keyValues` を使用した場合に NGSI-LD と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:free_bike_status:id:ZMAW:94046191",  
    "type": "free_bike_status",  
    "last_updated": 1450156464,  
    "ttl": 864,  
    "version": "3.0-RC",  
    "data": {  
        "bikes": [  
            {  
                "bike_id": "bike:001:0023",  
                "lat": 9.6,  
                "lon": 18.6,  
                "is_reserved": true,  
                "is_disabled": false,  
                "rental_uris": {  
                    "android": "urn:ngsi-ld:free_bike_status:android:DDCU:76475938",  
                    "ios": "urn:ngsi-ld:free_bike_status:ios:OJIQ:89241157",  
                    "web": "urn:ngsi-ld:free_bike_status:web:XCVS:38778408"  
                },  
                "vehicle_type_id": "regular bike",  
                "last_reported": 1450156464,  
                "current_range_meters": 864.6,  
                "station_id": "Madrid puerta del sol",  
                "pricing_plan_id": "Tourist 1 day"  
            },  
            {  
                "bike_id": "bike:001:0024",  
                "lat": 9.6,  
                "lon": 18.6,  
                "is_reserved": true,  
                "is_disabled": false,  
                "rental_uris": {  
                    "android": "urn:ngsi-ld:free_bike_status:android:DDCU:76475938",  
                    "ios": "urn:ngsi-ld:free_bike_status:ios:OJIQ:89241157",  
                    "web": "urn:ngsi-ld:free_bike_status:web:XCVS:38778408"  
                },  
                "vehicle_type_id": "regular bike",  
                "last_reported": 1450156464,  
                "current_range_meters": 864.6,  
                "station_id": "Madrid puerta del sol",  
                "pricing_plan_id": "Tourist 1 day"  
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
#### Free_bike_status NGSI-LD 正規化例  
以下は、free_bike_status を JSON-LD 形式で正規化した例である。これはオプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:free_bike_status:id:ZMAW:94046191",  
    "type": "free_bike_status",  
    "last_updated": {  
        "type": "Property",  
        "value": 1450156464  
    },  
    "ttl": {  
        "type": "Property",  
        "value": 864  
    },  
    "version": {  
        "type": "Property",  
        "value": "3.0-RC"  
    },  
    "data": {  
        "type": "Property",  
        "value": {  
            "bikes": [  
                {  
                    "bike_id": "bike:001:0023",  
                    "lat": 9.6,  
                    "lon": 18.6,  
                    "is_reserved": true,  
                    "is_disabled": false,  
                    "rental_uris": {  
                        "android": "urn:ngsi-ld:free_bike_status:android:DDCU:76475938",  
                        "ios": "urn:ngsi-ld:free_bike_status:ios:OJIQ:89241157",  
                        "web": "urn:ngsi-ld:free_bike_status:web:XCVS:38778408"  
                    },  
                    "vehicle_type_id": "regular bike",  
                    "last_reported": 1450156464,  
                    "current_range_meters": 864.6,  
                    "station_id": "Madrid puerta del sol",  
                    "pricing_plan_id": "Tourist 1 day"  
                },  
                {  
                    "bike_id": "bike:001:0024",  
                    "lat": 9.6,  
                    "lon": 18.6,  
                    "is_reserved": true,  
                    "is_disabled": false,  
                    "rental_uris": {  
                        "android": "urn:ngsi-ld:free_bike_status:android:DDCU:76475938",  
                        "ios": "urn:ngsi-ld:free_bike_status:ios:OJIQ:89241157",  
                        "web": "urn:ngsi-ld:free_bike_status:web:XCVS:38778408"  
                    },  
                    "vehicle_type_id": "regular bike",  
                    "last_reported": 1450156464,  
                    "current_range_meters": 864.6,  
                    "station_id": "Madrid puerta del sol",  
                    "pricing_plan_id": "Tourist 1 day"  
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
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
