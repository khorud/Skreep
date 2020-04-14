# Skreep
[![PyPI version fury.io](https://d25lcipzij17d.cloudfront.net/badge.svg?id=py&type=6&v=0.1.3&x2=0)](https://pypi.org/project/skreep/)<br />
It's fun data scraping with just a few lines of code. Basically Skreep is a function to make it easier to run selenium.

## Installation
```Python 3```<br />
```python -m pip install -U skreep```

## Example
[Us here :: Reference](https://www.youtube.com/channel/UC1d-WpQcyHl3AvLgrFykJbA)
```
from skreep.skreep import Skreep
from skreep.download import dl
from skreep.datasheet import sheet
from skreep.save import Save
from skreep.display import display

data = sheet('datasheet')
sk = Skreep()
sv = Save(name='file_name')

for i in data:
    sk.get(i, sc=5)
    title = display(sk.tag('h1', sc=5))
    sv.save(title)

sk.quit()
```
## Usage documentation
* ```sheet(datasheet)``` : Load datasheet
* ```Skreep()``` : Main Class
* ```Save(name=file_name, ext=csv|txt)``` : Save file
* ```display(elm)``` or ```.text``` : print
* ```dl(url, set=default|list)``` : Download file
* ```.quit()``` : end
* ```.get(url, sc=0)``` : get url
* ```.tag(args, set=default|in, sc=0)``` : tag element, ```set=in``` arguments required: ```object, tag``` default just use ```tag```
* ```.cls(args, set=default|in, sc=0)``` : class element
* ```.id(args, set=default|in, sc=0)``` : id element
* ```.path(args, set=default|in, sc=0)``` : xpath element
* ```.paths(args, set=default|in, sc=0)``` : xpath elements, argument required plural path
* ```.img(args, set=pa|pta|ota, sc=0)``` : Generally used to extract image urls. ```set:pa is default.``` <br />```set=pa``` arguments required : ```path, attribute```<br />```set=pta``` arguments required : ```path, tag, attribute```<br />```set=ota``` arguments required : ```object, tag, attribute```

## Dependency
```selenium```
## Driver
```Chrome``` ```https://chromedriver.chromium.org/downloads``` must be in the same project directory.
## Donate
BTC ```37rkr9cpVVcxg8vUpF65Cp9Mjgu1WrKD3d``` or Paypal [Here](https://paypal.me/dian26?locale.x=id_ID "Donate")
