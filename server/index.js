import express from 'express';
import router from './src/router';

const app = express();

let port = 8080;
app.listen(port, () => {
  console.log(' server is started and listen on port [' + port + ']');
});

//all the requests will be handled by routes middleware
app.use('/', router);
