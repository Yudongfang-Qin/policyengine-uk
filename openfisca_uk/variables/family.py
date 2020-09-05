from openfisca_core.model_api import *
from openfisca_uk.entities import *
import numpy as np

# Derived variables

## Family

class younger_adult_age(Variable):
    value_type = int
    entity = Family
    label = u'Minimum age of an adult in the family'
    definition_period = ETERNITY

    def formula(family, period, parameters):
        return family.min(max_(family.members('age', period), 16))

class older_adult_age(Variable):
    value_type = int
    entity = Family
    label = u'Maximum age of an adult in the family'
    definition_period = ETERNITY

    def formula(family, period, parameters):
        return family.max(max_(family.members('age', period), 16))

class family_earnings(Variable):
    value_type = float
    entity = Family
    label = u'Amount of earnings per week across the family'
    definition_period = ETERNITY

    def formula(family, period, parameters):
        return family.sum(family.members('total_earnings', period))

class family_pension_income(Variable):
    value_type = float
    entity = Family
    label = u'Amount of pension income per week across the family'
    definition_period = ETERNITY

    def formula(family, period, parameters):
        return family.sum(family.members('pension_income', period))

class family_total_income(Variable):
    value_type = float
    entity = Family
    label = u'Amount of total income per week across the family'
    definition_period = ETERNITY

    def formula(family, period, parameters):
        return family('family_earnings', period) + family('family_pension_income', period)

class family_JSA_receipt(Variable):
    value_type = bool
    entity = Family
    label = u'Whether the family receives JSA'
    definition_period = ETERNITY

    def formula(family, period, parameters):
        return family.any(family.members('JSA_receipt', period))

class family_IS_receipt(Variable):
    value_type = bool
    entity = Family
    label = u'Whether the family receives Income Support'
    definition_period = ETERNITY

    def formula(family, period, parameters):
        return family.any(family.members('IS_receipt', period))

class is_lone_parent(Variable):
    value_type = bool
    entity = Family
    label = u'Whether the family structure is a lone parent'
    definition_period = ETERNITY

    def formula(family, period, parameters):
        return (family.nb_persons(Family.ADULT) == 1) * (family.nb_persons(Family.CHILD) > 0)

class is_couple(Variable):
    value_type = bool
    entity = Family
    label = u'Whether the family structure is a lone parent'
    definition_period = ETERNITY

    def formula(family, period, parameters):
        return (family.nb_persons(Family.ADULT) == 2)

class is_single(Variable):
    value_type = bool
    entity = Family
    label = u'Whether the family structure is a lone parent'
    definition_period = ETERNITY

    def formula(family, period, parameters):
        return (family.nb_persons(Family.ADULT) == 1) * (family.nb_persons(Family.CHILD) == 0)