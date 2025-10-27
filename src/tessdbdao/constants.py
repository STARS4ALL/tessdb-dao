# ----------------------------------------------------------------------
# Copyright (c) 2022
#
# See the LICENSE file for details
# see the AUTHORS file for authors
# ----------------------------------------------------------------------

from enum import StrEnum


class ObserverType(StrEnum):
    PERSON = "Individual"
    ORG = "Organization"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.value}')"


class PhotometerModel(StrEnum):
    TESSW = "TESS-W"
    TESSWDL = "TESS-WDL"  # Variant with datalogger
    TESS4C = "TESS4C"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.value}')"


class ValidState(StrEnum):
    CURRENT = "Current"
    EXPIRED = "Expired"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.value}')"


# As returned by Nominatim search
class PopulationCentre(StrEnum):
    VILLAGE = "village"
    MUNICIP = "municipality"
    TOWN = "town"
    CITY = "city"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.value}')"


class TimestampSource(StrEnum):
    SUBSCRIBER = "Subscriber"
    PUBLISHER = "Publisher"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.value}')"


class ReadingSource(StrEnum):
    DIRECT = "Direct"
    IMPORTED = "Imported"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.value}')"


class RegisterState(StrEnum):
    MANUAL = "Manual"
    AUTO = "Automatic"
    UNKNOWN = "Unknown"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.value}')"
