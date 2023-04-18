import scrapy
from scrapy.linkextractors import LinkExtractor
from urllib.parse import urlparse, parse_qsl

class googleShoppingSpider(scrapy.Spider):
    name = "googleShoppingSpider"
    links = []

    def __init__(self, searchQuery="", *args, **kwargs):
        super(googleShoppingSpider, self).__init__(*args, **kwargs)
        self.searchQuery = searchQuery


    def start_requests(self):
        url = f'https://www.google.com/search?q={self.searchQuery}&source=lnms&tbm=shop'
        yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        found_urls = []
        
        link_extractor = LinkExtractor(allow=r'url\?q=http')
    
        for link in link_extractor.extract_links(response):
            if not check_word_repetition(link.url, "google.com"):
                found_urls.append(link.url)

        for url in found_urls:
            yield scrapy.Request(url=url, callback=self.get_actual_urls)

    def get_actual_urls(self, response):
        # actual_url = extract_actual_url(response.url)
        print(response.url)
        self.links.append(response.url)



def check_word_repetition(url_string, word):
    url_string = url_string.lower()
    word_count = url_string.count(word.lower())
    return word_count > 1

def extract_actual_url(google_url):
    parsed_url = urlparse(google_url)
    query_params = dict(parse_qsl(parsed_url.query))
    actual_url = query_params.get('url', '')
    return actual_url

# Code to connect to Netprism API

# print('starting netprism connection')
# netprism_api_url = 'https://canary.netprism.dev/v1/task'
# load_dotenv()
# api_key = os.getenv('API_KEY')
# headers = {
#     'Authorization': f'Bearer {api_key}',
#     'Content-Type': 'application/json'
# }
# request_body = {
#     'url': 'https://www.champion.com/closed-bottom-jersey-pants.html?country=US&currency=USD',
#     'type': 'webpage',
#     'options': {
#         'jsRender': True
#     }
# }
# response2 = await requests.post(netprism_api_url, headers=headers, json=request_body)
# response_json = response2.json()
# print(response2.json)
# # Retrieve the task ID from the response
# data = response_json['data']
# decoded_html = base64.b64decode(data)
# print(decoded_html)
# print('finished netprism connection')
# with open("output.txt", "w") as f:
#     # Write some text to the file
    # f.write(decoded_html.decode('utf-8'))