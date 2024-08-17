from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, BaseModel, Field, confloat, conint, constr


class FormFactor(Enum):
    bicycle = 'bicycle'
    car = 'car'
    moped = 'moped'
    other = 'other'
    scooter = 'scooter'


class PropulsionType(Enum):
    human = 'human'
    electric_assist = 'electric_assist'
    electric = 'electric'
    combustion = 'combustion'


class VehicleType(BaseModel):
    form_factor: FormFactor = Field(
        ..., description="The vehicle's general form factor."
    )
    max_range_meters: Optional[confloat(ge=0.0)] = Field(
        None,
        description='The furthest distance in meters that the vehicle can travel without recharging or refueling when it has the maximum amount of energy potential.',
    )
    name: Optional[str] = Field(
        None, description='The public name of this vehicle type.'
    )
    propulsion_type: PropulsionType = Field(
        ..., description='The primary propulsion type of the vehicle.'
    )
    vehicle_type_id: str = Field(
        ..., description='Unique identifier of a vehicle type.'
    )


class Data(BaseModel):
    vehicle_types: List[VehicleType] = Field(
        ...,
        description='Array that contains one object per vehicle type in the system as defined below.',
    )


class Type(Enum):
    vehicle_types = 'vehicle_types'


class Version(Enum):
    field_2_1_RC = '2.1-RC'
    field_2_1 = 2.1
    field_2_2 = 2.2
    field_3_0_RC = '3.0-RC'
    field_3_0 = 3.0


class VehicleTypes(BaseModel):
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
        None, description='NGSI entity type. It has to be vehicle_types'
    )
    version: Optional[Version] = Field(
        None,
        description='GBFS version number to which the feed conforms, according to the versioning framework.',
    )
