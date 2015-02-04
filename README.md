## Synopsis

Simple convex hull and traveling salesman problem (TSP) "solver". Just written
as a programming exercise and to get familiar with python Flask apps.

Please note that the TSP solution is not optimal. I was testing out a
hypothesis that calculating a convex hull could help direct a TSP solver that
is close to optimal. That said, sometimes you will see crossed lines, and
situations where you could obviously improve the path. There are a few changes
I can think of where I could sacrifice more runtime for better accuracy.

Demo available [here](http://tsp.lrjn.flynnhub.com/).

## Running

Requires Flask:
```bash
$ pip install flask
```

To run the server:
```bash
$ python server.py
```

By default, serves on port 5000 or `$PORT`.  `http://localhost:5000/`


## Unit Tests

I use nose as a test runner, but there's no hard dependency there.
```bash
$ pip install nose
$ nosetests
```


## License

Copyright 2014 John Zila

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
