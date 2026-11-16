# R6: kiểm độc lập quyết định âm và việc áp

*Reviewer độc lập, model: Opus, 16/11/2026. Không phải agent đã quyết. Phạm vi: 86 chữ trong hồ sơ R6. Không xét nhãn `loai`, không xét chữ ngoài hồ sơ. Script kiểm nằm ở scratchpad (`work/r6_verify/verify.py`). Đề xuất sửa: `de_xuat_sua.json`.*

## Kết luận

- **Quyết định âm:** đồng ý cả 86 chữ.
  - Đổi âm: đồng ý 6/6.
  - 吹: đồng ý 1/1. char_note đúng sự thật.
  - needs_review: đồng ý 31/31.
  - Giữ: đồng ý 49/49 (gồm 吹).
  - Không có quyết định nào sai rõ ràng.
- **Việc áp:** đủ 53 mục, đúng `hanviet`, `status`, `review_reason`. Có 3 nhóm lỗi khi áp. Không lỗi nào làm đổi âm.
  1. 4 mục có `pt_noi_dung` bị dính dấu ngoặc kép do lỗi quoting CSV: 守株待兔, 吹牛, 卡片, 卡通.
  2. `char_note` cấp mục của 乒乓球 bị cụt.
  3. 13 mục needs_review vẫn còn `tone_flags` trên chữ `uncertain`. Điều này trái TIEU_CHUAN mục 3.
- **Không có thay đổi ngoài quyết định.** 10.843 mục không thuộc fixes_r6/fixes_r9 giữ nguyên `hanviet`, `nghia_vi`, `loai`, `status`, `tu_viet`, `khac_biet`, `review_reason`, `phan_tich`, `hanviet_chars` so với merged_v4.

## 1. Sáu quyết định đổi âm

Đã đối chiếu từng trích dẫn Thiều Chửu với `01_sources/thieuchuu/hanviet/dataV4.json`. Số "#N" trong hồ sơ là chỉ số đếm từ 0 trong mảng dữ liệu, và khớp cả 8 số.

| Chữ | Quyết định | Kết luận | Bằng chứng, nhận xét |
|---|---|---|---|
| 兔 | thỏ → thố | **Đồng ý** (theo chỉ thị) | Xem mục 1a. |
| 踹 | đoán → sủy | **Đồng ý** | TC #8880, am_han `đoán, sủy`: "Dọi gót chân xuống đất. Một âm là {sủy}. Xéo nát." Nghĩa mục là "đá, đạp mạnh", gần "xéo nát" hơn "dọi gót". sủy là âm của cùng chữ trong TC, có sẵn trong cands. Lập luận âm tiết (chuài ~ 揣 chuǎi = sủy; đoán ~ duàn) hợp lý. hvpinyin chỉ có "soại". |
| 滴 | tích → trích | **Đồng ý** | TC #9558, am_han `tích, trích`: "Ta quen đọc là chữ {trích}. Nguyễn Trãi: {Điểm trích sổ tàn canh} [點滴數殘更]". Cả hai âm có nguồn. Chọn âm "ta quen đọc" là nhất quán với tiền lệ R1 (歪 oa, 幻 ảo). |
| 哈 | ha → cáp | **Đồng ý** (đảo R1, lý lẽ đứng vững) | Xem mục 1b. |
| 咖 | ca → già | **Đồng ý** (đảo R1, lý lẽ đứng vững) | Xem mục 1b. |
| 啃 | khẳng → khẩn | **Đồng ý** | Unihan xác nhận `U+5543 kSemanticVariant U+9F66<kFenn` (啃 → 齦). TC #2296 齦, am_han `ngân, khẩn`: "Một âm là {khẩn}. Cắn xương, nhá xương", đúng nghĩa "gặm". hvpinyin cũng có 齦 khẩn/ken3, khớp kěn. "khẳng" chỉ có ở hvpinyin, ghi pinyin `*`. Đã thêm cands_bosung, đúng R1 §1.1. Một lỗi nhỏ khi áp: `via` ghi "啃" thay vì "齦" (đề xuất ở JSON). |

### 1a. 兔: kiểm việc áp và cách ghi nguồn

- **Áp đúng, đủ mục.** Deck có đúng 2 mục chứa 兔, cả hai đã đổi:
  - 兔子: THỎ TỬ → THỐ TỬ;
  - 守株待兔: THỦ CHU ĐÃI THỎ → THỦ CHU ĐÃI THỐ.
- `hanviet_chars`: hv `thố`, source `wiktionary_web:https://en.wiktionary.org/wiki/兔`, certainty `chosen`.
- **"thỏ" giữ trong nghĩa Việt.**
  - `nghia_vi` "thỏ" và "ôm cây đợi thỏ…" không đổi.
  - `pt_noi_dung` viết "兔 thố (con thỏ)".
  - Câu "tiếng Việt nói 'ôm cây đợi thỏ'" vẫn giữ, nhưng ô này dính lỗi quoting (mục 4).
- **Nguồn ghi đúng.** Đã mở lại Wiktionary (en, trang 兔, mục Vietnamese) hôm nay. Trang ghi đúng như hồ sơ: "Hán Việt readings: thố[1][2][3][4]", "Nôm readings: thỏ[1][2][3], thò[1], xỏ[1]".
- **Điều phải nói rõ: các nguồn cục bộ đều ghi "thỏ" cho 兔, không nguồn nào ghi "thố".**
  - Bản Thiều Chửu số hóa: 兔 #6564 am_han `thỏ` ("Con thỏ… ngọc thỏ 玉兔"), và 兎 #5823 cũng ghi `thỏ`.
  - hvpinyin: `thỏ`.
  - Unihan kVietnamese: `thỏ`.
  - "thố" chỉ có từ Wiktionary web. Ngoài ra có một bằng chứng **gián tiếp**: chữ khác là 菟 (#8222, am_han `thỏ, thố, đồ`, "Cũng đọc là chữ {thố}").
  - Mục 菟 không phải mục của 兔, nên chỉ coi là gợi ý cùng dãy âm, không phải nguồn trực tiếp.
  - char_note, cands_bosung và bảng quyết định đều nói đúng điều này: "Thiều Chửu gián tiếp qua 菟…; bản Thiều Chửu số hóa ghi 兔 'thỏ'". Chấp nhận.
- **Ghi nhận về tài liệu:** ID `wiktionary_web:` được validator chấp nhận (`validate_drafts.py`), nhưng `01_sources/SOURCES.md` chưa đăng ký. SOURCES.md mục 3 còn ghi "không gọi API từng chữ". Nên bổ sung một dòng cho nguồn tra web thủ công này.

### 1b. 咖 và 哈: đảo quyết định R1

- R1 giữ 咖 "ca" ("phiên âm 咖啡") và 哈 "ha" ("thán từ tượng thanh"). Đó là ngoại lệ dựa trên nhận định, R1 không dẫn nguồn.
- R1 §1.5 quy định: âm chỉ có ở hvpinyin thì chỉ giữ khi (a) có từ Việt chứng thực, hoặc (b) chữ không có mục Thiều Chửu. Ngoài hai trường hợp đó thì theo Thiều Chửu.
- 咖 và 哈 đều có mục TC, và mục TC **phủ đúng nghĩa** của mục deck:
  - 咖 #5860, am_han `già`: "{Già phê} [咖啡] cây cà phê." Đây đúng là từ của mục.
  - 哈 #6609, am_han `cáp`: "{Cáp cáp} [哈哈] tiếng cười hầng hậc, khanh khách." Đúng nghĩa thán từ hā.
- "ca" và "ha" không có từ Hán Việt chứng thực. "Cà phê" là từ vay tiếng Pháp. "Cáp" có "Cáp Nhĩ Tân" (哈爾濱) chứng thực.
- Vậy ngoại lệ R1 không có cơ sở theo chính quy ước R1, và R6 sửa cho đúng là hợp lý.
- So với 呵 (giữ ha): nhất quán.
  - 呵 "ha" có hai nguồn (hvpinyin he1 và Unihan kVietnamese).
  - Mục TC của 呵 chỉ ghi `a` với nghĩa "tiếng giúp lời", không phủ nghĩa hē.
  - 哈 "ha" chỉ có ở hvpinyin, còn mục TC phủ đúng nghĩa.

## 2. 吹: char_note mới

**Đồng ý.** char_note mới viết: "Thiều Chửu #5304 ghi cùng chữ hai âm 'xuy, xúy': nghĩa thổi đọc xuy (xuy tiêu 吹簫, xuy địch 吹笛); 'Một âm là xúy', dùng trong 'cổ xúy' 鼓吹."

Kiểm với TC #5304 (am_han `xuy, xúy`): "Thổi. Như {xuy tiêu} [吹簫]…, {xuy địch} [吹笛]… Một âm là {xúy}. {Cổ xúy} [鼓吹], {nạo xúy} [鐃吹]…".

- Hai âm là của cùng một chữ: đúng.
- Số mục #5304: đúng.
- "Cổ xúy" đọc âm xúy: đúng.
- Wiktionary cũng ghi "xuy, xúy/xuý, súy/suý".

Giữ XUY cho 4 mục (nghĩa "thổi"; 吹捧 vẫn là "thổi phồng") là hợp lý. `hanviet` của 4 mục không đổi. char_note đã vào bản cuối đúng nguyên văn, riêng 吹捧 có thêm đoạn về 捧.

## 3. needs_review (31 chữ, 41 mục) và danh sách 49 chữ "giữ"

**needs_review: đồng ý 31/31.**

- Đã kiểm lại trực tiếp trong dataV4.json.
  - 29 chữ **không có mục TC**, cũng không xuất hiện trong phần nghĩa của mục khác: 啤 乒 乓 嗯 胳 捡/撿 搞 嘿 愣 叼 唬 咧 嗦 嘀 垮 憋 挎 捂 捅 掺/摻 揍 暨 沏 涮 溜 甩 趴 蹦.
  - 2 chữ **có mục TC nhưng khác nghĩa**:
    - 吭: `hàng, hạng`, nghĩa cổ họng, không phải kēng.
    - 卡: `tạp, khải`, nghĩa trạm canh/sở thuế, không phải "thẻ".
  - 橱 có TC `thụ`, nhưng TC giảng "Tục dùng như chữ thụ 樹", không phải nghĩa "tủ". Lý do ghi trong quyết định là đúng.
- Theo hồ sơ, âm đang dùng của cả 31 chữ chỉ có nguồn hvpinyin. Không có Unihan, kaikki hay Wiktionary cho cùng âm, và không có từ Việt chứng thực.
  - Unihan chỉ có âm khác, thường là Nôm: 胳 cặc, 搞 cào, 咧 lác, 垮 khoai, 捅 thòng.
  - Dị thể dẫn ra đều khác âm tiết hoặc khác nghĩa: 搞~攪 giảo, 嘿~默 mặc, 唬~諕/虓/猇, 甩~摔 suất.
  - Không chữ nào thực ra có nguồn thứ hai mà bị đặt nhầm needs_review.
- Ghi nhận: đặt needs_review cho chữ "không có mục TC" là siết chặt hơn R1 §1.5 (R1 cho giữ). Đây là nguyên tắc R6 ghi rõ ở đầu file quyết định và không đổi âm, nên tôi không phản đối.

**Giữ: đồng ý 49/49.** Không có chữ "giữ" nào mà âm chỉ dựa vào một mình hvpinyin không chứng thực. Từng nhóm:

- **Âm có trong Thiều Chửu:** 咱 gia (TC trực tiếp, và 喒 "gia môn"), 姥 mỗ, 椎 truy, 歪 oa, 哨 sáo, 吗 mạ, 撞 chàng, 晃 hoảng, 挣 tránh (qua 掙), 钉 đinh, 刹 sát, 玫 mai, 璃 lê, 侄 điệt, 仇 thù, 吹 xuy.
- **Hai nguồn từ điển:** 单 đơn, 份 phần, 帅 soái, 呵 ha, 惦 điếm. Nguồn thứ hai là Unihan kVietnamese.
  - 惦 là trường hợp yếu nhất: không có từ Việt, Unihan chỉ là "phiếu thứ ba" theo SOURCES.md.
  - Tuy vậy, nó đạt đúng tiêu chí R6 đã nêu ("có nguồn từ điển thứ hai"). Nếu anh muốn siết hơn nữa thì 惦 là ứng viên needs_review đầu tiên. Không coi là sai.
- **Chỉ có hvpinyin nhưng có từ Việt chứng thực:**
  - 带 đới (nhiệt đới), 延 diên (diên trì; địa danh Diên An), 扩 khuếch, 综 tổng (tổng hợp), 摆 bài (bài trí), 潮 trào (trào lưu), 迫 bức (áp bức), 姆 mẫu (bảo mẫu).
  - 旋 hoàn (khải hoàn), 勾 cấu (cấu kết), 去 khử (khử trùng), 叛 phản (phản nghịch), 峡 hiệp (Tam Hiệp), 胧 lung (mông lung), 萎 ủy (ủy mị), 礁 tiêu (ám tiêu), 饺 cảo (sủi cảo), 缅 miến (Miến Điện), 姐 tỷ.
  - Lưu ý nhỏ về 姐 tỷ: "tỷ muội" thường viết 姊妹. Từ chứng thực sát hơn cho 姐 là "đại tỷ" (大姐) và "tỷ tỷ". Điều này không đổi kết luận.
- **Nhiều âm có nguồn, chọn theo từ hoặc nghĩa:** 层, 分, 浓, 领, 并, 顶, 间, 裸.
- **什 thậm:** hvpinyin ghi riêng thậm cho shén, và nguồn gián tiếp TC 甚 có nghĩa nghi vấn (什麼 = 甚麼). Chấp nhận.

Đếm theo số note_key: 姥 2 mục, 姐 3 mục, 咧 2 mục, khác với số đếm theo lần xuất hiện trong hồ sơ (3/4/3) vì có từ lặp chữ như 姥姥, 姐姐, 大大咧咧. Không lệch.

## 4. Việc áp

Đối chiếu `quyet_dinh_am.json` → `06_review/fixes_r6_doc_am.tsv` → `07_final/hanviet_10898.jsonl` / `needs_review.tsv`, so với `merged_v4.jsonl`.

| Kiểm | Kết quả |
|---|---|
| Số dòng fixes_r6 | 53 = 8 mục đổi + 4 mục 吹 + 41 mục needs_review (乒乓球 gộp 1). Tập note_key trùng khít với JSON. |
| `hanviet` bản cuối | Khớp `hanviet_moi` (hoặc giữ nguyên) ở 53/53 mục. |
| `status` / `review_reason` | Khớp 53/53. Cả 41 mục needs_review có `hanviet_chars` của chữ đó ở mức `uncertain`; 8 mục đổi ở mức `chosen`. |
| `char_note` | Khớp 52/53. **Lệch 1:** 乒乓球 bị cụt thành "…; 乓=bàng (chỉ hvpinyin". Nguyên nhân: `finalize.py` `clean_note()` tách theo "; " (kể cả "; " nằm trong ngoặc) rồi bỏ đoạn trùng nội dung. Ghi chú trong `hanviet_chars` vẫn đủ. |
| `pt_noi_dung` | **Lệch 4 mục: 守株待兔, 吹牛, 卡片, 卡通.** `r6_apply.py` ghi bằng `csv.writer` mặc định (QUOTE_MINIMAL), nên ô có `"` bị bọc ngoặc và nhân đôi. Bước merge và finalize đọc với QUOTE_NONE, nên bản cuối (cả .jsonl và .tsv) mang nguyên văn kiểu `"tiếng Việt nói ""ôm cây đợi thỏ"": … (con thỏ)"`. Ba mục sau quyết định không hề đụng `pt_noi_dung`, vậy là đổi ngoài quyết định do lỗi định dạng. |
| `nghia_vi` / `loai` / `tu_viet` / `khac_biet` của 53 mục | Không đổi so với merged_v4. |
| `tone_flags` | **Lệch 13 mục (14 cờ):** chữ đã thành `uncertain` vẫn mang cờ `ngoai_le`. Gồm 卡 ×7, 啤酒, 乒乓球 (乓), 咧嘴, 大大咧咧 (2 cờ), 嘀咕, 捂. TIEU_CHUAN mục 3 chỉ cho gắn cờ khi certainty là sure hoặc chosen. |
| `07_final/needs_review.tsv` | 43 dòng = tập `status=needs_review` trong jsonl (41 mục R6 mới + 2 mục có từ trước). Khớp tuyệt đối cả hanviet và review_reason. Không mục needs_review cũ nào bị mất. |
| `cands_bosung` | Đã có 2 dòng (兔 thố, 啃 khẩn). Dòng 啃 ghi source `thieuchuu` mà thiếu "via 齦" ở trường source (via chỉ nằm trong evidence). Nhỏ. |
| Mục ngoài fixes_r6/r9 (10.843) | `hanviet`, `nghia_vi`, `loai`, `status`, `tu_viet`, `khac_biet`, `review_reason`, `phan_tich`, `hanviet_chars`: **0 khác biệt**. Chỉ có `char_note` cấp mục xuất hiện ở 2.297 mục, do finalize khôi phục từ TSV gốc. Đây là hành vi của finalize, không phải thay đổi R6, và các trường cần kiểm không đổi. |
| fixes_r9 (2 mục) | 裸体 KHỎA THỂ → LÕA THỂ; 未成年人 không đổi âm. Ngoài phạm vi R6, chỉ ghi nhận. |

## 5. Đề xuất (chi tiết trong `de_xuat_sua.json`)

Tất cả đề xuất là sửa lỗi áp, không đổi âm nào. Nên sửa ở gốc rồi chạy lại finalize:

1. **Sửa quoting.** Trong `r6_apply.py`, ghi với `quoting=csv.QUOTE_NONE` (hoặc thống nhất cách đọc) rồi sinh lại fixes_r6. Kết quả mong đợi: `pt_noi_dung` của 4 mục trở về giá trị trong JSON hoặc merged_v4.
2. **Sửa char_note 乒乓球.** Viết lại không có "; " trong ngoặc, ví dụ "乒=binh, 乓=bàng (cả hai chỉ hvpinyin, chưa có nguồn thứ hai) — giữ tạm, certainty: uncertain". Hoặc sửa `clean_note` để không tách bên trong ngoặc.
3. **Bỏ tone_flags của chữ uncertain** ở 13 mục: lọc theo certainty trong finalize hoặc tone_flags.py.
4. **Nhỏ.** 啃: đổi `via` thành 齦 và ghi via trong source của cands_bosung. Đăng ký `wiktionary_web` trong SOURCES.md.
