from datetime import datetime

class TidyUp(object):
    def process_item(self, item, spider):
        item['startup_date_creation']= map(datetime.isoformat, item['startup_date_creation'])
        return item
    
