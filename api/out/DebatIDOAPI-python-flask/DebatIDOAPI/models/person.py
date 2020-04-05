# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from DebatIDOAPI.models.base_model_ import Model
from DebatIDOAPI import util


class Person(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, protagonist_id=None, surname=None, role=None, date_update=None):  # noqa: E501
        """Person - a model defined in OpenAPI

        :param id: The id of this Person.  # noqa: E501
        :type id: int
        :param protagonist_id: The protagonist_id of this Person.  # noqa: E501
        :type protagonist_id: int
        :param surname: The surname of this Person.  # noqa: E501
        :type surname: str
        :param role: The role of this Person.  # noqa: E501
        :type role: str
        :param date_update: The date_update of this Person.  # noqa: E501
        :type date_update: str
        """
        self.openapi_types = {
            'id': int,
            'protagonist_id': int,
            'surname': str,
            'role': str,
            'date_update': str
        }

        self.attribute_map = {
            'id': 'id',
            'protagonist_id': 'protagonistID',
            'surname': 'surname',
            'role': 'role',
            'date_update': 'dateUpdate'
        }

        self._id = id
        self._protagonist_id = protagonist_id
        self._surname = surname
        self._role = role
        self._date_update = date_update

    @classmethod
    def from_dict(cls, dikt) -> 'Person':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The person of this Person.  # noqa: E501
        :rtype: Person
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Person.


        :return: The id of this Person.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Person.


        :param id: The id of this Person.
        :type id: int
        """

        self._id = id

    @property
    def protagonist_id(self):
        """Gets the protagonist_id of this Person.


        :return: The protagonist_id of this Person.
        :rtype: int
        """
        return self._protagonist_id

    @protagonist_id.setter
    def protagonist_id(self, protagonist_id):
        """Sets the protagonist_id of this Person.


        :param protagonist_id: The protagonist_id of this Person.
        :type protagonist_id: int
        """

        self._protagonist_id = protagonist_id

    @property
    def surname(self):
        """Gets the surname of this Person.


        :return: The surname of this Person.
        :rtype: str
        """
        return self._surname

    @surname.setter
    def surname(self, surname):
        """Sets the surname of this Person.


        :param surname: The surname of this Person.
        :type surname: str
        """

        self._surname = surname

    @property
    def role(self):
        """Gets the role of this Person.


        :return: The role of this Person.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this Person.


        :param role: The role of this Person.
        :type role: str
        """

        self._role = role

    @property
    def date_update(self):
        """Gets the date_update of this Person.


        :return: The date_update of this Person.
        :rtype: str
        """
        return self._date_update

    @date_update.setter
    def date_update(self, date_update):
        """Sets the date_update of this Person.


        :param date_update: The date_update of this Person.
        :type date_update: str
        """

        self._date_update = date_update