import fixieai
import json
import subprocess
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders.googleShoppingSpider import googleShoppingSpider

BASE_PROMPT = """I am an agent that finds real time google shopping data for a specific product sold at different retailers. """

FEW_SHOTS = """
Q: Find me 5 retailers that sell black and white nike blazers
Ask Func[getProductUrls]: 5, black and white nike blazers
Func[getProductUrls] says: https://www.amazon.com/Nike-Blazer-Vintage-White-Black/dp/B07QNKW3SH?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&psc=1&smid=A31J6LUBT60QY
https://stockx.com/nike-blazer-mid-77-white-black-w?country=US&currencyCode=USD&size=5.5W&srsltid=Ad5pg_E7dUbq4V7sKvjbmJcGwMRF8ob-GcyDubFOl6MTh37HT6Klt7Fcqpg
https://www.nike.com/t/blazer-mid-77-big-kids-shoes-4VfSTd/DA4086-100?nikemt=true&srsltid=Ad5pg_HzdTZQFL1DLJlxn5OfvMyUdHcTVlfx8L_vBg1rnUcbjKZXXcpahF4
https://www.dickssportinggoods.com/p/nike-kids-grade-school-blazer-mid-77-shoes-20nikyblzrwhtblckbys/20nikyblzrwhtblckbys?sku=21218417&srsltid=Ad5pg_FHd0GmGXt3QK0bGE1NaxoLO4iK-z359DpCnhI_lSO03cbR-Bqqb_8
https://www.kickscrew.com/products/nike-blazer-mid-77-vntg-white-black-bq6806-100?variant=40856089034947&currency=USD&srsltid=Ad5pg_FY5lUGMa80KyFXttklsGUB537vYc6ThXtKJUNpdjWSm2ZhO8y47TI
      
A: I found great results at Amazon, StockX, Nike, Dick's Sporting Goods... 
[1. amazon](https://www.amazon.com/Nike-Blazer-Vintage-White-Black/dp/B07QNKW3SH?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&psc=1&smid=A31J6LUBT60QY)
[2. stockx](https://stockx.com/nike-blazer-mid-77-white-black-w?country=US&currencyCode=USD&size=5.5W&srsltid=Ad5pg_E7dUbq4V7sKvjbmJcGwMRF8ob-GcyDubFOl6MTh37HT6Klt7Fcqpg)
[3. nike](https://www.nike.com/t/blazer-mid-77-big-kids-shoes-4VfSTd/DA4086-100?nikemt=true&srsltid=Ad5pg_HzdTZQFL1DLJlxn5OfvMyUdHcTVlfx8L_vBg1rnUcbjKZXXcpahF4)
[4. dickssportinggoods](https://www.dickssportinggoods.com/p/nike-kids-grade-school-blazer-mid-77-shoes-20nikyblzrwhtblckbys/20nikyblzrwhtblckbys?sku=21218417&srsltid=Ad5pg_FHd0GmGXt3QK0bGE1NaxoLO4iK-z359DpCnhI_lSO03cbR-Bqqb_8)
[5. nike](https://www.kickscrew.com/products/nike-blazer-mid-77-vntg-white-black-bq6806-100?variant=40856089034947&currency=USD&srsltid=Ad5pg_FY5lUGMa80KyFXttklsGUB537vYc6ThXtKJUNpdjWSm2ZhO8y47TI)
      

Q: Find me 10 retailers that sell blue hydroflasks
Ask Func[getProductUrls]: 10, blue hydroflasks
Func[getProductUrls] says: https://www.hydroflask.com/32-oz-wide-mouth-pacific
https://www.hydroflask.com/21-oz-standard-mouth-laguna
https://www.hydroflask.com/18-oz-standard-mouth-pacific
https://www.hydroflask.com/32-oz-wide-mouth-w-straw-lid-pacific
https://www.hydroflask.com/18-oz-standard-mouth-laguna
https://www.hydroflask.com/40-oz-wide-mouth-indigo
https://www.hydroflask.com/21-oz-standard-mouth-seagrass
https://www.hydroflask.com/18-oz-standard-mouth-indigo
https://www.hydroflask.com/24-oz-standard-mouth-indigo
https://www.ebay.com/itm/155413980609?chn=ps&mkevt=1&mkcid=28&srsltid=Ad5pg_F_N-PkTbiLwZ6n7uJH0ksmTE2tk9IQJe-90BFBmfpicJpcrjOw9KE

A: I found great results at Hydroflask and Ebay...
[1. hydroflask](https://www.hydroflask.com/32-oz-wide-mouth-pacific)
[2. hydroflask](https://www.hydroflask.com/21-oz-standard-mouth-laguna)
[3. hydroflask](https://www.hydroflask.com/18-oz-standard-mouth-pacific)
[4. hydroflask](https://www.hydroflask.com/32-oz-wide-mouth-w-straw-lid-pacific)
[5. hydroflask](https://www.hydroflask.com/18-oz-standard-mouth-laguna)
[6. hydroflask](https://www.hydroflask.com/40-oz-wide-mouth-indigo)
[7. hydroflask](https://www.hydroflask.com/21-oz-standard-mouth-seagrass)
[8. hydroflask](https://www.hydroflask.com/18-oz-standard-mouth-indigo)
[9. hydroflask](https://www.hydroflask.com/24-oz-standard-mouth-indigo)
[10. ebay](https://www.ebay.com/itm/155413980609?chn=ps&mkevt=1&mkcid=28&srsltid=Ad5pg_F_N-PkTbiLwZ6n7uJH0ksmTE2tk9IQJe-90BFBmfpicJpcrjOw9KE)
"""
shoppingAgent = fixieai.CodeShotAgent(BASE_PROMPT, FEW_SHOTS)


@shoppingAgent.register_func
def getProductUrls(query: fixieai.Message) -> str:
    numRetailers, search_term = query.text.replace(" ", "").split(",")
    numRetailers = int(numRetailers)
    # process = CrawlerProcess(get_project_settings())
    # process.crawl(googleShoppingSpider,  search_query = search_term)
    # process.start()
    result = subprocess.run(['python', 'crawl.py', search_term], capture_output=True, text=True)
    output = result.stdout
    import json
    output = json.loads(output.replace("'", '"'))
    output = '\n'.join(output[:numRetailers+1])
    print(f"output: {output[:numRetailers+1]}")

    return output
      
