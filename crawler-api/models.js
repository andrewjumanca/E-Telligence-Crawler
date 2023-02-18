import mongoose from "mongoose";

let models = {}
const uri = 'mongodb+srv://matthew:pa33word@crawler.0jer4eh.mongodb.net/test?authMechanism=DEFAULT';
const productSchema = {product_name: String, seller: String, price: String, URL: String};
const storageSchema = new mongoose.Schema({product_name: String, urls: [productSchema]});

try {
    await mongoose.connect(uri);
    console.log('Connected to Mongodb database');
} catch (error) {
    console.log(error);
}

models.Products = mongoose.model('Products', storageSchema);
console.log('Finished creating models');

export default models;