import express from 'express';
import { promises as fs } from 'fs';

var router = express.Router();

/* GET JSON file and view it */
router.get('/', async (req, res) => {
  try {
    const json = await fs.readFile('./testResults.json');
    const results = JSON.parse(json);
    res.json(results)
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
    res.json({"status": "success"});
  } catch (error) {
    console.log(error); 
    res.status(500).send(error);
  }
});

export default router;