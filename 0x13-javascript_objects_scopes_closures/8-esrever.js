#!/usr/bin/node
exports.esrever = function (list) {
  const newVersion = [];
  for (let i = list.length - 1; i >= 0; i--) {
    newVersion.push(list[i]);
  }
  return newVersion;
};
