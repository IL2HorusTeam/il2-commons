# -*- coding: utf-8 -*-
from candv import Values, VerboseConstant, VerboseValueConstant

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
        super(VerboseValueConstant, self).__init__(verbose_name=verbose_name,
                                                   help_text=help_text)
        self.belligerent = belligerent

    def merge_into_group(self, group):
        super(Country, self).merge_into_group(group)
        group.belligerent = self.belligerent


class Countries(Values):
    au = Country(Belligerents.red, _("Australia"))
    fi = Country(Belligerents.blue, _("Finland"))
    fr = Country(Belligerents.red, _("France"))
    de = Country(Belligerents.blue, _("Germany"))
    hu = Country(Belligerents.blue, _("Hungary"))
    jp = Country(Belligerents.blue, _("Japan"))
    nl = Country(Belligerents.red, _("Netherlands"))
    nz = Country(Belligerents.red, _("New Zealand"))
    pl = Country(Belligerents.red, _("Poland"))
    ro = Country(Belligerents.blue, _("Romania"))
    sk = Country(Belligerents.blue, _("Slovakia"))
    su = Country(Belligerents.red, _("Soviet Union"))
    uk = Country(Belligerents.red, _("United Kingdom"))


class AirForce(VerboseValueConstant):

    def __init__(self, country, default_squadron_prefix, value,
                 verbose_name=None, help_text=None):
        super(VerboseValueConstant, self).__init__(value,
                                                   verbose_name=verbose_name,
                                                   help_text=help_text)
        self.country = country
        self.default_squadron_prefix = default_squadron_prefix

    def merge_into_group(self, group):
        super(AirForce, self).merge_into_group(group)
        group.country = self.country
        group.default_squadron_prefix = self.default_squadron_prefix


class AirForces(Values):
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
