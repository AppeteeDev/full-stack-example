# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from SPOTAPI.models.base_model_ import Model
from SPOTAPI.models.company import Company
from SPOTAPI.models.person import Person
from SPOTAPI import util

from SPOTAPI.models.company import Company  # noqa: E501
from SPOTAPI.models.person import Person  # noqa: E501

class Protagonist(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, type=None, name=None, link=None, photo=None, date_update=None, person=None, company=None):  # noqa: E501
        """Protagonist - a model defined in OpenAPI

        :param id: The id of this Protagonist.  # noqa: E501
        :type id: int
        :param type: The type of this Protagonist.  # noqa: E501
        :type type: str
        :param name: The name of this Protagonist.  # noqa: E501
        :type name: str
        :param link: The link of this Protagonist.  # noqa: E501
        :type link: str
        :param photo: The photo of this Protagonist.  # noqa: E501
        :type photo: str
        :param date_update: The date_update of this Protagonist.  # noqa: E501
        :type date_update: str
        :param person: The person of this Protagonist.  # noqa: E501
        :type person: Person
        :param company: The company of this Protagonist.  # noqa: E501
        :type company: Company
        """
        self.openapi_types = {
            'id': int,
            'type': str,
            'name': str,
            'link': str,
            'photo': str,
            'date_update': str,
            'person': Person,
            'company': Company
        }

        self.attribute_map = {
            'id': 'id',
            'type': 'type',
            'name': 'name',
            'link': 'link',
            'photo': 'photo',
            'date_update': 'dateUpdate',
            'person': 'person',
            'company': 'company'
        }

        self._id = id
        self._type = type
        self._name = name
        self._link = link
        self._photo = photo
        self._date_update = date_update
        self._person = person
        self._company = company

    @classmethod
    def from_dict(cls, dikt) -> 'Protagonist':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The protagonist of this Protagonist.  # noqa: E501
        :rtype: Protagonist
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Protagonist.


        :return: The id of this Protagonist.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Protagonist.


        :param id: The id of this Protagonist.
        :type id: int
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this Protagonist.


        :return: The type of this Protagonist.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Protagonist.


        :param type: The type of this Protagonist.
        :type type: str
        """
        allowed_values = ["person", "company"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def name(self):
        """Gets the name of this Protagonist.


        :return: The name of this Protagonist.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Protagonist.


        :param name: The name of this Protagonist.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def link(self):
        """Gets the link of this Protagonist.


        :return: The link of this Protagonist.
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this Protagonist.


        :param link: The link of this Protagonist.
        :type link: str
        """

        self._link = link

    @property
    def photo(self):
        """Gets the photo of this Protagonist.


        :return: The photo of this Protagonist.
        :rtype: str
        """
        return self._photo

    @photo.setter
    def photo(self, photo):
        """Sets the photo of this Protagonist.


        :param photo: The photo of this Protagonist.
        :type photo: str
        """

        self._photo = photo

    @property
    def date_update(self):
        """Gets the date_update of this Protagonist.


        :return: The date_update of this Protagonist.
        :rtype: str
        """
        return self._date_update

    @date_update.setter
    def date_update(self, date_update):
        """Sets the date_update of this Protagonist.


        :param date_update: The date_update of this Protagonist.
        :type date_update: str
        """

        self._date_update = date_update

    @property
    def person(self):
        """Gets the person of this Protagonist.


        :return: The person of this Protagonist.
        :rtype: Person
        """
        return self._person

    @person.setter
    def person(self, person):
        """Sets the person of this Protagonist.


        :param person: The person of this Protagonist.
        :type person: Person
        """

        self._person = person

    @property
    def company(self):
        """Gets the company of this Protagonist.


        :return: The company of this Protagonist.
        :rtype: Company
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this Protagonist.


        :param company: The company of this Protagonist.
        :type company: Company
        """

        self._company = company
