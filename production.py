#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.model import fields

__all__ = ['Production']


class Production:
    __metaclass__ = PoolMeta
    __name__ = 'production'
    sequence = fields.Integer('Sequence')

    @classmethod
    def __setup__(cls):
        super(Production, cls).__setup__()
        cls._order = [('sequence', 'ASC')]

    @staticmethod
    def order_sequence(tables):
        table, _ = tables[None]
        return [table.sequence == None, table.sequence]
