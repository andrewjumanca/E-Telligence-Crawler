import express from 'express';
import fetch from 'node-fetch';
import { spawn } from 'child_process';

var router = express.Router();

router.get('/', async (req, res) => {
  try {
    // run the python script
    const url = 'http://localhost:3000/api/v1/return?productName=';
    const query = req.query.productName;
    const pythonProcess = spawn('python3', ['hello.py', query]);
    for await (const data of pythonProcess.stdout) {
      console.log(`stdout from the pythonProcess: ${data}`);
    }
    // const results = await fetch(url + query).then(resp => resp.json());
    // console.log(results);
    // res.json(results);
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
    console.log('saved to database');
    // res.redirect('/return?productName=' + json.productName);
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