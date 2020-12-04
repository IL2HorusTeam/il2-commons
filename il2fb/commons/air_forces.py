from typing import Optional

from candv import Values
from candv import VerboseValueConstant
from candv import with_constant_class

from .countries import COUNTRIES
from .countries import CountryConstant

from .exceptions import IL2FBLookupError
from .typing import String

from ._translations import gettext_lazy as _
from ._utils import export


@export
class AirForceConstant(VerboseValueConstant):

  def __init__(
    self,
    country: CountryConstant,
    default_regiment_id: str,
    value: str,
    verbose_name: Optional[String] = None,
    help_text: Optional[String] = None,
  ):
    super().__init__(value, verbose_name=verbose_name, help_text=help_text)
    self.country = country

    if default_regiment_id is not None:
      self.default_regiment_id = str(default_regiment_id)
    else:
      self.default_regiment_id = None

  def merge_into_group(self, group):
    super().merge_into_group(group)
    group.country = self.country
    group.default_regiment_id = self.default_regiment_id

  def to_primitive(self, *args, **kwargs):
    primitive = super().to_primitive(*args, **kwargs)
    country = self.country and self.country.to_primitive(*args, **kwargs)
    primitive['country'] = country
    primitive['default_regiment_id'] = self.default_regiment_id
    return primitive


@export
class AIR_FORCES(with_constant_class(AirForceConstant), Values):
  ALA = AirForceConstant(
    country=COUNTRIES.FR,
    default_regiment_id="fr01",
    value="fr",
    verbose_name=_("ALA"),
    help_text=_("Army of the Air"),
  )
  FAF = AirForceConstant(
    country=COUNTRIES.FI,
    default_regiment_id="f01",
    value="fi",
    verbose_name=_("FAF"),
    help_text=_("Finnish Air Force"),
  )
  FAR = AirForceConstant(
    country=COUNTRIES.RO,
    default_regiment_id="ro01",
    value="ro",
    verbose_name=_("FAR"),
    help_text=_("Romanian Air Force"),
  )
  HAF = AirForceConstant(
    country=COUNTRIES.HU,
    default_regiment_id="h01",
    value="hu",
    verbose_name=_("HAF"),
    help_text=_("Hungarian Air Force"),
  )
  LUFTWAFFE = AirForceConstant(
    country=COUNTRIES.DE,
    default_regiment_id="g01",
    value="de",
    verbose_name=_("Luftwaffe"),
    help_text=_("German Air Force"),
  )
  IJA = AirForceConstant(
    country=COUNTRIES.JP,
    default_regiment_id="ja01",
    value="ja",
    verbose_name=_("IJA"),
    help_text=_("Imperial Japanese Army"),
  )
  IJN = AirForceConstant(
    country=COUNTRIES.JP,
    default_regiment_id="IN_NN",
    value="in",
    verbose_name=_("IJN"),
    help_text=_("Imperial Japanese Navy"),
  )
  PAF = AirForceConstant(
    country=COUNTRIES.PL,
    default_regiment_id="pl01",
    value="pl",
    verbose_name=_("PAF"),
    help_text=_("Polish Air Force"),
  )
  RAI = AirForceConstant(
    country=COUNTRIES.IT,
    default_regiment_id="i01",
    value="it",
    verbose_name=_("RAI"),
    help_text=_("Regia Aeronautica Italiana"),
  )
  RAAF = AirForceConstant(
    country=COUNTRIES.AU,
    default_regiment_id="RA_NN",
    value="ra",
    verbose_name=_("RAAF"),
    help_text=_("Royal Australian Air Force"),
  )
  RAF = AirForceConstant(
    country=COUNTRIES.UK,
    default_regiment_id="gb01",
    value="gb",
    verbose_name=_("RAF"),
    help_text=_("Royal Air Force"),
  )
  RN = AirForceConstant(
    country=COUNTRIES.UK,
    default_regiment_id="RN_NN",
    value="rn",
    verbose_name=_("RN"),
    help_text=_("Royal Navy"),
  )
  RNLAF = AirForceConstant(
    country=COUNTRIES.NL,
    default_regiment_id="DU_NN",
    value="du",
    verbose_name=_("RNLAF"),
    help_text=_("Royal Netherlands Air Force"),
  )
  RNZAF = AirForceConstant(
    country=COUNTRIES.NZ,
    default_regiment_id="RZ_NN",
    value="rz",
    verbose_name=_("RNZAF"),
    help_text=_("Royal New Zealand Air Force"),
  )
  SAF = AirForceConstant(
    country=COUNTRIES.SK,
    default_regiment_id="sk01",
    value="sk",
    verbose_name=_("SAF"),
    help_text=_("Slovak Air Force"),
  )
  USAAF = AirForceConstant(
    country=COUNTRIES.US,
    default_regiment_id="usa01",
    value="us",
    verbose_name=_("USAAF"),
    help_text=_("United States Army Air Forces"),
  )
  USMC = AirForceConstant(
    country=COUNTRIES.US,
    default_regiment_id="UM_NN",
    value="um",
    verbose_name=_("USMC"),
    help_text=_("United States Marine Corps"),
  )
  USN = AirForceConstant(
    country=COUNTRIES.US,
    default_regiment_id="UN_NN",
    value="un",
    verbose_name=_("USN"),
    help_text=_("United States Navy"),
  )
  VVS_RKKA = AirForceConstant(
    country=COUNTRIES.SU,
    default_regiment_id="r01",
    value="ru",
    verbose_name=_("VVS RKKA"),
    help_text=_("Workers-Peasants Red Army Air Forces"),
  )
  NONE = AirForceConstant(
    country=None,
    default_regiment_id=None,
    value="nn",
    verbose_name=_("None"),
    help_text=_("No Air Force"),
  )

  @classmethod
  def get_flight_prefixes(cls):
    return [x.default_regiment_id for x in cls.iterconstants()]

  @classmethod
  def get_by_flight_prefix(cls, prefix):
    for constant in cls.iterconstants():
      if constant.default_regiment_id == prefix:
        return constant

    raise IL2FBLookupError(
      f"air force with prefix '{prefix}' is not present in '{cls.__name__}'"
    )

  @classmethod
  def filter_by_country(cls, country):
    return filter(lambda x: x.country == country, cls.constants())
