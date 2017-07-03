#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
from trytond.pool import PoolMeta, Pool
from trytond.model import fields
from trytond.pyson import Eval

__all__ = ['Production']


class Production:
    "Production"
    __name__ = 'production'
    __metaclass__ = PoolMeta

    sequence = fields.Integer('Sequence')

    @classmethod
    def __setup__(cls):
        super(Production, cls).__setup__()
        cls._order = [('sequence', 'ASC')]

    @staticmethod
    def order_sequence(tables):
        table, _ = tables[None]
        return [table.sequence == None, table.sequence]
