# ProgDown

Progress-bar badges for Markdown in SVG format

[![CircleCI](https://circleci.com/gh/YAS-opensource/ProgDown.svg?style=svg)](https://circleci.com/gh/YAS-opensource/ProgDown)
[![Maintainability](https://api.codeclimate.com/v1/badges/98662a5d50c39656e17f/maintainability)](https://codeclimate.com/github/YAS-opensource/ProgDown/maintainability)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/dae907fd89fd48419685cb0f7982b590)](https://www.codacy.com/app/geektrovert/ProgDown?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=YAS-opensource/ProgDown&amp;utm_campaign=Badge_Grade)
[![Code style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://black.readthedocs.io/en/stable/)

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg?style=for-the-badge)](https://GitHub.com/YAS-opensource/ProgDown/graphs/commit-activity)
![GitHub last commit (branch)](https://img.shields.io/github/last-commit/YAS-opensource/ProgDown/master.svg?style=for-the-badge)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](http://makeapullrequest.com)

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/Naereen/)
[![GPLv3 license](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](./LICENSE)
[![Open Source Love svg3](https://badges.frapsoft.com/os/v3/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

## How to use

### Default

![ProgDown](https://progdown.herokuapp.com/?progress=20)

```md
![ProgDown](https://progdown.herokuapp.com/?progress=20)
```

![ProgDown](https://progdown.herokuapp.com/?progress=34)

```md
![ProgDown](https://progdown.herokuapp.com/?progress=34)
```

![ProgDown](https://progdown.herokuapp.com/?progress=80)

```md
![ProgDown](https://progdown.herokuapp.com/?progress=80)
```

### Custom range

You don't need to calculate the progress by hand and copy paste it here, just pass the total range as `total` and it's done, simple as that.

![ProgDown](https://progdown.herokuapp.com/?progress=10&total=20)

```md
![ProgDown](https://progdown.herokuapp.com/?progress=10&total=20)
```

![ProgDown](https://progdown.herokuapp.com/?progress=755&total=1000)

```md
![ProgDown](https://progdown.herokuapp.com/?progress=755&total=1000)
```

### Custom Title

You can also give it a custom title.

![ProgDown](https://progdown.herokuapp.com/?progress=50&total=100&title=Custom)

```md
![ProgDown](https://progdown.herokuapp.com/?progress=50&total=100&title=Custom)
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
