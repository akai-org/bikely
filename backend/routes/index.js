const express = require('express');
const router = express.Router();

router.get('/', function (req, res, next) {
  const response = fetch('https://maps.nextbike.net/maps/nextbike.json?city=192,394')
  res.json({ ...response });
});

module.exports = router;
