""" Module to wrap factors in class """
import json
import pkgutil


class RefrigerationAndAcEquipmentEmissionFactors:
    """ Wrapper class for heat_content_factors.json """
    def __init__(self):
        self.factors = json.loads(pkgutil.get_data('atom6ghg.factors',
            'source_data/refrigeration_and_ac_equipment_emission_factors.json'))

    def __getitem__(self, item):
        return self.factors.get(item)
