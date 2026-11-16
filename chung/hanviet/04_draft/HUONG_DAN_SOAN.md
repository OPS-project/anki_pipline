# Hướng dẫn soạn nháp Hán Việt (cho agent soạn)

*Điều phối viết ngày 16/11/2026. Đọc kèm `../TIEU_CHUAN.md` (mục 1–6). Khi hai file mâu thuẫn, TIEU_CHUAN.md thắng.*

Người dùng cuối là người Việt, đang học tiếng Trung nghe-trước, biết tiếng Nhật và đọc tiếng Anh tốt. Họ muốn dùng Hán Việt để **hiểu và nhớ nghĩa từ**. Nội dung của bạn hiện ở mặt sau thẻ Anki, nên phải **ngắn, đúng, tự nhiên**.

## Quy trình làm việc (bắt buộc)

1. Đọc file đầu vào bằng Read, theo từng khúc khoảng 100 dòng (offset/limit), chỉ trong khoảng dòng được giao. Dòng 1 là header.
2. Soạn xong mỗi khúc thì ghi ngay bằng Write vào `04_draft/out/_parts/<tên_phần>_kNN.tsv` (NN = 01, 02…), **không có header**. Mỗi dòng 11 cột cách nhau bằng **ký tự TAB thật**, theo đúng thứ tự ở mục 5 TIEU_CHUAN.
3. Hết khoảng dòng được giao thì ghép các khúc thành `04_draft/out/<tên_phần>.tsv`, có header 11 cột ở dòng đầu. Kiểm: số dòng dữ liệu = số mục được giao; mỗi dòng đúng 11 cột; không trùng `note_key`. Có thể dùng một lệnh Python nhỏ, chạy bằng `/c/Python314/python -I`.
4. Không đọc hay ghi file của agent khác. Không sửa file đầu vào.
5. **File tạm** (script chuyển đổi, bản rút gọn…) chỉ được để trong thư mục riêng `C:/Users/trinh-v/AppData/Local/Temp/claude/ad1c1fd31c67307a/43f64388-07fc-4045-ac80-4a54f3550946/scratchpad/work/hanviet_draft/<tên_phần>/`. Không dùng thư mục scratchpad gốc, vì nhiều agent chạy song song và đã có vụ ghi đè nhau. Nếu soạn ở dạng rút gọn, mỗi dòng phải chứa `note_key` hoặc chính chữ Hán của mục, để kiểm được khớp dòng.

## Cột `hanviet`

- Ghi `=` khi `hv_pre` không có `?` và đúng với nghĩa của từ.
- Khi có `?` hoặc `hv_pre` sai nghĩa, chọn âm trong `hv_cands` (**chỉ được chọn trong danh sách này**) theo thứ tự ưu tiên:
  1. Tiếng Việt có từ Hán Việt tương ứng thì dùng âm của từ đó. Ví dụ: 过程 → QUÁ TRÌNH, 过去 → QUÁ KHỨ, 经过 → KINH QUA.
  2. Không có thì chọn âm ứng với nghĩa chữ đang dùng: 行 xíng → hành, 行 háng → hàng; 子 → tử (chỉ đọc "tí" khi là địa chi); 不 → bất; 西 → tây; 气 → khí.
  3. Chữ mang thanh nhẹ (ví dụ 东西 dōngxi, 客气 kèqi): vẫn lấy âm Hán Việt của chữ gốc (TÂY, KHÍ).
- Ghi lý do vào `char_note` khi chọn khác `hv_pre` hoặc thay `?`, ví dụ `过=quá (quá trình)`.
- **Quy ước đã thống nhất** (thêm 16/11, sau các lô đầu):
  - 单 dān → **ĐƠN** (đơn giản, đơn vị). Script hay chọn sai thành ĐAN.
  - 调 tiáo (điều chỉnh, điều tra) → **ĐIỀU**; 调 diào → ĐIỆU.
  - 要 theo pinyin: yào → YẾU (trọng yếu), yāo → YÊU (yêu cầu).
- Khi **từ Việt dùng một âm không có trong `hv_cands`** (ví dụ 资源 "tài nguyên" trong khi nguồn chỉ cho 资 = tư), xử lý như sau: **không** tự thêm âm; giữ âm có nguồn trong `hanviet`; ghi từ Việt thật vào `tu_viet`; ghi vào `char_note` "từ Việt đọc 'tài'"; vẫn để `draft`.
- Các chữ nhiều âm khác (推 suy/thôi, 当 đương/đáng, 尽 tận/tẫn…): chọn theo nghĩa và ghi `char_note`. Một agent review sẽ thống nhất toàn bộ sau.
- Thật sự không chọn được thì giữ `?` ở chữ đó, đặt `status=needs_review`, ghi `review_reason`.

## Cột `nghia_vi`

- Tiếng Việt hiện đại, tự nhiên, ngắn (thường dưới 12 từ), **đúng nghĩa trong câu ví dụ** (`sentence` / `sentence_en`).
- `cv_vi` (CVDICT) phần lớn do máy dịch: dùng làm gợi ý, nhưng phải sửa lỗi dịch và bỏ phần rác như "LT:個|个[ge4]".
- Từ nhiều nghĩa: ghi nghĩa trong câu trước, có thể thêm `; cũng: …` (tối đa một nghĩa phụ phổ biến).
- Không chứa chữ Hán, không chứa tiếng Anh.
- Lượng từ / hư từ: mô tả chức năng ngắn gọn. Ví dụ 个: "lượng từ chung (cái, con, người…)"; 了: "trợ từ chỉ hành động đã xong / thay đổi trạng thái".

## Cột `loai`: hỏi theo thứ tự này

1. **Hư từ**, trợ từ, lượng từ, giới từ, liên từ có chức năng ngữ pháp → `hu_tu`. Ví dụ: 的, 了, 吗, 个, 把, 被, 就, 都.
2. Từ **phiên âm** tiếng nước ngoài (咖啡, 沙发, 巧克力) → `phien_am`. **Tên riêng** → `ten_rieng`.
3. Tiếng Việt **ngày nay** có từ Hán Việt này (người Việt bình thường hiểu được) không?
   - Có, nghĩa về cơ bản giống → `cung_dung`, điền `tu_viet`. Ví dụ: 永远 vĩnh viễn, 经济 kinh tế, 学生 học sinh, 注意 chú ý.
   - Có, nhưng nghĩa hoặc cách dùng khác đáng kể → `khac_dung`, điền `tu_viet` + `khac_biet`. Ví dụ: 东西 đông tây (tiếng Trung: đồ vật); 环境 hoàn cảnh (tiếng Trung: môi trường); 爱人 ái nhân (vợ/chồng); 新闻 tân văn (tin tức); 点心 điểm tâm (tiếng Trung: bánh ngọt, đồ ăn nhẹ; tiếng Việt: bữa sáng).
4. Không có từ đó, nhưng các chữ đóng góp nghĩa rõ → `ghep_nghia`. Ví dụ: 手机 thủ cơ, 气温 khí ôn.
5. **Từ một chữ** (hoặc từ mà tiếng Việt không dùng đứng riêng), nhưng âm Hán Việt quen trong từ Việt khác **cùng nghĩa** → `yeu_to`. `pt_noi_dung` nêu 1–2 từ Việt thông dụng. Ví dụ: 书 THƯ, `goi_nho` "như thư viện, thư pháp". 汗 HÃN: không có từ Việt thông dụng → `khong_giup`.
   - Nếu âm Hán Việt **đứng riêng là một từ Việt** cùng nghĩa (茶 trà) → `cung_dung`.
   - Nếu đứng riêng là từ Việt nghĩa khác (书 thư = lá thư) → vẫn có thể là `yeu_to`, nhưng thêm `khac_biet`: "'thư' đứng riêng trong tiếng Việt là lá thư".
6. Hán Việt không giúp hiểu hay nhớ (từ khẩu ngữ, chữ hầu như không gặp trong tiếng Việt) → `khong_giup`. Ví dụ 搞, 啤 (nếu không phải phiên âm), 嘿.

**Không thổi phồng `cung_dung`.** Chỉ dùng khi người Việt hiện đại thật sự dùng từ đó. "Khí ôn", "thủ cơ" không phải từ Việt, nên là `ghep_nghia`. Không chắc thì chọn nhãn yếu hơn, hoặc `needs_review` kèm lý do.

## Cột `khac_biet`

Một câu, có chừng mực, không dùng "luôn luôn / không bao giờ". Ví dụ: "Tiếng Trung chủ yếu nghĩa 'môi trường, điều kiện xung quanh'; tiếng Việt 'hoàn cảnh' thường chỉ tình cảnh của người."

## Cột `pt_kieu` / `pt_noi_dung`

**Chỉ ghi khi thật sự giúp hiểu hoặc nhớ.** Khoảng một nửa số mục để trống là bình thường. Từ `cung_dung` hiển nhiên (học sinh) thì không cần.

- `cau_tao`: tách thành tố, nghĩa từng chữ lấy theo `tc_char` (Thiều Chửu) và **đúng là nghĩa đang tham gia vào từ**. Ví dụ: `气 khí (hơi, không khí) + 温 ôn (ấm, nhiệt) → nhiệt độ không khí`.
- `goi_nho`: liên tưởng của bạn, ví dụ `手 tay + 机 máy → máy cầm tay`, hoặc từ Việt cùng yếu tố. **Không** viết như thể đó là từ nguyên.
- **Không** viết nguồn gốc lịch sử, điển tích hay thành ngữ gốc trừ khi chắc chắn và phổ biến. Không chắc thì bỏ.
- Ngắn, dưới 20 từ. Được dùng chữ Hán của chính từ đó trong phân tích.

## Khi nào `needs_review`

Áp dụng TIEU_CHUAN mục 4. Thêm ba trường hợp:
- `meaning_en` và câu ví dụ có vẻ lệch nhau.
- Không chắc từ Việt có thật hay đúng nghĩa.
- Thành ngữ bốn chữ khó.

**Đừng lạm dụng.** Mục bình thường mà bạn chắc thì để `draft`.

## Ví dụ dòng đầu ra

Các cột cách nhau bằng TAB; ở đây hiển thị là `⇥`.

```
zh:…:1792758601212⇥=⇥nhiệt độ không khí⇥ghep_nghia⇥⇥⇥cau_tao⇥气 khí (hơi) + 温 ôn (ấm) → độ ấm của không khí⇥draft⇥⇥
zh:…:1792758601214⇥=⇥mãi mãi, vĩnh viễn⇥cung_dung⇥vĩnh viễn⇥⇥⇥⇥draft⇥⇥
zh:…:1792758600040⇥ĐÔNG TÂY⇥đồ vật, thứ (đồ đạc)⇥khac_dung⇥đông tây⇥Nghĩa "đồ vật" khi đọc dōngxi (thanh nhẹ); tiếng Việt "đông tây" chỉ phương hướng⇥⇥⇥draft⇥⇥西=tây (thanh nhẹ, chữ gốc tây)
```
