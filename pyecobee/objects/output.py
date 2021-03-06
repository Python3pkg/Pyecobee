"""
This module is home to the Output class
"""
from .ecobee_object import EcobeeObject


class Output(EcobeeObject):
    """
    This class has been auto generated by scraping
    https://www.ecobee.com/home/developer/api/documentation/v1/objects/Output.shtml

    Attribute names have been generated by converting ecobee property names from camelCase to snake_case.

    A getter property has been generated for each attribute.
    A setter property has been generated for each attribute whose value of READONLY is "no".

    An __init__ argument without a default value has been generated if the value of REQUIRED is "yes".
    An __init__ argument with a default value of None has been generated if the value of REQUIRED is "no".
   """
    __slots__ = ['_name', '_zone', '_output_id', '_type', '_send_update', '_active_closed', '_activation_time',
                 '_deactivation_time']

    attribute_name_map = {'name': 'name', 'zone': 'zone', 'output_id': 'outputId', 'outputId': 'output_id',
                          'type': 'type', 'send_update': 'sendUpdate', 'sendUpdate': 'send_update',
                          'active_closed': 'activeClosed', 'activeClosed': 'active_closed',
                          'activation_time': 'activationTime', 'activationTime': 'activation_time',
                          'deactivation_time': 'deactivationTime', 'deactivationTime': 'deactivation_time'}

    attribute_type_map = {'name': 'six.text_type', 'zone': 'int', 'output_id': 'int', 'type': 'six.text_type',
                          'send_update': 'bool', 'active_closed': 'bool', 'activation_time': 'int',
                          'deactivation_time': 'int'}

    def __init__(self, name=None, zone=None, output_id=None, type=None, send_update=None, active_closed=None,
                 activation_time=None, deactivation_time=None):
        """
        Construct an Output instance
        """
        self._name = name
        self._zone = zone
        self._output_id = output_id
        self._type = type
        self._send_update = send_update
        self._active_closed = active_closed
        self._activation_time = activation_time
        self._deactivation_time = deactivation_time

    @property
    def name(self):
        """
        Gets the name attribute of this Output instance.

        :return: The value of the name attribute of this Output instance.
        :rtype: six.text_type
        """

        return self._name

    @property
    def zone(self):
        """
        Gets the zone attribute of this Output instance.

        :return: The value of the zone attribute of this Output instance.
        :rtype: int
        """

        return self._zone

    @property
    def output_id(self):
        """
        Gets the output_id attribute of this Output instance.

        :return: The value of the output_id attribute of this Output instance.
        :rtype: int
        """

        return self._output_id

    @property
    def type(self):
        """
        Gets the type attribute of this Output instance.

        :return: The value of the type attribute of this Output instance.
        :rtype: six.text_type
        """

        return self._type

    @property
    def send_update(self):
        """
        Gets the send_update attribute of this Output instance.

        :return: The value of the send_update attribute of this Output instance.
        :rtype: bool
        """

        return self._send_update

    @property
    def active_closed(self):
        """
        Gets the active_closed attribute of this Output instance.

        :return: The value of the active_closed attribute of this Output instance.
        :rtype: bool
        """

        return self._active_closed

    @property
    def activation_time(self):
        """
        Gets the activation_time attribute of this Output instance.

        :return: The value of the activation_time attribute of this Output instance.
        :rtype: int
        """

        return self._activation_time

    @property
    def deactivation_time(self):
        """
        Gets the deactivation_time attribute of this Output instance.

        :return: The value of the deactivation_time attribute of this Output instance.
        :rtype: int
        """

        return self._deactivation_time
