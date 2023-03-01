import mongoose from "mongoose";

let models = {}
const uri = 'mongodb+srv://admin:pa33word@crawler.0jer4eh.mongodb.net/test';
const productSchema = {product_name: String, seller: String, price: String, URL: String};

const storageSchema = new mongoose.Schema({product_name: String, urls: [String]});

try {
    await mongoose.connect(uri);
    console.log('Connected to Mongodb database');
} catch (error) {
    console.log(error);
}

models.Products = mongoose.model('Products', storageSchema);
console.log('Finished creating models');

export default models;