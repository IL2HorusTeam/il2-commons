# -*- coding: utf-8 -*-
import os

from candv import Values, VerboseConstant, VerboseValueConstant

from il2_commons import SupportedLanguages
from il2_commons.utils.translation import ugettext_lazy as _


class Belligerents(Values):
    none = VerboseValueConstant(0, _("neutral"))
    red = VerboseValueConstant(1, _("allies"))
    blue = VerboseValueConstant(2, _("axis"))
    green = VerboseValueConstant(3, _("green"))
    gold = VerboseValueConstant(4, _("gold"))
    purple = VerboseValueConstant(5, _("purple"))
    aqua = VerboseValueConstant(6, _("aqua"))
    maroon = VerboseValueConstant(7, _("maroon"))
    navy = VerboseValueConstant(8, _("navy"))
    emerald = VerboseValueConstant(9, _("emerald"))
    olive = VerboseValueConstant(10, _("olive"))
    magenta = VerboseValueConstant(11, _("magenta"))
    teal = VerboseValueConstant(12, _("teal"))
    orange = VerboseValueConstant(13, _("orange"))
    turquoise = VerboseValueConstant(14, _("turquoise"))
    brown = VerboseValueConstant(15, _("brown"))
    salad = VerboseValueConstant(16, _("salad"))


class Country(VerboseConstant):

    def __init__(self, belligerent, verbose_name=None, help_text=None):
        super(Country, self).__init__(verbose_name=verbose_name,
                                      help_text=help_text)
        self.belligerent = belligerent

    def merge_into_group(self, group):
        super(Country, self).merge_into_group(group)
        group.belligerent = self.belligerent


class Countries(Values):
    constant_class = Country

    au = Country(Belligerents.red, _("Australia"))
    fi = Country(Belligerents.blue, _("Finland"))
    fr = Country(Belligerents.red, _("France"))
    de = Country(Belligerents.blue, _("Germany"))
    hu = Country(Belligerents.blue, _("Hungary"))
    jp = Country(Belligerents.blue, _("Japan"))
    it = Country(Belligerents.blue, _("Italy"))
    nl = Country(Belligerents.red, _("Netherlands"))
    nz = Country(Belligerents.red, _("New Zealand"))
    pl = Country(Belligerents.red, _("Poland"))
    ro = Country(Belligerents.blue, _("Romania"))
    sk = Country(Belligerents.blue, _("Slovakia"))
    su = Country(Belligerents.red, _("Soviet Union"))
    uk = Country(Belligerents.red, _("United Kingdom"))
    us = Country(Belligerents.red, _("United States"))

    @classmethod
    def filter_by_belligerent(cls, belligerent):
        return filter(lambda x: x.belligerent == belligerent, cls.constants())


class AirForce(VerboseValueConstant):

    def __init__(self, country, default_squadron_prefix, value,
                 verbose_name=None, help_text=None):
        super(AirForce, self).__init__(value, verbose_name=verbose_name,
                                              help_text=help_text)
        self.country = country
        self.default_squadron_prefix = default_squadron_prefix

    def merge_into_group(self, group):
        super(AirForce, self).merge_into_group(group)
        group.country = self.country
        group.default_squadron_prefix = self.default_squadron_prefix


class AirForces(Values):
    constant_class = AirForce

    ala = AirForce(
        country=Countries.fr,
        default_squadron_prefix='fr01',
        value='fr',
        verbose_name=_("ALA"),
        help_text=_("Army of the Air"))
    faf = AirForce(
        country=Countries.fi,
        default_squadron_prefix='f01',
        value='fi',
        verbose_name=_("FAF"),
        help_text=_("Finnish Air Force"))
    far = AirForce(
        country=Countries.nl,
        default_squadron_prefix='ro01',
        value='ro',
        verbose_name=_("FAR"),
        help_text=_("Romanian Air Force"))
    haf = AirForce(
        country=Countries.hu,
        default_squadron_prefix='h01',
        value='hu',
        verbose_name=_("HAF"),
        help_text=_("Hungarian Air Force"))
    luftwaffe = AirForce(
        country=Countries.de,
        default_squadron_prefix='g01',
        value='de',
        verbose_name=_("Luftwaffe"))
    ija = AirForce(
        country=Countries.jp,
        default_squadron_prefix='ja01',
        value='ja',
        verbose_name=_("IJA"),
        help_text=_("Imperial Japanese Army"))
    ijn = AirForce(
        country=Countries.jp,
        default_squadron_prefix='IN_NN',
        value='in',
        verbose_name=_("IJN"),
        help_text=_("Imperial Japanese Navy"))
    paf = AirForce(
        country=Countries.pl,
        default_squadron_prefix='pl01',
        value='pl',
        verbose_name=_("PAF"),
        help_text=_("Polish Air Force"))
    rai = AirForce(
        country=Countries.it,
        default_squadron_prefix='i01',
        value='it',
        verbose_name=_("RAI"),
        help_text=_("Regia Aeronautica Italiana"))
    raaf = AirForce(
        country=Countries.au,
        default_squadron_prefix='RA_NN',
        value='ra',
        verbose_name=_("RAAF"),
        help_text=_("Royal Australian Air Force"))
    raf = AirForce(
        country=Countries.uk,
        default_squadron_prefix='gb01',
        value='gb',
        verbose_name=_("RAF"),
        help_text=_("Royal Air Force"))
    rn = AirForce(
        country=Countries.uk,
        default_squadron_prefix='RN_NN',
        value='rn',
        verbose_name=_("RN"),
        help_text=_("Royal Navy"))
    rnlaf = AirForce(
        country=Countries.nl,
        default_squadron_prefix='DU_NN',
        value='du',
        verbose_name=_("RNLAF"),
        help_text=_("Royal Netherlands Air Force"))
    rnzaf = AirForce(
        country=Countries.nz,
        default_squadron_prefix='RZ_NN',
        value='rz',
        verbose_name=_("RNZAF"),
        help_text=_("Royal New Zealand Air Force"))
    saf = AirForce(
        country=Countries.sk,
        default_squadron_prefix='sk01',
        value='sk',
        verbose_name=_("SAF"),
        help_text=_("Slovak Air Force"))
    usaaf = AirForce(
        country=Countries.us,
        default_squadron_prefix='usa01',
        value='us',
        verbose_name=_("USAAF"),
        help_text=_("United States Army Air Forces"))
    usmc = AirForce(
        country=Countries.us,
        default_squadron_prefix='UM_NN',
        value='um',
        verbose_name=_("USMC"),
        help_text=_("United States Marine Corps"))
    usn = AirForce(
        country=Countries.us,
        default_squadron_prefix='UN_NN',
        value='un',
        verbose_name=_("USN"),
        help_text=_("United States Navy"))
    vvs_rkka = AirForce(
        country=Countries.su,
        default_squadron_prefix='r01',
        value='ru',
        verbose_name=_("VVS RKKA"),
        help_text=_("Workers-Peasants Red Army Air Forces"))

    @classmethod
    def get_by_squadron_prefix(cls, prefix):
        for constant in cls.iterconstants():
            if constant.default_squadron_prefix == prefix:
                return constant
        raise ValueError("Airforce with prefix '{0}' is not present in '{1}'"
                         .format(prefix, cls.__name__))

    @classmethod
    def filter_by_country(cls, country):
        return filter(lambda x: x.country == country, cls.constants())

    @classmethod
    def filter_by_belligerent(cls, belligerent):
        return filter(lambda x: x.country.belligerent == belligerent,
                      cls.constants())


def _get_data_file_path(file_name):
    root = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(root, 'data', file_name)


class Regiment(object):

    def __init__(self, airforce, code_name):
        self.airforce = airforce
        self.code_name = code_name

    def __getattr__(self, name):
        if not name.startswith('verbose_name_'):
            return super(Regiment, self).__getattr__(name)

        start = name.rindex('_') + 1
        language_code = name[start:]
        default_language_code = SupportedLanguages.get_default().name

        if not SupportedLanguages.contains(language_code):
            language_code = default_language_code

        value = self._get_verbose_name(language_code)
        if not value and language_code != default_language_code:
            default_name = 'verbose_name_{0}'.format(default_language_code)
            value = getattr(self, default_name)

        setattr(self, name, value)
        return value

    def _get_verbose_name(self, language_code):
        file_name = "regShort_{0}.properties".format(language_code)
        file_path = _get_data_file_path(file_name)

        with open(file_path) as f:
            for line in f:
                if line.startswith(self.code_name):
                    start = len(self.code_name)
                    return line[start:].strip().decode("unicode_escape")
        return ''