from candv import Values
from candv import VerboseValueConstant
from candv import with_constant_class

from .countries import Countries
from ._translations import gettext_lazy as _


class AirForce(VerboseValueConstant):

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
    super(AirForce, self).merge_into_group(group)
    group.country = self.country
    group.default_flight_prefix = self.default_flight_prefix

  def to_primitive(self, context=None):
    primitive = super(AirForce, self).to_primitive(context)
    country = self.country and self.country.to_primitive(context)
    primitive.update({
      'country': country,
      'default_flight_prefix': self.default_flight_prefix,
    })
    return primitive


class AirForces(with_constant_class(AirForce), Values):
  ala = AirForce(
    country=Countries.fr,
    default_flight_prefix='fr01',
    value='fr',
    verbose_name=_("ALA"),
    help_text=_("Army of the Air"),
  )
  faf = AirForce(
    country=Countries.fi,
    default_flight_prefix='f01',
    value='fi',
    verbose_name=_("FAF"),
    help_text=_("Finnish Air Force"),
  )
  far = AirForce(
    country=Countries.ro,
    default_flight_prefix='ro01',
    value='ro',
    verbose_name=_("FAR"),
    help_text=_("Romanian Air Force"),
  )
  haf = AirForce(
    country=Countries.hu,
    default_flight_prefix='h01',
    value='hu',
    verbose_name=_("HAF"),
    help_text=_("Hungarian Air Force"),
  )
  luftwaffe = AirForce(
    country=Countries.de,
    default_flight_prefix='g01',
    value='de',
    verbose_name=_("Luftwaffe"),
    help_text=_("German Air Force"),
  )
  ija = AirForce(
    country=Countries.jp,
    default_flight_prefix='ja01',
    value='ja',
    verbose_name=_("IJA"),
    help_text=_("Imperial Japanese Army"),
  )
  ijn = AirForce(
    country=Countries.jp,
    default_flight_prefix='IN_NN',
    value='in',
    verbose_name=_("IJN"),
    help_text=_("Imperial Japanese Navy"),
  )
  paf = AirForce(
    country=Countries.pl,
    default_flight_prefix='pl01',
    value='pl',
    verbose_name=_("PAF"),
    help_text=_("Polish Air Force"),
  )
  rai = AirForce(
    country=Countries.it,
    default_flight_prefix='i01',
    value='it',
    verbose_name=_("RAI"),
    help_text=_("Regia Aeronautica Italiana"),
  )
  raaf = AirForce(
    country=Countries.au,
    default_flight_prefix='RA_NN',
    value='ra',
    verbose_name=_("RAAF"),
    help_text=_("Royal Australian Air Force"),
  )
  raf = AirForce(
    country=Countries.uk,
    default_flight_prefix='gb01',
    value='gb',
    verbose_name=_("RAF"),
    help_text=_("Royal Air Force"),
  )
  rn = AirForce(
    country=Countries.uk,
    default_flight_prefix='RN_NN',
    value='rn',
    verbose_name=_("RN"),
    help_text=_("Royal Navy"),
  )
  rnlaf = AirForce(
    country=Countries.nl,
    default_flight_prefix='DU_NN',
    value='du',
    verbose_name=_("RNLAF"),
    help_text=_("Royal Netherlands Air Force"),
  )
  rnzaf = AirForce(
    country=Countries.nz,
    default_flight_prefix='RZ_NN',
    value='rz',
    verbose_name=_("RNZAF"),
    help_text=_("Royal New Zealand Air Force"),
  )
  saf = AirForce(
    country=Countries.sk,
    default_flight_prefix='sk01',
    value='sk',
    verbose_name=_("SAF"),
    help_text=_("Slovak Air Force"),
  )
  usaaf = AirForce(
    country=Countries.us,
    default_flight_prefix='usa01',
    value='us',
    verbose_name=_("USAAF"),
    help_text=_("United States Army Air Forces"),
  )
  usmc = AirForce(
    country=Countries.us,
    default_flight_prefix='UM_NN',
    value='um',
    verbose_name=_("USMC"),
    help_text=_("United States Marine Corps"),
  )
  usn = AirForce(
    country=Countries.us,
    default_flight_prefix='UN_NN',
    value='un',
    verbose_name=_("USN"),
    help_text=_("United States Navy"),
  )
  vvs_rkka = AirForce(
    country=Countries.su,
    default_flight_prefix='r01',
    value='ru',
    verbose_name=_("VVS RKKA"),
    help_text=_("Workers-Peasants Red Army Air Forces"),
  )
  none = AirForce(
    country=None,
    default_flight_prefix=None,
    value='nn',
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

    raise ValueError(
      "Air force with prefix '{0}' is not present in '{1}'"
      .format(prefix, cls.__name__)
    )

  @classmethod
  def filter_by_country(cls, country):
    return filter(lambda x: x.country == country, cls.constants())
