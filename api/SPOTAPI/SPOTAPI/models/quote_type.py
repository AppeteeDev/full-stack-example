# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from SPOTAPI.models.base_model_ import Model
from SPOTAPI import util


class QuoteType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, title=None):  # noqa: E501
        """QuoteType - a model defined in OpenAPI

        :param id: The id of this QuoteType.  # noqa: E501
        :type id: int
        :param title: The title of this QuoteType.  # noqa: E501
        :type title: str
        """
        self.openapi_types = {
            'id': int,
            'title': str
        }

        self.attribute_map = {
            'id': 'id',
            'title': 'title'
        }

        self._id = id
        self._title = title

    @classmethod
    def from_dict(cls, dikt) -> 'QuoteType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The quoteType of this QuoteType.  # noqa: E501
        :rtype: QuoteType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this QuoteType.


        :return: The id of this QuoteType.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QuoteType.


        :param id: The id of this QuoteType.
        :type id: int
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this QuoteType.


        :return: The title of this QuoteType.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this QuoteType.


        :param title: The title of this QuoteType.
        :type title: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title
