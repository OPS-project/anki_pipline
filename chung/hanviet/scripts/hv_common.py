"""Hàm dùng chung cho mọi script Hán Việt (điều phối viết; agent KHÔNG sửa, cần đổi thì báo).

reading_key(s): khóa so khớp âm Hán Việt, bỏ khác biệt chính tả:
  - vị trí dấu thanh (hoà/hòa, thuỷ/thủy), hoa/thường
  - i/y cuối âm sau phụ âm (kì/kỳ, lí/lý, mĩ/mỹ); giữ 'y' đứng một mình hoặc đầu âm (y, yên)
  Kết quả: phần chữ không dấu thanh (vẫn giữ ă â ê ô ơ ư đ) + số thanh 1..6
  (1 ngang, 2 huyền, 3 hỏi, 4 ngã, 5 sắc, 6 nặng).
display(s): chuẩn hiển thị: chữ thường, NFC, dấu kiểu thông dụng (hòa, thủy, quý), i/y theo nguồn.
"""
import unicodedata, re

TONE_MARKS = {"̀": 2, "̉": 3, "̃": 4, "́": 5, "̣": 6}
MARK_OF = {v: k for k, v in TONE_MARKS.items()}
VOWELS = "aăâeêioôơuưy"


def split_tone(s: str):
    d = unicodedata.normalize("NFD", s.strip().lower())
    tone = 1
    out = []
    for ch in d:
        if ch in TONE_MARKS:
            tone = TONE_MARKS[ch]
        else:
            out.append(ch)
    return unicodedata.normalize("NFC", "".join(out)), tone


def reading_key(s: str) -> str:
    base, tone = split_tone(s)
    if len(base) > 1 and base.endswith("y") and (base[-2] not in VOWELS or base == "quy"):
        base = base[:-1] + "i"
    return f"{base}{tone}"


def _tone_pos(base: str) -> int:
    """Vị trí đặt dấu kiểu mới."""
    idx = [i for i, c in enumerate(base) if c in VOWELS]
    if not idx:
        return -1
    # gi/qu đầu âm: bỏ nguyên âm đầu khỏi nhóm nếu còn nguyên âm khác
    if base.startswith(("gi", "qu")) and len(idx) > 1 and idx[0] == 1:
        idx = idx[1:]
    for i in idx:
        if base[i] in "ăâêôơư":
            return i if base[i] != "ư" or not (i + 1 < len(base) and base[i + 1] == "ơ") else i + 1
    group_end_consonant = idx[-1] < len(base) - 1
    if len(idx) == 1:
        return idx[0]
    if group_end_consonant:
        return idx[-1]
    # nguyên âm mở cuối (không phụ âm cuối): dấu ở nguyên âm áp chót, kiểu thông dụng: hòa, thủy, mía
    return idx[-2]


def display(s: str) -> str:
    base, tone = split_tone(s)
    if tone == 1:
        return base
    p = _tone_pos(base)
    if p < 0:
        return base
    d = unicodedata.normalize("NFD", base[: p + 1]) + MARK_OF[tone]
    return unicodedata.normalize("NFC", d + base[p + 1:])


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    for a, b in [("thuỷ", "thủy"), ("hoà", "hòa"), ("kì", "kỳ"), ("lí", "lý"), ("ki", "ky"), ("quý", "quí"), ("y", "y")]:
        print(a, b, reading_key(a), reading_key(b), reading_key(a) == reading_key(b), display(a), display(b))
