// main.ts - runner for the LAST WILL AND TESTAMENT meme entry.
// Copies POST.json (which records the public X post URL) into
// MAKEFUN_OUTPUT_DIR and prints the recorded URL.
import {readFileSync, mkdirSync, writeFileSync} from 'node:fs';
import {URL} from 'node:url';

const postJsonUrl = new URL('./POST.json', import.meta.url);
const rawData = readFileSync(postJsonUrl, 'utf-8');
const postData = JSON.parse(rawData);

const outputDir = process.env.MAKEFUN_OUTPUT_DIR;
if (outputDir) {
  mkdirSync(outputDir, {recursive: true});
  writeFileSync(new URL('POST.json', `file://${outputDir}/`), rawData);
}

if (postData.url && typeof postData.url === 'string' && postData.url.trim() !== '') {
  console.log(postData.url);
} else {
  console.log('POST.json has no URL yet - fill in the public post URL before submitting.');
}
