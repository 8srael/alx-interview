#!/usr/bin/node

const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  request.get(`${API_URL}/films/${process.argv[2]}`, function (error, _, body) {
    if (error) {
      console.log(error);
    } else {
      const characters = JSON.parse(body).characters;

      for (const character of characters) {
        request.get(character, function (error, _, body) {
          if (error) {
            console.log(error);
          } else {
            console.log(JSON.parse(body).name);
          }
        });
      }
    }
  });
}
