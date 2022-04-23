import axios from 'axios';

const express = require('express');
const router = express.Router();


router.get('/', function (req, res, next) {

  const config = {
    method: 'get',
    url: 'https://api.geoapify.com/v1/geocode/search?text=38%20Upper%20Montagu%20Street%2C%20Westminster%20W1H%201LJ%2C%20United%20Kingdom&apiKey=f28181fa81514c0291007b444b415657',
    headers: {}
  };

  axios(config)
  .then(function (response) {
    console.log(response.data);
  })
  .catch(function (error) {
    console.log(error);
  });
});
