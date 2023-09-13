# E-Telligence-Crawler

## <a href="https://etelligenceapi.live">The E-Telligence API</a>
--was designed as part of a <a href="http://ischool.uw.edu/capstone/projects/2023/netprism-comparing-product-pricing-e-telligence-api">capstone project</a> for the University of Washington Information School featuring <a href="http://www.netprism.com">NetPrism LLC</a>, an e-commerce solutions company using web intelligence to deliver a catered product menu. The purpose of this project was to perform web-crawling in a fashion different to how most modern search engines crawl the web for product information. To see our final presentation and demo video, you can click <a href="https://youtu.be/AGd3WSaR9XQ?si=8D_SNsztSexAqjXU">here</a>.

Our API and algorithm works by beginning multiple web crawls from a conglomerate of meta-search engines. By browsing through top listing on shopping pages, we generate a large table of initial links this way. However, the uniqueness of our Python algorithm along with the capabilites of the <a href="https://scrapy.org">Scrapy</a> framework, we eliminate duplicate links, invalid listings, and pages with spam or pop-ups. 

The end goal of our API would be to deliver clean, product-related data in order to supply information for a product recommendation system, general e-commerce insights, or even price tracking data for other applications NetPrism would pursue.

This code based was developed by Ahmed Ghaddah, Matthew Ramirez, Andrew Jumanca, Christopher Ku, and Ryan Carroll.
