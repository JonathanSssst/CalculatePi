# Calculating Pi

## Project Description

This project implements a method to calculate the mathematical constant π (pi) using Python, based on geometric principles. By approximating the circumference of a circle using inscribed and circumscribed regular polygons, we can compute an approximate value of π. The project aims to demonstrate how to calculate π using simple mathematical principles and explore the relationship between calculation precision and performance.

## Mathematical Principle

The calculation method is based on Archimedes' approach, using inscribed and circumscribed regular polygons to approximate π:

1. For a regular n-sided polygon inscribed in a unit circle, the perimeter formula is: `2n × sin(180°/n)`
2. For a regular n-sided polygon circumscribed around a unit circle, the perimeter formula is: `2n × tan(180°/n)`
3. The approximate value of π is taken as the average of these two perimeters divided by 2: `π ≈ (inscribed perimeter + circumscribed perimeter) / 4`

As n increases, the perimeters of the polygons will get closer to the circumference of the circle, and the approximate value of π will become more accurate.

## Code Structure

- `main.py`: Main program file containing the core code for calculating π
- `blog.md`: Detailed article explaining the project background, mathematical principles, and code analysis
- `README.md`: Project description document

## Usage

1. Ensure Python 3.x is installed
2. Clone or download this repository
3. Run the following command:

```bash
python main.py
```

## Notes

1. When n is very large (e.g., 10^16), the calculation may consume more time and system resources
2. Due to floating-point precision limitations, the accuracy will not improve significantly after n exceeds a certain value
3. The program uses the `input()` function at the end to pause, allowing you to view the results

## License

This project is licensed under the MIT License - see the LICENSE file for details

## Contributing

Contributions are welcome! Please submit issues and pull requests to improve this project.
