# Hán Việt cho deck HSK: bàn giao

*Ngày 16/11/2026. Trạng thái: **xong phần dữ liệu và kiểm định**. Chưa build APKG, chưa import.*

Bộ dữ liệu gồm âm Hán Việt, nghĩa tiếng Việt, phân loại liên hệ Việt–Trung, phân tích hoặc gợi nhớ, và nhãn ngoại lệ thanh điệu cho **đủ 10.898 mục** của deck `Tiếng Trung HSK`. Toàn bộ là **bản nháp do AI biên soạn**, đã qua nhiều vòng kiểm tự động và review chéo giữa các agent, chưa có người thẩm định.

## Đọc gì trước

| File | Nội dung |
|---|---|
| `reports/bao_cao_kiem_dinh.md` | Đã kiểm gì, lỗi gì, đã sửa gì, độ phủ, hạn chế, agent và model |
| `reports/de_xuat_build.md` | Trường và bố cục thẻ đề xuất; quy trình kiểm import trên collection tạm |
| `reports/tom_tat_cho_Codex.md` | Tóm tắt và câu hỏi để Codex phản biện |
| `07_final/needs_review.tsv` | Mục còn chờ quyết |
| `06_review/quy_uoc_doc_am_chot.md` | Quy ước đọc âm đã chốt (phần đầu là sửa đổi của điều phối) |
| `01_sources/SOURCES.md` | Nguồn từ điển, phiên bản, giấy phép |

## Dữ liệu bàn giao (`07_final/`)

| File | Nội dung |
|---|---|
| `hanviet_10898.jsonl` | Dữ liệu đầy đủ, một dòng một mục, khóa `note_key` (kèm `anki_guid` / `anki_note_id`). Lược đồ ở `TIEU_CHUAN.md` |
| `hanviet_10898.tsv` | Bản phẳng để mở bằng Excel (UTF-8 BOM) |
| `stats.md` / `stats.json` | Thống kê |
| `merged_v1` … `v4` | Bản hợp nhất trung gian, giữ để truy vết |

## Cấu trúc thư mục

| Thư mục | Nội dung |
|---|---|
| `00_base/` | Kiểm kê deck |
| `01_sources/` | Nguồn tải về. **Lưu ý:** gồm dump kaikki 1,2 GB |
| `02_chars/` | Ứng viên âm theo chữ và theo mục |
| `03_tone/` | Quy tắc thanh điệu và dữ liệu đo |
| `04_draft/` | Đầu vào và bản soạn theo lô (Sonnet / Opus) |
| `05_validate/` | Kết quả validator |
| `06_review/` | Quy ước, đầu vào review, `fixes_*.tsv` (bản sửa từng vòng), `log_*.tsv` (nhật ký từng mục) |
| `07_final/` | Dữ liệu bàn giao |
| `scripts/` | Mọi script, tái lập được |
| `CHECKPOINT.md` | Nhật ký điều phối từng pha |

**Tái lập bản cuối:**

```
/c/Python314/python -I scripts/finalize.py --outdir 07_final
```

## Giấy phép và sử dụng

- Thiều Chửu (dataV4.json) không kèm giấy phép.
- CVDICT và CC-CEDICT theo CC BY-SA.

Chỉ dùng cho học cá nhân, **không phát hành lại** bộ dữ liệu hay deck chứa dữ liệu này.
