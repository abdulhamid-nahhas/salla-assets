# ملصق باركود نون: Code128، مقاس 50x30 مم عند 300 dpi (591x354)
import barcode, io
from barcode.writer import ImageWriter
from PIL import Image, ImageDraw, ImageFont
CODE="NASCART001"
W,H=591,354
bc=barcode.get("code128",CODE,writer=ImageWriter())
buf=io.BytesIO()
bc.write(buf,options={"module_width":0.33,"module_height":16,"quiet_zone":2,"write_text":False,"dpi":300})
b=Image.open(buf).convert("L")
bw=W-40
b=b.resize((bw,int(b.height*bw/b.width)),Image.NEAREST) if b.width>bw else b
img=Image.new("L",(W,H),255)
d=ImageDraw.Draw(img)
bh=205
b=b.crop((0,0,b.width,b.height)).resize((b.width,bh),Image.NEAREST)
img.paste(b,((W-b.width)//2,28))
f=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf",52)
tw=d.textlength(CODE,font=f)
d.text(((W-tw)/2,250),CODE,font=f,fill=0)
img.convert("RGB").save("NASCART001-label-50x30mm.png",dpi=(300,300))
