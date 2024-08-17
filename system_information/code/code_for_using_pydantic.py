from __future__ import annotations

from enum import Enum
from typing import Optional, Union

from pydantic import AnyUrl, BaseModel, EmailStr, Field, conint, constr


class Android(BaseModel):
    discovery_uri: Optional[AnyUrl] = Field(
        None,
        description='URI that can be used to discover if the rental Android app is installed on the device (added in v1.1).',
    )
    store_uri: Optional[AnyUrl] = Field(
        None,
        description='URI where the rental Android app can be downloaded from (added in v1.1).',
    )


class Ios(BaseModel):
    discovery_uri: Optional[AnyUrl] = Field(
        None,
        description='URI that can be used to discover if the rental iOS app is installed on the device (added in v1.1).',
    )
    store_uri: Optional[AnyUrl] = Field(
        None,
        description='URI where the rental iOS app can be downloaded from (added in v1.1).',
    )


class RentalApps(BaseModel):
    android: Optional[Android] = Field(
        None,
        description='Contains rental app download and app discovery information for the Android platform. (added in v1.1)',
    )
    ios: Optional[Ios] = Field(
        None,
        description='Contains rental information for the iOS platform (added in v1.1).',
    )


class Data(BaseModel):
    email: Optional[EmailStr] = Field(
        None,
        description="Email address actively monitored by the operator's customer service department.",
    )
    feed_contact_email: Optional[EmailStr] = Field(
        None,
        description='A single contact email address for consumers of this feed to report technical issues (added in v1.1).',
    )
    language: constr(pattern=r'^[a-z]{2,3}(-[A-Z]{2})?$') = Field(
        ...,
        description='The language that will be used throughout the rest of the files. It must match the value in the gbfs.json file.',
    )
    license_url: Optional[AnyUrl] = Field(
        None,
        description='A fully qualified URL of a page that defines the license terms for the GBFS data for this system.',
    )
    name: str = Field(
        ..., description='Name of the system to be displayed to customers.'
    )
    operator: Optional[str] = Field(None, description='Name of the operator')
    phone_number: Optional[str] = Field(
        None,
        description="A single voice telephone number for the specified system that presents the telephone number as typical for the system's service area.",
    )
    purchase_url: Optional[AnyUrl] = Field(
        None, description='URL where a customer can purchase a membership.'
    )
    rental_apps: Optional[RentalApps] = Field(
        None,
        description='Contains rental app information in the android and ios JSON objects (added in v1.1).',
    )
    short_name: Optional[str] = Field(
        None, description='Optional abbreviation for a system.'
    )
    start_date: Optional[constr(pattern=r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$')] = Field(
        None, description='Date that the system began operations.'
    )
    system_id: str = Field(
        ...,
        description='Identifier for this vehicle share system. This should be globally unique (even between different systems).',
    )
    timezone: str = Field(..., description='The time zone where the system is located.')
    url: Optional[AnyUrl] = Field(
        None, description='The URL of the vehicle share system.'
    )


class Type(Enum):
    system_information = 'system_information'


class Version(Enum):
    field_1_1_RC = '1.1-RC'
    field_1_1 = 1.1
    field_2_0 = 2.0
    field_2_1_RC = '2.1-RC'
    field_2_1_RC2 = '2.1-RC2'
    field_2_1 = 2.1
    field_2_2 = 2.2
    field_3_0 = 3.0


class SystemInformation(BaseModel):
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
        None, description='NGSI entity type. It has to be system_information'
    )
    version: Optional[Version] = Field(
        None,
        description='GBFS version number to which the feed conforms, according to the versioning framework (added in v1.1).',
    )
