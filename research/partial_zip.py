import struct,zlib,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
for name in sys.argv[1:]:
 raw=(ROOT/'downloads'/name).read_bytes();pos=0;out=ROOT/'inspection'/(Path(name).stem+'_partial');out.mkdir(exist_ok=True)
 while raw[pos:pos+4]==b'PK\x03\x04':
  sig,ver,flags,method,tm,dt,crc,comp,uncomp,namelen,extra=struct.unpack_from('<I5H3I2H',raw,pos)
  fn=raw[pos+30:pos+30+namelen].decode('utf8',errors='replace');start=pos+30+namelen+extra
  print(name,fn,method,flags,comp,uncomp,'available',len(raw)-start)
  if not comp or comp==4294967295 or start+comp>len(raw):break
  body=raw[start:start+comp]
  if method==8:body=zlib.decompress(body,-15)
  if fn in ['collection.anki2','collection.anki21','collection.anki21b','media','meta']:(out/fn).write_bytes(body)
  pos=start+comp
