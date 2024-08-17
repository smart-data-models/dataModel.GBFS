from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, BaseModel, Field, confloat, conint, constr


class Time(BaseModel):
    end: Optional[confloat(ge=1450155600.0)] = Field(
        None, description='End time of the alert.'
    )
    start: Optional[confloat(ge=1450155600.0)] = Field(
        None, description='Start time of the alert.'
    )


class Type(Enum):
    system_closure = 'system_closure'
    station_closure = 'station_closure'
    station_move = 'station_move'
    other = 'other'


class Alert(BaseModel):
    alert_id: str = Field(..., description='Identifier for this alert.')
    description: Optional[str] = Field(
        None, description='Detailed description of the alert.'
    )
    last_updated: Optional[confloat(ge=1450155600.0)] = Field(
        None, description='Indicates the last time the info for the alert was updated.'
    )
    region_ids: Optional[List[str]] = Field(
        None,
        description='Array of identifiers of the regions for which this alert applies.',
    )
    station_ids: Optional[List[str]] = Field(
        None,
        description='Array of identifiers of the stations for which this alert applies.',
    )
    summary: str = Field(
        ...,
        description='A short summary of this alert to be displayed to the customer.',
    )
    times: Optional[List[Time]] = Field(
        None, description='Array of objects indicating when the alert is in effect.'
    )
    type: Type = Field(..., description='Type of alert.')
    url: Optional[AnyUrl] = Field(
        None,
        description='URL where the customer can learn more information about this alert.',
    )


class Data(BaseModel):
    alerts: List[Alert]


class Type1(Enum):
    system_alerts = 'system_alerts'


class Version(Enum):
    field_1_1_RC = '1.1-RC'
    field_1_1 = 1.1
    field_2_0_RC = '2.0-RC'
    field_2_0 = 2.0
    field_2_1_RC = '2.1-RC'
    field_2_1_RC2 = '2.1-RC2'
    field_2_1 = 2.1
    field_2_2 = 2.2
    field_3_0_RC = '3.0-RC'
    field_3_0 = 3.0


class SystemAlerts(BaseModel):
    data: Optional[Data] = Field(
        None, description='Array that contains ad-hoc alerts for the system.'
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
    type: Optional[Type1] = Field(
        None, description='NGSI entity type. It has to be system_alerts'
    )
    version: Optional[Version] = Field(
        None,
        description='GBFS version number to which the feed conforms, according to the versioning framework (added in v1.1).',
    )
