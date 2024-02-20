#!/usr/bin/node

const request = require('request');
const targetUrl = process.argv[2];

request
  .get(targetUrl)
  .on('response', function (response) {
    console.log('code:', response.statusCode);
  });
