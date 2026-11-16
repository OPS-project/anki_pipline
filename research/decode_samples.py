from pathlib import Path
import subprocess,re,json,concurrent.futures
import imageio_ffmpeg
ROOT=Path(__file__).resolve().parent
exe=imageio_ffmpeg.get_ffmpeg_exe()
paths=list((ROOT/'inspection').glob('*/sample_*'))
def decode(p):
 r=subprocess.run([exe,'-hide_banner','-i',str(p),'-f','null','-'],stdout=subprocess.DEVNULL,stderr=subprocess.PIPE,encoding='utf8',errors='replace')
 duration=re.search(r'Duration:\s+(\d+):(\d+):([\d.]+)',r.stderr)
 if duration:duration=round(int(duration[1])*3600+int(duration[2])*60+float(duration[3]),3)
 return {'file':str(p.relative_to(ROOT)),'decoded':r.returncode==0,'duration_s':duration,'error':r.stderr[-500:]if r.returncode else ''}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:results=list(ex.map(decode,paths))
(ROOT/'inspection/audio_decode_audit.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf8')
print('Decoded',sum(r['decoded']for r in results),'of',len(results));print([r for r in results if not r['decoded']])
