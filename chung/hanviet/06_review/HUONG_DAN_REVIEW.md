# Hướng dẫn review ngữ nghĩa (pha 5, reviewer Opus)

*Điều phối viết ngày 16/11/2026. Đọc kèm `../TIEU_CHUAN.md`, `../04_draft/HUONG_DAN_SOAN.md`, `quy_uoc_doc_am_chot.md` (quy ước âm đã chốt ở R1) và `../scripts/README_tools.md`.*

Bạn là reviewer **độc lập**: không phải người soạn các mục này. Nhiệm vụ là kiểm từng mục trong tập được giao, sửa chỗ sai, và ghi nhật ký.

## Kiểm gì ở mỗi mục

1. **`nghia_vi`**: đúng nghĩa hiện đại của cả từ trong câu ví dụ, tự nhiên, ngắn. Không lẫn rác CVDICT; không phải nghĩa của cách đọc khác.
2. **`loai`**:
   - `cung_dung` chỉ khi người Việt hiện đại thật sự dùng từ đó với nghĩa về cơ bản như vậy.
   - `khac_dung` phải có khác biệt **đáng kể** và `khac_biet` phải nói đúng chỗ khác.
   - Thành ngữ chỉ là `cung_dung` nếu dạng Hán Việt đó quen với người Việt.
   - Xem lại `yeu_to` / `ghep_nghia` / `khong_giup` có hợp lý không.
3. **`tu_viet`**: là từ Việt có thật, và khớp `loai`.
4. **`khac_biet`**: chính xác, có chừng mực.
5. **`phan_tich`**:
   - `cau_tao` phải đúng nghĩa thành tố đang tham gia vào từ.
   - `goi_nho` không được viết như từ nguyên.
   - **Xóa** mọi khẳng định nguồn gốc lịch sử hay từ nguyên không có nguồn.
6. **`hanviet`**: tuân `quy_uoc_doc_am_chot.md`.
   - **Không** đổi âm trái quy ước R1. Nếu bạn cho rằng quy ước sai, ghi vào nhật ký (`verdict=policy`) để điều phối quyết, đừng tự sửa.
   - Được sửa âm khi rõ ràng sai nghĩa và quy ước không nói tới chữ đó. Âm mới **phải** nằm trong ứng viên của chữ (validator kiểm).
7. **`status`**:
   - Mục `needs_review` mà bạn giải được, có căn cứ → `draft`, xóa `review_reason`.
   - Mục bạn thấy không chắc → `needs_review` kèm lý do.
   - **Không** có trạng thái "đã xác minh". Review của agent không biến nội dung thành đã thẩm định.

## Đầu ra (mỗi reviewer chỉ ghi file của mình)

**1. `06_review/fixes_r2_<tên_tập>.tsv`**: chỉ chứa mục **cần sửa**.
- 12 cột: `note_key hanviet nghia_vi loai tu_viet khac_biet pt_kieu pt_noi_dung status review_reason char_note reviewer`.
- Mỗi dòng mang **đủ giá trị hiện tại** của mọi cột, lấy từ file tập review (các cột "giá trị hiện tại"), chỉ thay cột cần sửa.
- `hanviet` viết đầy đủ (không dùng "="); `char_note` giữ nguyên nếu không đổi.
- `reviewer = opus:r2_<tên_tập>`.
- Merge thay **cả dòng**, nên thiếu cột nào là mất cột đó.

**2. `06_review/log_r2_<tên_tập>.tsv`**: **mọi** mục đã kiểm, cột `note_key verdict van_de ghi_chu`.
- `verdict` ∈ `ok` | `fixed` | `needs_review` | `policy`.
- `van_de`: nhãn ngắn, ví dụ `nghia_sai`, `loai_thoi_phong`, `khac_biet_sai`, `etym_khong_nguon`, `am_sai`, `rac_cv`, `khac`.

**3. Tự kiểm trước khi xong:**

```
/c/Python314/python -I scripts/validate_drafts.py --inputs 04_draft/input --outs 04_draft/out --fixes 06_review \
  --items 00_base/items.jsonl --item-hv 02_chars/item_hv.jsonl --report <scratch>/rep.md --json <scratch>/iss.jsonl
```

Mọi dòng trong file fixes của bạn phải **0 lỗi**.

File tạm chỉ để trong `scratchpad/work/hanviet_review/<tên_tập>/`, đường dẫn đầy đủ: `C:/Users/trinh-v/AppData/Local/Temp/claude/ad1c1fd31c67307a/43f64388-07fc-4045-ac80-4a54f3550946/scratchpad/work/hanviet_review/<tên_tập>/`. Đọc file tập theo khúc khoảng 100 dòng.

## Lỗi hệ thống

Nếu thấy **cùng một kiểu lỗi lặp lại** (ví dụ cùng người soạn thổi phồng `cung_dung` cho thành ngữ, hoặc một quy luật sai nghĩa của một chữ):
- sửa trong tập của bạn;
- **ghi rõ mẫu lỗi** trong báo cáo cuối: mô tả, ví dụ, ước lượng phạm vi, `drafted_by` liên quan. Điều phối sẽ quyết việc sửa cả nhóm ngoài tập của bạn.

## R4: kiểm lại cả nhóm `cung_dung` (thêm 16/11, sau kết quả mẫu R3)

Mẫu R3 (set_sample_01) cho thấy khoảng 20% mục `cung_dung` do Sonnet soạn bị gắn sai nhãn. R4 kiểm lại **toàn bộ** mục `cung_dung` còn lại (`06_review/inputs_r4/set_cd_NN.tsv`), theo các mẫu lỗi đã thấy:

1. **Thổi phồng `cung_dung`** cho từ Hán Việt cổ, văn chương hoặc chỉ có trong từ điển, mà người Việt hiện đại không dùng:
   - Ví dụ: 火车 hỏa xa, 年纪 niên kỷ, 他人 tha nhân, 除夕 trừ tịch, 难题 nan đề, 势必 thế tất.
   - Sửa thành `ghep_nghia` (hoặc `yeu_to` / `khong_giup`), bỏ `tu_viet`.
   - Có thể ghi `goi_nho`, ví dụ "hỏa (lửa) + xa (xe)".
   - Từ Việt dùng thứ tự khác (养老院: tiếng Việt nói "viện dưỡng lão") cũng **không** phải `cung_dung` nguyên dạng. Ghi `ghep_nghia` kèm `goi_nho` nêu từ Việt đảo.
2. **`cung_dung` lẽ ra `khac_dung`:** từ Việt có thật nhưng nghĩa hoặc sắc thái lệch đáng kể so với nghĩa trong câu.
   - Ví dụ: 遭遇 tao ngộ, 接近 tiếp cận, 动态 động thái, 父亲 phụ thân, 女儿 nữ nhi, 不及 bất cập, 欲望 dục vọng.
   - Thêm `khac_biet`.
   - Dấu hiệu: mục `cung_dung` mà **có** `khac_biet`.
3. **Thành ngữ:** chỉ là `cung_dung` khi dạng Hán Việt quen với người Việt (cử nhất phản tam, bất tri bất giác). Các thành ngữ khác là `ghep_nghia`.
4. **Phân tích:**
   - Không ghi nghĩa thuần Việt ở chỗ phải ghi âm Hán Việt ("丸 viên" đúng; "叉 chạc" sai).
   - Không gán nghĩa phái sinh làm nghĩa gốc.
   - Bỏ mnemonic gây nhầm.
5. **Mức đúng:** người Việt bình thường hiểu từ đó **với nghĩa này** khi đọc báo hay nói chuyện. Không chắc thì hạ nhãn. Không cần đẩy `needs_review` vì lý do nhãn.

Cột trong `set_cd_NN.tsv` là bản gọn; dòng fix vẫn đủ 11 cột + `reviewer`, lấy giá trị hiện tại từ file tập. Đầu ra: `fixes_r4_<tập>.tsv`, `log_r4_<tập>.tsv`.

## R5: lượt rà cuối có mục tiêu (thêm 16/11)

Tập: `06_review/inputs_r5/set_r5_NN.tsv`. Cột `flags` cho biết vì sao mục bị lọc:

- **L1:** `loai` là `ghep_nghia` / `yeu_to` / `khong_giup`, nhưng âm Hán Việt cả từ lại nằm trong `nghia_vi`.
  - Nếu người Việt hiện đại thật sự dùng từ đó với nghĩa này → `cung_dung` (thêm `tu_viet`).
  - Nếu không dùng → viết lại `nghia_vi` bằng từ Việt thường dùng, không lặp âm Hán Việt.
- **L2:** thành ngữ 4 chữ đang là `ghep_nghia`, ở lô vốn ít gắn `cung_dung`. Chỉ nâng lên `cung_dung` khi dạng Hán Việt **nguyên văn** quen với người Việt.
- **L4:** áp quyết định của điều phối (xem phần đầu `quy_uoc_doc_am_chot.md`):
  - 打量 dǎliang đọc LƯƠNG.
  - 油腻 đọc NỊ; 细腻 giữ NHỊ.
  - Mục chứa 幻 / 推: kiểm `loai` có còn đúng sau khi R1 đổi âm không (幻 = ảo: 幻影 ảo ảnh, 幻觉 ảo giác…; 推 thôi = đẩy, suy = suy xét / tiến cử).
  - Xóa hoặc sửa mọi câu "nghĩa gốc…", "vốn…", "bắt nguồn…", "có gốc…" không có nguồn. Ví dụ 要 ghi "nghĩa gốc: quan trọng" là **sai**.
  - Đây là trường hợp duy nhất được đổi `hanviet`, và âm mới phải nằm trong ứng viên.
- **L5:** mục được nêu trong `06_review/r3_phan_tich_toan_cuc.md` (thành ngữ nhóm B/C, cặp mâu thuẫn, từ nguyên).
  - Đọc đề xuất trong file đó và đối chiếu với **giá trị hiện tại**, vì nhiều mục R4 đã sửa rồi.
  - Chỉ sửa chỗ còn sai.
- **L6:** `tu_viet` khác âm Hán Việt cả từ.
  - Nếu `tu_viet` là từ Việt đảo thứ tự, từ khác, hoặc câu dịch (khu tự trị, ôm cây đợi thỏ, khẩu trang cho 口罩…) → không phải `cung_dung` nguyên dạng.
    - Thường đổi thành `ghep_nghia` (bỏ `tu_viet`), nêu từ Việt trong `goi_nho`.
    - Hoặc đổi thành `khac_dung` nếu từ Việt cùng chữ có thật nhưng lệch nghĩa.
  - Nếu chỉ khác do từ Việt đọc âm khác nguồn (tài nguyên, thân phận) → giữ, bảo đảm `char_note` có "từ Việt đọc '…'".

Đầu ra: `fixes_r5_<tập>.tsv` và `log_r5_<tập>.tsv`, đúng định dạng như các vòng trước.

## Báo cáo cuối (ngắn)

- Số mục đã kiểm.
- Số `ok` / `fixed` / `needs_review` / `policy`.
- Phân bố `van_de`.
- Mẫu lỗi hệ thống.
- Bất đồng với quy ước R1.
- Model: Opus.
