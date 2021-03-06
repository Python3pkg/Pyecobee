"""
This module is home to the HierarchyPrivilege class
"""
from .ecobee_object import EcobeeObject


class HierarchyPrivilege(EcobeeObject):
    """
    This class has been auto generated by scraping
    https://www.ecobee.com/home/developer/api/documentation/v1/objects/HierarchyPrivilege.shtml

    Attribute names have been generated by converting ecobee property names from camelCase to snake_case.

    A getter property has been generated for each attribute.
    A setter property has been generated for each attribute whose value of READONLY is "no".

    An __init__ argument without a default value has been generated if the value of REQUIRED is "yes".
    An __init__ argument with a default value of None has been generated if the value of REQUIRED is "no".
   """
    __slots__ = ['_set_path', '_user_name', '_set_name', '_allow_all', '_allow_none', '_allow_view', '_allow_program',
                 '_allow_vacation', '_allow_settings', '_allow_details', '_allow_report', '_allow_security',
                 '_allow_hierarchy', '_allow_alerts', '_allow_manage_account']

    attribute_name_map = {'set_path': 'setPath', 'setPath': 'set_path', 'user_name': 'userName',
                          'userName': 'user_name', 'set_name': 'setName', 'setName': 'set_name',
                          'allow_all': 'allowAll', 'allowAll': 'allow_all', 'allow_none': 'allowNone',
                          'allowNone': 'allow_none', 'allow_view': 'allowView', 'allowView': 'allow_view',
                          'allow_program': 'allowProgram', 'allowProgram': 'allow_program',
                          'allow_vacation': 'allowVacation', 'allowVacation': 'allow_vacation',
                          'allow_settings': 'allowSettings', 'allowSettings': 'allow_settings',
                          'allow_details': 'allowDetails', 'allowDetails': 'allow_details',
                          'allow_report': 'allowReport', 'allowReport': 'allow_report',
                          'allow_security': 'allowSecurity', 'allowSecurity': 'allow_security',
                          'allow_hierarchy': 'allowHierarchy', 'allowHierarchy': 'allow_hierarchy',
                          'allow_alerts': 'allowAlerts', 'allowAlerts': 'allow_alerts',
                          'allow_manage_account': 'allowManageAccount', 'allowManageAccount': 'allow_manage_account'}

    attribute_type_map = {'set_path': 'six.text_type', 'user_name': 'six.text_type', 'set_name': 'six.text_type',
                          'allow_all': 'bool', 'allow_none': 'bool', 'allow_view': 'bool', 'allow_program': 'bool',
                          'allow_vacation': 'bool', 'allow_settings': 'bool', 'allow_details': 'bool',
                          'allow_report': 'bool', 'allow_security': 'bool', 'allow_hierarchy': 'bool',
                          'allow_alerts': 'bool', 'allow_manage_account': 'bool'}

    def __init__(self, set_path, user_name, set_name=None, allow_all=None, allow_none=None, allow_view=None,
                 allow_program=None, allow_vacation=None, allow_settings=None, allow_details=None, allow_report=None,
                 allow_security=None, allow_hierarchy=None, allow_alerts=None, allow_manage_account=None):
        """
        Construct a HierarchyPrivilege instance
        """
        self._set_path = set_path
        self._user_name = user_name
        self._set_name = set_name
        self._allow_all = allow_all
        self._allow_none = allow_none
        self._allow_view = allow_view
        self._allow_program = allow_program
        self._allow_vacation = allow_vacation
        self._allow_settings = allow_settings
        self._allow_details = allow_details
        self._allow_report = allow_report
        self._allow_security = allow_security
        self._allow_hierarchy = allow_hierarchy
        self._allow_alerts = allow_alerts
        self._allow_manage_account = allow_manage_account

    @property
    def set_path(self):
        """
        Gets the set_path attribute of this HierarchyPrivilege instance.

        :return: The value of the set_path attribute of this HierarchyPrivilege instance.
        :rtype: six.text_type

        Sets the set_path attribute of this HierarchyPrivilege instance.

        :param set_path: The set_path value to set for the set_path attribute of this HierarchyPrivilege instance.
        :type: six.text_type
        """

        return self._set_path

    @set_path.setter
    def set_path(self, set_path):
        self._set_path = set_path

    @property
    def user_name(self):
        """
        Gets the user_name attribute of this HierarchyPrivilege instance.

        :return: The value of the user_name attribute of this HierarchyPrivilege instance.
        :rtype: six.text_type

        Sets the user_name attribute of this HierarchyPrivilege instance.

        :param user_name: The user_name value to set for the user_name attribute of this HierarchyPrivilege instance.
        :type: six.text_type
        """

        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        self._user_name = user_name

    @property
    def set_name(self):
        """
        Gets the set_name attribute of this HierarchyPrivilege instance.

        :return: The value of the set_name attribute of this HierarchyPrivilege instance.
        :rtype: six.text_type
        """

        return self._set_name

    @property
    def allow_all(self):
        """
        Gets the allow_all attribute of this HierarchyPrivilege instance.

        :return: The value of the allow_all attribute of this HierarchyPrivilege instance.
        :rtype: bool

        Sets the allow_all attribute of this HierarchyPrivilege instance.

        :param allow_all: The allow_all value to set for the allow_all attribute of this HierarchyPrivilege instance.
        :type: bool
        """

        return self._allow_all

    @allow_all.setter
    def allow_all(self, allow_all):
        self._allow_all = allow_all

    @property
    def allow_none(self):
        """
        Gets the allow_none attribute of this HierarchyPrivilege instance.

        :return: The value of the allow_none attribute of this HierarchyPrivilege instance.
        :rtype: bool

        Sets the allow_none attribute of this HierarchyPrivilege instance.

        :param allow_none: The allow_none value to set for the allow_none attribute of this HierarchyPrivilege instance.
        :type: bool
        """

        return self._allow_none

    @allow_none.setter
    def allow_none(self, allow_none):
        self._allow_none = allow_none

    @property
    def allow_view(self):
        """
        Gets the allow_view attribute of this HierarchyPrivilege instance.

        :return: The value of the allow_view attribute of this HierarchyPrivilege instance.
        :rtype: bool

        Sets the allow_view attribute of this HierarchyPrivilege instance.

        :param allow_view: The allow_view value to set for the allow_view attribute of this HierarchyPrivilege instance.
        :type: bool
        """

        return self._allow_view

    @allow_view.setter
    def allow_view(self, allow_view):
        self._allow_view = allow_view

    @property
    def allow_program(self):
        """
        Gets the allow_program attribute of this HierarchyPrivilege instance.

        :return: The value of the allow_program attribute of this HierarchyPrivilege instance.
        :rtype: bool

        Sets the allow_program attribute of this HierarchyPrivilege instance.

        :param allow_program: The allow_program value to set for the allow_program attribute of this HierarchyPrivilege instance.
        :type: bool
        """

        return self._allow_program

    @allow_program.setter
    def allow_program(self, allow_program):
        self._allow_program = allow_program

    @property
    def allow_vacation(self):
        """
        Gets the allow_vacation attribute of this HierarchyPrivilege instance.

        :return: The value of the allow_vacation attribute of this HierarchyPrivilege instance.
        :rtype: bool

        Sets the allow_vacation attribute of this HierarchyPrivilege instance.

        :param allow_vacation: The allow_vacation value to set for the allow_vacation attribute of this HierarchyPrivilege instance.
        :type: bool
        """

        return self._allow_vacation

    @allow_vacation.setter
    def allow_vacation(self, allow_vacation):
        self._allow_vacation = allow_vacation

    @property
    def allow_settings(self):
        """
        Gets the allow_settings attribute of this HierarchyPrivilege instance.

        :return: The value of the allow_settings attribute of this HierarchyPrivilege instance.
        :rtype: bool

        Sets the allow_settings attribute of this HierarchyPrivilege instance.

        :param allow_settings: The allow_settings value to set for the allow_settings attribute of this HierarchyPrivilege instance.
        :type: bool
        """

        return self._allow_settings

    @allow_settings.setter
    def allow_settings(self, allow_settings):
        self._allow_settings = allow_settings

    @property
    def allow_details(self):
        """
        Gets the allow_details attribute of this HierarchyPrivilege instance.

        :return: The value of the allow_details attribute of this HierarchyPrivilege instance.
        :rtype: bool

        Sets the allow_details attribute of this HierarchyPrivilege instance.

        :param allow_details: The allow_details value to set for the allow_details attribute of this HierarchyPrivilege instance.
        :type: bool
        """

        return self._allow_details

    @allow_details.setter
    def allow_details(self, allow_details):
        self._allow_details = allow_details

    @property
    def allow_report(self):
        """
        Gets the allow_report attribute of this HierarchyPrivilege instance.

        :return: The value of the allow_report attribute of this HierarchyPrivilege instance.
        :rtype: bool

        Sets the allow_report attribute of this HierarchyPrivilege instance.

        :param allow_report: The allow_report value to set for the allow_report attribute of this HierarchyPrivilege instance.
        :type: bool
        """

        return self._allow_report

    @allow_report.setter
    def allow_report(self, allow_report):
        self._allow_report = allow_report

    @property
    def allow_security(self):
        """
        Gets the allow_security attribute of this HierarchyPrivilege instance.

        :return: The value of the allow_security attribute of this HierarchyPrivilege instance.
        :rtype: bool

        Sets the allow_security attribute of this HierarchyPrivilege instance.

        :param allow_security: The allow_security value to set for the allow_security attribute of this HierarchyPrivilege instance.
        :type: bool
        """

        return self._allow_security

    @allow_security.setter
    def allow_security(self, allow_security):
        self._allow_security = allow_security

    @property
    def allow_hierarchy(self):
        """
        Gets the allow_hierarchy attribute of this HierarchyPrivilege instance.

        :return: The value of the allow_hierarchy attribute of this HierarchyPrivilege instance.
        :rtype: bool

        Sets the allow_hierarchy attribute of this HierarchyPrivilege instance.

        :param allow_hierarchy: The allow_hierarchy value to set for the allow_hierarchy attribute of this HierarchyPrivilege instance.
        :type: bool
        """

        return self._allow_hierarchy

    @allow_hierarchy.setter
    def allow_hierarchy(self, allow_hierarchy):
        self._allow_hierarchy = allow_hierarchy

    @property
    def allow_alerts(self):
        """
        Gets the allow_alerts attribute of this HierarchyPrivilege instance.

        :return: The value of the allow_alerts attribute of this HierarchyPrivilege instance.
        :rtype: bool

        Sets the allow_alerts attribute of this HierarchyPrivilege instance.

        :param allow_alerts: The allow_alerts value to set for the allow_alerts attribute of this HierarchyPrivilege instance.
        :type: bool
        """

        return self._allow_alerts

    @allow_alerts.setter
    def allow_alerts(self, allow_alerts):
        self._allow_alerts = allow_alerts

    @property
    def allow_manage_account(self):
        """
        Gets the allow_manage_account attribute of this HierarchyPrivilege instance.

        :return: The value of the allow_manage_account attribute of this HierarchyPrivilege instance.
        :rtype: bool

        Sets the allow_manage_account attribute of this HierarchyPrivilege instance.

        :param allow_manage_account: The allow_manage_account value to set for the allow_manage_account attribute of this HierarchyPrivilege instance.
        :type: bool
        """

        return self._allow_manage_account

    @allow_manage_account.setter
    def allow_manage_account(self, allow_manage_account):
        self._allow_manage_account = allow_manage_account
