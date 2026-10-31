# ورقة A4 فيها 12 ملصق NASCART001 (3×4) مقاس 50×30 مم، 300 dpi، بإطار قص رفيع
from PIL import Image, ImageDraw
L=Image.open("NASCART001-label-50x30mm.png").convert("RGB")
W,H=2480,3508; w,h=L.size; cols,rows=3,4; gap=40
x0=(W-(cols*w+(cols-1)*gap))//2; y0=(H-(rows*h+(rows-1)*gap))//2
P=Image.new("RGB",(W,H),"white"); d=ImageDraw.Draw(P)
for r in range(rows):
    for c in range(cols):
        x=x0+c*(w+gap); y=y0+r*(h+gap)
        P.paste(L,(x,y)); d.rectangle([x,y,x+w-1,y+h-1],outline=(190,190,190),width=2)
P.save("NASCART001-A4-12-labels.pdf",resolution=300)
