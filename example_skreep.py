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