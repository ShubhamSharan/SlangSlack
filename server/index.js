import express from 'express';
import router from './src/router';
import path from 'path';

const app = express();

let port = 8080;
app.listen(port, () => {
  console.log(' server is started and listen on port [' + port + ']');
  console.log(`http://localhost:8080`);

});
app.use(express.static(path.join(__dirname ,'assets')))
app.use(express.static(path.join(__dirname ,'images')))

//all the requests will be handled by routes middleware
app.get('/', router)