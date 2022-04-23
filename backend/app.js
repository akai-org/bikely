const express = require('express');
const logger = require('morgan');

const stations = require('./routes/stations.get');

const app = express();

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

app.use('/stations', stations);

app.listen(3001)
