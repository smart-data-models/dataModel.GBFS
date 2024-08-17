from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, BaseModel, Field, conint, constr


class Day(Enum):
    sun = 'sun'
    mon = 'mon'
    tue = 'tue'
    wed = 'wed'
    thu = 'thu'
    fri = 'fri'
    sat = 'sat'


class UserType(Enum):
    member = 'member'
    nonmember = 'nonmember'


class RentalHour(BaseModel):
    days: List[Day] = Field(
        ...,
        description='An array of abbreviations (first 3 letters) of English names of the days of the week for which this object applies.',
        max_length=7,
        min_length=1,
    )
    end_time: constr(pattern=r'^([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$') = Field(
        ..., description='End time for the hours of operation of the system.'
    )
    start_time: constr(pattern=r'^([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$') = Field(
        ..., description='Start time for the hours of operation of the system.'
    )
    user_types: List[UserType] = Field(
        ...,
        description='Array of member and nonmember value(s) indicating that this set of rental hours applies to either members or non-members only.',
        max_length=2,
        min_length=1,
    )


class Data(BaseModel):
    rental_hours: List[RentalHour]


class Type(Enum):
    system_hours = 'system_hours'


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


class SystemHours(BaseModel):
    data: Optional[Data] = Field(
        None, description='Array that contains system hours of operations.'
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
        None, description='NGSI entity type. It has to be system_hours'
    )
    version: Optional[Version] = Field(
        None,
        description='GBFS version number to which the feed conforms, according to the versioning framework (added in v1.1).',
    )
