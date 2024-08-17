from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, BaseModel, Field, conint, constr


class Region(BaseModel):
    name: str = Field(..., description='Public name for this region.')
    region_id: str = Field(..., description='identifier of the region.')


class Data(BaseModel):
    regions: List[Region] = Field(..., description='Array of regions.')


class Type(Enum):
    system_regions = 'system_regions'


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


class SystemRegions(BaseModel):
    data: Optional[Data] = Field(None, description='Global data about the regions')
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
        None, description='NGSI entity type. It has to be system_regions'
    )
    version: Optional[Version] = Field(
        None,
        description='GBFS version number to which the feed conforms, according to the versioning framework (added in v1.1).',
    )
