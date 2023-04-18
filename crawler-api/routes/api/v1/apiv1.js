import express from 'express';
import fetch from 'node-fetch';
import spawn from 'await-spawn';

var router = express.Router();

router.get('/', async (req, res) => {
  try {
    // run the python script
    const url = 'http://localhost:3000/api/v1/return?productName=';
    const query = req.query.productName;
    console.log(`Got ${query}`);
    try {
      const pythonProcess = await spawn('python', ['eTelligenceCrawler/crawl.py', query]);
    } catch (error) {
      console.log(error.stderr.toString());
    }
    try {
      console.log('Fetching from database...');
      const results = await fetch(url + query).then(resp => resp.json());
      res.json(results);
    } catch (error) {
      res.status(500).json({ 'status': 'failure', 'error': error});
      console.log(error);
    }
  } catch (error) {
    console.log(error); 
    res.status(500).send(error);
  }
});

/* POST Add data to database */
router.post('/send', async (req, res) => {
  try {
    const json = req.body;
    const newProduct = new req.models.Products({
      product_name: json.product_name,
      urls: json.urls
    })
    await newProduct.save();
    console.log('Saved to database');
    res.status(200).json({ 'status': 'success' });
  } catch (error) {
    console.log(error); 
    res.status(500).send(error);
  }
});

router.get('/return', async (req, res) => {
  try {
    let productName = req.query.productName;
    let products = await req.models.Products.findOne( { product_name: productName } );
    res.json({products});
  } catch (error) {
    console.log(error); 
    res.status(500).send(error);
  }
});

export default router;