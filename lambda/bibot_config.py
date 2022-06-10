#
# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the "Software"), to deal in the Software
# without restriction, including without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

ORIGINAL_VALUE = 0
TOP_RESOLUTION = 1

SLOT_CONFIG = {
    'count':            {'type': ORIGINAL_VALUE, 'remember': True},
    'dimension':        {'type': ORIGINAL_VALUE, 'remember': True},
    'wave':             {'type': TOP_RESOLUTION, 'remember': True,  'error': 'I couldn\'t find a category called "{}".'},
    'marca':            {'type': TOP_RESOLUTION, 'remember': True,  'error': 'I couldn\'t find a category called "{}".'},
    'atributo':         {'type': TOP_RESOLUTION, 'remember': True,  'error': 'I couldn\'t find a category called "{}".'},
    'one_wave':         {'type': TOP_RESOLUTION, 'remember': False,  'error': 'I couldn\'t find a category called "{}".'},
    'another_wave':     {'type': TOP_RESOLUTION, 'remember': False,  'error': 'I couldn\'t find a category called "{}".'},
    'one_marca':        {'type': TOP_RESOLUTION, 'remember': False, 'error': 'I couldn\'t find an marca called "{}".'},
    'another_marca':    {'type': TOP_RESOLUTION, 'remember': False, 'error': 'I couldn\'t find an marca called "{}".'},
    'one_atributo':     {'type': TOP_RESOLUTION, 'remember': False,  'error': 'I couldn\'t find a category called "{}".'},
    'another_atributo': {'type': TOP_RESOLUTION, 'remember': False,  'error': 'I couldn\'t find a category called "{}".'},
}

DIMENSIONS = {
    'waves':      {'slot': 'wave',  'column': 'w.wave',  'singular': 'wave'},
    'marcas':     {'slot': 'marca',  'column': 'm.marca',  'singular': 'marca'},
    'atributos':  {'slot': 'atributo',  'column': 'da.det_atributo',  'singular': 'atributo'},
}


class SlotError(Exception):
    pass

