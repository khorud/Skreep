# Skreep
It's fun data scraping with just a few lines of code. Basically Skreep is a function to make it easier to run selenium.

## Installation
```Python 3```<br />
```pip install skreep```

## Example
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
* ```sheet(str)``` : Load datasheet
* ```Skreep()``` : Main Class
* ```Save(name=str, ext=str)``` : Save file, ```ext:default extension is``` csv
* ```display(var)``` or ```.text``` : print
* ```dl(url, set=str|list)``` : Download file, ```set:default is``` single file
* ```.quit()``` : end
* ```.get(url, sc=int)``` : get url, ```sc:default wait is``` 0 seconds
* ```.tag(elm1|elm2, set=str|in, sc=int)``` : read section tag-name, use ```elm1``` if ```set=in``` is used. ```set:default is``` single element
* ```.clas(elm1|elm2, set=str|in, sc=int)``` : read section class-name
* ```.id(elm1|elm2, set=str|in, sc=int)``` : read section id-name
* ```.path(elm1|elm2, set=str|in, sc=int)``` : read section xpath-name
* ```.paths(elm, sc=int)``` : read section list xpath-name
* ```.img(elm1|elm2|elm3, set=pa|pta|ota, sc=int)``` : Generally used to extract image urls. ```set:pa is default``` <br />tes

## Dependency
```selenium```
## Driver
```https://chromedriver.chromium.org/downloads```
## Donate
BTC ```37rkr9cpVVcxg8vUpF65Cp9Mjgu1WrKD3d``` or Paypal [Here](https://paypal.me/dian26?locale.x=id_ID "Donate")
