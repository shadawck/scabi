# Scabi  

Implement vulnerabilities scanning on top of package management system like apt, pip, composer...

# Install

You can install ```scabi``` either via pip (PyPI) or from source.
To install using pip:
```sh
python3 -m pip install scabi
```
Or manually:
```
git clone https://github.com/remiflavien1/scabi
cd scabi
python3 setup.py install
```

## CLI
```
Scabi

Usage:
  scabi <pms> <package> [--verbose --detail ] [--oss  --mitre] [-s FILE]
  scabi -h --help --version

Options:
  -v --verbose      Show full output.
  -d --detail       Show CVE details.
  -o --oss          Search vulnerabilities only through OSS.
  -m --mitre        Search vulnerabilities only through MITRE.
  -s --save FILE    Save output to file.
  -h --help         Show this screen.
```

Example of output for the python module ```django```:

```sh
$ scabi -v pip django
```

```
The dependencies for <django> are :
... pytz
... sqlparse
... asgiref
... argon2-cffi
... bcrypt

>>>>>>>>>>>>>>> SEARCH IN OSS INDEX <<<<<<<<<<<<<<<
NO VULNERABILITIES FOUND

>>>>>>>>>>>>>>> SEARCH IN MITRE DATABASE <<<<<<<<<<<<<<<

-------------- Package: <bcrypt> --------------

CVE : CVE-2020-5229
CVE DETAIL https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-5229
DESCRIPTION Opencast before 8.1 stores passwords using the rather outdated and cryptographically insecure MD5 hash algorithm. ...

CVE : CVE-2019-13421
CVE DETAIL https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-13421
DESCRIPTION Search Guard versions before 23.1 had an issue that an administrative user is able to retrieve bcrypt password hashes of other users configured in the internal user database.
...

```
