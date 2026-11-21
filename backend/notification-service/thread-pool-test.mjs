import { readFile } from 'node:fs/promises';
import { pbkdf2 } from 'node:crypto';
import { performance } from 'node:perf_hooks';

function runCrypto() {
  return new Promise((resolve, reject) => {
    pbkdf2('password', 'salt', 500000, 64, 'sha512', (error, key) => {
      if (error) reject(error);
      else resolve(key);
    });
  });
}

// Baseline measurement
let start = performance.now();

await readFile('test-file.txt', 'utf8');

console.log(
  `Baseline file read: ${(performance.now() - start).toFixed(2)} ms`
);

// Start four crypto operations without waiting
console.log('\nStarting 4 crypto operations...');

const cryptoStart = performance.now();

const cryptoJobs = [
  runCrypto(),
  runCrypto(),
  runCrypto(),
  runCrypto(),
];

// Immediately attempt a file read
start = performance.now();

await readFile('test-file.txt', 'utf8');

console.log(
  `File read during crypto: ${(performance.now() - start).toFixed(2)} ms`
);

// Wait for crypto operations to finish
await Promise.all(cryptoJobs);

console.log(
  `Crypto operations finished: ${(performance.now() - cryptoStart).toFixed(2)} ms`
);