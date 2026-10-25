from pathlib import Path
import hashlib,re
root=Path(__file__).resolve().parents[1]
p=root/'index.html'
s=p.read_text()
for name in ('products.js','app.js','style.css'):
 digest=hashlib.sha256((root/name).read_bytes()).hexdigest()[:12]
 s=re.sub(re.escape('./'+name)+r'\?v=[a-f0-9]+','./'+name+'?v='+digest,s)
p.write_text(s)
