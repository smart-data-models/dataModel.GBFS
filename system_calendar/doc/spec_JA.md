エンティティ：system_calendar  
======================  
[オープンライセンス](https://github.com/smart-data-models//dataModel.GBFS/blob/master/system_calendar/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述です。**システムの動作カレンダーを示す。規格GBFS2.2による。  
バージョン: 0.0.1  

## プロパティのリスト  

- `data`: システムの操作カレンダーを格納する配列です。  - `id`: エンティティのユニークな識別子  - `last_updated`: フィードのデータがPOSIX時間で更新された最後の時間。  - `ttl`: フィードのデータが再び更新されるまでの秒数（常にデータを更新する場合は0）。  - `type`: NGSIエンティティタイプ。それはsystem_calendarでなければならない。  - `version`: フィードが準拠している GBFS のバージョン番号 (v1.1 で追加)。    
必須項目  
- `data`  - `id`  - `last_updated`  - `ttl`  - `type`  - `version`    
規格のマッピング [GBFS 2.2](https://github.com/NABSA/gbfs/blob/v2.2/gbfs.md)  
## データモデルによるプロパティの記述  
アルファベット順（クリックすると詳細が表示されます  
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
  version: 0.0.1    
```  
</details>    
## ペイロードの例  
#### system_calendar NGSI-v2 key-values の例。  
key-valuesとしてJSON-LD形式のsystem_calendarの例を示します。これは`options=keyValues`を使った場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### system_calendar NGSI-v2 正規化された例。  
正規化されたJSON-LD形式のsystem_calendarの例を示します。これは、オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### system_calendar NGSI-LDのキーバリューの例。  
JSON-LD形式でkey-valuesとしてsystem_calendarを作成した例です。これは`options=keyValues`を使った場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
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
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### system_calendar NGSI-LD 正規化例  
ここでは、JSON-LD形式のsystem_calendarを正規化した例を示します。これはオプションを使用しない場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
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
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
