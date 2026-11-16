# R6: quyết định âm Hán Việt cho chữ nghi vấn

*Model: Opus, 16/11/2026. Đầu vào: `ho_so_nghi_van.md/.tsv`, `web_bang_chung.json`, `quy_uoc_doc_am_chot.md`, `r1_report.md` mục 6, `TIEU_CHUAN.md`. Dữ liệu máy đọc: `quyet_dinh_am.json` (Sonnet áp). Không đổi nhãn `loai` nào.*

## Tóm tắt

- 86 chữ: **giữ 49**, **đổi 6** (8 mục), **needs_review 31** chữ (41 mục, vì 乒乓球 chung một mục).
- Nguyên tắc needs_review: âm đang dùng chỉ có ở hvpinyin, không có nguồn từ điển thứ hai, không có từ Việt chứng thực, và không có âm Thiều Chửu áp được (chữ vắng Thiều Chửu, hoặc Thiều Chửu chỉ có âm cho nghĩa/âm tiết khác). Mục giữ nguyên âm trong `hanviet`, chỉ đổi `status`.
- Hai âm cùng có nguồn của một chữ (姥 mỗ/mụ, 吹 xuy/xúy) là chuyện chọn quy ước, không phải bất định về độ đúng: chọn một, ghi char_note, không đặt needs_review.
- Cần thêm 2 dòng `cands_bosung`: (兔, thố) và (啃, khẩn).

## Đổi âm

| Chữ | Cũ → mới | Mục (hanzi: cũ → mới) | Căn cứ |
|---|---|---|---|
| 兔 | thỏ → thố | 兔子: THỎ TỬ → THỐ TỬ; 守株待兔: THỦ CHU ĐÃI THỎ → THỦ CHU ĐÃI THỐ | Chỉ thị điều phối. Âm Hán Việt là THỐ: Wiktionary (en, trang 兔, truy cập 16/11/2026) ghi Hán Việt = thố, Nôm = thỏ/thò/xỏ; Thiều Chửu gián tiếp qua 菟 #8222 ('thỏ, thố, đồ'; 'Cũng đọc là chữ thố'). Bản Thiều Chửu số hóa ghi 兔 #6564 'thỏ'. 'thỏ' là từ Việt, giữ trong nghia_vi và có thể trong goi_nho. |
| 踹 | đoán → sủy | 踹: ĐOÁN → SỦY | Thiều Chửu #8880 ghi 'đoán, sủy': đoán = 'dọi gót chân xuống đất'; 'Một âm là sủy. Xéo nát'. Nghĩa mục (đá, đạp mạnh, giẫm) và âm tiết chuài khớp âm sủy (cùng kiểu ch-/s- như 揣 chuǎi = sủy, Thiều Chửu); đoán ứng âm tiết duàn. sủy có sẵn trong cands (thieuchuu). |
| 滴 | tích → trích | 滴: TÍCH → TRÍCH; 水滴石穿: THỦY TÍCH THẠCH XUYÊN → THỦY TRÍCH THẠCH XUYÊN | Thiều Chửu #9558 ghi 'tích, trích' và nói rõ 'Ta quen đọc là chữ trích', dẫn Nguyễn Trãi 'Điểm trích sổ tàn canh' 點滴數殘更. Cả hai âm đều có nguồn; theo chính lời Thiều Chửu về cách đọc quen của người Việt (cùng cách R1 đã xử lý 歪 'ta quen đọc oa'). trích có sẵn trong cands (thieuchuu). |
| 哈 | ha → cáp | 哈: HA → CÁP | Thiều Chửu #6609 chỉ ghi cáp, có cả nghĩa tiếng cười: 'Cáp cáp 哈哈 tiếng cười hầng hậc, khanh khách' (đúng nghĩa thán từ của mục). 'ha/hà' chỉ có ở hvpinyin; từ Việt chứng thực cáp: 'Cáp Nhĩ Tân' (哈爾濱). Theo quy ước R1 mục 1.5: chữ có mục Thiều Chửu thì theo Thiều Chửu. cáp có sẵn trong cands (thieuchuu). |
| 咖 | ca → già | 咖啡: CA PHÊ → GIÀ PHÊ | Thiều Chửu #5860 ghi 咖 'già' và nêu đúng từ này: 'Già phê 咖啡 cây cà phê'. 'ca' chỉ có ở hvpinyin, không có từ Việt Hán Việt chứng thực ('cà phê' là từ vay mượn tiếng Pháp, không phải âm Hán Việt). già có sẵn trong cands (thieuchuu). Đảo lại quyết định R1 ('ca, phiên âm') vì Thiều Chửu có mục trực tiếp cho 咖啡. |
| 啃 | khẳng → khẩn | 啃: KHẲNG → KHẨN | 啃 là dị thể nghĩa của 齦 (Unihan kSemanticVariant, có trong hồ sơ). Thiều Chửu 齦 #2296: 'ngân, khẩn… Một âm là khẩn. Cắn xương, nhá xương' (đúng nghĩa gặm); hvpinyin ghi 齦 khẩn cho ken3, khớp pinyin kěn. 'khẳng' chỉ có ở hvpinyin (mục 啃, pinyin *). Âm khẩn chưa nằm trong cands của 啃 → cần dòng cands_bosung. |

Câu `pt_noi_dung` cần sửa (đã ghi trong JSON): 兔子, 守株待兔 (兔 thỏ → 兔 thố (con thỏ)); 水滴石穿 (滴 tích → 滴 trích). Không mục nào bị ảnh hưởng ở `tu_viet`/`khac_biet`/`loai`.

## needs_review mới

| Chữ | Âm giữ tạm | Mục | Lý do |
|---|---|---|---|
| 吭 | khang | 一声不吭 | 吭 kēng (lên tiếng): âm 'khang' chỉ có ở hvpinyin, không có từ Việt chứng thực; Thiều Chửu chỉ ghi hàng/hạng với nghĩa cổ họng (háng), chưa chắc áp được cho kēng. |
| 卡 | ca | 信用卡, 卡, 银行卡, 卡片, 打卡, 卡车, 卡通 | 卡 kǎ (thẻ, chữ phiên âm card/car): âm 'ca' chỉ có ở hvpinyin (gắn theo ka3), không có nguồn thứ hai hay từ Việt chứng thực; Thiều Chửu chỉ ghi tạp/khải với nghĩa trạm canh, sở thuế (qiǎ), chưa chắc áp được cho nghĩa thẻ. |
| 啤 | bia | 啤酒 | 啤: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ. 'bia' trùng từ Việt vay mượn tiếng Pháp (bière), không phải từ Hán Việt. |
| 乒 | binh | 乒乓球 | 乒/乓: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực (binh, bàng); Thiều Chửu không có chữ. |
| 乓 | bàng | 乒乓球 | 乒/乓: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực (binh, bàng); Thiều Chửu không có chữ. |
| 嗯 | ân | 嗯 | 嗯: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ; char_note cũ đã nghi 'âm đặt tạm'. |
| 胳 | cách | 胳膊 | 胳: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực (cả dị thể 肐 cũng chỉ hvpinyin); Thiều Chửu không có chữ; Unihan chỉ ghi âm Nôm. |
| 捡 | kiểm | 捡 | 捡/撿: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ. |
| 搞 | cảo | 搞, 搞笑, 搞鬼 | 搞: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ. Dị thể Unihan 攪 có Thiều Chửu 'giảo' (quấy) nhưng khác âm tiết (jiǎo) và khác nghĩa (làm) nên không thay được; Unihan 'cào' là âm Nôm. |
| 嘿 | hắc | 嘿 | 嘿 hēi: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ. Dị thể 默 mặc chỉ ứng âm mò (lặng im), không ứng thán từ hēi. |
| 愣 | lăng | 发愣, 愣 | 愣: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ. |
| 叼 | điêu | 叼 | 叼: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ. |
| 唬 | hổ | 吓唬 | 唬 hǔ: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ; các dị thể (諕 hào, 虓 hao, 猇 khiêu) khác âm tiết, không thay được. |
| 咧 | liệt | 咧嘴, 大大咧咧 | 咧: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ; Unihan chỉ ghi âm Nôm 'lác'. |
| 嗦 | sách | 哆嗦 | 嗦: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ. |
| 嘀 | đê | 嘀咕 | 嘀: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ. |
| 垮 | khỏa | 垮 | 垮: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ; Unihan chỉ ghi 'khoai'. |
| 憋 | biệt | 憋 | 憋: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ. |
| 挎 | khóa | 挎 | 挎: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ. |
| 捂 | ngộ | 捂 | 捂: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ. |
| 捅 | thống | 捅 | 捅: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ; Unihan chỉ ghi âm Nôm 'thòng'. |
| 掺 | sam | 掺 | 掺/摻: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực (hvpinyin sam cho chān, sảm cho shǎn); Thiều Chửu không có chữ. |
| 揍 | tấu | 揍 | 揍: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ. |
| 暨 | kỵ | 暨 | 暨: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ. |
| 橱 | trù | 橱窗 | 橱/櫥 (tủ): âm 'trù' chỉ có ở hvpinyin, không có từ Việt chứng thực; Thiều Chửu ghi 橱 'thụ' nhưng giảng 'tục dùng như chữ thụ 樹' (nghĩa cây), không khớp nghĩa tủ. |
| 沏 | thế | 沏 | 沏: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ. |
| 涮 | xuyến | 涮 | 涮: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ. |
| 溜 | lưu | 溜, 溜达 | 溜: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực (hvpinyin lưu/lựu); Thiều Chửu không có chữ. |
| 甩 | súy | 甩 | 甩: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ. Dị thể chuyên biệt 摔 có Thiều Chửu 'suất' (quẳng xuống đất) nhưng khác chữ, khác âm tiết (shuāi) nên chưa đủ để thay. |
| 趴 | bát | 趴 | 趴: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ. |
| 蹦 | bính | 蹦 | 蹦: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ. |

## Bảng đủ 86 chữ

| Chữ | Nhóm | Quyết định | Số mục | Căn cứ |
|---|---|---|---|---|
| 兔 | 1 | doi:thố | 2 | Chỉ thị điều phối. Âm Hán Việt là THỐ: Wiktionary (en, trang 兔, truy cập 16/11/2026) ghi Hán Việt = thố, Nôm = thỏ/thò/xỏ; Thiều Chửu gián tiếp qua 菟 #8222 ('thỏ, thố, đồ'; 'Cũng đọc là chữ thố'). Bản Thiều Chửu số hóa ghi 兔 #6564 'thỏ'. 'thỏ' là từ Việt, giữ trong nghia_vi và có thể trong goi_nho. |
| 吹 | 1 | giu | 4 | Chỉ thị điều phối. xuy và xúy là hai âm có nguồn của CÙNG chữ 吹 (Thiều Chửu #5304 'xuy, xúy'; Wiktionary: xuy, xúy/xuý, súy/suý). Nghĩa 'thổi' → xuy (xuy tiêu, xuy địch); xúy dùng trong 'cổ xúy' 鼓吹 (không có mục 鼓吹 trong deck). 吹捧 (tâng bốc) vẫn là 'thổi phồng' → xuy. Giữ XUY cho cả 4 mục; chỉ cập nhật char_note. |
| 咱 | 2 | giu | 1 | Thiều Chửu #6626 ghi 'cha, gia'; mục dị thể 喒 #8459: 'Về phương bắc kêu là chữ gia. Như gia môn 喒門 chúng ta', đúng từ 咱们. 'ta' (hvpinyin/kaikki) là đại từ thuần Việt, không dùng làm âm Hán Việt. |
| 姥 | 2 | giu | 2 | Thiều Chửu ghi 'mỗ, mụ' (cùng chữ). Cả hai đều là âm Hán Việt có nguồn; không từ Việt nào chứng thực riêng âm nào. Giữ mỗ (âm đầu của Thiều Chửu, R1 đã chọn), không phải bất định về độ đúng nên không đặt needs_review. 'lão' chỉ có ở hvpinyin (theo pinyin lǎo). |
| 踹 | 2 | doi:sủy | 1 | Thiều Chửu #8880 ghi 'đoán, sủy': đoán = 'dọi gót chân xuống đất'; 'Một âm là sủy. Xéo nát'. Nghĩa mục (đá, đạp mạnh, giẫm) và âm tiết chuài khớp âm sủy (cùng kiểu ch-/s- như 揣 chuǎi = sủy, Thiều Chửu); đoán ứng âm tiết duàn. sủy có sẵn trong cands (thieuchuu). |
| 椎 | 2 | giu | 1 | 颈椎 jǐng zhuī: Thiều Chửu 'truy, trùy' (trùy là âm khác: 'còn có âm là trùy' cho cái vồ/búi tóc). Âm tiết zhuī ứng truy; hvpinyin chuy/trùy/chùy gắn với chuí (槌). Giữ truy. |
| 歪 | 2 | giu | 2 | Thiều Chửu: 'oai, oa… Ta quen đọc là chữ oa'. Giữ oa. |
| 滴 | 2 | doi:trích | 2 | Thiều Chửu #9558 ghi 'tích, trích' và nói rõ 'Ta quen đọc là chữ trích', dẫn Nguyễn Trãi 'Điểm trích sổ tàn canh' 點滴數殘更. Cả hai âm đều có nguồn; theo chính lời Thiều Chửu về cách đọc quen của người Việt (cùng cách R1 đã xử lý 歪 'ta quen đọc oa'). trích có sẵn trong cands (thieuchuu). |
| 哨 | 2 | giu | 2 | Thiều Chửu: 'Một âm là sáo. Sáo tử 哨子 cái còi… tuần sáo, phóng sáo'; khớp cả nghĩa còi và chốt gác; hvpinyin cũng ghi sáo. Ghi nhận: từ Việt 'tiền tiêu' 前哨 đọc 'tiêu' (pt của 哨 đã nhắc), không đổi âm mục. |
| 吗 | 2 | giu | 1 | Thiều Chửu 嗎 #219 'mạ': 'Tục dùng làm tiếng giúp lời'. 'ma' chỉ có ở hvpinyin. Giữ mạ (hu_tu). |
| 撞 | 2 | giu | 4 | Thiều Chửu và Unihan đều ghi chàng ('chàng chung 撞鐘 đánh chuông'); 'tràng' chỉ có ở hvpinyin. Giữ chàng. |
| 晃 | 2 | giu | 4 | Thiều Chửu + hvpinyin đều ghi hoảng; 'hoàng' chỉ có ở hvpinyin. Giữ hoảng. |
| 挣 | 2 | giu | 2 | Thiều Chửu (via 掙) + Unihan ghi tránh; 'tranh' chỉ có ở hvpinyin. Giữ tránh. |
| 钉 | 2 | giu | 4 | đinh có ở cả ba nguồn và là từ Việt 'đinh'; 'đính' chỉ có ở hvpinyin (dìng). Giữ đinh. |
| 刹 | 2 | giu | 2 | sát có ở Thiều Chửu + hvpinyin; từ Việt 'sát na' 刹那, 'cổ sát'. 'sa' chỉ có ở hvpinyin (shā). Giữ sát. |
| 呵 | 2 | giu | 2 | ha có hai nguồn (hvpinyin hē + Unihan kVietnamese); Thiều Chửu chỉ ghi âm 'a' (tiếng đệm, nghĩa khác). Giữ ha. |
| 哈 | 2 | doi:cáp | 1 | Thiều Chửu #6609 chỉ ghi cáp, có cả nghĩa tiếng cười: 'Cáp cáp 哈哈 tiếng cười hầng hậc, khanh khách' (đúng nghĩa thán từ của mục). 'ha/hà' chỉ có ở hvpinyin; từ Việt chứng thực cáp: 'Cáp Nhĩ Tân' (哈爾濱). Theo quy ước R1 mục 1.5: chữ có mục Thiều Chửu thì theo Thiều Chửu. cáp có sẵn trong cands (thieuchuu). |
| 吭 | 2 | needs_review | 1 | 吭 kēng (lên tiếng): âm 'khang' chỉ có ở hvpinyin, không có từ Việt chứng thực; Thiều Chửu chỉ ghi hàng/hạng với nghĩa cổ họng (háng), chưa chắc áp được cho kēng. |
| 什 | 2 | giu | 2 | 什么 shén: hvpinyin ghi riêng thậm cho shén (thập cho shí). Nguồn thứ hai gián tiếp: 什麼 = 甚麼, và Thiều Chửu 甚 'thậm… Nào. Như thậm nhật quy lai 甚日歸來 ngày nào trở về' (nghĩa nghi vấn); từ Việt 'thậm chí'. Thập (Thiều Chửu/Unihan) là âm cho nghĩa 'mười', sai âm tiết shén. Giữ thậm. |
| 缅 | 2 | giu | 1 | Từ Việt 'Miến Điện' (緬甸) chứng thực âm miến của chính chữ này, cùng pinyin miǎn; Thiều Chửu ghi miễn/diến nhưng không tách âm theo nghĩa. Giữ miến (R1). |
| 姐 | 3 | giu | 3 | tỷ: từ Việt 'tỷ muội', 'tỷ tỷ' (hvpinyin); thư theo từ Việt 'tiểu thư' cho 小姐 (Thiều Chửu). Giữ theo từ như hiện tại. |
| 饺 | 3 | giu | 1 | cảo: từ Việt 'sủi cảo', 'há cảo' (hvpinyin). Giữ. |
| 咖 | 3 | doi:già | 1 | Thiều Chửu #5860 ghi 咖 'già' và nêu đúng từ này: 'Già phê 咖啡 cây cà phê'. 'ca' chỉ có ở hvpinyin, không có từ Việt Hán Việt chứng thực ('cà phê' là từ vay mượn tiếng Pháp, không phải âm Hán Việt). già có sẵn trong cands (thieuchuu). Đảo lại quyết định R1 ('ca, phiên âm') vì Thiều Chửu có mục trực tiếp cho 咖啡. |
| 卡 | 3 | needs_review | 7 | 卡 kǎ (thẻ, chữ phiên âm card/car): âm 'ca' chỉ có ở hvpinyin (gắn theo ka3), không có nguồn thứ hai hay từ Việt chứng thực; Thiều Chửu chỉ ghi tạp/khải với nghĩa trạm canh, sở thuế (qiǎ), chưa chắc áp được cho nghĩa thẻ. |
| 单 | 3 | giu | 23 | đơn: hvpinyin + Unihan; từ Việt đơn giản, đơn vị, cô đơn, thực đơn. Giữ (R1). |
| 啤 | 3 | needs_review | 1 | 啤: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ. 'bia' trùng từ Việt vay mượn tiếng Pháp (bière), không phải từ Hán Việt. |
| 层 | 3 | giu | 9 | tầng: hvpinyin, Unihan, kaikki, Wiktionary; từ Việt tầng lớp, giai tầng. Giữ. |
| 带 | 3 | giu | 19 | đới: hvpinyin; từ Việt nhiệt đới, ôn đới, hàn đới. Giữ (R1). |
| 乒 | 3 | needs_review | 1 | 乒/乓: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực (binh, bàng); Thiều Chửu không có chữ. |
| 乓 | 3 | needs_review | 1 | 乒/乓: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực (binh, bàng); Thiều Chửu không có chữ. |
| 份 | 3 | giu | 8 | phần: hvpinyin + Unihan; từ Việt cổ phần. Giữ (R1). |
| 嗯 | 3 | needs_review | 1 | 嗯: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ; char_note cũ đã nghi 'âm đặt tạm'. |
| 帅 | 3 | giu | 1 | soái: hvpinyin + Unihan; từ Việt nguyên soái, thống soái. Giữ. |
| 胳 | 3 | needs_review | 1 | 胳: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực (cả dị thể 肐 cũng chỉ hvpinyin); Thiều Chửu không có chữ; Unihan chỉ ghi âm Nôm. |
| 延 | 3 | giu | 10 | diên: hvpinyin; từ Việt diên trì. Giữ (R1). |
| 分 | 3 | giu | 55 | phân/phận/phần theo từ (thành phần, phần tử; bổn phận…). Giữ (R1). |
| 扩 | 3 | giu | 7 | khuếch: hvpinyin; từ Việt khuếch đại, khuếch tán, khuếch trương. Giữ. |
| 捡 | 3 | needs_review | 1 | 捡/撿: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ. |
| 搞 | 3 | needs_review | 3 | 搞: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ. Dị thể Unihan 攪 có Thiều Chửu 'giảo' (quấy) nhưng khác âm tiết (jiǎo) và khác nghĩa (làm) nên không thay được; Unihan 'cào' là âm Nôm. |
| 浓 | 3 | giu | 5 | nồng: hvpinyin, kaikki, Wiktionary; từ Việt nồng độ, nồng hậu. Giữ. |
| 玫 | 3 | giu | 1 | mai: hvpinyin + Thiều Chửu (via 玟); từ Việt 'mai khôi'. Giữ. |
| 璃 | 3 | giu | 1 | lê: hvpinyin + Unihan; từ Việt 'pha lê'. Giữ. |
| 综 | 3 | giu | 3 | tổng (综合 tổng hợp) / tông (错综). Giữ (R1). |
| 领 | 3 | giu | 25 | lãnh/lĩnh theo nghĩa (lãnh đạo, lãnh thổ / lĩnh vực, chiếm lĩnh). Giữ (R1). |
| 侄 | 3 | giu | 1 | điệt: Thiều Chửu 侄 'Tục mượn làm chữ điệt 姪 cháu' + Thiều Chửu 姪 điệt + hvpinyin. Giữ. |
| 并 | 3 | giu | 11 | tịnh (並) / tính (併, thôn tính). Giữ (R1). |
| 嘿 | 3 | needs_review | 1 | 嘿 hēi: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ. Dị thể 默 mặc chỉ ứng âm mò (lặng im), không ứng thán từ hēi. |
| 顶 | 3 | giu | 7 | đỉnh: hvpinyin, kaikki, Wiktionary; từ Việt đỉnh, đỉnh cao. Giữ. |
| 摆 | 3 | giu | 7 | bài: hvpinyin; từ Việt bài trí. Giữ (R1). |
| 潮 | 3 | giu | 7 | triều/trào theo nghĩa; từ Việt trào lưu, cao trào. Giữ (R1). |
| 迫 | 3 | giu | 12 | bách/bức theo từ Việt (cưỡng bách, cấp bách / áp bức, bức thiết). Giữ. |
| 间 | 3 | giu | 26 | gian/gián theo từ Việt (gián tiếp, gián đoạn). Giữ. |
| 仇 | 3 | giu | 4 | thù: Thiều Chửu (via 讎) + hvpinyin + Unihan; từ Việt thù hận, báo thù. Giữ. |
| 姆 | 3 | giu | 1 | mẫu: từ Việt 'bảo mẫu' (保姆). Giữ. |
| 旋 | 3 | giu | 6 | toàn; riêng 凯旋 hoàn theo từ Việt 'khải hoàn'. Giữ (R1). |
| 勾 | 3 | giu | 3 | câu; riêng 勾结 cấu theo từ Việt 'cấu kết'. Giữ. |
| 去 | 3 | giu | 19 | khứ; khử cho nghĩa loại bỏ theo từ Việt trừ khử, khử trùng. Giữ. |
| 愣 | 3 | needs_review | 2 | 愣: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ. |
| 叛 | 3 | giu | 2 | phản: hvpinyin; từ Việt phản bội, phản nghịch. Giữ. |
| 叼 | 3 | needs_review | 1 | 叼: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ. |
| 唬 | 3 | needs_review | 1 | 唬 hǔ: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ; các dị thể (諕 hào, 虓 hao, 猇 khiêu) khác âm tiết, không thay được. |
| 咧 | 3 | needs_review | 2 | 咧: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ; Unihan chỉ ghi âm Nôm 'lác'. |
| 嗦 | 3 | needs_review | 1 | 嗦: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ. |
| 啃 | 3 | doi:khẩn | 1 | 啃 là dị thể nghĩa của 齦 (Unihan kSemanticVariant, có trong hồ sơ). Thiều Chửu 齦 #2296: 'ngân, khẩn… Một âm là khẩn. Cắn xương, nhá xương' (đúng nghĩa gặm); hvpinyin ghi 齦 khẩn cho ken3, khớp pinyin kěn. 'khẳng' chỉ có ở hvpinyin (mục 啃, pinyin *). Âm khẩn chưa nằm trong cands của 啃 → cần dòng cands_bosung. |
| 嘀 | 3 | needs_review | 1 | 嘀: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ. |
| 垮 | 3 | needs_review | 1 | 垮: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ; Unihan chỉ ghi 'khoai'. |
| 峡 | 3 | giu | 2 | hiệp: hvpinyin; từ Việt 'Tam Hiệp' (三峽). Giữ (R1). |
| 惦 | 3 | giu | 1 | điếm có hai nguồn (hvpinyin + Unihan kVietnamese). Giữ. |
| 憋 | 3 | needs_review | 1 | 憋: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ. |
| 挎 | 3 | needs_review | 1 | 挎: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ. |
| 捂 | 3 | needs_review | 1 | 捂: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ. |
| 捅 | 3 | needs_review | 1 | 捅: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ; Unihan chỉ ghi âm Nôm 'thòng'. |
| 掺 | 3 | needs_review | 1 | 掺/摻: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực (hvpinyin sam cho chān, sảm cho shǎn); Thiều Chửu không có chữ. |
| 揍 | 3 | needs_review | 1 | 揍: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ. |
| 暨 | 3 | needs_review | 1 | 暨: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ. |
| 胧 | 3 | giu | 1 | lung: từ Việt 'mông lung'. Giữ. |
| 萎 | 3 | giu | 2 | ủy: từ Việt 'ủy mị' (萎靡). Giữ. |
| 橱 | 3 | needs_review | 1 | 橱/櫥 (tủ): âm 'trù' chỉ có ở hvpinyin, không có từ Việt chứng thực; Thiều Chửu ghi 橱 'thụ' nhưng giảng 'tục dùng như chữ thụ 樹' (nghĩa cây), không khớp nghĩa tủ. |
| 沏 | 3 | needs_review | 1 | 沏: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ. |
| 涮 | 3 | needs_review | 1 | 涮: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ. |
| 溜 | 3 | needs_review | 2 | 溜: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực (hvpinyin lưu/lựu); Thiều Chửu không có chữ. |
| 甩 | 3 | needs_review | 1 | 甩: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ. Dị thể chuyên biệt 摔 có Thiều Chửu 'suất' (quẳng xuống đất) nhưng khác chữ, khác âm tiết (shuāi) nên chưa đủ để thay. |
| 礁 | 3 | giu | 1 | tiêu: từ Việt 'ám tiêu' (暗礁, đá ngầm). Ghi nhận Thiều Chửu ghi tiều đúng nghĩa đá ngầm; nếu muốn chặt theo Thiều Chửu có thể đổi tiều, nhưng căn cứ R1 vẫn đứng. |
| 裸 | 3 | giu | 3 | khỏa (khỏa thân) / lõa (lõa thể) theo từ Việt, đã chốt ở điều phối r9. Giữ. |
| 趴 | 3 | needs_review | 1 | 趴: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ. |
| 蹦 | 3 | needs_review | 1 | 蹦: âm chỉ có ở hvpinyin, không có nguồn từ điển thứ hai/từ Việt chứng thực; Thiều Chửu không có chữ. |

## cands_bosung

| Chữ | Âm | Nguồn | Bằng chứng |
|---|---|---|---|
| 兔 | thố | wiktionary_web:https://en.wiktionary.org/wiki/兔 | Wiktionary (en), trang 兔, truy cập 2026-11-16: 'Hán Việt readings: thố / Nôm readings: thỏ, thò, xỏ'. Gián tiếp Thiều Chửu: 菟 #8222 am_han 'thỏ, thố, đồ', 'Cũng đọc là chữ thố' (bản số hóa ghi 兔 #6564 'thỏ'). |
| 啃 | khẩn | thieuchuu(via 齦 #2296);hvpinyin(via 齦, ken3) | 啃 kSemanticVariant 齦 (Unihan). Thiều Chửu 齦 #2296 am_han 'ngân, khẩn': 'Một âm là khẩn. Cắn xương, nhá xương.' hvpinyin: 齦:['khẩn']/ken3. |

## Ghi chú cho người áp

- 吹: không đổi `hanviet`; chỉ thay `char_note` ở 4 mục (吹, 吹捧, 吹牛, 风吹雨打).
- Các chữ đổi âm dùng âm đã có trong cands (sủy, trích, già, cáp) trừ thố và khẩn (cần cands_bosung trước khi validator chạy).
- 咖 và 哈 đảo quyết định R1: Thiều Chửu có mục trực tiếp cho đúng nghĩa (咖啡 'già phê'; 哈哈 'cáp cáp'), nên theo quy ước R1 mục 1.5 phải theo Thiều Chửu.
- 礁: giữ tiêu (từ Việt 'ám tiêu'), nhưng Thiều Chửu ghi tiều đúng nghĩa; anh có thể đổi nếu muốn chặt.

