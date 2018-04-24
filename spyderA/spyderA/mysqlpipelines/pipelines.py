from .sql import Sql
from spyderA.items import SpyderaItem


class SpyderaPipeline(object):

    def process_item(self, item, spider):
        if isinstance(item, SpyderaItem):
            title = item['title']
            ret = Sql.select_title(title)
            if ret[0] == 1:
                print('exists')
                pass
            else:
                author = item['author']
                Sql.insert_title_author(title, author)
                print('start save')

