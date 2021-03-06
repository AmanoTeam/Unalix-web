This is a simple web application (and also a Web API) written in Python. It uses [this](https://github.com/AmanoTeam/Unalix) library to allow users to remove tracking fields from URLs and unshort shortened URLs.

### Installation

_**Note**: You will need at least Python 3.6 and a Unix-like operating system._

Install all required dependences:

```bash
apt-get --assume-yes install \
    'python3' 'python3-pip' 'python3-setuptools' 'python3-wheel' 'git'
```

Create a separate user:

```bash
adduser --shell '/bin/bash' \
    --disabled-login \
    'unalix'

sudo -i --user='unalix'
```

Clone this repo:

```bash
git clone --ipv4 \
    --single-branch \
    --no-tags \
    --depth '1' \
    'https://github.com/AmanoTeam/Unalix-web'
```

Install all required libraries:

```bash
python3 -m pip install --force-reinstall \
    --disable-pip-version-check \
    --no-warn-script-location \
    --user \
    --upgrade \
    'setuptools' 'wheel' 'testresources' 'virtualenv' 'pip'

python3 -m virtualenv --download \
    --no-periodic-update \
    "${HOME}/Unalix-web/venv"

source "${HOME}/Unalix-web/venv/bin/activate"

pip install --force-reinstall \
    --disable-pip-version-check \
    --no-warn-script-location \
    --upgrade \
    'django' 'gunicorn' 'git+https://github.com/AmanoTeam/Unalix'
```

Start the webserver

```bash
cd "${HOME}/Unalix-web"

"${PWD}/venv/bin/gunicorn" \
    --workers '1' \
    --bind '127.0.0.1:35678' \
    'unalixweb.wsgi:application'
```

Now you have an instance running at `http://127.0.0.1:35678/`.

### API usage

Removing tracking fields:

```bash
url='https://deezer.com/track/891177062?utm_source=deezer'

curl --url 'http://127.0.0.1:35678/' \
    --get \
    --data-urlencode "url=${url}" \
    --data-urlencode 'output=json' \
    --data-urlencode 'method=clear'
```

Unshortening a shortened URL:

```bash
url='https://bitly.is/Pricing-Pop-Up'

curl --url 'http://127.0.0.1:35678/' \
    --get \
    --data-urlencode "url=${url}" \
    --data-urlencode 'output=json' \
    --data-urlencode 'method=unshort'
```

Output from both examples:

```json
{"new_url": "https://deezer.com/track/891177062"}
{"new_url": "https://bitly.com/pages/pricing"}
```

_**Note**: You can replace `http://127.0.0.1:35678/` with the address of any public instance._

### Public instances

Don't want to run Unalix locally? Take a look at these public instances:

- [unalix.amanoteam.com](https://unalix.amanoteam.com/) ([hidden service](http://5hluj6f4emkqnd2gjuvppv6544pzyfsw56eewx4cgatesunx75z2vwid.onion/))

### Third party software

Unalix-web includes some third party software. See them below:

- **unshort.link**
  - Author: Simon Frey
  - Repository: [simonfrey/unshort.link](https://github.com/simonfrey/unshort.link)
  - License: [GNU Affero General Public License v3.0](https://github.com/simonfrey/unshort.link/blob/master/LICENSE.md)
