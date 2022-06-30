BOT_NAME = 'data_science'

SPIDER_MODULES = ['data_science.spiders']
NEWSPIDERS_MODULES = 'data_science.spiders'

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'

ROBOTSTXT_OBEY = False

LOG_LEVEL = 'EORROR'

LOG_LEVEL = 'EORROR'

DOWNLOADER_MIDDLEWARES = {
    'data_science.middlewares.DownloaderMiddleWare':543
}
ITEM_PIPELINES = {
    'data_science.pipelines.WangyiproPipeline':300
}