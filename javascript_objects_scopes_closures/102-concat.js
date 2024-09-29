#!/usr/bin/node

const fs = require('fs');

const [sourceFile1, sourceFile2, destFile] = process.argv.slice(2);

fs.readFile(sourceFile1, 'utf8', (err, data1) => {
  if (err) {
    console.error(`Error reading ${sourceFile1}: ${err}`);
    return;
  }

  fs.readFile(sourceFile2, 'utf8', (err, data2) => {
    if (err) {
      console.error(`Error reading ${sourceFile2}: ${err}`);
      return;
    }

    fs.writeFile(destFile, data1 + data2, (err) => {
      if (err) {
        console.error(`Error writing to ${destFile}: ${err}`);
        return;
      }

      // Output the contents of the destination file
      console.log(data1 + data2);
    });
  });
});
