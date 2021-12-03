Entity: System_pricing_plans  
============================  
[オープンライセンス](https://github.com/smart-data-models//dataModel.GBFS/blob/master/system_pricing_plans/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述です。**システムの価格設定方法を説明します。標準GBFS2.2**による。  
バージョン: 0.0.1  

## プロパティのリスト  

- `data`: 以下に定義されているように、プランごとに1つのオブジェクトを含む配列。  - `id`: エンティティのユニークな識別子  - `last_updated`: フィードのデータがPOSIX時間で更新された最後の時間。  - `ttl`: フィードのデータが再び更新されるまでの秒数（常にデータを更新する場合は0）。  - `type`: NGSIエンティティタイプ。それはsystem_pricing_plansでなければなりません。  - `version`: フィードが準拠している GBFS のバージョン番号 (v1.1 で追加)。    
必須項目  
- `data`  - `id`  - `last_updated`  - `ttl`  - `type`  - `version`    
規格のマッピング [GBFS 2.2](https://github.com/NABSA/gbfs/blob/v2.2/gbfs.md)  
## データモデルによるプロパティの記述  
アルファベット順（クリックすると詳細が表示されます  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
system_pricing_plans:    
  description: 'Describes the pricing schemes of the system. According to the Standard GBFS 2.2'    
  properties:    
    data:    
      description: 'Array that contains one object per plan as defined below.'    
      properties:    
        plans:    
          items:    
            properties:    
              currency:    
                description: 'Currency used to pay the fare in ISO 4217 code.'    
                pattern: ^\w{3}$    
                type: string    
              description:    
                description: 'Customer-readable description of the pricing plan.'    
                type: string    
              is_taxable:    
                description: 'Will additional tax be added to the base price?'    
                type: boolean    
              name:    
                description: 'Name of this pricing plan.'    
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
                      description: 'The kilometer at which the rate will no longer apply (added in v2.1-RC2).'    
                      minimum: 0    
                      type: number    
                    interval:    
                      description: 'Interval in kilometers at which the rate of this segment is either reapplied indefinitely, or if defined, up until (but not including) end kilometer (added in v2.1-RC2).'    
                      minimum: 0    
                      type: number    
                    rate:    
                      description: 'Rate that is charged for each kilometer interval after the start (added in v2.1-RC2).'    
                      type: number    
                    start:    
                      description: 'Number of kilometers that have to elapse before this segment starts applying (added in v2.1-RC2).'    
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
                      description: 'The minute at which the rate will no longer apply (added in v2.1-RC2).'    
                      minimum: 0    
                      type: number    
                    interval:    
                      description: 'Interval in minutes at which the rate of this segment is either reapplied (added in v2.1-RC2).'    
                      minimum: 0    
                      type: number    
                    rate:    
                      description: 'Rate that is charged for each minute interval after the start (added in v2.1-RC2).'    
                      type: number    
                    start:    
                      description: 'Number of minutes that have to elapse before this segment starts applying (added in v2.1-RC2).'    
                      minimum: 0    
                      type: number    
                  type: object    
                type: array    
              plan_id:    
                description: 'Identifier of a pricing plan in the system.'    
                type: string    
              price:    
                description: 'Fare price.'    
                minimum: 0    
                type: number    
              surge_pricing:    
                description: 'Is there currently an increase in price in response to increased demand in this pricing plan? (added in v2.1-RC2)'    
                type: boolean    
              url:    
                description: 'URL where the customer can learn more about this pricing plan.'    
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
      description: 'NGSI entity type. It has to be system_pricing_plans'    
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
  version: 0.0.1    
```  
</details>    
## ペイロードの例  
#### system_pricing_plans NGSI-v2 key-valuesの例。  
system_pricing_plansをkey-valuesとしてJSON-LD形式で出力した例です。これは、`options=keyValues`を使用した場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
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
            "rate": 0.50,  
            "interval": 1  
          }  
        ]  
      }  
    ]  
  }  
}  
```  
#### system_pricing_plans NGSI-v2 正規化例  
ここでは、JSON-LD形式のsystem_pricing_plansを正規化した例を示します。これは、オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:system_pricing_plans:id:FNNO:60592292",  
  "type": "system_pricing_plans",  
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
              "rate": 0.50,  
              "interval": 1  
            }  
          ]  
        }  
      ]  
    }  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### system_pricing_plans NGSI-LD key-valuesの例。  
JSON-LD形式でkey-valuesとしてsystem_pricing_plansを作成した例を示します。これは、`options=keyValues`を使った場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
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
            "rate": 0.50,  
            "interval": 1  
          }  
        ]  
      }  
    ]  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### system_pricing_plans NGSI-LD 正規化例  
ここでは、JSON-LD形式のsystem_pricing_plansを正規化した例を示します。これは、オプションを使用しない場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
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
              "rate": 0.50,  
              "interval": 1  
            }  
          ]  
        }  
      ]  
    }  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。