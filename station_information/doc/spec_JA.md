Entity: Station_information  
===========================  
[オープンライセンス](https://github.com/smart-data-models//dataModel.GBFS/blob/master/station_information/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述。**システムオペレーター、システムの所在地、導入年、URL、連絡先、タイムゾーンなどの詳細情報。規格GBFS2.2による。  
バージョン: 0.0.1  

## プロパティのリスト  

- `data`: 以下に定義されているように、各ステーションごとに1つのオブジェクトを含む配列です。  - `id`: エンティティのユニークな識別子  - `last_updated`: フィードのデータがPOSIX時間で更新された最後の時間。  - `ttl`: フィードのデータが再び更新されるまでの秒数（常にデータを更新する場合は0）。  - `type`: NGSIエンティティタイプ。ステーション情報でなければならない。  - `version`: フィードが準拠している GBFS のバージョン番号 (v1.1 で追加)。    
必須項目  
- `data`  - `id`  - `last_updated`  - `ttl`  - `type`  - `version`    
規格のマッピング [GBFS 2.2](https://github.com/NABSA/gbfs/blob/v2.2/gbfs.md)  
## データモデルによるプロパティの記述  
アルファベット順（クリックすると詳細が表示されます  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
station_information:    
  description: 'Details including system operator, system location, year implemented, URL, contact info, time zone. According to the Standard GBFS 2.2'    
  properties:    
    data:    
      description: 'Array that contains one object per station as defined below.'    
      properties:    
        stations:    
          items:    
            properties:    
              address:    
                description: 'Address where station is located.'    
                type: string    
              capacity:    
                description: 'Number of total docking points installed at this station, both available and unavailable.'    
                minimum: 0    
                type: number    
              cross_street:    
                description: 'Cross street or landmark where the station is located.'    
                type: string    
              is_valet_station:    
                description: 'Are valet services provided at this station? (added in v2.1-RC)'    
                type: boolean    
              is_virtual_station:    
                description: 'Is this station a location with or without physical infrastructure? (added in v2.1-RC)'    
                type: boolean    
              lat:    
                description: 'The latitude of the station.'    
                maximum: 90    
                minimum: -90    
                type: number    
              lon:    
                description: 'The longitude fo the station.'    
                maximum: 180    
                minimum: -180    
                type: number    
              name:    
                description: 'Public name of the station.'    
                type: string    
              post_code:    
                description: 'Postal code where station is located.'    
                type: string    
              region_id:    
                description: 'Identifier of the region where the station is located.'    
                type: string    
              rental_methods:    
                description: 'Payment methods accepted at this station.'    
                items:    
                  enum:    
                    - key    
                    - creditcard    
                    - paypass    
                    - applepay    
                    - androidpay    
                    - transitcard    
                    - accountnumber    
                    - phone    
                  type: string    
                minItems: 1    
                type: array    
              rental_uris:    
                description: 'Contains rental uris for Android, iOS, and web in the android, ios, and web fields (added in v1.1).'    
                properties:    
                  android:    
                    description: 'URI that can be passed to an Android app with an intent (added in v1.1).'    
                    format: uri    
                    type: string    
                  ios:    
                    description: 'URI that can be used on iOS to launch the rental app for this station (added in v1.1).'    
                    format: uri    
                    type: string    
                  web:    
                    description: 'URL that can be used by a web browser to show more information about renting a vehicle at this station (added in v1.1).'    
                    format: uri    
                    type: string    
                type: object    
              short_name:    
                description: 'Short name or other type of identifier.'    
                type: string    
              station_area:    
                description: 'A multipolygon that describes the area of a virtual station (added in v2.1-RC).'    
                properties:    
                  coordinates:    
                    items:    
                      items:    
                        items:    
                          items:    
                            type: number    
                          minItems: 2    
                          type: array    
                        minItems: 4    
                        type: array    
                      type: array    
                    type: array    
                  type:    
                    enum:    
                      - Multipolygon    
                    type: string    
                required:    
                  - type    
                  - coordinates    
                type: object    
              station_id:    
                description: 'Identifier of a station.'    
                type: string    
              vehicle_capacity:    
                additionalProperties:    
                  type: number    
                description: 'An object where each key is a vehicle_type_id and the value is a number presenting the total number of vehicles of this type that can park within the station_area (added in v2.1-RC).'    
                type: object    
              vehicle_type_capacity:    
                additionalProperties:    
                  type: number    
                description: 'An object where each key is a vehicle_type_id and the value is a number representing the total docking points installed at this station for each vehicle type (added in v2.1-RC).'    
                type: object    
            required:    
              - station_id    
              - name    
              - lat    
              - lon    
            type: object    
          type: array    
      required:    
        - stations    
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
      description: 'NGSI entity type. It has to be station_information'    
      enum:    
        - station_information    
      type: string    
      x-ngsi:    
        type: Property    
    version:    
      description: 'GBFS version number to which the feed conforms, according to the versioning framework (added in v1.1).'    
      enum:    
        - 2.1-RC2    
        - 2.1    
        - 2.2    
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
  version: 0.0.1    
```  
</details>    
## ペイロードの例  
#### station_information NGSI-v2 key-values の例。  
Station_informationをkey-valuesとしてJSON-LD形式で記述した例を示します。これは`options=keyValues`を使った場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:station_information:id:FNNO:60592292",  
  "type": "station_information",  
  "last_updated": 1609866247,  
  "ttl": 0,  
  "version": "3.0",  
  "data": {  
    "stations": [  
      {  
        "station_id": "station12",  
        "name": "SE Belmont & SE 10 th",  
        "lat": -82.655775,  
        "lon": 45.516445,  
        "is_valet_station": false,  
        "is_virtual_station": true,  
        "station_area": {  
          "type": "Multipolygon",  
          "coordinates": [  
            [  
              [  
                [  
                  -122.655775,  
                  45.516445  
                ],  
                [  
                  -122.655705,  
                  45.516445  
                ],  
                [  
                  -122.655705,  
                  45.516495  
                ],  
                [  
                  -122.655775,  
                  45.516495  
                ],  
                [  
                  -122.655775,  
                  45.516445  
                ]  
              ]  
            ]  
          ]  
        },  
        "capacity": 16,  
        "vehicle_capacity": {  
          "abc123": 8,  
          "def456": 8,  
          "ghi789": 16  
        }  
      }  
    ]  
  }  
}  
```  
#### station_information NGSI-v2 正規化例  
正規化されたJSON-LD形式のstation_informationの例を示します。これは、オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:station_information:id:FNNO:60592292",  
  "type": "station_information",  
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
      "stations": [  
        {  
          "station_id": "station12",  
          "name": "SE Belmont & SE 10 th",  
          "lat": -82.655775,  
          "lon": 45.516445,  
          "is_valet_station": false,  
          "is_virtual_station": true,  
          "station_area": {  
            "type": "Multipolygon",  
            "coordinates": [  
              [  
                [  
                  [  
                    -122.655775,  
                    45.516445  
                  ],  
                  [  
                    -122.655705,  
                    45.516445  
                  ],  
                  [  
                    -122.655705,  
                    45.516495  
                  ],  
                  [  
                    -122.655775,  
                    45.516495  
                  ],  
                  [  
                    -122.655775,  
                    45.516445  
                  ]  
                ]  
              ]  
            ]  
          },  
          "capacity": 16,  
          "vehicle_capacity": {  
            "abc123": 8,  
            "def456": 8,  
            "ghi789": 16  
          }  
        }  
      ]  
    }  
  }  
}  
```  
#### station_information NGSI-LD key-values の例。  
Station_informationをkey-valuesとしてJSON-LD形式で記述した例を示します。これは`options=keyValues`を使った場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:station_information:id:FNNO:60592292",  
  "type": "station_information",  
  "last_updated": 1609866247,  
  "ttl": 0,  
  "version": "3.0",  
  "data": {  
    "stations": [  
      {  
        "station_id": "station12",  
        "name": "SE Belmont & SE 10 th",  
        "lat": -82.655775,  
        "lon": 45.516445,  
        "is_valet_station": false,  
        "is_virtual_station": true,  
        "station_area": {  
          "type": "Multipolygon",  
          "coordinates": [  
            [  
              [  
                [  
                  -122.655775,  
                  45.516445  
                ],  
                [  
                  -122.655705,  
                  45.516445  
                ],  
                [  
                  -122.655705,  
                  45.516495  
                ],  
                [  
                  -122.655775,  
                  45.516495  
                ],  
                [  
                  -122.655775,  
                  45.516445  
                ]  
              ]  
            ]  
          ]  
        },  
        "capacity": 16,  
        "vehicle_capacity": {  
          "abc123": 8,  
          "def456": 8,  
          "ghi789": 16  
        }  
      }  
    ]  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### station_information NGSI-LDの正規化例  
ここでは、JSON-LD形式のstation_informationを正規化した例を示します。これはオプションを使用しない場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:station_information:id:FNNO:60592292",  
  "type": "station_information",  
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
      "stations": [  
        {  
          "station_id": "station12",  
          "name": "SE Belmont & SE 10 th",  
          "lat": -82.655775,  
          "lon": 45.516445,  
          "is_valet_station": false,  
          "is_virtual_station": true,  
          "station_area": {  
            "type": "Multipolygon",  
            "coordinates": [  
              [  
                [  
                  [  
                    -122.655775,  
                    45.516445  
                  ],  
                  [  
                    -122.655705,  
                    45.516445  
                  ],  
                  [  
                    -122.655705,  
                    45.516495  
                  ],  
                  [  
                    -122.655775,  
                    45.516495  
                  ],  
                  [  
                    -122.655775,  
                    45.516445  
                  ]  
                ]  
              ]  
            ]  
          },  
          "capacity": 16,  
          "vehicle_capacity": {  
            "abc123": 8,  
            "def456": 8,  
            "ghi789": 16  
          }  
        }  
      ]  
    }  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
