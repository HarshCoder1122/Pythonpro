<div align="center">

# 🎂 Pythonpro

### Find your exact age from a date of birth, built for fun while learning Python classes.

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](work.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

[![Last commit](https://img.shields.io/github/last-commit/HarshCoder1122/Pythonpro?style=flat-square)](https://github.com/HarshCoder1122/Pythonpro/commits/main)
[![Issues](https://img.shields.io/github/issues/HarshCoder1122/Pythonpro?style=flat-square)](https://github.com/HarshCoder1122/Pythonpro/issues)

</div>

## Table of contents

- [What it does](#what-it-does)
- [Getting started](#getting-started)
- [How it works](#how-it-works)
- [Project structure](#project-structure)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

## What it does

`age.py` defines a small `person` class holding a name, country and date of birth, and calculates the person's current age in whole years. It correctly subtracts one year if this year's birthday has not happened yet.

The repo also contains `work.html` and `style.css`, a small static page from the same learning journey.

## Getting started

No dependencies. You only need Python 3.

```bash
git clone https://github.com/HarshCoder1122/Pythonpro.git
cd Pythonpro
python age.py
```

To use your own details, edit this line at the bottom of [age.py](age.py):

```python
person1 = person("Your Name", "Your Country", date(2000, 1, 31))
```

## How it works

```python
today = date.today()
age = today.year - self.Date_of_Birth.year
if today < date(today.year, self.Date_of_Birth.month, self.Date_of_Birth.day):
    age -= 1
```

The birthday check compares today with this year's birthday. Note that a 29 February birth date raises an error in non-leap years, which is a nice first issue to fix.

## Project structure

```text
Pythonpro/
├── age.py        # person class and age calculation
├── work.html     # Static practice page
├── style.css     # Styles for work.html
├── README.md
├── LICENSE
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
└── SECURITY.md
```

## Roadmap

- [ ] Ask for the date of birth with `input()`
- [ ] Handle 29 February birthdays
- [ ] Show years, months and days
- [ ] Show days until the next birthday

## Contributing

Beginner contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) and follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## License

Released under the [MIT License](LICENSE).

<div align="center"><sub>Built by <a href="https://github.com/HarshCoder1122">Harsh</a>. Created for fun.</sub></div>
