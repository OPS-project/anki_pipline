# Tóm tắt để Codex phản biện (thiết kế và lập luận, không chạy code)

*Claude (điều phối), 16/11/2026. Trả lời theo prompt Hán Việt do Codex soạn.*

## Đã làm theo yêu cầu

| Yêu cầu | Cách đáp ứng | Nơi xem |
|---|---|---|
| Đủ 10.898 mục, bám khóa gốc | `07_final/hanviet_10898.jsonl`; kiểm cuối 0 lỗi | `07_final/stats.md` |
| Âm Hán Việt có nguồn truy vết | Mỗi chữ ghi nguồn (Thiều Chửu / hvpinyin / Unihan…) và `certainty`; validator bắt âm ngoài ứng viên | `01_sources/SOURCES.md`, `02_chars/` |
| Giản → phồn nhiều chữ | Ưu tiên phồn thể theo entry từ điển khớp pinyin; OpenCC; còn mơ hồ thì vào tập khó cho Opus | `scripts/build_inputs.py` |
| Nghĩa hiện đại theo cả từ | Neo bằng `meaning_en` + câu ví dụ + CVDICT/CEDICT; không ghép nghĩa chữ | `TIEU_CHUAN.md` mục 2 |
| Tách cấu tạo / gợi nhớ / từ nguyên | `phan_tich.kieu` = `cau_tao` hoặc `goi_nho`. Không có trường từ nguyên nào được điền, vì không có nguồn. Đã xóa các khẳng định từ nguyên ngầm | `bao_cao_kiem_dinh.md` mục 2.3 |
| Nhãn bản nháp; `needs_review` có lý do | Mọi mục mang `label: "bản nháp AI"`; còn 43 `needs_review`, đúng bằng số bất định âm còn tồn tại sau R6 | `07_final/needs_review.tsv` |
| Thanh điệu chỉ là lớp hỗ trợ | Tài liệu đo có ghi giới hạn; nhãn "ngoại lệ" chỉ gắn khi đủ điều kiện | `03_tone/quy_tac_thanh_dieu.md` |
| Sonnet làm việc thường, Opus làm việc khó và kiểm định | 34 Sonnet, 18 Opus; reviewer luôn khác người soạn | `bao_cao_kiem_dinh.md` mục 6 |
| Lỗi hệ thống thì sửa cả nhóm | Âm Nôm (R1); chữ nhiều âm (R1); `cung_dung` thổi phồng (R4, **toàn bộ** 2.390 mục); lọc có mục tiêu (R5) | `bao_cao_kiem_dinh.md` mục 2.3 |
| Không build, không import | Không tạo APKG mới; bản build đang học không bị sửa | — |

## Điểm mong Codex phản biện

1. **Độ phủ review.** 5.905 mục (chủ yếu `ghep_nghia`) chỉ được kiểm qua mẫu 5% và các bộ lọc. Mẫu cho thấy khoảng 8–10% cần sửa, phần lớn là ranh giới nhãn. Có nên chi thêm một vòng review toàn bộ nhóm này không, hay để anh sửa dần khi học (tag `sai-hanviet`)?
2. **Nguyên tắc "không chắc thì hạ nhãn"** ở R4. Nguyên tắc này giảm thổi phồng nhưng hạ cả một số từ thông dụng. Ranh giới `cung_dung` nên đặt ở đâu?
3. **Âm theo nguồn nhưng lạ tai:** 奖 tưởng, 量 lương, 推 thôi, 领 lĩnh. Theo nguồn hay theo thói quen người Việt?
4. **Cách xử lý từ Việt đọc âm không có trong nguồn** (tài nguyên, thân phận): giữ âm nguồn và ghi chú "từ Việt đọc '…'". Có minh bạch đủ không, hay nên hiện âm từ Việt trên thẻ?
5. **Đề xuất bố cục và quy trình kiểm import** ở `reports/de_xuat_build.md`.
6. **Hạn chế trình bày:** "中 giữa" thay vì "中 trung (giữa)", khoảng 390 mục.

**Cập nhật R6 (theo phản hồi):**
- 兔 → THỐ ở mọi mục (nguồn Wiktionary).
- 吹: sửa phát biểu sai trong báo cáo; xuy và xúy cùng một chữ.
- Đổi 5 chữ theo Thiều Chửu.
- 41 mục âm chỉ có hvpinyin chuyển `needs_review`.
- Đề xuất build bản 2: không thêm trường, dùng `Notes`, giữ `char_note` và trạng thái chưa chắc trong phần thu gọn, ẩn cờ thanh.
