# coding: utf-8

from candv import Values, VerboseValueConstant, with_constant_class

from .utils import translations


_ = translations.ugettext_lazy


class TargetType(VerboseValueConstant):
    pass


class TargetTypes(with_constant_class(TargetType), Values):
    destroy = VerboseValueConstant(0, _("destroy"))
    destroy_area = VerboseValueConstant(1, _("destroy area"))
    destroy_bridge = VerboseValueConstant(2, _("destroy bridge"))
    recon = VerboseValueConstant(3, _("recon"))
    escort = VerboseValueConstant(4, _("escort"))
    cover = VerboseValueConstant(5, _("cover"))
    cover_area = VerboseValueConstant(6, _("cover area"))
    cover_bridge = VerboseValueConstant(7, _("cover bridge"))


class TargetPriority(VerboseValueConstant):
    pass


class TargetPriorities(with_constant_class(TargetPriority), Values):
    primary = TargetPriority(0, _("primary"))
    secondary = TargetPriority(1, _("secondary"))
    hidden = TargetPriority(2, _("hidden"))
