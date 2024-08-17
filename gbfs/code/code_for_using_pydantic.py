from __future__ import annotations

from enum import Enum
from typing import Dict, List, Optional, Union

from pydantic import AnyUrl, BaseModel, Field, conint, constr


class Name(Enum):
    gbfs = 'gbfs'
    gbfs_versions = 'gbfs_versions'
    system_information = 'system_information'
    vehicle_types = 'vehicle_types'
    station_information = 'station_information'
    station_status = 'station_status'
    free_bike_status = 'free_bike_status'
    system_hours = 'system_hours'
    system_alerts = 'system_alerts'
    system_calendar = 'system_calendar'
    system_regions = 'system_regions'
    system_pricing_plans = 'system_pricing_plans'
    geofencing_zones = 'geofencing_zones'


class Feed(BaseModel):
    name: Name = Field(
        ...,
        description='Key identifying the type of feed this is. The key must be the base file name defined in the spec for the corresponding feed type.',
    )
    url: AnyUrl = Field(..., description='URL for the feed.')


class Data(BaseModel):
    feeds: Optional[List[Feed]] = Field(
        None,
        description='An array of all of the feeds that are published by the auto-discovery file. Each element in the array is an object with the keys below.',
    )


class Type(Enum):
    gbfs = 'gbfs'


class Version(Enum):
    field_2_1_RC = '2.1-RC'
    field_2_1_RC2 = '2.1-RC2'
    field_2_1 = 2.1
    field_2_2 = 2.2
    field_3_0_RC = '3.0-RC'
    field_3_0 = 3.0


class Gbfs(BaseModel):
    data: Optional[Dict[constr(pattern=r'^[a-z]{2,3}(-[A-Z]{2})?$'), Data]] = Field(
        None, description='Response data in the form of name:value pairs.'
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
        None, description='NGSI entity type. It has to be gbfs'
    )
    version: Optional[Version] = Field(
        None,
        description='GBFS version number to which the feed conforms, according to the versioning framework (added in v1.1).',
    )
