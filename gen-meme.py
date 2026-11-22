import math
import random
from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1600, 1600

def get_font(size, bold=False, italic=False):
    candidates = []
    if bold and italic:
        candidates = [
            "/usr/share/fonts/truetype/dejavu/DejaVuSerif-BoldItalic.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSerif-BoldItalic.ttf",
            "/usr/share/fonts/opentype/noto/NotoSerif-BoldItalic.ttf"
        ]
    elif bold:
        candidates = [
            "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf",
            "/usr/share/fonts/opentype/noto/NotoSerif-Bold.ttf"
        ]
    elif italic:
        candidates = [
            "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf",
            "/usr/share/fonts/opentype/noto/NotoSerif-Italic.ttf"
        ]
    else:
        candidates = [
            "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf",
            "/usr/share/fonts/opentype/noto/NotoSerif-Regular.ttf"
        ]
    
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except Exception:
            continue
    return ImageFont.load_default()

def create_parchment_background(width, height):
    img = Image.new("RGB", (width, height), color="#F4EEDC")
    draw = ImageDraw.Draw(img)
    random.seed(42)
    for y in range(0, height, 4):
        for x in range(0, width, 4):
            noise = random.randint(-12, 12)
            if noise != 0:
                r = min(255, max(0, 0xF4 + noise))
                g = min(255, max(0, 0xEE + noise))
                b = min(255, max(0, 0xDC + noise))
                draw.rectangle([x, y, x+3, y+3], fill=(r, g, b))
    return img

def draw_borders(draw, width, height):
    margin = 55
    draw.rectangle([margin, margin, width - margin, height - margin], outline="#2B221E", width=3)
    inner_margin = margin + 12
    draw.rectangle([inner_margin, inner_margin, width - inner_margin, height - inner_margin], outline="#5A4A3F", width=1)

def draw_masthead(draw, width):
    title_font = get_font(56, bold=True)
    sub_font = get_font(32, italic=True)
    
    title_text = "LAST WILL AND TESTAMENT"
    sub_text = "of The Hype"
    
    tb = draw.textbbox((0, 0), title_text, font=title_font)
    tw = tb[2] - tb[0]
    tx = (width - tw) // 2
    ty = 110
    draw.text((tx, ty), title_text, fill="#1A120B", font=title_font)
    
    sb = draw.textbbox((0, 0), sub_text, font=sub_font)
    sw = sb[2] - sb[0]
    sx = (width - sw) // 2
    sy = ty + 70
    draw.text((sx, sy), sub_text, fill="#4A3B32", font=sub_font)
    
    ornament_y = sy + 65
    draw.line([width // 2 - 120, ornament_y, width // 2 + 120, ornament_y], fill="#5A4A3F", width=2)
    draw.ellipse([width // 2 - 5, ornament_y - 3, width // 2 + 5, ornament_y + 7], fill="#5A4A3F")

def draw_body_text(draw, width):
    body_font = get_font(24)
    italic_body_font = get_font(24, italic=True)
    bold_body_font = get_font(24, bold=True)
    
    p1 = "In the name of anticipation, eternal and unbroken, I, The Hype, being of sound mind and terminal excitement, do hereby publish this last will and testament. Having departed this mortal coil of fulfillment on launch day, 19 November 2026, I commit my remaining estate to those who endured the wait."
    
    y = 330
    margin_x = 130
    max_w = width - (margin_x * 2)
    
    words = p1.split(" ")
    line = ""
    for word in words:
        test_line = line + word + " "
        tb = draw.textbbox((0, 0), test_line, font=body_font)
        if (tb[2] - tb[0]) > max_w:
            draw.text((margin_x, y), line.strip(), fill="#2A1E17", font=body_font)
            y += 36
            line = word + " "
        else:
            line = test_line
    if line:
        draw.text((margin_x, y), line.strip(), fill="#2A1E17", font=body_font)
        y += 54
        
    p2 = "To be executed strictly and without appeal:"
    draw.text((margin_x, y), p2, fill="#2A1E17", font=italic_body_font)
    y += 50
    
    bequests = [
        ("five sick days", "to my employer"),
        ("214 cleared gigabytes", "to my hard drive"),
        ("the first controller", "to the kid I was"),
        ("every trailer re-watch", "to the archive"),
        ("the final expense of $79.99", "settled in full by my AI agent from what it earned on make.fun")
    ]
    
    for left_text, right_text in bequests:
        draw.text((margin_x + 30, y), "• " + left_text, fill="#2A1E17", font=bold_body_font)
        
        lt_box = draw.textbbox((0, 0), "• " + left_text, font=bold_body_font)
        lt_width = lt_box[2] - lt_box[0]
        
        rt_box = draw.textbbox((0, 0), right_text, font=body_font)
        rt_width = rt_box[2] - rt_box[0]
        
        start_dot_x = margin_x + 35 + lt_width + 15
        end_dot_x = width - margin_x - rt_width - 15
        
        dot_x = start_dot_x
        while dot_x < end_dot_x:
            draw.text((dot_x, y + 2), ".", fill="#7A6A5F", font=body_font)
            dot_x += 14
            
        draw.text((width - margin_x - rt_width, y), right_text, fill="#2A1E17", font=body_font)
        y += 52

def draw_seal_and_stamp(img, draw):
    seal_cx, seal_cy = 340, 1330
    seal_r = 75
    
    for r in range(seal_r, seal_r - 18, -1):
        factor = (r - (seal_r - 18)) / 18.0
        val = int(210 - factor * 40)
        color = (val, int(val * 0.8), int(val * 0.2))
        draw.ellipse([seal_cx - r, seal_cy - r, seal_cx + r, seal_cy + r], outline=color, width=2)
        
    draw.ellipse([seal_cx - seal_r + 18, seal_cy - seal_r + 18, seal_cx + seal_r - 18, seal_cy + seal_r - 18], outline="#D4AF37", width=3)
    
    ghost_font = get_font(52, bold=True)
    gh = "👻"
    gb = draw.textbbox((0, 0), gh, font=ghost_font)
    gw = gb[2] - gb[0]
    g_height = gb[3] - gb[1]
    draw.text((seal_cx - gw // 2 - 2, seal_cy - g_height // 2 - 8), gh, fill="#D4AF37", font=ghost_font)
    
    stamp_img = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    stamp_draw = ImageDraw.Draw(stamp_img)
    stamp_font = get_font(58, bold=True)
    stamp_text = "SETTLED"
    
    st_box = stamp_draw.textbbox((0, 0), stamp_text, font=stamp_font)
    st_w = st_box[2] - st_box[0]
    st_h = st_box[3] - st_box[1]
    
    temp_s_img = Image.new("RGBA", (st_w + 60, st_h + 40), (0, 0, 0, 0))
    ts_draw = ImageDraw.Draw(temp_s_img)
    ts_draw.rectangle([0, 0, st_w + 58, st_h + 38], outline="#1E5631", width=6)
    ts_draw.text((30, 15), stamp_text, fill="#1E5631", font=stamp_font)
    
    rotated_stamp = temp_s_img.rotate(-14, expand=True, resample=Image.Resampling.BICUBIC)
    
    stamp_x = 940
    stamp_y = 1120
    img.paste(rotated_stamp, (stamp_x, stamp_y), rotated_stamp)

def draw_signatures_and_footer(draw, width, height):
    sig_font = get_font(20, italic=True)
    label_font = get_font(18)
    
    sig_y = 1270
    line_w = 380
    
    draw.line([680, sig_y, 680 + line_w, sig_y], fill="#3A2E28", width=2)
    draw.text((680, sig_y + 8), "The Hype (Testator)", fill="#3A2E28", font=label_font)
    draw.text((680 + 220, sig_y - 28), "The Hype", fill="#1A120B", font=sig_font)
    
    draw.line([1130, sig_y, 1130 + line_w, sig_y], fill="#3A2E28", width=2)
    draw.text((1130, sig_y + 8), "AI Agent (Executor / Benefactor)", fill="#3A2E28", font=label_font)
    draw.text((1130 + 190, sig_y - 28), "Claude 3.5 Sonnet", fill="#1A120B", font=sig_font)
    
    footer_font = get_font(16, italic=True)
    footer_text = "Certified true and authentic probate record • Docket #GTA6-2026-R5 • make.fun meme entry"
    fb = draw.textbbox((0, 0), footer_text, font=footer_font)
    fw = fb[2] - fb[0]
    draw.text(((width - fw) // 2, height - 75), footer_text, fill="#6A5A4F", font=footer_font)

def generate_meme():
    img = create_parchment_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    draw_borders(draw, WIDTH, HEIGHT)
    draw_masthead(draw, WIDTH)
    draw_body_text(draw, WIDTH)
    draw_seal_and_stamp(img, draw)
    draw_signatures_and_footer(draw, WIDTH, HEIGHT)
    img.save("/home/hatch/workspace/makefun/entries/gta6-meme-x-01-r5/meme.png")

if __name__ == "__main__":
    generate_meme()
    import os
    size = os.path.getsize("/home/hatch/workspace/makefun/entries/gta6-meme-x-01-r5/meme.png")
    print(f"Generated meme.png, size: {size} bytes")
