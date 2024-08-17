from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, BaseModel, Field, confloat, conint, constr


class PerKmPricingItem(BaseModel):
    end: Optional[confloat(ge=0.0)] = Field(
        None,
        description='The kilometer at which the rate will no longer apply (added in v2.1-RC2).',
    )
    interval: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Interval in kilometers at which the rate of this segment is either reapplied indefinitely, or if defined, up until (but not including) end kilometer (added in v2.1-RC2).',
    )
    rate: Optional[float] = Field(
        None,
        description='Rate that is charged for each kilometer interval after the start (added in v2.1-RC2).',
    )
    start: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Number of kilometers that have to elapse before this segment starts applying (added in v2.1-RC2).',
    )


class PerMinPricingItem(BaseModel):
    end: Optional[confloat(ge=0.0)] = Field(
        None,
        description='The minute at which the rate will no longer apply (added in v2.1-RC2).',
    )
    interval: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Interval in minutes at which the rate of this segment is either reapplied (added in v2.1-RC2).',
    )
    rate: Optional[float] = Field(
        None,
        description='Rate that is charged for each minute interval after the start (added in v2.1-RC2).',
    )
    start: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Number of minutes that have to elapse before this segment starts applying (added in v2.1-RC2).',
    )


class Plan(BaseModel):
    currency: Optional[constr(pattern=r'^\\w{3}$')] = Field(
        None, description='Currency used to pay the fare in ISO 4217 code.'
    )
    description: Optional[str] = Field(
        None, description='Customer-readable description of the pricing plan.'
    )
    is_taxable: Optional[bool] = Field(
        None, description='Will additional tax be added to the base price?'
    )
    name: Optional[str] = Field(None, description='Name of this pricing plan.')
    per_km_pricing: Optional[List[PerKmPricingItem]] = Field(
        None,
        description='Array of segments when the price is a function of distance travelled, displayed in kilometers (added in v2.1-RC2).',
    )
    per_min_pricing: Optional[List[PerMinPricingItem]] = Field(
        None,
        description='Array of segments when the price is a function of time travelled, displayed in minutes (added in v2.1-RC2).',
    )
    plan_id: Optional[str] = Field(
        None, description='Identifier of a pricing plan in the system.'
    )
    price: Optional[confloat(ge=0.0)] = Field(None, description='Fare price.')
    surge_pricing: Optional[bool] = Field(
        None,
        description='Is there currently an increase in price in response to increased demand in this pricing plan? (added in v2.1-RC2)',
    )
    url: Optional[AnyUrl] = Field(
        None,
        description='URL where the customer can learn more about this pricing plan.',
    )


class Data(BaseModel):
    plans: List[Plan]


class Type(Enum):
    system_pricing_plans = 'system_pricing_plans'


class Version(Enum):
    field_2_2 = 2.2
    field_3_0_RC = '3.0-RC'
    field_3_0 = 3.0


class SystemPricingPlans(BaseModel):
    data: Optional[Data] = Field(
        None, description='Array that contains one object per plan as defined below.'
    )
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    last_updated: Optional[conint(ge=1450155600)] = Field(
        None, description='Last time the data in the feed was updated in POSIX time.'
    )
    ttl: Optional[conint(ge=0)] = Field(
        None,
        description='Number of seconds before the data in the feed will be updated again (0 if the data should always be refreshed).',
    )
    type: Optional[Type] = Field(
        None, description='NGSI entity type. It has to be system_pricing_plans'
    )
    version: Optional[Version] = Field(
        None,
        description='GBFS version number to which the feed conforms, according to the versioning framework (added in v1.1).',
    )
