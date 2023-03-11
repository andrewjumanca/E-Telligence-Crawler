import fixieai

BASE_PROMPT = """I am an agent that finds real time google shopping data for a specific product sold at different retailers."""

FEW_SHOTS = """
Q: Find me 5 retailers that sell black and white nike blazers
Ask Func[getProductUrls]: 5, black and white nike blazers
Func[example] says: 
       https://www.amazon.com/Nike-Blazer-Vintage-White-Black/dp/B07QNKW3SH?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&psc=1&smid=A31J6LUBT60QY,
       https://stockx.com/nike-blazer-mid-77-white-black-w?country=US&currencyCode=USD&size=5.5W&srsltid=Ad5pg_E7dUbq4V7sKvjbmJcGwMRF8ob-GcyDubFOl6MTh37HT6Klt7Fcqpg,
       https://www.nike.com/t/blazer-mid-77-big-kids-shoes-4VfSTd/DA4086-100?nikemt=true&srsltid=Ad5pg_HzdTZQFL1DLJlxn5OfvMyUdHcTVlfx8L_vBg1rnUcbjKZXXcpahF4,
       https://www.dickssportinggoods.com/p/nike-kids-grade-school-blazer-mid-77-shoes-20nikyblzrwhtblckbys/20nikyblzrwhtblckbys?sku=21218417&srsltid=Ad5pg_FHd0GmGXt3QK0bGE1NaxoLO4iK-z359DpCnhI_lSO03cbR-Bqqb_8,
       https://www.kickscrew.com/products/nike-blazer-mid-77-vntg-white-black-bq6806-100?variant=40856089034947&currency=USD&srsltid=Ad5pg_FY5lUGMa80KyFXttklsGUB537vYc6ThXtKJUNpdjWSm2ZhO8y47TI
      
A: Here are 5 urls for retailers that sell black and white nike blazers:
       https://www.amazon.com/Nike-Blazer-Vintage-White-Black/dp/B07QNKW3SH?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&psc=1&smid=A31J6LUBT60QY,
       https://stockx.com/nike-blazer-mid-77-white-black-w?country=US&currencyCode=USD&size=5.5W&srsltid=Ad5pg_E7dUbq4V7sKvjbmJcGwMRF8ob-GcyDubFOl6MTh37HT6Klt7Fcqpg,
       https://www.nike.com/t/blazer-mid-77-big-kids-shoes-4VfSTd/DA4086-100?nikemt=true&srsltid=Ad5pg_HzdTZQFL1DLJlxn5OfvMyUdHcTVlfx8L_vBg1rnUcbjKZXXcpahF4,
       https://www.dickssportinggoods.com/p/nike-kids-grade-school-blazer-mid-77-shoes-20nikyblzrwhtblckbys/20nikyblzrwhtblckbys?sku=21218417&srsltid=Ad5pg_FHd0GmGXt3QK0bGE1NaxoLO4iK-z359DpCnhI_lSO03cbR-Bqqb_8,
       https://www.kickscrew.com/products/nike-blazer-mid-77-vntg-white-black-bq6806-100?variant=40856089034947&currency=USD&srsltid=Ad5pg_FY5lUGMa80KyFXttklsGUB537vYc6ThXtKJUNpdjWSm2ZhO8y47TI
      

Q: Find me 10 retailers that also sell blue hydroflasks
Ask Func[getProductUrls]: 10, blue hydroflasks
Func[example] says: 
       https://www.hydroflask.com/32-oz-wide-mouth-pacific,
       https://www.hydroflask.com/21-oz-standard-mouth-laguna,
       https://www.hydroflask.com/18-oz-standard-mouth-pacific,
       https://www.hydroflask.com/32-oz-wide-mouth-w-straw-lid-pacific,
       https://www.hydroflask.com/18-oz-standard-mouth-laguna,
       https://www.hydroflask.com/40-oz-wide-mouth-indigo,
       https://www.hydroflask.com/21-oz-standard-mouth-seagrass,
       https://www.hydroflask.com/18-oz-standard-mouth-indigo,
       https://www.hydroflask.com/24-oz-standard-mouth-indigo,
       https://www.ebay.com/itm/155413980609?chn=ps&mkevt=1&mkcid=28&srsltid=Ad5pg_F_N-PkTbiLwZ6n7uJH0ksmTE2tk9IQJe-90BFBmfpicJpcrjOw9KE

A: Here are 10 urls for retailers that sell blue hydroflasks:
       https://www.hydroflask.com/32-oz-wide-mouth-pacific,
       https://www.hydroflask.com/21-oz-standard-mouth-laguna,
       https://www.hydroflask.com/18-oz-standard-mouth-pacific,
       https://www.hydroflask.com/32-oz-wide-mouth-w-straw-lid-pacific,
       https://www.hydroflask.com/18-oz-standard-mouth-laguna,
       https://www.hydroflask.com/40-oz-wide-mouth-indigo,
       https://www.hydroflask.com/21-oz-standard-mouth-seagrass,
       https://www.hydroflask.com/18-oz-standard-mouth-indigo,
       https://www.hydroflask.com/24-oz-standard-mouth-indigo,
       https://www.ebay.com/itm/155413980609?chn=ps&mkevt=1&mkcid=28&srsltid=Ad5pg_F_N-PkTbiLwZ6n7uJH0ksmTE2tk9IQJe-90BFBmfpicJpcrjOw9KE
"""
shoppingAgent = fixieai.CodeShotAgent(BASE_PROMPT, FEW_SHOTS)


@shoppingAgent.register_func
def getProductUrls(query: fixieai.Message) -> str:
    numProducts, search_term = query.text.replace(" ", "").split(",")
    return "https://www.amazon.com/Nike-Blazer-Vintage-White-Black/dp/B07QNKW3SH?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&psc=1&smid=A31J6LUBT60QY, https://stockx.com/nike-blazer-mid-77-white-black-w?country=US&currencyCode=USD&size=5.5W&srsltid=Ad5pg_E7dUbq4V7sKvjbmJcGwMRF8ob-GcyDubFOl6MTh37HT6Klt7Fcqpg, https://www.nike.com/t/blazer-mid-77-big-kids-shoes-4VfSTd/DA4086-100?nikemt=true&srsltid=Ad5pg_HzdTZQFL1DLJlxn5OfvMyUdHcTVlfx8L_vBg1rnUcbjKZXXcpahF4, https://www.dickssportinggoods.com/p/nike-kids-grade-school-blazer-mid-77-shoes-20nikyblzrwhtblckbys/20nikyblzrwhtblckbys?sku=21218417&srsltid=Ad5pg_FHd0GmGXt3QK0bGE1NaxoLO4iK-z359DpCnhI_lSO03cbR-Bqqb_8, https://www.kickscrew.com/products/nike-blazer-mid-77-vntg-white-black-bq6806-100?variant=40856089034947&currency=USD&srsltid=Ad5pg_FY5lUGMa80KyFXttklsGUB537vYc6ThXtKJUNpdjWSm2ZhO8y47TI"
      
