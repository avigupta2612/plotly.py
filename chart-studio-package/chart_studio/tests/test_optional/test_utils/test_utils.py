import json as _json
from unittest import TestCase

import _plotly_utils.utils
from chart_studio.grid_objs import Column
from plotly import utils
from plotly.tests.test_optional.test_utils.test_utils import numeric_list, \
    mixed_list, np_list


class TestJSONEncoder(TestCase):
    def test_column_json_encoding(self):
        columns = [
            Column(numeric_list, 'col 1'),
            Column(mixed_list, 'col 2'),
            Column(np_list, 'col 3')
        ]
        json_columns = _json.dumps(
            columns, cls=_plotly_utils.utils.PlotlyJSONEncoder, sort_keys=True
        )
        print(json_columns)
        assert('[{"data": [1, 2, 3], "name": "col 1"}, '
               '{"data": [1, "A", "2014-01-05T00:00:00", '
               '"2014-01-05T01:01:01", '
               '"2014-01-05T01:01:01.000001"], '
               '"name": "col 2"}, '
               '{"data": [1, 2, 3, null, null, null, '
               '"2014-01-05T00:00:00"], "name": "col 3"}]' == json_columns)