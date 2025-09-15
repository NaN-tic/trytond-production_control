#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.model import fields


class Production(metaclass=PoolMeta):
    __name__ = 'production'
    sequence = fields.Integer('Sequence')

    @classmethod
    def __setup__(cls):
        super(Production, cls).__setup__()
        cls._order = [
            ('sequence', 'ASC'),
            ('id', 'DESC'),
            ]

    @staticmethod
    def order_sequence(tables):
        table, _ = tables[None]
        return [table.sequence == None, table.sequence]
