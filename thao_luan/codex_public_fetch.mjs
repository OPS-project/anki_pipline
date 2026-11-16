// Public AnkiWeb metadata/download only. No login, credentials, or persisted keys.
import {mkdir,writeFile,readdir} from 'node:fs/promises';
import {T} from '../research/inspection/anki_api_standalone.mjs';
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
for(const spec of process.argv.slice(2)){
 const [id,slug,mode]=spec.split(':');
 try{
  const data=await T({sharedId:Number(id)},{fetch:(u,o)=>fetch(new URL(u,'https://ankiweb.net'),o)});
  const v=JSON.parse(JSON.stringify(data)).available;
  if(!v){console.log(id,'unavailable');await sleep(3300);continue;}
  const safe={source:`https://ankiweb.net/shared/info/${id}`,date:new Date().toISOString(),downloaded_by:'Codex',title:v.title,updated:v.lastUpdated,size:v.size,description:v.description,supportUrl:v.supportUrl,notes:v.deck?.notes,audio:v.deck?.audio,images:v.deck?.images,sampleNotes:v.deck?.sampleNotes};
  const dir=new URL(`../chung/raw/${slug}/`,import.meta.url);
  await mkdir(dir,{recursive:true});
  if((await readdir(dir)).length){console.log(id,'directory not empty; skipped');await sleep(3300);continue;}
  await writeFile(new URL('_meta.json',dir),JSON.stringify(safe,null,2));
  console.log(JSON.stringify({id,title:v.title,size:v.size,notes:v.deck?.notes,audio:v.deck?.audio,images:v.deck?.images,updated:v.lastUpdated}));
  await sleep(3300);
  if(mode==='download'&&v.deck?.downloadKey){
   const r=await fetch(`https://ankiweb.net/svc/shared/download-deck/${id}?t=${encodeURIComponent(v.deck.downloadKey)}`);
   if(r.status===429){console.log(id,'429; stopped');break;}
   if(r.ok){const b=new Uint8Array(await r.arrayBuffer());if(b[0]===80&&b[1]===75){await writeFile(new URL('deck.apkg',dir),b);console.log(id,'downloaded',b.length);}else console.log(id,'download non-ZIP',r.status,b.length);}
   else console.log(id,'download status',r.status);
   await sleep(3300);
  }
 }catch(e){console.log(id,'request failed (detail omitted)');await sleep(10000);}
}
