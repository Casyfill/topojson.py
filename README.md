# TOPOJSON.PY [![Build Status](https://travis-ci.org/Casyfill/topojson.py.svg?branch=master)](https://travis-ci.org/Casyfill/topojson.py)

### Note: currently all updates are on [Casyfill's fork](https://github.com/Casyfill/topojson.py). We're working on updating this package. 
For current status, go to the [project](https://github.com/Casyfill/topojson.py/projects/1).



Translation of [topojson](https://github.com/mbostock/topojson), licensed under same BSD license as original, current usage:

input can be a file-like object, a path to a file, or a dict, output can be a path or a file-like object, if omited a dict is returned

current tested options are `quantization` and `simplify`.

```python
from topojson import topojson
#give it a path in and out
topojson(inPath,outPath, quantization=1e6, simplify=0.0001)
```

can also go the other way.

```python
from topojson import geojson
geojson(topojson,input_name=None,out_geojson=None)
```
`topojson` may be a dict, a path, or a file like object, `input_name` is a string and if omited
the first object in `topojson.objects` is used, `geojson` may be a file like object or
a path if omitied the dict is returned

known issues:
- coding style only a mother could love
- holds everything in memory, this could be bad
- should be able to incrementally add features to a topojson object
