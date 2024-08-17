from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, BaseModel, Field, confloat, conint, constr


class VehicleDocksAvailableItem(BaseModel):
    count: Optional[confloat(ge=0.0)] = Field(
        None,
        description='A number representing the total number of available docks for the defined vehicle type (added in v2.1-RC).',
    )
    vehicle_type_ids: Optional[List[str]] = Field(
        None,
        description='An array of strings where each string represents a vehicle_type_id that is able to use a particular type of dock at the station (added in v2.1-RC).',
    )


class Vehicle(BaseModel):
    bike_id: Optional[str] = Field(
        None, description='Rotated identifier of a vehicle (added in v2.1-RC).'
    )
    current_range_meters: Optional[confloat(ge=0.0)] = Field(
        None,
        description="The furthest distance in meters that the vehicle can travel without recharging or refueling with the vehicle's current charge or fuel (added in v2.1-RC).",
    )
    is_disabled: Optional[bool] = Field(
        None,
        description='Is the vehicle currently disabled (broken)? (added in v2.1-RC)',
    )
    is_reserved: Optional[bool] = Field(
        None,
        description='Is the vehicle currently reserved for someone else? (added in v2.1-RC)',
    )
    vehicle_type_id: Optional[str] = Field(
        None,
        description='The vehicle_type_id of this vehicle as described in vehicle_types.json (added in v2.1-RC).',
    )


class VehiclesTypesAvailableItem(BaseModel):
    count: Optional[confloat(ge=0.0)] = Field(
        None,
        description='A number representing the total amount of this vehicle type at the station (added in v2.1-RC).',
    )
    vehicle_type_id: Optional[str] = Field(
        None,
        description='The vehicle_type_id of vehicle at the station (added in v2.1-RC).',
    )


class Station(BaseModel):
    is_installed: Optional[bool] = Field(
        None, description='Is the station currently on the street?'
    )
    is_renting: Optional[bool] = Field(
        None, description='Is the station currently renting vehicles?'
    )
    is_returning: Optional[bool] = Field(
        None, description='Is the station accepting vehicle returns?'
    )
    last_reported: Optional[confloat(ge=1450155600.0)] = Field(
        None,
        description="The last time this station reported its status to the operator's backend in POSIX time.",
    )
    num_bikes_available: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Number of vehicles of any type physically available for rental at the station.',
    )
    num_bikes_disabled: Optional[confloat(ge=0.0)] = Field(
        None, description='Number of disabled vehicles of any type at the station.'
    )
    num_docks_available: Optional[confloat(ge=0.0)] = Field(
        None, description='Number of functional docks physically at the station.'
    )
    num_docks_disabled: Optional[confloat(ge=0.0)] = Field(
        None, description='Number of empty but disabled docks at the station.'
    )
    station_id: Optional[str] = Field(None, description='Identifier of a station.')
    vehicle_docks_available: Optional[List[VehicleDocksAvailableItem]] = Field(
        None,
        description='Object displaying available docks by vehicle type (added in v2.1-RC).',
    )
    vehicles: Optional[List[Vehicle]] = Field(
        None,
        description='Array of objects containing data about a specific vehicle that is present at the docking station (added in v2.1-RC).',
    )
    vehicles_types_available: Optional[List[VehiclesTypesAvailableItem]] = Field(
        None,
        description='Array of objects displaying the total number of each vehicle type at the station (added in v2.1-RC).',
    )


class Data(BaseModel):
    stations: List[Station]


class Type(Enum):
    station_status = 'station_status'


class Version(Enum):
    field_2_1_RC2 = '2.1-RC2'
    field_2_1 = 2.1
    field_2_2 = 2.2
    field_3_0 = 3.0


class StationStatus(BaseModel):
    data: Optional[Data] = Field(
        None, description='Array that contains one object per station as defined below.'
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
        None, description='NGSI entity type. It has to be station_status'
    )
    version: Optional[Version] = Field(
        None,
        description='GBFS version number to which the feed conforms, according to the versioning framework (added in v1.1).',
    )
