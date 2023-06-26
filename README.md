
# MongoPy
![Interrogate](/interrogate_badge.svg)
[![CodeQL](https://github.com/sagarmotghare/mongopy/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/sagarmotghare/mongopy/actions/workflows/github-code-scanning/codeql)
[![Pylint]()](https://github.com/sagarmotghare/mongopy/actions/workflows/pylint.yml)

A simple package to do operation on MongoDB database. Use below command to install a package.

``` pip install git+https://github.com/sagarmotghare/mongopy.git ```
# How to Use:
``` py
import mongopy as mp

db = mp.Mongo(MONGODB_URL)
db.get_collection_dataframe("users")
```
# Support
Having problems or got a question?
- Ask more detailed questions on the mail: [sagarmotghare@proton.me](mailto:%20sagarmotghare@proton.me)
- Use [Github](https://github.com/sagarmotghare/mongopy) for submitting issues and pull requests.
# Changelog
## 0.0.1 (released June 10, 2023)
- First version including all functions
## 0.0.2 (released June 10, 2023)
- Installation Issue Resolves
## 0.0.3 (released June 23, 2023)
- rename package from mongo to mongopy
