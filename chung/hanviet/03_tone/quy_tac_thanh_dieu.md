# Quy tắc thanh điệu Hán Việt → Mandarin (số đo, kiểm lại được)

Người làm: Sonnet. Dữ liệu: `tone_rule_table.csv` (từng ô), `tone_rule_items.csv` (từng chữ), `tone_rule_summary.json`. Tái lập: `scripts/tone_rule_measure.py <Unihan.zip> 00_base/chars.txt 03_tone`.

## 1. Định nghĩa
- **Thanh Hán Việt**: lấy từ dấu thanh của âm HV trong `kVietnamese`: ngang, huyền, hỏi, ngã, sắc, nặng.
- **Nhập thanh**: âm HV tận cùng bằng `-p`, `-t`, `-c`, `-ch` (suy từ chính tả, sau khi bỏ dấu). Âm như vậy chỉ mang sắc hoặc nặng, nên ô "nhập" chỉ có ở hai thanh này.
- **Phụ âm vang** (cột `vang`): âm HV bắt đầu bằng m, n, nh, ng/ngh, l, v, d, gi, y, hoặc bằng nguyên âm (a, e, i, o, u, y, kể cả có dấu mũ/móc).
- **Phụ âm tắc** (cột `tac`): mọi âm còn lại: b, c/k/q, ch, đ, g, h, kh, p, ph, r, s, t, th, tr, x. Tên "tắc" chỉ là nhãn gọn; nhóm này gồm cả âm xát (h, kh, ph, s, x, th, r...). Chữ `đ` được xếp vào nhóm này, `d` thì vào nhóm vang.
- **Thanh Mandarin**: thanh của `kMandarin` (T1 āēīōū, T2 áéíóú, T3 ǎěǐǒǔ, T4 àèìòù; không có dấu = T5).

## 2. Tập đo
Một chữ được đo khi: có `kVietnamese` (trực tiếp, hoặc qua `kTraditionalVariant` của chữ đó, lấy chữ phồn thể đầu tiên có `kVietnamese`), **đúng một** âm HV, và **đúng một** `kMandarin`. Tập chữ lấy từ `00_base/chars.txt` (chữ CJK trong trường `hanzi`, 3.088 chữ khác nhau). Unihan: `Unihan.zip` (Unihan_Readings.txt, Unihan_Variants.txt).

Kết quả: **2.077 / 3.088 chữ (67,3%)** được đo; 636 trong số này lấy âm HV qua chữ phồn thể.

Loại theo lý do (tổng 1.011): không có `kVietnamese` 947; có nhiều hơn một âm HV 49; có nhiều hơn một `kMandarin` 15; không có `kMandarin` 0. (Lý do xét theo thứ tự trên, mỗi chữ tính một lần.)

| Cấp (theo xuất hiện sớm nhất) | Chữ trong deck | Được đo | Không có kVietnamese | Nhiều âm HV | Nhiều kMandarin |
|---|---|---|---|---|---|
| HSK1 | 248 | 208 | 31 | 7 | 2 |
| HSK2 | 123 | 102 | 17 | 2 | 2 |
| HSK3 | 284 | 225 | 53 | 4 | 2 |
| HSK4 | 441 | 340 | 95 | 5 | 1 |
| HSK5 | 431 | 327 | 95 | 7 | 2 |
| HSK6 | 413 | 272 | 126 | 14 | 1 |
| HSK7-9 | 1.148 | 603 | 530 | 10 | 5 |
| Tổng | 3.088 | 2.077 | 947 | 49 | 15 |

Chữ càng ở cấp cao càng thiếu dữ liệu (HSK7-9 chỉ đo được 52,5%).

## 3. Bảng quy tắc rút gọn
Số đếm đầy đủ T1–T5 nằm trong `tone_rule_table.csv`. Cột "dùng được" theo tiêu chí mục 5 (tỷ lệ ≥80% và n ≥30).

| Thanh HV | Phụ âm đầu | Nhập thanh | n | Thanh Mandarin phổ biến nhất | Tỷ lệ | Dùng được |
|---|---|---|---|---|---|---|
| ngang | tắc | không | 350 | T1 (310) | 88,6% | có |
| ngang | vang | không | 198 | T2 (140), T1 49 | 70,7% | không |
| huyền | tắc | không | 247 | T2 (200) | 81,0% | có |
| huyền | vang | không | 40 | T2 (14), T4 11, T1 9 | 35,0% | không |
| hỏi | tắc | không | 188 | T3 (161) | 85,6% | có |
| hỏi | vang | không | 30 | T3 (19), T4 8 | 63,3% | không |
| ngã | tắc | không | 39 | T4 (21), T3 15 | 53,8% | không |
| ngã | vang | không | 71 | T3 (62) | 87,3% | có |
| sắc | tắc | không | 249 | T4 (193), T3 42 | 77,5% | không |
| sắc | tắc | nhập | 163 | T4 (53), T1 51, T2 43 | 32,5% | không |
| sắc | vang | không | 62 | T4 (34) | 54,8% | không |
| sắc | vang | nhập | 32 | T1 (14), T4 12 | 43,8% | không |
| nặng | tắc | không | 149 | T4 (136) | 91,3% | có |
| nặng | tắc | nhập | 93 | T2 (62), T4 22 | 66,7% | không |
| nặng | vang | không | 96 | T4 (79) | 82,3% | có |
| nặng | vang | nhập | 70 | T4 (65) | 92,9% | có |

Bảy ô "có" gộp 1.171 chữ (56% tập đo); trong đó thanh phổ biến nhất khớp 1.013 chữ (86,5%). Toàn tập đo: đoán theo thanh phổ biến nhất của từng ô khớp 1.563 / 2.077 (75,3%); quy tắc đơn giản không chia ô (ngang→T1, huyền→T2, hỏi→T3, ngã→T3 hoặc T4, sắc/nặng→T4) khớp 1.450 / 2.077 (69,8%). Cả hai là số **trong mẫu**: các ô và ngưỡng chọn sau khi nhìn dữ liệu nên tỷ lệ có thể lạc quan hơn so với chữ mới.

Nhận xét ngắn: thanh ngang mà phụ âm vang không theo T1 mà nghiêng T2 (70,7%); sắc nhập thanh rải khá đều T1–T4 nên không dùng được; chỉ nặng-nhập-vang nghiêng rõ về T4.

## 4. Giới hạn bắt buộc
1. Unihan thiếu khoảng 30% chữ của deck (947/3.088 = 30,7% không có `kVietnamese`, phần lớn là chữ giản thể không nối được sang chữ phồn thể có âm HV, và chữ hiếm ở cấp cao). Thiếu này không ngẫu nhiên: tập đo nghiêng về chữ thường gặp.
2. `kMandarin` là một cách đọc phổ biến của chữ, **không** phải cách đọc trong từ cụ thể (đa âm, thanh nhẹ, biến điệu 不/一, biến điệu thanh 3 không được phản ánh).
3. Phân lớp phụ âm đầu theo chính tả Việt chỉ là xấp xỉ (âm HV phản ánh một tầng lịch sử khác với phụ âm Quan thoại); "tắc" gồm cả âm xát.
4. "Nhập thanh" suy từ phụ âm cuối chính tả (-p, -t, -c, -ch), không có thông tin trực tiếp về thanh trung cổ.
5. Tỷ lệ chỉ đúng cho **tập đo** (2.077 chữ, thiên về chữ thường gặp, một âm HV, một kMandarin). Không được suy ra tỷ lệ cho toàn deck hay cho chữ ngoài tập đo.
6. Đoán đúng số thanh của chữ ≠ phát âm đúng thanh trong câu: biến điệu (thanh 3 liên tiếp, 不, 一), thanh nhẹ và ngữ lưu làm thanh thật trong lời nói khác thanh gốc.
7. Chữ có nhiều âm HV (49 chữ) hoặc nhiều kMandarin (15 chữ) đã bị loại, nên chưa có số đo cho các chữ đa âm.

## 5. Đề xuất điều kiện gắn nhãn "ngoại lệ"
Gắn nhãn "ngoại lệ thanh điệu" cho một chữ trong một từ **chỉ khi tất cả** các điều kiện sau đúng:
1. Âm HV của chữ đã chọn chắc chắn: có đúng một ứng viên có nguồn (không phải suy đoán, không còn nhiều âm).
2. Thanh Mandarin lấy theo pinyin **của từ** (`word_pinyin`), không lấy `kMandarin`.
3. Ô quy tắc tương ứng (thanh HV × lớp phụ âm × nhập thanh) có tỷ lệ ≥80% và n ≥30 (hiện là bảy ô đánh dấu "có" ở mục 3), và thanh dự đoán là thanh phổ biến nhất của ô đó.
4. Chữ không mang thanh nhẹ trong từ.
5. Khi đó, nếu thanh trong từ khác thanh dự đoán của ô thì gắn nhãn "ngoại lệ"; nếu khớp thì không gắn nhãn.

Không đủ điều kiện nào thì để trống (không gắn "ngoại lệ", cũng không gắn "theo quy tắc"). Nhãn chỉ nói về xu hướng của một tập mẫu, không phải quy luật.
