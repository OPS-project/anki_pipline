# Hán Việt cho deck HSK: checkpoint

Điều phối: Claude (Opus 5.5). Yêu cầu: prompt do Codex soạn, anh chuyển ngày 16/11/2026.

**Phạm vi:** dữ liệu Hán Việt + nghĩa Việt cho đủ 10.898 mục.
- **Không** build APKG, **không** import.
- **Không** dịch câu ví dụ sang tiếng Việt.
- Chỉ ghi vào `chung/hanviet/`.

## Thư mục

| Thư mục | Nội dung |
|---|---|
| `00_base/` | `items.jsonl`: 10.898 mục theo NoteKey; `chars.txt` |
| `01_sources/` | Nguồn từ điển tải về (mỗi nguồn một thư mục), `SOURCES.md` |
| `02_chars/` | `chars.jsonl`: ứng viên âm Hán Việt + nghĩa từng chữ, có nguồn |
| `03_tone/` | Tài liệu quy tắc thanh điệu + dữ liệu đo |
| `04_draft/` | Bản soạn theo lô (mỗi agent một file) |
| `05_validate/` | Kết quả kiểm tự động |
| `06_review/` | Review ngữ nghĩa (Opus) |
| `07_final/` | Dữ liệu hợp nhất |
| `scripts/` | Script do agent viết |
| `reports/` | Báo cáo bàn giao |

## Tiến độ

| Pha | Việc | Agent / model | Trạng thái |
|---|---|---|---|
| 1a | Kiểm kê deck → `00_base/`; tài liệu thanh điệu → `03_tone/` | Sonnet | **xong** |
| 1b | Nguồn từ điển + giấy phép → `01_sources/`, `02_chars/` | Sonnet | **xong** |
| 2a | Ghép ứng viên âm theo mục → `02_chars/item_hv.jsonl`; chia lô → `04_draft/input/` | Sonnet | **xong** |
| 2b | Validator, merge, tone_flags → `scripts/` | Sonnet | **xong** |
| 3 | Soạn nháp: hard_01–04 (Opus ×3); batch_NN chia a = dòng 2–351, b = dòng 352–701 (Sonnet, mỗi agent 350 mục) | Opus + Sonnet | đang chạy |
| 4 | Kiểm tự động toàn bộ | — | chờ |
| 5 | Review ngữ nghĩa độc lập (Opus) | — | chờ |
| 6 | Hợp nhất, báo cáo, đề xuất bố cục, bản cho Codex | — | chờ |

## Nhật ký agent

- **1a, Sonnet** (80k token, 14 lượt công cụ):
  - `items.jsonl` có 10.898 dòng. `note_key`, `guid`, note id đều duy nhất. Khớp nguồn HSKStory 0 lệch. Không có hanzi đồng hình.
  - `chars.txt` có 3.088 chữ.
  - 62 mục có từ mục tiêu lặp trong câu.
  - Quy tắc thanh đo trên 2.077/3.088 chữ. 7 ô đạt ngưỡng ≥80% và n ≥30.
  - **Quyết định điều phối:** giữ ngưỡng 80%, n ≥30 như yêu cầu. Ghi rõ đây là ô chọn sau khi nhìn dữ liệu nên tỷ lệ có thể lạc quan. Đo lại khi có âm Hán Việt cho phần chữ Unihan thiếu.
- **1b, Sonnet** (125k token, 52 lượt công cụ):
  - **Nguồn chính:** Thiều Chửu dataV4.json (không có giấy phép; chỉ dùng học cá nhân, không phát hành lại) và hanviet-pinyin (MIT).
  - **Nguồn từ:** CVDICT (CC BY-SA, phần lớn dịch bằng GPT-4o) và CC-CEDICT.
  - **Phụ:** Unihan 18.0, OpenCC, kaikki.
  - **Độ phủ:** 3.088/3.088 chữ có ≥1 âm có nguồn. Từ khớp pinyin: CVDICT 99,5%, CEDICT 99,7%.
  - Dump kaikki nặng 1,2 GB nằm trong `01_sources/kaikki/`.
- **2a, Sonnet** (92k token):
  - `item_hv.jsonl` có 10.898 dòng.
  - Theo chữ-trong-mục: 20.084 `sure`, 719 `chosen`, 796 `uncertain`.
  - Tập khó 1.092 mục → hard_01–04. Tập thường 9.806 mục → batch_01–15 (batch_15 chỉ có 6 mục).
- **2b, Sonnet** (116k token):
  - Viết `validate_drafts.py`, `merge_drafts.py`, `tone_flags.py`, `README_tools.md`; tự kiểm đạt.
  - Chạy tone_flags trên `item_hv` thật: 12.197 chữ đủ điều kiện, 643 ngoại lệ.
  - **Điều phối chấp nhận** 12 giả định giao diện, xem báo cáo trong `scripts/README_tools.md`.
- **Điều phối:** thêm loại `yeu_to`; viết `04_draft/HUONG_DAN_SOAN.md`.
- **Pha 3, đợt 1:**
  - Opus: hard_01, hard_02, hard_03 + hard_04.
  - Sonnet: batch_01a, 01b, 02a, 02b.
- **Pha 3, đợt 2:** Sonnet batch_03a/b, 04a/b, 05a/b.
- **batch_03b xong** (Sonnet, 350 mục, 0 needs_review). Điều phối kiểm 18 mẫu ngẫu nhiên: ổn, không thấy lỗi hệ thống.
- **Pha 3, đợt 3:** Sonnet batch_06a/b, 07a/b, 08a/b.
- **Đã xong** (Sonnet): 01a, 01b, 02a, 02b, 03a, 03b, 04a, 04b, 05a, 05b.
  - Validator tạm (`05_validate/report_interim.md`):
    - Lỗi chỉ ở 01b: 方便面 "MÌ" (sai số âm, âm ngoài cands); 11 mục `yeu_to` có `tu_viet`.
    - 5 cảnh báo nhỏ.
- **Vấn đề vận hành:** agent ghi đè file tạm của nhau ở scratchpad gốc. Đã sửa hướng dẫn (thư mục tạm riêng), đã nhắn mọi agent đang chạy. Các agent đã xong đều báo đã đối chiếu nội dung từng dòng.
- **Lỗi hệ thống cấp chữ, cần review thống nhất:**
  - 单 đan/đơn, 受 thọ/thụ, 推 suy/thôi, 当 đương/đáng, 尽 tận/tẫn, 调 điều/điệu.
  - 份 phần (từ Việt "thân phận"), 资 tư (từ Việt "tài nguyên").
  - 要 yếu/yêu, 找 trảo/hoa, 喝 húp.
- **Đợt 4:** Sonnet 09a/b, 10a/b, 11a/b.
- **Đợt 5:** Sonnet 12a/b, 13a/b, 14a, 14b + batch_15. Đến đây **đã giao hết các lô**.
- **Đã xong thêm:** 06a, 06b, 07a, 08a (Sonnet); hard_01, hard_02 (Opus).
  - Quy ước đọc âm Opus đề xuất được gom vào `06_review/quy_uoc_doc_am_de_xuat.md`.
- **Chuẩn bị review:** Sonnet viết `scripts/char_consistency.py` và `scripts/make_review_inputs.py`.

### Pha 3: xong (16/11)

- Đủ 33 file out: 28 phần Sonnet, 4 hard Opus, batch_15.
- **Validator v1:** 0 thiếu, 0 trùng. 15 lỗi cấu trúc (13 `tu_viet` ở `yeu_to`, 方便面 "MÌ").
- **Điều phối sửa** bằng `06_review/fixes_r0_struct.tsv` (14 dòng, script `scripts/fix_r0_struct.py`).
- **Merge v1:** `07_final/merged_v1.jsonl`, 10.898 mục.
  - 38 `needs_review`.
  - Phân loại: ghep_nghia 5.853, cung_dung 2.800, yeu_to 755, khong_giup 640, khac_dung 577, hu_tu 229, phien_am 31, ten_rieng 13.
- **Báo cáo cho R1:**
  - `06_review/char_consistency.md`: 85 nhóm chữ–pinyin có ≥2 âm.
  - `06_review/am_khong_thieuchuu_sau_soan.tsv`: 146 nhóm, 341 mục.
- **Đang chạy:** R1 (Opus) thống nhất âm cấp chữ → `fixes_r1_doc_am.tsv`.

### R1: xong (Opus)

- **Kết quả:**
  - 192 quy tắc; 186 mục đổi âm (87 âm Nôm, 46 hvpinyin-only, 53 thống nhất).
  - `needs_review`: 38 → 12.
  - Đầu ra: `06_review/fixes_r1_doc_am.tsv` (218 dòng), `quy_uoc_doc_am_chot.md`, `r1_report.md`, `scripts/r1_apply.py`.
- **Điều phối:** `fixes_r1b_wording.tsv` sửa 11 dòng gợi nhớ khẳng định từ nguyên không nguồn ("có gốc từ chữ này" → liên tưởng).
- **Merge v2:** `07_final/merged_v2.jsonl`. Đầu vào review ở `06_review/inputs/`, seed 20261116, split 370.

### Pha 5: review, đang chạy (7 agent Opus)

Hướng dẫn: `06_review/HUONG_DAN_REVIEW.md`.

| Tập | Số mục | Ghi chú |
|---|---|---|
| set_hard_01 | 370 | |
| set_hard_02 | 370 | |
| set_hard_03 | 352 | |
| set_khac_01 | 370 | |
| set_khac02_needs_r1 | 147 + 11 | Cộng các mục R1 đổi nằm ngoài các tập khác (kiểm loại / `tu_viet` của mục âm Nôm) |
| set_sample_01 | 370 | |
| set_sample_02 | 169 | Cộng phân tích toàn cục → `r3_phan_tich_toan_cuc.md` |

Đầu ra mỗi tập: `fixes_r2_<tập>.tsv` + `log_r2_<tập>.tsv`.

**Đã xong:**

| Tập | Đã kiểm | Sửa | needs_review | Ghi chú |
|---|---|---|---|---|
| set_hard_01 | 370 | 9 | 0 | 0 policy |
| set_hard_02 | 370 | 6 | 1 (夯实) | 0 policy |
| set_hard_03 | 352 | 4 | 0 | 1 policy (打量) |

**Quyết định điều phối, chờ áp ở fix cuối (`fixes_r9_dieu_phoi.tsv`):**
- 打量 dǎliang: nghĩa "đo bằng mắt" → LƯƠNG, theo nguyên tắc liáng = lương của R1.
- Rà toàn cục `pt_noi_dung` tìm chữ "vốn…" (từ nguyên ngầm) và "phục tòng" (trái R1: 服从 đọc phục tùng). Kết hợp với `r3_phan_tich_toan_cuc.md`.
- `char_note` bị lặp đoạn / chuỗi script: dọn ở bản cuối. Trường nội bộ, không hiện trên thẻ.
- 腻: 油腻 → NỊ; 细腻 giữ NHỊ.
- Rà các mục chứa 幻 / 推 ngoài tập R2 xem `loai` có lỗi thời sau khi R1 đổi âm không.
- Đã ghi phần sửa đổi điều phối vào đầu `quy_uoc_doc_am_chot.md`.

**Kết quả thêm:**

| Tập | Đã kiểm | Sửa | Ghi chú |
|---|---|---|---|
| set_khac_01 | 370 | 28 | |
| set_sample_01 | 370 | 37 | **~20% `cung_dung` sai → lỗi hệ thống** |
| set_khac02_needs_r1 | 341 | 57 | 1 needs_review (掰), 2 policy |

**R4 (5 agent Opus):** kiểm lại toàn bộ 2.390 mục `cung_dung` chưa review → `fixes_r4_set_cd_NN.tsv`. Script: `scripts/make_r4_inputs.py`.

| Tập | Đã kiểm | Sửa | Ghi chú |
|---|---|---|---|
| set_sample_02 | 169 | 22 | Phân tích toàn cục ở `r3_phan_tich_toan_cuc.md` |

`r3_phan_tich_toan_cuc.md` gồm:
- 27 thành ngữ thổi phồng rõ (nhóm C) và 27 thành ngữ sách vở (nhóm B).
- Tỷ lệ gắn `cung_dung` cho mục 4 chữ lệch theo lô: 07b 49%, 13b 60%, trong khi 10a 3%.
- 6 cặp từ có `loai` mâu thuẫn.
- 5 khẳng định "nghĩa gốc" không nguồn.

**R5 (sau R4), lọc có mục tiêu:** `scripts/make_r5_inputs.py` chạy trên merge v3. Chỉ lấy L1, L2, L4, L5:

| Nhóm | Nội dung | Số mục (thử trên v2) |
|---|---|---|
| L1 | `ghep_nghia` / `yeu_to` / `khong_giup` mà âm Hán Việt có trong `nghia_vi` | 33 |
| L2 | Thành ngữ 4 chữ ở các lô ít gắn `cung_dung` | 229 |
| L4 | 幻 / 推 / 腻 / 打量 và từ khóa từ nguyên | 75 |
| L5 | note_key nêu trong r3 | 117 |

**L3 bỏ** (pt dạng "中 giữa" thay vì "中 trung (giữa)": chủ yếu là kiểu trình bày, 391 mục). Ghi là hạn chế trình bày trong báo cáo.

### R4: xong (5 agent Opus, mỗi agent 478 mục)

| Tập | Đổi `loai` | Tỷ lệ |
|---|---|---|
| set_cd_01 | 101 | 21% |
| set_cd_02 | 85 | 18% |
| set_cd_03 | 133 | 28% |
| set_cd_04 | 135 | 28% |
| set_cd_05 | 83 | 17% |

- **Tổng:** khoảng 537 / 2.390 (22%) đổi nhãn.
- **Hướng đổi:** phần lớn sang `ghep_nghia` (thổi phồng, thành ngữ, từ Việt đảo thứ tự) và `khac_dung` (bỏ sót lệch nghĩa).
- **Rủi ro ngược chiều:** "không chắc thì hạ nhãn" làm hạ một số từ khá thông dụng (身心, 常规…). Ranh giới có phần chủ quan.
- **Điều phối chốt:** 根深蒂固 → `ghep_nghia` + `goi_nho` "thâm căn cố đế", theo quy tắc R4.
- **Merge v3:** 2 `needs_review`.
  - Phân loại: ghep_nghia 6.159, cung_dung 2.227, khac_dung 814, yeu_to 756, khong_giup 667, hu_tu 231, phien_am 31, ten_rieng 13.
- **Lỗi merge:** char_note cấp mục bị mất ở mục "=" (宗教 "từ Việt đọc 'tôn'"…). Sửa trong `finalize.py`.

### R5: đang chạy

- 2 agent Opus, 484 mục: L1 54, L2 199, L4 71, L5 117, L6 55 (có trùng).
  - L2 đã sửa logic: "lô thấp" tính theo v1, bỏ mục đã được review.
  - Phần A: set_r5_01 dòng 2–243. Phần B: dòng 244–451 + set_r5_02.
- Sonnet đang viết `scripts/finalize.py`.

### R5 và hoàn thiện: XONG (16/11)

- **R5:** r5_a sửa 75/242, r5_b sửa 45/242.
  - Áp 打量 ĐẢ LƯƠNG và 油腻 DU NỊ.
  - L1 (`nghia_vi` lặp âm Hán Việt) đã rà hết.
- **Điều phối r9** (`fixes_r9_dieu_phoi.tsv`):
  - 裸体 → LÕA THỂ (裸, 裸露 giữ KHỎA).
  - 未成年人 → `ghep_nghia`.
  - Giữ 督促 ĐỐC XÚC.
- **Sửa `finalize.py`:** gộp `char_note` trùng theo nội dung sau tiền tố "chữ:".
- **`finalize.py` → `07_final/`:**
  - Kiểm cuối 0 lỗi; 2 `needs_review` (夯实, 掰); 679 mục có cờ thanh.
  - Độ phủ review: 4.993 mục.
- **Báo cáo:** `README.md`, `reports/bao_cao_kiem_dinh.md`, `reports/de_xuat_build.md`, `reports/tom_tat_cho_Codex.md`.
- **Trạng thái:** HOÀN THÀNH phần dữ liệu và kiểm định. Chưa build/import. Chờ anh và Codex phản biện.

### R6: sửa có giới hạn theo phản hồi anh/Codex (16/11), XONG

- **Sonnet:** hồ sơ 86 chữ (`06_review/r6/ho_so_nghi_van.*`); công cụ nhận `02_chars/cands_bosung.jsonl`.
- **Opus quyết** (`06_review/r6/quyet_dinh_am.*`):
  - Đổi âm: 兔 THỐ, 踹 SỦY, 滴 TRÍCH, 咖 GIÀ, 哈 CÁP, 啃 KHẨN.
  - 吹 giữ XUY, sửa ghi chú.
  - 31 chữ (41 mục) chuyển `needs_review`.
- **Sonnet áp:** `fixes_r6_doc_am.tsv` (53 dòng).
- **Opus khác kiểm độc lập** (`06_review/r6/kiem_doc_lap.md`): đồng ý 86/86. Phát hiện 3 lỗi khi áp, Sonnet đã sửa tận gốc:
  - ngoặc kép CSV;
  - `clean_note` cắt trong ngoặc;
  - tone_flags trên chữ uncertain.
- **Bản cuối:** 43 `needs_review`; 665 mục có cờ thanh (ẩn ở bản build đầu).
- **Báo cáo** đã sửa: phát biểu sai về 吹, số `needs_review`, đề xuất build bản 2 (dùng `Notes`, không thêm trường).

### Build bản 2: XONG (16/11, anh yêu cầu "build")

- **File:** `chung/build/zh/Tieng_Trung_HSK_nghe_cau_v2_hanviet.apkg`. Bản 1 giữ nguyên.
- **Cách làm:** khối Hán Việt vào trường `Notes`; template đưa Notes vào ô từ mục tiêu; CSS `.hv-*`; tone_flags ẩn.
- **Tag:** `hanviet::draft`, `hanviet::needs_review` (43).
- **Kiểm cập nhật trên collection tạm** (`scripts/test_update_v2.py`): 0 mới / 10.898 cập nhật; số thẻ không đổi; revlog và FSRS của 50 thẻ đã học không đổi; template mới áp; 0 Notes rỗng.
- **Chưa thử trên điện thoại.** Chưa import vào Anki thật của anh.

### Kế hoạch pha 4–5 (điều phối chốt)

1. Soạn xong → chạy validator toàn bộ → sửa lỗi cấu trúc → merge → tone_flags.
2. **Phát hiện (điều phối, 16/11):** `hvpinyin` lẫn **âm Nôm** (冷 lạnh, 油 dầu, 箱 rương, 捕 bắt, 哭 khóc…).
   - 134 cặp chữ–âm (370 mục) có âm `hv_pre` không được Thiều Chửu xác nhận. Danh sách: `06_review/hv_pre_khong_co_thieuchuu.tsv`.
   - Một số là âm Hán Việt thật mà bản Thiều Chửu này thiếu (领 lãnh, 带 đới, 层 tầng).
   - **R1 phải phân loại:**
     - Âm Nôm → thay bằng âm Hán Việt có nguồn; từ Nôm có thể đưa vào `goi_nho`.
     - Âm Hán Việt thông dụng → giữ, ghi căn cứ (từ Việt chứa âm đó).
   - **R1 (Opus):** thống nhất âm cấp chữ trên toàn bộ mục. Dựa trên `char_consistency` và quy ước đề xuất, viết `06_review/quy_uoc_doc_am_chot.md` và `fixes_r1_*.tsv` áp cho **cả nhóm** liên quan. Chạy **trước**, rồi merge lại.
3. **R2/R3 (Opus, song song, tập không chồng nhau), lấy dữ liệu sau R1:**
   - R2a, R2b: toàn bộ set_hard (do Opus soạn; reviewer phải là agent khác).
   - R2c: set_needs + set_khac.
   - R3: set_sample (5% phân tầng + mọi `phien_am` / `ten_rieng`). Kiểm thêm tính nhất quán nhãn `cung_dung` / `ghep_nghia`, thành ngữ.
   - Có lỗi hệ thống thì sửa cả nhóm.
4. Merge cuối → validator → báo cáo.
- **Điều phối:** viết `scripts/hv_common.py` (`reading_key`, `display`; dấu thanh kiểu thông dụng hòa/thủy/quý), thêm mục 5 TSV vào TIEU_CHUAN.
