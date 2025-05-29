# Area-o-meter
A test project. A library to calculate areas of geometric shapes.
## Usage
Download the wheel from "Releases" page.
Install:
`pip install path/to/distribution/area_o_meter-X.X.X-py3-none-any.whl`
Use:
```
from meter.shapes.circle import Circle
from meter.shapes.triangle import Triangle
from meter.utils import are_equiareal
```
## Development
Install dev dependencies:
`pip install -r requirements-dev.txt`
Lint:
`ruff check`
Test:
`pytest`
Build:
`python -m build --wheel`
## Features
## Requirements and considerations
- Make a Python library for computation of the area of triangles and circles
- Intended for distributing to the company's clients
    - Code quality is a priority
    - GitHub Releases was chosen as the mechanism of distribution. Releases are produced automatically via GitHub Actions
- Unit tests
- Easiness of adding new shapes
- Calculating the area without knowing the type of a shape in compile-time
    - Polymorphism is achieved using Python Protocols, allowing area calculation without knowing the shape type in advance
- Checking if the triangle is right-angled
