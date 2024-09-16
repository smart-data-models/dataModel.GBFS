from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, BaseModel, ConfigDict, Field, conint, constr


class Version1(Enum):
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


class Version(BaseModel):
    url: AnyUrl = Field(..., description='URL of the corresponding gbfs.json endpoint')
    version: Version1 = Field(
        ..., description='The semantic version of the feed in the form X.Y'
    )


class Data(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    versions: List[Version] = Field(
        ...,
        description='Contains one object, as defined below, for each of the available versions of a feed. The array must be sorted by increasing MAJOR and MINOR version number.',
    )


class Type(Enum):
    gbfs_versions = 'gbfs_versions'


class Version2(Enum):
    field_1_1_RC = '1.1-RC'
    field_1_1 = 1.1
    field_2_0_RC = '2.0-RC'
    field_2_0 = 2.0
    field_2_1_RC = '2.1-RC'
    field_2_1 = 2.1
    field_2_2 = 2.2
    field_3_0_RC = '3.0-RC'
    field_3_0 = 3.0


class GbfsVersions(BaseModel):
    data: Optional[Data] = Field(
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
        None, description='NGSI entity type. It has to be gbfs_versions'
    )
    version: Optional[Version2] = Field(
        None,
        description='GBFS version number to which the feed conforms, according to the versioning framework.',
    )