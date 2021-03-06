"""
This module is home to the Program class
"""
from .ecobee_object import EcobeeObject


class Program(EcobeeObject):
    """
    This class has been auto generated by scraping
    https://www.ecobee.com/home/developer/api/documentation/v1/objects/Program.shtml

    Attribute names have been generated by converting ecobee property names from camelCase to snake_case.

    A getter property has been generated for each attribute.
    A setter property has been generated for each attribute whose value of READONLY is "no".

    An __init__ argument without a default value has been generated if the value of REQUIRED is "yes".
    An __init__ argument with a default value of None has been generated if the value of REQUIRED is "no".
   """
    __slots__ = ['_schedule', '_climates', '_current_climate_ref']

    attribute_name_map = {'schedule': 'schedule', 'climates': 'climates', 'current_climate_ref': 'currentClimateRef',
                          'currentClimateRef': 'current_climate_ref'}

    attribute_type_map = {'schedule': 'List[six.text_type]', 'climates': 'List[Climate]',
                          'current_climate_ref': 'six.text_type'}

    def __init__(self, schedule, climates, current_climate_ref=None):
        """
        Construct a Program instance
        """
        self._schedule = schedule
        self._climates = climates
        self._current_climate_ref = current_climate_ref

    @property
    def schedule(self):
        """
        Gets the schedule attribute of this Program instance.

        :return: The value of the schedule attribute of this Program instance.
        :rtype: List[six.text_type]

        Sets the schedule attribute of this Program instance.

        :param schedule: The schedule value to set for the schedule attribute of this Program instance.
        :type: List[six.text_type]
        """

        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        self._schedule = schedule

    @property
    def climates(self):
        """
        Gets the climates attribute of this Program instance.

        :return: The value of the climates attribute of this Program instance.
        :rtype: List[Climate]

        Sets the climates attribute of this Program instance.

        :param climates: The climates value to set for the climates attribute of this Program instance.
        :type: List[Climate]
        """

        return self._climates

    @climates.setter
    def climates(self, climates):
        self._climates = climates

    @property
    def current_climate_ref(self):
        """
        Gets the current_climate_ref attribute of this Program instance.

        :return: The value of the current_climate_ref attribute of this Program instance.
        :rtype: six.text_type
        """

        return self._current_climate_ref
