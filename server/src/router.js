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
  res.sendFile(__dirname + '/index.html');
  //res.send("Hello World");
});

module.exports = router;
