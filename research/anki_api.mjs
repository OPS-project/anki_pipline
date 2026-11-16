import {readFile,writeFile} from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const root=path.dirname(fileURLToPath(import.meta.url));
const source=await readFile(path.join(root,'inspection','anki_frontend.mjs'),'utf8');
await writeFile(path.join(root,'inspection','anki_api_standalone.mjs'),source.replace(/^import[^;]+;/,'const $e=Error, We=Error; const x=()=>{};'));
const api=await import('./inspection/anki_api_standalone.mjs');
for(const sid of process.argv.slice(2)){
 try{
  const data=await api.T({sharedId:sid},{fetch:(url,opts)=>fetch(new URL(url,'https://ankiweb.net'),opts)});
  const plain=JSON.parse(JSON.stringify(data));
  await writeFile(path.join(root,'inspection',`anki_${sid}.json`),JSON.stringify(plain,null,2));
  const v=plain.available;
  console.log(JSON.stringify({sid,status:v?'available':'missing',title:v?.title,size:v?.size,updated:v?.lastUpdated,notes:v?.deck?.notes,audio:v?.deck?.audio,images:v?.deck?.images,support:v?.supportUrl}));
 }catch(e){console.log(JSON.stringify({sid,error:e.message}));}
}
