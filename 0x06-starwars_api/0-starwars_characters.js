#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    const characterPromises = characters.map((character) => {
      return new Promise((resolve, reject) => {
        request(character, function (error, response, body) {
          if (error) {
            reject(error);
          } else {
            resolve(JSON.parse(body).name);
          }
        });
      });
    });
    Promise.all(characterPromises).then((names) => {
      names.forEach((name) => {
        console.log(name);
      });
    }).catch((error) => {
      console.log(error);
    });
  }
});
