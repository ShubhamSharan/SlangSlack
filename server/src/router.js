import path from 'path';
import { RequestHandlerService } from './services/RequestHandlerService';

const express = require('express');
const router = express.Router();

router.get('/*', (req, res, next) => {
  // Run it before all of the URL
  next();
});

/**
 * default routes re-direct to products
 */

router.get('/', (req, res) => {
  console.log("Should hit ");
  res.sendFile(path.join(__dirname,'index.html'))
});

module.exports = router;
