from candv import Values
from candv import VerboseValueConstant
from candv import with_constant_class

from .countries import COUNTRY
from .exceptions import IL2FBLookupError

from ._translations import gettext_lazy as _
from ._utils import export


@export
class AirForceConstant(VerboseValueConstant):

  def __init__(
    self,
    country,
    default_flight_prefix,
    value,
    verbose_name=None,
    help_text=None,
  ):
    super().__init__(value, verbose_name=verbose_name, help_text=help_text)
    self.country = country

    if default_flight_prefix is not None:
      self.default_flight_prefix = str(default_flight_prefix)
    else:
      self.default_flight_prefix = None

  def merge_into_group(self, group):
    super().merge_into_group(group)
    group.country = self.country
    group.default_flight_prefix = self.default_flight_prefix

  def to_primitive(self, context=None):
    primitive = super().to_primitive(context)
    country = self.country and self.country.to_primitive(context)
    primitive.update({
      'country': country,
      'default_flight_prefix': self.default_flight_prefix,
    })
    return primitive


@export
class AIR_FORCE(with_constant_class(AirForceConstant), Values):
  ALA = AirForceConstant(
    country=COUNTRY.FR,
    default_flight_prefix="fr01",
    value="fr",
    verbose_name=_("ALA"),
    help_text=_("Army of the Air"),
  )
  FAF = AirForceConstant(
    country=COUNTRY.FI,
    default_flight_prefix="f01",
    value="fi",
    verbose_name=_("FAF"),
    help_text=_("Finnish Air Force"),
  )
  FAR = AirForceConstant(
    country=COUNTRY.RO,
    default_flight_prefix="ro01",
    value="ro",
    verbose_name=_("FAR"),
    help_text=_("Romanian Air Force"),
  )
  HAF = AirForceConstant(
    country=COUNTRY.HU,
    default_flight_prefix="h01",
    value="hu",
    verbose_name=_("HAF"),
    help_text=_("Hungarian Air Force"),
  )
  LUFTWAFFE = AirForceConstant(
    country=COUNTRY.DE,
    default_flight_prefix="g01",
    value="de",
    verbose_name=_("Luftwaffe"),
    help_text=_("German Air Force"),
  )
  IJA = AirForceConstant(
    country=COUNTRY.JP,
    default_flight_prefix="ja01",
    value="ja",
    verbose_name=_("IJA"),
    help_text=_("Imperial Japanese Army"),
  )
  IJN = AirForceConstant(
    country=COUNTRY.JP,
    default_flight_prefix="IN_NN",
    value="in",
    verbose_name=_("IJN"),
    help_text=_("Imperial Japanese Navy"),
  )
  PAF = AirForceConstant(
    country=COUNTRY.PL,
    default_flight_prefix="pl01",
    value="pl",
    verbose_name=_("PAF"),
    help_text=_("Polish Air Force"),
  )
  RAI = AirForceConstant(
    country=COUNTRY.IT,
    default_flight_prefix="i01",
    value="it",
    verbose_name=_("RAI"),
    help_text=_("Regia Aeronautica Italiana"),
  )
  RAAF = AirForceConstant(
    country=COUNTRY.AU,
    default_flight_prefix="RA_NN",
    value="ra",
    verbose_name=_("RAAF"),
    help_text=_("Royal Australian Air Force"),
  )
  RAF = AirForceConstant(
    country=COUNTRY.UK,
    default_flight_prefix="gb01",
    value="gb",
    verbose_name=_("RAF"),
    help_text=_("Royal Air Force"),
  )
  RN = AirForceConstant(
    country=COUNTRY.UK,
    default_flight_prefix="RN_NN",
    value="rn",
    verbose_name=_("RN"),
    help_text=_("Royal Navy"),
  )
  RNLAF = AirForceConstant(
    country=COUNTRY.NL,
    default_flight_prefix="DU_NN",
    value="du",
    verbose_name=_("RNLAF"),
    help_text=_("Royal Netherlands Air Force"),
  )
  RNZAF = AirForceConstant(
    country=COUNTRY.NZ,
    default_flight_prefix="RZ_NN",
    value="rz",
    verbose_name=_("RNZAF"),
    help_text=_("Royal New Zealand Air Force"),
  )
  SAF = AirForceConstant(
    country=COUNTRY.SK,
    default_flight_prefix="sk01",
    value="sk",
    verbose_name=_("SAF"),
    help_text=_("Slovak Air Force"),
  )
  USAAF = AirForceConstant(
    country=COUNTRY.US,
    default_flight_prefix="usa01",
    value="us",
    verbose_name=_("USAAF"),
    help_text=_("United States Army Air Forces"),
  )
  USMC = AirForceConstant(
    country=COUNTRY.US,
    default_flight_prefix="UM_NN",
    value="um",
    verbose_name=_("USMC"),
    help_text=_("United States Marine Corps"),
  )
  USN = AirForceConstant(
    country=COUNTRY.US,
    default_flight_prefix="UN_NN",
    value="un",
    verbose_name=_("USN"),
    help_text=_("United States Navy"),
  )
  VVS_RKKA = AirForceConstant(
    country=COUNTRY.SU,
    default_flight_prefix="r01",
    value="ru",
    verbose_name=_("VVS RKKA"),
    help_text=_("Workers-Peasants Red Army Air Forces"),
  )
  NONE = AirForceConstant(
    country=None,
    default_flight_prefix=None,
    value="nn",
    verbose_name=_("None"),
    help_text=_("No Air Force"),
  )

  @classmethod
  def get_flight_prefixes(cls):
    return [x.default_flight_prefix for x in cls.iterconstants()]

  @classmethod
  def get_by_flight_prefix(cls, prefix):
    for constant in cls.iterconstants():
      if constant.default_flight_prefix == prefix:
        return constant

    raise IL2FBLookupError(
      f"air force with prefix '{prefix}' is not present in '{cls.__name__}'"
    )

  @classmethod
  def filter_by_country(cls, country):
    return filter(lambda x: x.country == country, cls.constants())
