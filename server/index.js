import express from 'express';
import router from './src/router';

const app = express();

let port = 8080;
app.listen(port, () => {
  console.log(' server is started and listen on port [' + port + ']');
  console.log(`http://localhost:8080`);

});
app.use(express.static(__dirname + '/server'))


//all the requests will be handled by routes middleware
app.get('/', (request, response) => {
  response.sendFile(__dirname + 'index.html')
})