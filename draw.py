#!/usr/bin/env python3
"""Draw the front page for make.fun news-image-20261123.

Programmatic drawing only (Python + PIL): masthead, headlines and small
drawn illustrations. No AI-generated pictures, no photographs, no invented
facts. Every line on the page was verified against a reputable outlet on
23 November 2026; the sources are listed in README.md.

Deterministic: fixed text, fixed geometry, no randomness, no clock.
Run:  python3 draw.py   -> writes entry.png next to this file.
"""

import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 242, 231)      # newsprint cream
INK = (20, 20, 20)           # near-black
RED = (178, 34, 34)          # headline red
BLUE = (38, 70, 110)         # deep blue for art
GREY = (110, 108, 100)       # secondary text
RULE = (20, 20, 20)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap to a pixel width; returns list of lines."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(draw, x, y, text, fnt, width, fill=INK, leading=None):
    lines = wrap(draw, text, fnt, width)
    lh = leading or int(fnt.size * 1.28)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += lh
    return y


def hline(draw, y, x0, x1, width=2, fill=RULE):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


# ---------------------------------------------------------------- icons
def icon_capitol(draw, x, y, s):
    """US Capitol dome, simplified, on a pale blue panel."""
    draw.rectangle([x, y, x + s, y + s], fill=(214, 226, 238))
    cx = x + s // 2
    # dome
    draw.pieslice([cx - 26, y + 12, cx + 26, y + 64], 180, 360, fill=(250, 250, 250),
                  outline=INK, width=2)
    draw.rectangle([cx - 3, y + 4, cx + 3, y + 16], fill=INK)
    # small flag on the finial
    draw.polygon([(cx + 3, y + 2), (cx + 15, y + 6), (cx + 3, y + 10)], fill=RED)
    # drum + base
    draw.rectangle([cx - 30, y + 62, cx + 30, y + 70], fill=(250, 250, 250),
                   outline=INK, width=2)
    draw.rectangle([cx - 38, y + 70, cx + 38, y + s - 14], fill=(250, 250, 250),
                   outline=INK, width=2)
    for i in range(5):
        px = cx - 30 + i * 15
        draw.line([(px, y + 74), (px, y + s - 18)], fill=INK, width=2)
    draw.rectangle([cx - 44, y + s - 14, cx + 44, y + s - 8], fill=INK)


def icon_ship(draw, x, y, s):
    """Warship at sea with an explosion burst above it."""
    draw.rectangle([x, y, x + s, y + s], fill=(206, 224, 232))
    # sea
    draw.rectangle([x, y + s - 26, x + s, y + s], fill=(70, 120, 160))
    for wx in range(x + 6, x + s - 6, 18):
        draw.arc([wx, y + s - 22, wx + 14, y + s - 12], 0, 180, fill=(220, 235, 245),
                 width=2)
    # hull
    draw.polygon([(x + 12, y + s - 44), (x + s - 10, y + s - 44),
                  (x + s - 24, y + s - 26), (x + 26, y + s - 26)],
                 fill=(60, 60, 66), outline=INK)
    # superstructure + mast
    draw.rectangle([x + s // 2 - 16, y + s - 66, x + s // 2 + 16, y + s - 44],
                   fill=(90, 90, 96), outline=INK)
    draw.line([(x + s // 2, y + s - 66), (x + s // 2, y + s - 82)], fill=INK, width=3)
    # explosion burst
    cx, cy = x + s - 30, y + 26
    for r, col in ((26, (255, 200, 60)), (18, (255, 140, 40)), (10, (220, 60, 30))):
        pts = []
        for k in range(12):
            import math
            ang = math.pi * k / 6
            rr = r if k % 2 == 0 else r * 0.55
            pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
        draw.polygon(pts, fill=col, outline=INK)


def icon_gavel(draw, x, y, s):
    """A gavel on a pale tan panel."""
    draw.rectangle([x, y, x + s, y + s], fill=(238, 226, 204))
    # handle (diagonal)
    draw.line([(x + 22, y + s - 22), (x + s - 34, y + 30)], fill=(120, 72, 30), width=9)
    # head
    draw.polygon([(x + s - 52, y + 14), (x + s - 14, y + 30),
                  (x + s - 30, y + 62), (x + s - 68, y + 46)],
                 fill=(150, 96, 44), outline=INK)
    draw.line([(x + s - 52, y + 14), (x + s - 30, y + 62)], fill=INK, width=2)
    # sound block
    draw.rectangle([x + 18, y + s - 34, x + 58, y + s - 22], fill=(120, 72, 30),
                   outline=INK)


def icon_badge(draw, x, y, s):
    """A gold five-point star badge."""
    import math
    draw.rectangle([x, y, x + s, y + s], fill=(232, 232, 226))
    cx, cy = x + s // 2, y + s // 2 + 2
    pts = []
    for k in range(10):
        ang = -math.pi / 2 + k * math.pi / 5
        rr = 42 if k % 2 == 0 else 18
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    draw.polygon(pts, fill=(212, 168, 40), outline=INK)
    draw.ellipse([cx - 9, cy - 9, cx + 9, cy + 9], fill=(247, 242, 231), outline=INK)
    draw.text((cx - 4, cy - 8), "★", font=font(SANS_B, 14), fill=INK)


def icon_skyline(draw, x, y, s):
    """City blocks under a smoky sky."""
    draw.rectangle([x, y, x + s, y + s], fill=(226, 222, 214))
    # smoke
    for (sx, sy, sr) in ((x + 30, y + 18, 12), (x + 48, y + 12, 15),
                         (x + 66, y + 20, 11), (x + s - 34, y + 16, 13)):
        draw.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=(150, 148, 142))
    base = y + s - 12
    for (bx, bw, bh) in ((x + 6, 22, 46), (x + 32, 26, 66), (x + 62, 20, 52),
                         (x + 86, 24, 74)):
        draw.rectangle([bx, base - bh, bx + bw, base], fill=(52, 52, 58), outline=INK)
        for wy in range(base - bh + 8, base - 6, 12):
            for wx in range(bx + 5, bx + bw - 4, 9):
                draw.rectangle([wx, wy, wx + 4, wy + 5], fill=(250, 210, 90))


def lead_art(draw, x, y, w, h):
    """Cracked dry earth under a pale sun: the climate talks fail."""
    draw.rectangle([x, y, x + w, y + h], fill=(233, 224, 203))
    # sun with rays
    import math
    sx, sy = x + w - 62, y + 52
    for k in range(12):
        ang = k * math.pi / 6
        draw.line([(sx + 34 * math.cos(ang), sy + 34 * math.sin(ang)),
                   (sx + 48 * math.cos(ang), sy + 48 * math.sin(ang))],
                  fill=(200, 150, 60), width=3)
    draw.ellipse([sx - 30, sy - 30, sx + 30, sy + 30], fill=(240, 190, 80),
                 outline=(200, 150, 60), width=2)
    # horizon + cracked ground
    hy = y + h - 84
    draw.rectangle([x, hy, x + w, y + h], fill=(196, 158, 104))
    draw.line([(x, hy), (x + w, hy)], fill=INK, width=2)
    # cracks
    cracks = [((x + 30, hy + 6), (x + 58, hy + 34), (x + 48, hy + 62), (x + 70, hy + 80)),
              ((x + 120, hy + 4), (x + 138, hy + 30), (x + 128, hy + 58)),
              ((x + 210, hy + 8), (x + 188, hy + 36), (x + 200, hy + 66), (x + 186, hy + 80)),
              ((x + 270, hy + 4), (x + 258, hy + 40), (x + 276, hy + 72))]
    for pts in cracks:
        draw.line(pts, fill=(90, 60, 30), width=3, joint="curve")
    # a small wilted sapling
    draw.line([(x + 96, hy), (x + 96, hy - 34)], fill=(90, 110, 60), width=3)
    draw.line([(x + 96, hy - 34), (x + 78, hy - 48)], fill=(90, 110, 60), width=3)
    draw.line([(x + 96, hy - 30), (x + 114, hy - 44)], fill=(90, 110, 60), width=3)


# ---------------------------------------------------------------- page
def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 30                      # page margin
    X0, X1 = M, W - M

    # frame
    d.rectangle([14, 14, W - 15, H - 15], outline=INK, width=2)

    # ---- masthead
    mast = font(SERIF_B, 66)
    d.text(((W - d.textlength("THE WORLD TODAY", font=mast)) / 2, 30),
           "THE WORLD TODAY", font=mast, fill=INK)
    hline(d, 112, X0, X1, 3)
    hline(d, 118, X0, X1, 1)

    # ---- dateline row
    d.text((X0, 128), "MONDAY 23 NOVEMBER 2026", font=font(SANS_B, 22), fill=INK)
    right = "SIX STORIES  ·  ONE DAY"
    d.text((X1 - d.textlength(right, font=font(SANS, 18)), 132), right,
           font=font(SANS, 18), fill=GREY)
    hline(d, 160, X0, X1, 1)

    # ---- lead story: COP31
    d.text((X0, 172), "CLIMATE  ·  ANTALYA, TURKEY", font=font(SANS_B, 20), fill=RED)
    head = font(SERIF_B, 56)
    d.text((X0, 198), "COP31 COLLAPSES", font=head, fill=INK)
    d.text((X0, 256), "WITHOUT A DEAL", font=head, fill=INK)
    deck = ("Nearly 200 countries leave the U.N. climate talks in Antalya "
            "with no deal, after two days of overtime rows over fossil fuels.")
    draw_wrapped(d, X0, 326, deck, font(SERIF, 24), 600, leading=30)
    lead_art(d, 668, 172, 326, 222)

    hline(d, 424, X0, X1, 3)

    # ---- four-story grid
    stories = [
        ("U.S. POLITICS", "DEMOCRATS SEIZE THE HOUSE",
         "258 seats — the biggest House majority since 1992 — as the final "
         "counts come in.", icon_capitol),
        ("WAR  ·  MEDITERRANEAN", "WARSHIP SUNK OFF LIBYA",
         "Suspected Ukrainian sea drones hit the Russian corvette Merkury "
         "at Benghazi; a second ship is struck.", icon_ship),
        ("AFRICA  ·  G20", "G20 ENDS IN GAVEL ROW",
         "Ramaphosa refuses to hand the presidency to a junior U.S. "
         "official as the Johannesburg summit closes.", icon_gavel),
        ("LATIN AMERICA", "MEXICO NABS TOP KINGPIN",
         "A fugitive on the FBI's most-wanted list is captured in a deadly "
         "firefight, officials say.", icon_badge),
    ]
    cell_w, cell_h = 472, 196
    gx, gy = X0, 440
    for i, (kick, title, deck_text, icon) in enumerate(stories):
        cx = gx + (i % 2) * (cell_w + 20)
        cy = gy + (i // 2) * (cell_h + 14)
        icon(d, cx, cy + 8, 112)
        tx = cx + 126
        d.text((tx, cy + 6), kick, font=font(SANS_B, 16), fill=RED)
        ty = draw_wrapped(d, tx, cy + 28, title, font(SERIF_B, 26),
                          cell_w - 126, leading=30)
        draw_wrapped(d, tx, ty + 2, deck_text, font(SERIF, 19),
                     cell_w - 126, leading=24)

    hline(d, 852, X0, X1, 2)

    # ---- Kyiv band
    icon_skyline(d, X0, 868, 112)
    tx = X0 + 126
    d.text((tx, 866), "UKRAINE", font=font(SANS_B, 16), fill=RED)
    d.text((tx, 886), "KYIV REGION HIT — SIX DEAD",
           font=font(SERIF_B, 26), fill=INK)
    draw_wrapped(d, tx, 918, "Russian strikes kill six and leave 14 missing after a "
                 "drone hits a block of flats, Ukraine says.",
                 font(SERIF, 19), X1 - tx, leading=24)

    hline(d, 962, X0, X1, 1)

    # ---- footer briefs + sources
    foot = ("ALSO TODAY:  Dozens missing after a factory fire in Indonesia  ·  "
            "U.S. presses Nvidia over chip sales to China")
    draw_wrapped(d, X0, 972, foot, font(SANS, 17), X1 - X0, fill=GREY, leading=21)

    img.save("entry.png", optimize=True)
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
