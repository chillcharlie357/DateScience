class WangyiproPipeline(object):
    def process_item(self,item,spider):
        with open('data_science.text','w',encoding='utf-8') as fp:
            fp.write(item)
        print(item)
        return item