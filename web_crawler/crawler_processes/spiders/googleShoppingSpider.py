import scrapy
from scrapy.linkextractors import LinkExtractor
from urllib.parse import urlparse, parse_qs, unquote
from JSONprocess import append_to_json
from dom_filteration import get_html_tags


# Our main shopping spider for Google. 
class googleShoppingSpider(scrapy.Spider):
    name = "googleShoppingSpider"

    def __init__(self, searchQuery='', **kwargs):
        super().__init__(**kwargs)
        self.searchQuery = searchQuery
        self.product_data = {'search_term': self.searchQuery,
                    'product':[{'url': "",
                               'title': "",
                               'image': "",
                               'price': ""}] }

    def start_requests(self):
        url = f'https://www.google.com/search?q={self.searchQuery}&source=lnms&tbm=shop'
        yield scrapy.Request(url=url, callback=self.parse)
    

    def parse(self, response):
        found_urls = []
        print(response)
        
        link_extractor = LinkExtractor(allow=(r'url\?q=http'))
    
        for link in link_extractor.extract_links(response):
            print("LINK: ", link.url)

            if not check_word_repetition(link.url, "google.com"):
                direct_url = extract_direct_url(link.url)
                if direct_url not in found_urls:
                    found_urls.append(direct_url)

        self.product_data['product'] = get_html_tags(found_urls)

    def closed(self, reason):
        try:
            append_to_json(self.product_data)
        except Exception as e:
            print(e)    


def check_word_repetition(url_string, word):
    url_string = url_string.lower()
    word_count = url_string.count(word.lower())
    return word_count > 1

def extract_direct_url(google_url):
        parsed_url = urlparse(google_url)
        query_params = parse_qs(parsed_url.query)
        direct_url = query_params.get('q')
        if direct_url:
            direct_url = direct_url[0]
            direct_url = unquote(direct_url)  # Decode URL
            return direct_url



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
