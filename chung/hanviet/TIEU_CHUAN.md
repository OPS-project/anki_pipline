# Tiêu chuẩn dữ liệu Hán Việt v1

*Điều phối (Opus) chốt ngày 16/11/2026. Người đọc: mọi agent soạn và review, và Codex khi phản biện.*

## 1. Một mục = một dòng JSON, khóa theo `note_key`

Mỗi dòng ứng với một mục trong `00_base/items.jsonl`. Trường rỗng thì bỏ hẳn, không ghi chuỗi rỗng.

```json
{
  "note_key": "zh:hskstory-hsk1:1792758600123",
  "hanzi": "手机",
  "word_pinyin": "shǒu jī",
  "hanviet": "THỦ CƠ",
  "hanviet_chars": [
    {"char": "手", "hv": "thủ", "source": "<id nguồn>", "via": "手", "certainty": "sure"},
    {"char": "机", "hv": "cơ", "source": "<id nguồn>", "via": "機", "certainty": "chosen", "note": "机→機 (máy); không phải 机 kỷ/ki"}
  ],
  "nghia_vi": "điện thoại di động",
  "nghia_basis": "words:<nguồn> exact_pinyin + meaning_en + câu ví dụ",
  "loai": "ghep_nghia",
  "phan_tich": {"kieu": "goi_nho", "noi_dung": "手 tay + 机 máy → máy cầm tay"},
  "status": "draft",
  "drafted_by": "sonnet:batch_03"
}
```

## 2. Định nghĩa từng trường

### `hanviet` và `hanviet_chars`

- `hanviet`: âm Hán Việt của cả từ. Viết HOA, mỗi chữ cách nhau một dấu cách. Chữ chưa có âm chắc chắn thì ghi `?`.
- `hanviet_chars[].source`: **bắt buộc** là ID một nguồn trong `01_sources/SOURCES.md`. Không có nguồn thì `hv` để trống, `certainty: "none"`, và cả mục chuyển `needs_review`. **Cấm điền âm theo hiểu biết của mô hình.**
- `via`: chữ thực sự dùng để tra (có thể là phồn thể). Khi chữ giản thể ứng với nhiều chữ phồn, phải chọn theo nghĩa trong từ và câu ví dụ, rồi ghi lý do vào `note`.
- `certainty` có ba mức:

| Mức | Nghĩa |
|---|---|
| `sure` | Chỉ một ứng viên có nguồn |
| `chosen` | Nhiều ứng viên; đã chọn theo nghĩa + pinyin, có lý do trong `note` |
| `uncertain` | Chưa chọn được → mục `needs_review` |

### `nghia_vi`

- Nghĩa tiếng Việt **ngắn** (thường dưới 12 từ), theo **nghĩa hiện đại của CẢ TỪ** trong mục này.
- Neo bằng ba thứ: `meaning_en` + câu ví dụ + nguồn từ vựng (`02_chars/words_source.jsonl`) nếu có.
- **Không** suy nghĩa từ bằng cách ghép nghĩa từng chữ.
- Từ nhiều nghĩa: ghi nghĩa đang dùng trong câu ví dụ trước. Có thể thêm `; cũng: …` nếu nghĩa khác phổ biến.

`nghia_basis`: ghi đã neo vào đâu, ví dụ `words:cvdict exact_pinyin`, `cedict+example`, `meaning_en+example (không có nguồn VI)`.

### `loai` (bắt buộc, chọn một)

| Giá trị | Khi nào | Ví dụ |
|---|---|---|
| `cung_dung` | Tiếng Việt có từ Hán Việt này với nghĩa hiện đại về cơ bản như tiếng Trung | 经济 kinh tế, 学生 học sinh |
| `khac_dung` | Tiếng Việt có từ này nhưng nghĩa hoặc cách dùng khác đáng kể. **Bắt buộc** có `khac_biet` | 环境 hoàn cảnh, 东西 đông tây (nghĩa "đồ vật") |
| `ghep_nghia` | Tiếng Việt không dùng từ này, nhưng các chữ đóng góp nghĩa rõ | 手机 thủ cơ |
| `yeu_to` | *(thêm 16/11)* Tiếng Việt không dùng đứng riêng, nhưng âm Hán Việt là yếu tố quen trong từ Việt khác **cùng nghĩa**. `phan_tich` nêu 1–2 từ Việt thông dụng | 书 THƯ: như "thư viện", "thư pháp" |
| `hu_tu` | Hư từ, trợ từ, lượng từ, từ ngữ pháp; Hán Việt không giúp hiểu nghĩa | 的, 了, 吗, 个 |
| `phien_am` | Từ phiên âm tiếng nước ngoài | 咖啡, 沙发 |
| `ten_rieng` | Tên riêng | — |
| `khong_giup` | Có âm Hán Việt nhưng không giúp nhớ nghĩa (từ khẩu ngữ, chữ không dùng trong tiếng Việt…) | — |

- `tu_viet`: từ tiếng Việt tương ứng, chỉ khi `loai` là `cung_dung` hoặc `khac_dung`. Ví dụ `"kinh tế"`.
- `khac_biet`: một câu nói rõ khác ở đâu. Ví dụ: "Tiếng Trung: môi trường, điều kiện xung quanh; tiếng Việt 'hoàn cảnh' thường chỉ tình cảnh của một người". Không khẳng định tuyệt đối "luôn luôn/không bao giờ".
- Nhãn `cung_dung` **không thay** `nghia_vi`: vẫn phải điền `nghia_vi`.

### `phan_tich` (tùy chọn)

**Chỉ ghi khi giúp hiểu hoặc nhớ.** Không ép mọi từ phải có. Có hai kiểu:

| Kiểu | Nghĩa |
|---|---|
| `cau_tao` | Phân tích thành tố có căn cứ: nghĩa từng chữ đã có trong nguồn chữ, và đúng là nghĩa đang tham gia vào từ |
| `goi_nho` | Liên tưởng do người soạn đề xuất, không khẳng định là từ nguyên |

### `tu_nguyen` (tùy chọn)

Chỉ ghi khi có nguồn cụ thể: `{"noi_dung": …, "nguon": …}`. Người soạn **không** tự viết nguồn gốc từ. Không có nguồn thì bỏ trường này.

### `status`, `review_reason`, `drafted_by`

- `status` có hai giá trị:
  - `draft`: AI soạn, chưa có người thẩm định. Review bởi agent khác vẫn giữ `draft`.
  - `needs_review`: chưa chắc. Bắt buộc ghi `review_reason` (lý do cụ thể, ví dụ "机 có thể ứng 機/机; câu ví dụ mơ hồ").
- **Không** có trạng thái "verified". Chỉ anh mới chuyển trạng thái sau khi tự kiểm.
- `drafted_by`: `<model>:<lô>`, ví dụ `sonnet:batch_03`, `opus:hard_01`.

## 3. Thanh điệu (do script tính sau, người soạn không điền)

`tone_flags: [{"char": …, "hv_tone": …, "class": "vang|tac", "nhap": bool, "predicted": …, "actual_in_word": …, "flag": "ngoai_le"}]`

Script chỉ gắn khi đủ **mọi** điều kiện trong `03_tone/quy_tac_thanh_dieu.md`:
- âm Hán Việt có `certainty: "sure"` hoặc `"chosen"`;
- thanh thực lấy theo **pinyin của từ**;
- ô quy tắc tương ứng có tỷ lệ ≥80% và n ≥30;
- chữ không mang thanh nhẹ trong từ.

Thiếu bất kỳ điều kiện nào thì để trống.

## 4. Việc người soạn PHẢI đưa sang `needs_review`

- Chữ không có âm Hán Việt có nguồn, hoặc nhiều âm mà chưa chọn được.
- Giản thể → phồn thể mơ hồ khi xét theo nghĩa trong câu.
- `meaning_en` mâu thuẫn với câu ví dụ, hoặc nghi lỗi dữ liệu gốc.
- Không chắc phân loại `cung_dung` hay `khac_dung`.
- Từ cổ, chuyên ngành, thành ngữ mà nghĩa không rõ từ nguồn.

## 5. Định dạng làm việc: đầu vào và đầu ra của người soạn (TSV)

JSON đầy đủ ở mục 1 là định dạng **sau hợp nhất**. Để tiết kiệm token, người soạn nhận và ghi file TSV (UTF-8, phân tách bằng tab, mỗi dòng một mục, không xuống dòng bên trong ô).

**Đầu vào `04_draft/input/<lô>.tsv`** do script pha 2 tạo:

```
note_key  level  hanzi  word_pinyin  meaning_en  sentence  sentence_en  hv_pre  hv_cands  cv_vi  ce_en  tc_char
```

| Cột | Nội dung |
|---|---|
| `hv_pre` | Âm Hán Việt script đã chọn cho cả từ, viết HOA; chữ chưa chọn được ghi `?` |
| `hv_cands` | Ứng viên từng chữ, dạng `手:thủ\|机→機:cơ,ki` (chữ, phồn thể nếu khác, các âm có nguồn) |
| `cv_vi` | Nghĩa từ CVDICT, khớp pinyin, đã rút gọn; rỗng nếu không có |
| `ce_en` | Nghĩa CC-CEDICT, khớp pinyin, rút gọn |
| `tc_char` | Nghĩa Thiều Chửu ngắn từng chữ, dạng `手: tay; 機: máy móc, cơ quan` |

**Đầu ra `04_draft/out/<lô>.tsv`**: đúng 11 cột, dòng đầu là header:

```
note_key  hanviet  nghia_vi  loai  tu_viet  khac_biet  pt_kieu  pt_noi_dung  status  review_reason  char_note
```

- `hanviet`: ghi `=` nếu đồng ý `hv_pre`. Nếu sửa, mỗi âm **phải nằm trong `hv_cands`** của chữ đó (validator sẽ kiểm). Muốn để chữ chưa chắc thì ghi `?` và đặt `status=needs_review`.
- `loai`: `cung_dung` / `khac_dung` / `ghep_nghia` / `yeu_to` / `hu_tu` / `phien_am` / `ten_rieng` / `khong_giup`.
- `pt_kieu`: `cau_tao` / `goi_nho` / rỗng.
- `status`: `draft` / `needs_review`. Nếu `needs_review` thì `review_reason` bắt buộc.
- `char_note`: lý do chọn âm khi có nhiều ứng viên. Tùy chọn.
- Ô rỗng để trống, không ghi chữ "null".

## 6. Không được làm

- Không sửa `meaning_en`, câu hay pinyin gốc.
- Không dịch câu ví dụ sang tiếng Việt.
- Không ghi đè file của agent khác. Mỗi agent ghi file riêng.
