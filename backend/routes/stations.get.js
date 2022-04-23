const axios = require('axios')

const express = require('express');
const router = express.Router();

router.get('/', function (req, res, next) {

  const query = req.query;
  const { lng, lat, limit} = query

  const url = new URL('https://maps.nextbike.net/maps/nextbike.json?city=192,394');
  if (!lat || !lng || !limit) {
    res.sendStatus(400)
    res.end()
  } else {
    url.searchParams.append('lng', lng)
    url.searchParams.append('lat', lat)
    url.searchParams.append('limit', limit)


    axios({
      method: 'get',
      url: url.toString(),
      responseType: 'json'
    })
    .then(function (response) {
      const data = response.data
      if (data.countries[0]) {
        const station = [
          ...data.countries[0].cities.map((city) => {
            return city.places
          })
        ].flat(Infinity)
        res.json(station)
      }
      else {
        res.json({})
      }
    }).catch((err) => console.log(err));
  }
});

module.exports = router;
