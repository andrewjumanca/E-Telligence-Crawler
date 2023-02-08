import scrapy

class bingShoppingSpider(scrapy.Spider):
    name = "bingShoppingSpider"
    start_urls = [
        'https://www.bing.com/shop?q=banana+pants&FORM=SHOPTB'
    ]

    def parse(self, response):
        pageNum = response.css("a.sb_pagS.sb_pagS_bp.sb_bp::text").extract_first()
        for product in response.css("li.br-item.br-allowCrdovrflw"):
            pNameSelectors = ['div.br-title span::attr(title)', 'div.br-title span::text', 'div.br-title::text', 'div.br-offTtl.b_primtxt::text']
            product_name = next(
                (product.css(selector).get() for selector in pNameSelectors if product.css(selector).get()), None
            )

            yield {
                'page': pageNum,
                'product_name': product_name,
                'seller': product.css("div.br-seller::text").extract_first(),
                'price': product.css("div.pd-price.br-standardPrice.promoted::text").extract_first(),
                'URL': product.css("a.br-titlelink::attr(href)").extract_first()
            }

        next_pages = response.css("a.sb_bp::attr(href)").getall()
        for next_page in next_pages:
            if "page=" + str(pageNum) in next_page:
                yield response.follow(next_page, self.parse)
        if next_page:
            yield response.follow(next_page, self.parse)
            
            