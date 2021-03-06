import scrapy, json, sqlite3, logging, datetime, os, psycopg2

insta_fs = "https://www.instagram.com/%s/?__a=1"
MAX_ENGAGEMENT_POSTS = 10
DB_NAME = os.environ.get('DATABASE_URL')

def get_handles():
    conn = psycopg2.connect(DB_NAME)
    c = conn.cursor()
    insta_handles = []
    try:
        op = c.execute("SELECT instagram_id from iprofile")
        insta_handles = list(set([x[0] for x in op]))
    except:
        pass
    c.close()
    return insta_handles

class InstaSpider(scrapy.Spider):
    name = "ifeed"
    def start_requests(self):
        insta_handles = get_handles()
        self.log("Handles =  are %s"%str(insta_handles), level = logging.INFO)
        for url in insta_handles:
            yield scrapy.Request(url= insta_fs % url, callback=self.parse)

    def parse(self, response):
        idata = json.loads(response.body.decode())
        today = datetime.date.today()
        followed_by = idata['user']['followed_by']['count']
        follows =  idata['user']['follows']['count']
        media = idata['user']['media']['count']
        posts = idata['user']['media']['nodes']
        end = min(len(posts), MAX_ENGAGEMENT_POSTS + 1)
        engagement_rate =  sum([x['likes']['count'] for x in posts[1:end]]) * 1./(MAX_ENGAGEMENT_POSTS * followed_by) if followed_by > 0 else 0.0
        data = {'instagram_id' : idata['user']['username'], 'followers_count' : followed_by, 'following_count' : follows , 'date' : today, 'media_likes' : media, 'engagement_rate' : engagement_rate}
        return data
