from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, BaseModel, Field, confloat, conint, constr


class RentalUris(BaseModel):
    android: Optional[AnyUrl] = Field(
        None,
        description='URI that can be passed to an Android app with an intent (added in v1.1).',
    )
    ios: Optional[AnyUrl] = Field(
        None,
        description='URI that can be used on iOS to launch the rental app for this vehicle (added in v1.1).',
    )
    web: Optional[AnyUrl] = Field(
        None,
        description='URL that can be used by a web browser to show more information about renting this vehicle (added in v1.1).',
    )


class Bike(BaseModel):
    bike_id: str = Field(
        ..., description='Rotating (as of v2.0) identifier of a vehicle.'
    )
    current_range_meters: Optional[confloat(ge=0.0)] = Field(
        None,
        description="The furthest distance in meters that the vehicle can travel without recharging or refueling with the vehicle's current charge or fuel (added in v2.1-RC).",
    )
    is_disabled: bool = Field(
        ..., description='Is the vehicle currently disabled (broken)?'
    )
    is_reserved: bool = Field(..., description='Is the vehicle currently reserved?')
    last_reported: Optional[confloat(ge=1450155600.0)] = Field(
        None,
        description="The last time this vehicle reported its status to the operator's backend in POSIX time (added in v2.1-RC).",
    )
    lat: Optional[confloat(ge=-90.0, le=90.0)] = Field(
        None, description='The latitude of the vehicle.'
    )
    lon: Optional[confloat(ge=-180.0, le=180.0)] = Field(
        None, description='The longitude of the vehicle.'
    )
    pricing_plan_id: Optional[str] = Field(
        None,
        description='The plan_id of the pricing plan this vehicle is eligible for (added in v2.1-RC2).',
    )
    rental_uris: Optional[RentalUris] = Field(
        None,
        description='Contains rental uris for Android, iOS, and web in the android, ios, and web fields (added in v1.1).',
    )
    station_id: Optional[str] = Field(
        None,
        description='Identifier referencing the station_id if the vehicle is currently at a station (added in v2.1-RC2).',
    )
    vehicle_type_id: Optional[str] = Field(
        None, description='The vehicle_type_id of this vehicle (added in v2.1-RC).'
    )


class Data(BaseModel):
    bikes: Optional[List[Bike]] = None


class Type(Enum):
    free_bike_status = 'free_bike_status'


class Version(Enum):
    field_2_2 = 2.2
    field_3_0_RC = '3.0-RC'
    field_3_0 = 3.0


class FreeBikeStatus(BaseModel):
    data: Optional[Data] = Field(
        None, description='Array that contains one object per bike as defined below.'
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
        None, description='NGSI entity type. It has to be free_bike_status'
    )
    version: Optional[Version] = Field(
        None,
        description='GBFS version number to which the feed conforms, according to the versioning framework (added in v1.1).',
    )
