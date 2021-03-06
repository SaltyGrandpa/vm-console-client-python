# coding: utf-8

"""
    Python InsightVM API Client

    OpenAPI spec version: 3
    Contact: support@rapid7.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AssetCreatedOrUpdatedReference(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'body': 'ReferenceWithAssetIDLink',
        'status_code': 'str'
    }

    attribute_map = {
        'body': 'body',
        'status_code': 'statusCode'
    }

    def __init__(self, body=None, status_code=None):  # noqa: E501
        """AssetCreatedOrUpdatedReference - a model defined in Swagger"""  # noqa: E501

        self._body = None
        self._status_code = None
        self.discriminator = None

        if body is not None:
            self.body = body
        if status_code is not None:
            self.status_code = status_code

    @property
    def body(self):
        """Gets the body of this AssetCreatedOrUpdatedReference.  # noqa: E501


        :return: The body of this AssetCreatedOrUpdatedReference.  # noqa: E501
        :rtype: ReferenceWithAssetIDLink
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this AssetCreatedOrUpdatedReference.


        :param body: The body of this AssetCreatedOrUpdatedReference.  # noqa: E501
        :type: ReferenceWithAssetIDLink
        """

        self._body = body

    @property
    def status_code(self):
        """Gets the status_code of this AssetCreatedOrUpdatedReference.  # noqa: E501


        :return: The status_code of this AssetCreatedOrUpdatedReference.  # noqa: E501
        :rtype: str
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this AssetCreatedOrUpdatedReference.


        :param status_code: The status_code of this AssetCreatedOrUpdatedReference.  # noqa: E501
        :type: str
        """
        allowed_values = ["100", "101", "102", "103", "200", "201", "202", "203", "204", "205", "206", "207", "208", "226", "300", "301", "302", "303", "304", "305", "307", "308", "400", "401", "402", "403", "404", "405", "406", "407", "408", "409", "410", "411", "412", "413", "414", "415", "416", "417", "418", "419", "420", "421", "422", "423", "424", "426", "428", "429", "431", "500", "501", "502", "503", "504", "505", "506", "507", "508", "509", "510", "511"]  # noqa: E501
        if status_code not in allowed_values:
            raise ValueError(
                "Invalid value for `status_code` ({0}), must be one of {1}"  # noqa: E501
                .format(status_code, allowed_values)
            )

        self._status_code = status_code

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AssetCreatedOrUpdatedReference, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AssetCreatedOrUpdatedReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
