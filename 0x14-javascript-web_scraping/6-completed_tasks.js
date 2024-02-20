#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const todos = JSON.parse(body);
    const completedTasksByUser = {};

    for (const task of todos) {
      if (task.completed === true) {
        if (task.userId in completedTasksByUser) {
          completedTasksByUser[task.userId]++;
        } else {
          completedTasksByUser[task.userId] = 1;
        }
      }
    }

    console.log(completedTasksByUser);
  }
});
