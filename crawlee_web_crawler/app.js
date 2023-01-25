// Cheerio Crawler:
// This is a plain HTTP crawler. It parses HTML using the Cheerio library and crawls the web using the
// specialized got-scraping HTTP client which masks as a browser. It's very fast and efficient, but can't handle JavaScript rendering.

import { CheerioCrawler, Dataset } from 'crawlee';

// CheerioCrawler crawls the web using HTTP requests
// and parses HTML using the Cheerio library.
const crawler = new CheerioCrawler({
    // Use the requestHandler to process each of the crawled pages.
    async requestHandler({ request, $, enqueueLinks, log }) {
        const title = $('title').text();
        log.info(`Title of ${request.loadedUrl} is '${title}'`);

        // Save results as JSON to ./storage/datasets/default
        await Dataset.pushData({ title, url: request.loadedUrl });

        // Extract links from the current page
        // and add them to the crawling queue.
        await enqueueLinks();
    },
});

// Add first URL to the queue and start the crawl.
const url = 'https://en.wikipedia.org/wiki/Kanye_West';
await crawler.run([url]);