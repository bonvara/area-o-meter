# Area-o-meter
Test project. A library to calculate areas of geometric shapes.
## Usage
Download from "Releases" page.
Install:
`pip install path/to/distribution/area_o_meter-X.X.X-py3-none-any.whl`
Use:
`from meter.types import Circle, Triangle`
## Features
## Requirements
- Вычисление площади фигуры без знания типа фигуры в compile-time
## Considerations
- The library is intended for distributing to the company's clients. GitHub Releases is the chosen mechanism for distribution. In the future it's recommended to publish the library into the company's (or the client's) PyPI repository
- Releases are produced automatically via GitHub Actions
- Protocols were used instead of inheritance from BaseShape abstract class. I've recently read "Pragmatic Programmer" on inheritance tax, and am learning to avoid using classic inheritance due to coupling, maintainability and bloat (bypassing) issues
- While calculating area without knowing the type of the shape in compile-time is natural for many interpreted languages such as Python, the point of the requirement was to express polymorphism
- Using inheritance in this case is ok because:
    - Modeling a true "is-a" relationship: circle is a kind of shape
    - We're inheriting from an abstract base class, so we're not sharing code, just the structure, 