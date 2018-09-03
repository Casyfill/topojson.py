import pytest
from os import path
import requests as rq
from .utils import validate_json
import json

# from glob import glob

test_dir = path.join(path.dirname(__file__), "data")


@pytest.fixture(scope="class")
def tpscheme(request):
    url = "https://raw.githubusercontent.com/calvinmetcalf/topojson.py/v1.1.x/test_objects/schema/topojson.json"
    request.cls.tpscheme = rq.get(url).json()


objs = {
    "square": {"type": "Topology", "bbox_length": 4, "geometries": 1},
    "square_with_hole": {"type": "Topology", "bbox_length": 4, "geometries": 1},
    "two_squares": {"type": "Topology", "bbox_length": 4, "geometries": 2},
}


@pytest.mark.usefixtures("tpscheme")
class TestTopojson(object):
    @pytest.mark.parametrize("type_, props", objs.items())
    def test_convert_geojson_to_topojson(self, type_, props):
        from topojson.conversion import convert

        path_to_file = path.join(test_dir, f"{type_}.geojson")

        with open(path_to_file, "r") as f:
            obj = json.load(f)

        tj = convert(obj)

        # check vs schema
        validate_json(tj, self.tpscheme)

        assert tj["type"] == props["type"]
        assert len(tj["bbox"]) == props["bbox_length"]
        assert len(tj["objects"]["name"]["geometries"]) == props["geometries"]
