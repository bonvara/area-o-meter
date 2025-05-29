# Area-o-meter
Test project. A library to calculate areas of geometric shapes.
## Use
1. Download the wheel from "Releases": https://github.com/bonvara/area-o-meter/releases
2. Install:  
```
pip install path/to/distribution/area_o_meter-X.X.X-py3-none-any.whl
```
3. Use:  
```
from meter.shapes.circle import Circle
from meter.shapes.triangle import Triangle
from meter.utils import are_equiareal
```
## Develop
Create and activate a virtual envirinment:
```
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```
Install dev dependencies: 
```
pip install -r requirements-dev.txt
```
Lint:  
```
ruff check
```  
Test:  
```
pytest
```  
Build:  
```
python -m build --wheel
```
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
