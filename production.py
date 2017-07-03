#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
from trytond.pool import PoolMeta, Pool
from trytond.model import fields
from trytond.pyson import Eval
import subprocess
import shutil
import os
import tempfile

__all__ = ['Production']


class Production:
    "Production"
    __name__ = 'production'
    __metaclass__ = PoolMeta

    prototype = fields.Function(fields.Binary('Prototype'), 'get_prototype')

    sequence = fields.Integer('Sequence')

    @classmethod
    def __setup__(cls):
        super(Production, cls).__setup__()
        cls._order = [('sequence', 'ASC')]

    @staticmethod
    def order_sequence(tables):
        table, _ = tables[None]
        return [table.sequence == None, table.sequence]

    def get_prototype(self, name=None):
        '''
        We should really not be writting the files on the disk.
        '''
        pool = Pool()
        Sale = pool.get('sale.sale')

        if self.origin and not isinstance(self.origin, Sale):
            return
        mockup = self.sale.mockups[0].mock_up

        path_name = tempfile.mkdtemp()
        path = self.to_jpg(mockup, path_name)
        with open(path, 'rb') as f:
            buffer_data = f.read()
            shutil.rmtree(path_name)

        return self.__class__.prototype.cast(buffer_data)  # py3 compatibility

    @staticmethod
    def to_jpg(pdf_binary, path_name):
        pdf_data = pdf_binary.data
        if not pdf_data:
            return None
        new_file, _input = tempfile.mkstemp()
        os.write(new_file, pdf_data)

        _output = path_name + '/' + str(pdf_binary.id) + '.jpg'

        subprocess.call(
            ["convert", '-quality', '90', '-density', '200x200',
            '-background', 'white', '-alpha', 'remove',
                _input + '[0]', _output])
        os.close(new_file)
        return _output
