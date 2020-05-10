# ProgRace

Progress-bar badges for Markdown in SVG format

[![CircleCI](https://circleci.com/gh/YAS-opensource/ProgRace.svg?style=svg)](https://circleci.com/gh/YAS-opensource/ProgRace)
[![Maintainability](https://api.codeclimate.com/v1/badges/98662a5d50c39656e17f/maintainability)](https://codeclimate.com/github/YAS-opensource/ProgRace/maintainability)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/dae907fd89fd48419685cb0f7982b590)](https://www.codacy.com/app/geektrovert/ProgRace?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=YAS-opensource/ProgRace&amp;utm_campaign=Badge_Grade)

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg?style=flat-square)](https://GitHub.com/YAS-opensource/ProgRace/graphs/commit-activity)
![GitHub last commit (branch)](https://img.shields.io/github/last-commit/YAS-opensource/ProgRace/master.svg?style=flat-square)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![GPLv3 license](https://img.shields.io/badge/License-GPL-blue.svg?style=flat-square)](./LICENSE)

## How to use

### Default

![ProgRace](https://progdown.herokuapp.com/?progress=20)

```md
![ProgRace](https://progdown.herokuapp.com/?progress=20)
```

![ProgRace](https://progdown.herokuapp.com/?progress=34)

```md
![ProgRace](https://progdown.herokuapp.com/?progress=34)
```

![ProgRace](https://progdown.herokuapp.com/?progress=80)

```md
![ProgRace](https://progdown.herokuapp.com/?progress=80)
```

### Custom range

You don't need to calculate the progress by hand and copy paste it here, just pass the total range as `total` and it's done, simple as that.

![ProgRace](https://progdown.herokuapp.com/?progress=10&total=20)

```md
![ProgRace](https://progdown.herokuapp.com/?progress=10&total=20)
```

![ProgRace](https://progdown.herokuapp.com/?progress=755&total=1000)

```md
![ProgRace](https://progdown.herokuapp.com/?progress=755&total=1000)
```

### Custom Title

You can also give it a custom title.

![ProgRace](https://progdown.herokuapp.com/?progress=50&total=100&title=Custom)

```md
![ProgRace](https://progdown.herokuapp.com/?progress=50&total=100&title=Custom)
```

## Contributing guideline

Install the dependencies:

```sh
pip install -r requirements.txt
```

Run the code:

```sh
python3 app.py
```

Open the browser and go to [localhost:3000](http://localhost:3000)

Happy hacking! Make sure to open a PR when you are done!

## Users

We will be happy to show the world our splendid users! To be listed here, just add your link to the project below this line and open a PR!

## License

MIT License

Copyright (c) 2019 [Samnan Rahee](https://github.com/Geektrovert), [Sihan Tawsik](https://github.com/SedativeHypnotics)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
