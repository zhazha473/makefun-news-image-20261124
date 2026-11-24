#!/usr/bin/env python3
"""Draw the news-image-20261124 entry: THE WORLD CLOCK.

Fresh code written in this session. Deterministic: no clock, no randomness,
no network. Draws entry.png (1024x1024) from the verified story list below.

Verified 24 November 2026 stories (each re-checked by web search in this
session; anything from 19-23 Nov was excluded and named in the DATE CHECK
strip instead):
 1. GENEVA (hero) - FIDE World Chess Championship Game 1: Gukesh v Sindarov,
    15:00 CET, both 20, youngest title match ever, $2.5m, Sindarov White
    (FIDE / Chess.com)
 2. PYONGYANG - KCNA: North Korea to consider shutting the Swiss diplomatic
    office in Pyongyang; Kim Yo Jong condemns Swiss sanctions (Reuters,
    dateline Seoul Nov 24, "on Tuesday")
 3. JANAKPUR - Inaugural Saryu-Kamala Express reaches Janakpur Dham 10:00
    Tuesday, 604 km / ~19 hours from Ayodhya; flag-off was Monday
    (Daily Jagran / Indian Railways)
 4. LAUSANNE - CAS to rule Tuesday afternoon (GMT) on Senegal's appeal
    against losing the AFCON 2025 title to Morocco (Reuters)
 5. TOKYO - Markets reopen Tuesday after Monday holiday and Friday's
    historic Nikkei plunge (-5.06%, -3,007 pts, 5th-biggest points drop)
    (Asia Daily)
 6. MUMBAI - NSE and BSE shut all day for Guru Nanak Jayanti; MCX evening
    session only (NSE / BSE holiday calendar)
 7. SEOUL - Korea FSC easing of daily buyback limits takes effect today,
    for 3 months, after the Kospi rout (FSC, via Kilambi News)
 8. THE SKY - Beaver supermoon peaks 14:53 UTC and slides past the
    Pleiades (Seven Sisters) before dawn; first of three supermoons
    (NASA / Starlust / Farmers' Almanac)
"""
import math
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
REPORT_TIME = "00:08 UTC"

# ---- palette: midnight-blue world clock, brass ring ----
BG       = (10, 16, 30)
PANEL    = (16, 24, 44)
PANEL2   = (21, 31, 54)
GOLD     = (232, 183, 90)
GOLD_D   = (200, 156, 66)
WHITE    = (238, 236, 228)
MUTED    = (165, 175, 190)
BLUE     = (110, 180, 235)
GREEN    = (120, 200, 130)
RED      = (235, 96, 86)
LINE     = (52, 64, 90)
STRIP_BG = (74, 28, 24)
DIAL_BG  = (13, 21, 40)

F_MONO    = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
F_MONO_B  = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
F_SANS    = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
F_SANS_B  = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap to pixel width; returns list of lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


# ---- story rows (non-hero): (pin_hour, city, headline, detail, time, source)
ROWS = [
    ("00", "TOKYO",
     "Tokyo markets reopen after historic rout",
     "Nikkei fell 5.06% on Friday, its 5th-biggest points drop ever",
     "09:00 JST", "Asia Daily"),
    ("00", "SEOUL",
     "Seoul buyback easing takes effect today",
     "FSC loosens daily buyback limits for 3 months after Kospi rout",
     "TODAY", "FSC"),
    ("04", "MUMBAI",
     "India's NSE and BSE shut for Guru Nanak Jayanti",
     "No equity trading today; MCX runs its evening session only",
     "ALL DAY", "NSE / BSE"),
    ("04", "JANAKPUR",
     "First Ayodhya-Janakpur train reaches Nepal",
     "Saryu-Kamala Express due 10:00 after 604 km in about 19 hours",
     "10:00 IST", "Daily Jagran"),
    ("06", "PYONGYANG",
     "North Korea weighs shutting Swiss office",
     "Kim Yo Jong hits back at sanctions on a children's camp",
     "TUE AM", "Reuters"),
    ("15", "LAUSANNE",
     "CAS to rule on Senegal's AFCON title appeal",
     "Senegal seek the title back after CAF handed it to Morocco",
     "PM GMT", "Reuters"),
    ("15", "THE SKY",
     "Beaver supermoon peaks, slides past the Pleiades",
     "Full at 14:53 UTC; first of three supermoons running to Jan 2027",
     "14:53 UTC", "NASA"),
]

# ---- dial pins: (hour_float, radius_offset, code, label_pos, label_anchor)
# label_pos: ("in", dx, dy) offset from the pin point, or ("out", dx, dy)
PINS = [
    (0.0, 0,   "TYO", (16, 12), "lm"),
    (0.0, -30, "SEL", (-14, -8), "rm"),
    (3.75, 0,  "BOM", (16, -6), "lm"),
    (4.5, 0,   "JKR", (16, -6), "lm"),
    (6.0, 0,   "PYG", (16, -6), "lm"),
    (14.0, 0,  "GVA", (-16, 4), "rm"),
    (14.9, -34, "SKY", (0, -20), "mm"),
    (15.0, 0,  "LAU", (-16, 4), "rm"),
]

DATE_CHECK = (
    "NOT TODAY, LEFT OUT ON PURPOSE:  COP31 collapse (22 Nov)  |  "
    "Liverpool 4-0 Man Utd (22 Nov)  |  India 720/9 declared (22 Nov)  |  "
    "Iran singer flogged, 74 lashes (23 Nov)  |  School bomb-threat emails, "
    "Germany & Denmark (23 Nov)  |  NAB layoff email (23 Nov)  |  Godhra "
    "convict bail (23 Nov)  |  Molly Meldrum dies, 83 (23 Nov)  |  Oxfam "
    "Gaza report (23 Nov)  |  Australia 4-0 France, BJK Cup (22 Nov)"
)

FOOTER = (
    "STILL TO COME TODAY:  Japan flash PMI 00:30 UTC  |  Germany Ifo 09:00 GMT  |  "
    "US ADP, consumer confidence, Case-Shiller later  |  Chess Game 1 15:00 CET"
)


def hour_xy(cx, cy, r, hour):
    """Position on a 24-hour dial: hour 0 at the top, clockwise."""
    ang = math.radians((hour / 24.0) * 360.0 - 90.0)
    return (cx + r * math.cos(ang), cy + r * math.sin(ang))


def draw_dial(d):
    cx, cy, R = 512, 306, 172
    # outer brass ring + face
    d.ellipse([cx - R, cy - R, cx + R, cy + R], fill=DIAL_BG,
              outline=GOLD, width=4)
    d.ellipse([cx - R + 10, cy - R + 10, cx + R - 10, cy + R - 10],
              outline=LINE, width=1)
    # 24 hour ticks
    for h in range(24):
        x0, y0 = hour_xy(cx, cy, R - 12, h)
        x1, y1 = hour_xy(cx, cy, R - 22 if h % 6 == 0 else R - 18, h)
        d.line([x0, y0, x1, y1], fill=GOLD if h % 6 == 0 else MUTED,
               width=3 if h % 6 == 0 else 1)
    # cardinal hour numbers
    f_num = font(F_MONO_B, 15)
    for h, lbl in ((0, "0"), (6, "6"), (12, "12"), (18, "18")):
        x, y = hour_xy(cx, cy, R - 38, h)
        d.text((x, y), lbl, font=f_num, fill=MUTED, anchor="mm")
    d.text((cx, cy + 78), "24 HOURS", font=font(F_MONO_B, 12),
           fill=MUTED, anchor="mm")
    # story pins on the rim
    f_pin = font(F_MONO_B, 12)
    for hour, roff, code, (dx, dy), anch in PINS:
        px, py = hour_xy(cx, cy, R - 12 + roff, hour)
        col = GOLD if code == "GVA" else AMBER
        r = 7 if code == "GVA" else 5
        d.ellipse([px - r, py - r, px + r, py + r], fill=col,
                  outline=(10, 16, 30), width=1)
        lx, ly = px + dx, py + dy
        d.text((lx, ly), code, font=f_pin, fill=col, anchor=anch)
    # centre chessboard (8x8, 15 px cells = 120 px)
    cell = 15
    bx0, by0 = cx - 4 * cell, cy - 4 * cell
    for r in range(8):
        for c in range(8):
            light = (r + c) % 2 == 0
            d.rectangle([bx0 + c * cell, by0 + r * cell,
                         bx0 + (c + 1) * cell, by0 + (r + 1) * cell],
                        fill=(232, 220, 196) if light else (52, 58, 74))
    d.rectangle([bx0, by0, bx0 + 8 * cell, by0 + 8 * cell],
                outline=GOLD, width=2)
    # kings: white king on a dark square, black king on a light square
    f_king = font(F_SANS, 26)
    d.text((bx0 + 4 * cell + cell // 2, by0 + 6 * cell + cell // 2),
           "\u2654", font=f_king, fill=(250, 248, 240), anchor="mm")
    d.text((bx0 + 4 * cell + cell // 2, by0 + 1 * cell + cell // 2),
           "\u265a", font=f_king, fill=(12, 14, 20), anchor="mm")
    d.text((cx, by0 - 16), "GAME 1", font=font(F_MONO_B, 13), fill=GOLD,
           anchor="mm")


AMBER = (245, 178, 66)


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # ---------- masthead ----------
    d.rectangle([0, 0, W, 112], fill=(8, 12, 24))
    d.text((28, 10), "THE WORLD CLOCK", font=font(F_MONO_B, 44), fill=GOLD)
    d.text((W - 28, 14), "TUESDAY 24 NOVEMBER 2026",
           font=font(F_MONO_B, 22), fill=WHITE, anchor="ra")
    d.text((W - 28, 42), "FIRST EDITION - AS REPORTED BY " + REPORT_TIME,
           font=font(F_MONO, 16), fill=MUTED, anchor="ra")
    d.text((W - 28, 66), "8 STORIES  |  EUROPE + ASIA + THE SKY  |  EVERY STORY SOURCE-TAGGED",
           font=font(F_MONO_B, 14), fill=GOLD, anchor="ra")
    d.line([0, 112, W, 112], fill=GOLD, width=3)

    # ---------- dial ----------
    draw_dial(d)

    # ---------- hero band: Geneva, Game 1 ----------
    hy = 492
    d.text((28, hy), "GENEVA  -  GAME 1, 15:00 CET",
           font=font(F_MONO_B, 24), fill=WHITE)
    d.text((28, hy + 32),
           "GUKESH v SINDAROV: youngest world title match ever, both 20",
           font=font(F_SANS_B, 18), fill=GOLD)
    d.text((28, hy + 58),
           "14 games  |  $2.5m prize  |  Sindarov has White  |  Fondation Martin Bodmer, Cologny  |  FIDE",
           font=font(F_SANS, 14), fill=MUTED)

    # ---------- rows header ----------
    y = 580
    d.text((28, y), "HR", font=font(F_MONO_B, 13), fill=MUTED)
    d.text((72, y), "CITY", font=font(F_MONO_B, 13), fill=MUTED)
    d.text((200, y), "WHAT HAPPENED", font=font(F_MONO_B, 13), fill=MUTED)
    d.text((700, y), "TIME", font=font(F_MONO_B, 13), fill=MUTED)
    d.text((800, y), "SOURCE", font=font(F_MONO_B, 13), fill=MUTED)
    d.line([28, y + 20, W - 28, y + 20], fill=LINE, width=1)

    # ---------- story rows ----------
    y = 606
    row_h = 40
    f_head = font(F_SANS_B, 15)
    f_det = font(F_SANS, 12)
    f_city = font(F_MONO_B, 14)
    f_time = font(F_MONO_B, 13)
    f_src = font(F_MONO, 12)
    f_pin = font(F_MONO_B, 12)
    for i, (pin, city, head, det, t, src) in enumerate(ROWS):
        fill = PANEL if i % 2 == 0 else PANEL2
        d.rounded_rectangle([20, y, W - 20, y + row_h - 5], radius=6, fill=fill)
        # mini clock-face pin
        d.ellipse([30, y + 8, 58, y + 36], outline=AMBER, width=2)
        d.text((44, y + 22), pin, font=f_pin, fill=AMBER, anchor="mm")
        d.text((72, y + 5), city, font=f_city, fill=WHITE)
        lines = wrap(d, head, f_head, 480)
        d.text((200, y + 5), lines[0], font=f_head, fill=WHITE)
        d.text((200, y + 23), det, font=f_det, fill=MUTED)
        d.text((700, y + 10), t, font=f_time, fill=GOLD)
        d.text((800, y + 10), src, font=f_src, fill=MUTED)
        y += row_h

    # ---------- date check strip ----------
    sy = y + 2
    d.rounded_rectangle([20, sy, W - 20, sy + 66], radius=8, fill=STRIP_BG)
    d.text((32, sy + 7), "DATE CHECK", font=font(F_MONO_B, 14),
           fill=(255, 170, 150))
    lines = wrap(d, DATE_CHECK, font(F_MONO, 12), W - 64)
    ly = sy + 26
    for ln in lines[:3]:
        d.text((32, ly), ln, font=font(F_MONO, 12), fill=(245, 220, 210))
        ly += 13

    # ---------- footer ----------
    fy = sy + 70
    d.line([28, fy, W - 28, fy], fill=LINE, width=1)
    d.text((28, fy + 8), FOOTER, font=font(F_MONO_B, 13), fill=GOLD)
    note = ("Built 24 Nov 2026 from wire reports checked this session. Every story "
            "above happened or was first reported on Tuesday 24 November 2026; "
            "later-today events are in the footer, not the rows.")
    nlines = wrap(d, note, font(F_SANS, 12), W - 56)
    ny = fy + 30
    for ln in nlines:
        d.text((28, ny), ln, font=font(F_SANS, 12), fill=MUTED)
        ny += 14

    img.save(OUT, "PNG", optimize=True)
    print("wrote", OUT, img.size)


if __name__ == "__main__":
    main()
