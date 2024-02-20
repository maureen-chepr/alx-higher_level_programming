#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const targetUrl = process.argv[2];
const filePath = process.argv[3];

request
  .get(targetUrl)
  .pipe(fs.createWriteStream(filePath));
