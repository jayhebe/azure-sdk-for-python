# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class ConfigurationDataType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Data type of the configuration.
    """

    BOOLEAN = "Boolean"
    NUMERIC = "Numeric"
    INTEGER = "Integer"
    ENUMERATION = "Enumeration"

class CreatedByType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of identity that created the resource.
    """

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"

class CreateMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The mode to create a new PostgreSQL server.
    """

    DEFAULT = "Default"
    CREATE = "Create"
    UPDATE = "Update"
    POINT_IN_TIME_RESTORE = "PointInTimeRestore"

class CreateModeForUpdate(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The mode to update a new PostgreSQL server.
    """

    DEFAULT = "Default"
    UPDATE = "Update"

class GeoRedundantBackupEnum(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """A value indicating whether Geo-Redundant backup is enabled on the server.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class HighAvailabilityMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The HA mode for the server.
    """

    DISABLED = "Disabled"
    ZONE_REDUNDANT = "ZoneRedundant"

class OperationOrigin(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The intended executor of the operation.
    """

    NOT_SPECIFIED = "NotSpecified"
    USER = "user"
    SYSTEM = "system"

class ServerHAState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """A state of a HA server that is visible to user.
    """

    NOT_ENABLED = "NotEnabled"
    CREATING_STANDBY = "CreatingStandby"
    REPLICATING_DATA = "ReplicatingData"
    FAILING_OVER = "FailingOver"
    HEALTHY = "Healthy"
    REMOVING_STANDBY = "RemovingStandby"

class ServerPublicNetworkAccessState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """public network access is enabled or not
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class ServerState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """A state of a server that is visible to user.
    """

    READY = "Ready"
    DROPPING = "Dropping"
    DISABLED = "Disabled"
    STARTING = "Starting"
    STOPPING = "Stopping"
    STOPPED = "Stopped"
    UPDATING = "Updating"

class ServerVersion(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The version of a server.
    """

    THIRTEEN = "13"
    TWELVE = "12"
    ELEVEN = "11"

class SkuTier(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The tier of the particular SKU, e.g. Burstable.
    """

    BURSTABLE = "Burstable"
    GENERAL_PURPOSE = "GeneralPurpose"
    MEMORY_OPTIMIZED = "MemoryOptimized"
