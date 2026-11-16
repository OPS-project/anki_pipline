# Báo cáo kiểm định dữ liệu Hán Việt cho deck HSK

*Điều phối: Claude (Opus 5.5). Ngày 16/11/2026. Người đọc: anh và Codex.*

**Nhãn chung:** toàn bộ nội dung là **bản nháp do AI biên soạn**. Review giữa các agent **không** biến nội dung thành "đã thẩm định". Chưa có người nào kiểm.

## 1. Kết quả chính

| Chỉ số | Giá trị |
|---|---|
| Số mục | **10.898 / 10.898**, khớp `note_key` gốc, không trùng, không mất |
| Có âm Hán Việt lấy từ nguồn | 10.897 mục. Riêng 掰 để `?` vì nguồn chỉ có âm Nôm |
| Có nghĩa tiếng Việt | 10.898 |
| `needs_review` còn lại | **43**: mọi bất định âm còn tồn tại (mục 5) |
| Có phân tích (cấu tạo hoặc gợi nhớ) | 7.005 |
| Có nhãn "ngoại lệ thanh điệu" | 665. Giữ trong dữ liệu, **ẩn ở bản build đầu**, chưa review riêng |

**Phân loại:**

| Loại | Số mục |
|---|---|
| ghép nghĩa (`ghep_nghia`) | 6.161 |
| cùng dùng (`cung_dung`) | 2.221 |
| khác dùng (`khac_dung`) | 816 |
| yếu tố (`yeu_to`) | 757 |
| không giúp (`khong_giup`) | 668 |
| hư từ (`hu_tu`) | 231 |
| phiên âm (`phien_am`) | 31 |
| tên riêng (`ten_rieng`) | 13 |

Số liệu đầy đủ: `07_final/stats.md`.

## 2. Đã kiểm gì

### 2.1 Kiểm tự động (toàn bộ)

- **Kiểm kê deck:** 10.898 mục khớp nguồn HSKStory gốc, 0 lệch (`00_base/README.md`).
- **Validator mọi file soạn và file sửa** (`scripts/validate_drafts.py`). Kiểm:
  - số cột, khóa, mất mục, trùng mục;
  - số âm bằng số chữ;
  - âm phải nằm trong danh sách ứng viên có nguồn;
  - loại và trạng thái hợp lệ;
  - ràng buộc giữa các trường (ví dụ `khac_dung` phải có `khac_biet`).

  Mọi file sửa đều 0 lỗi. Có 15 lỗi cũ trong 3 file soạn gốc, đã được thay bằng `fixes_r0_struct.tsv`.
- **Kiểm cuối** (`scripts/finalize.py`): đủ 10.898 mục theo thứ tự gốc; mọi âm có nguồn; loại và trạng thái hợp lệ. Kết quả: **0 lỗi**.

### 2.2 Review ngữ nghĩa (Opus, độc lập với người soạn)

| Vòng | Phạm vi | Đã kiểm | Đã sửa |
|---|---|---|---|
| R1: thống nhất âm cấp chữ | Mọi mục có chữ nhiều âm hoặc âm không có trong Thiều Chửu | toàn bộ (theo quy tắc) | 218 dòng (186 mục đổi âm, trong đó **87 âm Nôm** được thay bằng âm Hán Việt) |
| R2: mục khó | **Toàn bộ** 1.092 mục khó (Opus soạn) | 1.092 | 19 (1,7%) |
| R2: khác dùng + `needs_review` | **Toàn bộ** 517 mục `khac_dung` + 11 `needs_review` + 183 mục R1 đổi âm | 711 | 99 |
| R3: mẫu phân tầng | 539 mục (5% theo cấp × loại, seed 20261116) | 539 | 59 (khoảng 11%) |
| **R4: kiểm lại cả nhóm `cung_dung`** | **Toàn bộ** 2.390 mục `cung_dung` còn lại, sau khi R3 phát hiện lỗi hệ thống | 2.390 | 564 (537 đổi loại, khoảng 22%) |
| R5: rà cuối có lọc | 484 mục lọc bằng máy theo các mẫu lỗi đã biết | 484 | 120 |
| R6: chữ âm đáng ngờ | 86 chữ (兔, 吹, 18 chữ R1 "không chắc", 71 chữ không có trong Thiều Chửu). Opus quyết, Opus khác kiểm độc lập (đồng ý 86/86) | 86 chữ, 374 mục | 53 (8 đổi âm, 4 sửa ghi chú, 41 chuyển `needs_review`) |
| Điều phối | Sửa cấu trúc, câu từ nguyên, quyết định cuối | | 27 |

- **Độ phủ:** 4.993 mục đã qua ít nhất một vòng review ngữ nghĩa. 5.905 mục chỉ được kiểm tự động và qua mẫu, chủ yếu là `ghep_nghia`, `yeu_to`, `khong_giup`, `hu_tu`.
- **Không được hiểu** rằng 5.905 mục này đã được xác minh.

### 2.3 Lỗi hệ thống đã phát hiện và cách sửa cả nhóm

1. **Nguồn `hvpinyin` lẫn âm Nôm** (冷 lạnh, 油 dầu, 箱 rương, 捕 bắt, 哭 khóc, 围 vây, 譬 ví…).
   - R1 rà mọi âm không có trong Thiều Chửu: 146 nhóm, 341 mục. Thay 39 quy tắc âm Nôm, giữ 40 âm Hán Việt thông dụng có từ Việt chứng thực (lãnh, đới, tầng…).
   - R2 sửa lại loại và `tu_viet` cho các mục bị ảnh hưởng.
2. **Chữ nhiều âm bị đọc không nhất quán giữa các lô** (单, 受, 推, 调, 领, 旋…). R1 chốt 192 quy tắc theo pinyin, nghĩa và từ Việt (`06_review/quy_uoc_doc_am_chot.md`). Số nhóm còn khác âm giảm từ 85 xuống 57; các nhóm còn lại đều là khác biệt có chủ đích theo từ Việt (面 diện/miến, 行 hành/hạnh/hàng).
3. **Thổi phồng nhãn `cung_dung`.**
   - Mẫu R3 cho thấy khoảng 20% sai, gồm: từ Hán Việt cổ hoặc sách vở (hỏa xa, niên kỷ); từ lệch nghĩa so với câu ví dụ (移动 di động); thành ngữ; từ Việt đảo thứ tự.
   - R4 kiểm lại **toàn bộ** nhóm. Tỷ lệ sai thực tế theo tập: 17–28%.
4. **Thành ngữ gắn `cung_dung` lệch theo lô** (49–60% ở một số lô, gần 0% ở lô khác). R4 hạ các thành ngữ không quen; R5 rà các thành ngữ bị đánh thấp ở những lô ít gắn `cung_dung`.
5. **`nghia_vi` lặp lại chính âm Hán Việt ở mục `ghep_nghia`** (ví dụ "thị dân, người dân thành phố"). Bộ lọc bắt hết các mục có dấu hiệu này (54 mục); R5 sửa 45.
6. **Khẳng định từ nguyên không có nguồn** ("'dầu' có gốc từ chữ này", "nghĩa gốc là…"). Đã đổi thành liên tưởng hoặc xóa, bằng `fixes_r1b` và các vòng R2–R5.
7. **Lỗi công cụ:** merge làm mất `char_note` ở mục giữ nguyên âm (ví dụ "từ Việt đọc 'tôn'"). `finalize.py` khôi phục 1.131 mục và gộp ghi chú bị nhân bản.

## 3. Ước lượng chất lượng còn lại (dựa trên mẫu, không phải xác minh)

- **Nhóm chưa review riêng** (5.905 mục, chủ yếu `ghep_nghia`): mẫu R3 cho thấy khoảng 8–10% cần sửa, khoảng 3% là lỗi nặng.
  - Phần lớn là ranh giới nhãn: `ghep_nghia` lẽ ra `cung_dung` hoặc ngược lại.
  - Kế đến là phân tích ghi nghĩa thuần Việt ở chỗ phải ghi âm (xem mục 4).
  - Lỗi `nghia_vi` sai nghĩa hiếm, dưới 1% trên mẫu.
- **Âm Hán Việt:** sau R1 không reviewer nào phát hiện thêm lỗi âm ngoài các điểm "policy" đã được điều phối quyết.
- **Ranh giới `cung_dung` / `khac_dung` / `ghep_nghia` có phần chủ quan.** Nguyên tắc R4 "không chắc thì hạ nhãn" giảm thổi phồng, nhưng làm hạ một số từ khá thông dụng (身心 thân tâm, 常规 thường quy). Hạ nhãn ít hại hơn: thẻ vẫn hiện đủ âm Hán Việt và nghĩa.

## 4. Hạn chế đã biết

- **Nguồn:**
  - Thiều Chửu (dataV4.json) không kèm giấy phép, chỉ dùng cho học cá nhân, không phát hành lại.
  - CVDICT phần lớn do GPT-4o dịch, nên chỉ dùng làm gợi ý, không chép.
  - Chi tiết ở `01_sources/SOURCES.md`.
- **Từ Việt đọc âm không có trong nguồn** (资源 tài nguyên, 身份 thân phận, 慢性 mãn tính, 宗教 tôn giáo…): giữ âm có nguồn, ghi "từ Việt đọc '…'" trong `char_note`. Danh sách ở `06_review/r1_report.md`.
- **Âm đáng ngờ đã xử lý ở R6** (`06_review/r6/quyet_dinh_am.md`, `kiem_doc_lap.md`):
  - **兔 → THỐ** ở mọi mục (兔子 THỐ TỬ, 守株待兔 THỦ CHU ĐÃI THỐ). "thỏ" giữ trong nghĩa Việt.
    - Nguồn của "thố": Wiktionary ("Hán Việt readings: thố"; "thỏ" là âm Nôm). Thiều Chửu gián tiếp qua 菟 "cũng đọc là thố".
    - Lưu ý: bản Thiều Chửu số hóa, hvpinyin và Unihan đều ghi 兔 là "thỏ".
  - **吹:** bản trước viết "cổ xúy là chữ khác" là **sai**. Xuy và xúy đều là âm có nguồn của **cùng chữ** 吹 (Thiều Chửu #5304: "xuy, xúy… Một âm là xúy. Cổ xúy"). Bốn mục hiện có mang nghĩa "thổi" nên giữ XUY; ghi chú âm đã được sửa.
  - **Đổi theo Thiều Chửu:** 踹 SỦY, 滴 TRÍCH, 咖啡 GIÀ PHÊ, 哈 CÁP, 啃 KHẨN (qua 齦). 咖 và 哈 là đảo quyết định R1.
  - **Chữ khẩu ngữ mà âm chỉ có ở hvpinyin**, không có nguồn thứ hai hay từ Việt chứng thực: chuyển `needs_review` (mục 5), không đoán.
- **Kiểu trình bày phân tích chưa đồng nhất:** khoảng 390 mục ghi "中 giữa + 止 dừng" thay vì "中 trung (giữa)". Không sai nghĩa, nhưng có thể khiến người đọc tưởng "giữa" là âm. Chưa sửa.
- **Thanh điệu:**
  - Nhãn "ngoại lệ" chỉ gắn ở 7 ô quy tắc có tỷ lệ ≥80% và n ≥30. Các ô này được chọn sau khi nhìn dữ liệu, nên tỷ lệ có thể lạc quan.
  - Đoán đúng số thanh không có nghĩa là phát âm đúng thanh trong câu.
  - Chi tiết ở `03_tone/quy_tac_thanh_dieu.md`.
- **Chưa dịch câu ví dụ sang tiếng Việt** (ngoài phạm vi). Nghĩa và câu tiếng Anh giữ nguyên.

## 5. `needs_review` và bất đồng còn mở

**`07_final/needs_review.tsv`** (43 mục). Đây là **toàn bộ** bất định âm còn tồn tại; báo cáo không còn liệt kê vấn đề âm nào khác ngoài danh sách này.

| Nhóm | Số mục | Ví dụ |
|---|---|---|
| Âm chỉ có ở hvpinyin, Thiều Chửu không có chữ, không có nguồn thứ hai hay từ Việt chứng thực | 32 | 啤 乒乓 嗯 胳 捡 搞(3) 嘿 愣(2) 叼 唬 咧(2) 嗦 嘀 垮 憋 挎 捂 捅 掺 揍 暨 沏 涮 溜(2) 甩 趴 蹦 |
| Thiều Chửu có chữ nhưng âm thuộc nghĩa khác; âm đang dùng chỉ có ở hvpinyin | 9 | 卡 (7 mục: thẻ, xe tải…), 吭, 橱 |
| Từ trước R6 | 2 | 夯实 (hãng/kháng), 掰 (chỉ có âm Nôm "bẻ") |

Ở các mục này, âm hiện tại được giữ tạm. Chữ liên quan mang `certainty: uncertain`, không có cờ thanh điệu, và lý do nằm trong `review_reason`.

**Điều phối đã chốt** (căn cứ ghi trong phần đầu `quy_uoc_doc_am_chot.md`):

| Mục | Quyết định |
|---|---|
| 打量 | ĐẢ LƯƠNG |
| 油腻 / 细腻 | NỊ / NHỊ |
| 裸体 | LÕA THỂ (裸 vẫn KHỎA như "khỏa thân") |
| 督促 | Giữ ĐỐC XÚC, ghi "từ Việt đọc 'thúc'" |
| 根深蒂固 | `ghep_nghia` + gợi nhớ "thâm căn cố đế" |
| Âm Nôm | Không giữ từ Nôm trong `tu_viet` |

**Quyết định đã chốt, có căn cứ, không phải bất định:**
- 奖 tưởng, 量 liáng lương, 推 thôi (nghĩa "đẩy"), 领 lĩnh (nghĩa "nhận"). Đúng theo nguồn, nhưng có thể lạ tai với người học. Ghi chú âm trên thẻ nêu từ Việt quen dùng khi có.
- Ranh giới nhãn cùng dùng / khác dùng / ghép nghĩa có phần chủ quan (mục 3). Theo chỉ thị, không tranh luận lại trong bản này.

## 6. Agent và model đã dùng (thực tế)

| Pha | Việc | Model | Số agent |
|---|---|---|---|
| 1 | Kiểm kê deck, quy tắc thanh; tìm nguồn từ điển | Sonnet | 2 |
| 2 | Ghép ứng viên âm và chia lô; viết validator / merge / tone_flags | Sonnet | 2 |
| 3 | Soạn 9.806 mục thường (28 phần × khoảng 350 mục) | Sonnet | 28 |
| 3 | Soạn 1.092 mục khó | Opus | 3 |
| | Công cụ review; script hoàn thiện | Sonnet | 2 |
| R1 | Thống nhất âm cấp chữ | Opus | 1 |
| R2, R3 | Review tập khó, khác dùng, `needs_review`, mẫu | Opus | 7 |
| R4 | Kiểm lại toàn bộ `cung_dung` | Opus | 5 |
| R5 | Rà cuối có lọc | Opus | 2 |
| R6 | Hồ sơ nguồn và công cụ âm bổ sung; áp quyết định và sửa công cụ | Sonnet | 2 (1 agent được gọi lại để sửa) |
| R6 | Quyết âm chữ đáng ngờ; kiểm độc lập quyết định | Opus | 2 |
| Điều phối | Tiêu chuẩn, chia lô, quyết định, sửa nhỏ, hợp nhất, báo cáo | Opus (Claude) | 1 |

**Tổng:** 36 agent Sonnet, 20 agent Opus. Mỗi reviewer kiểm tập do agent **khác** soạn. Nhật ký chi tiết từng pha ở `CHECKPOINT.md`; log từng mục ở `06_review/log_r*_*.tsv`.
