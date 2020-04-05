# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from DebatIDOAPI.models.base_model_ import Model
from DebatIDOAPI.models.protagonist import Protagonist
from DebatIDOAPI.models.quote import Quote
from DebatIDOAPI import util

from DebatIDOAPI.models.protagonist import Protagonist  # noqa: E501
from DebatIDOAPI.models.quote import Quote  # noqa: E501

class QuoteAuthor(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, quote_id=None, quote=None, author_id=None, author=None):  # noqa: E501
        """QuoteAuthor - a model defined in OpenAPI

        :param quote_id: The quote_id of this QuoteAuthor.  # noqa: E501
        :type quote_id: int
        :param quote: The quote of this QuoteAuthor.  # noqa: E501
        :type quote: Quote
        :param author_id: The author_id of this QuoteAuthor.  # noqa: E501
        :type author_id: int
        :param author: The author of this QuoteAuthor.  # noqa: E501
        :type author: Protagonist
        """
        self.openapi_types = {
            'quote_id': int,
            'quote': Quote,
            'author_id': int,
            'author': Protagonist
        }

        self.attribute_map = {
            'quote_id': 'quoteID',
            'quote': 'quote',
            'author_id': 'authorID',
            'author': 'author'
        }

        self._quote_id = quote_id
        self._quote = quote
        self._author_id = author_id
        self._author = author

    @classmethod
    def from_dict(cls, dikt) -> 'QuoteAuthor':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The quoteAuthor of this QuoteAuthor.  # noqa: E501
        :rtype: QuoteAuthor
        """
        return util.deserialize_model(dikt, cls)

    @property
    def quote_id(self):
        """Gets the quote_id of this QuoteAuthor.


        :return: The quote_id of this QuoteAuthor.
        :rtype: int
        """
        return self._quote_id

    @quote_id.setter
    def quote_id(self, quote_id):
        """Sets the quote_id of this QuoteAuthor.


        :param quote_id: The quote_id of this QuoteAuthor.
        :type quote_id: int
        """

        self._quote_id = quote_id

    @property
    def quote(self):
        """Gets the quote of this QuoteAuthor.


        :return: The quote of this QuoteAuthor.
        :rtype: Quote
        """
        return self._quote

    @quote.setter
    def quote(self, quote):
        """Sets the quote of this QuoteAuthor.


        :param quote: The quote of this QuoteAuthor.
        :type quote: Quote
        """

        self._quote = quote

    @property
    def author_id(self):
        """Gets the author_id of this QuoteAuthor.


        :return: The author_id of this QuoteAuthor.
        :rtype: int
        """
        return self._author_id

    @author_id.setter
    def author_id(self, author_id):
        """Sets the author_id of this QuoteAuthor.


        :param author_id: The author_id of this QuoteAuthor.
        :type author_id: int
        """

        self._author_id = author_id

    @property
    def author(self):
        """Gets the author of this QuoteAuthor.


        :return: The author of this QuoteAuthor.
        :rtype: Protagonist
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this QuoteAuthor.


        :param author: The author of this QuoteAuthor.
        :type author: Protagonist
        """

        self._author = author
