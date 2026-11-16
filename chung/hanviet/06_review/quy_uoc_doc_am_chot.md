# Quy ước đọc âm Hán Việt cấp chữ: bản chốt R1

*Reviewer R1 (model: Opus), 16/11/2026. Thay cho `quy_uoc_doc_am_de_xuat.md` (bản đề xuất). Áp dụng bằng `scripts/r1_apply.py` → `06_review/fixes_r1_doc_am.tsv`. Bảng quyết định đầy đủ nằm trong script (mục `RULES`) và được in lại ở mục 4 (`python -I scripts/r1_apply.py --dump-rules`).*

> **Điều phối sửa đổi ngày 16/11/2026, sau R2. Khi mâu thuẫn, phần này thắng nội dung bên dưới.**
>
> 1. **Mục 1.2, âm Nôm đã thay.** **Không** giữ từ Nôm trong `tu_viet`. Tiếng Việt không dùng từ Hán Việt "du" với nghĩa "dầu", nên:
>    - `loai` là `khong_giup`, hoặc `yeu_to` nếu âm Hán Việt có trong từ Việt khác cùng nghĩa;
>    - bỏ `tu_viet`;
>    - liên hệ với từ Nôm ghi trong `pt_noi_dung` dạng `goi_nho`: "âm gần với từ Việt 'dầu' (liên tưởng, không khẳng định từ nguyên)".
>
>    Đã áp qua `fixes_r1b_wording.tsv` và `fixes_r2_set_khac02_needs_r1.tsv`.
> 2. **Câu "'X' trong tiếng Việt có gốc từ chữ này"** là khẳng định từ nguyên không có nguồn. Đã đổi thành liên tưởng.
> 3. **腻:** 油腻 đọc NỊ (theo Thiều Chửu); 细腻 đọc NHỊ (theo từ Việt "tế nhị").
> 4. **打量 dǎliang:** nghĩa "đo bằng mắt" nên đọc LƯƠNG, theo nguyên tắc liáng = lương.

## 1. Thứ tự ưu tiên khi chọn âm cho một chữ trong một từ

1. Âm phải nằm trong `cands` của chữ đó (item_hv). Không tự thêm âm.
2. **Âm Hán Việt, không phải âm Nôm hay âm Việt hóa.** Nếu âm đang dùng là từ thuần Việt hay âm Việt hóa (lạnh, dầu, tơ, rương, khóc, vây, ví, bánh, lồng, lò, chiên, thùng, má…), thay bằng âm Hán Việt có nguồn, ưu tiên Thiều Chửu.
   - `tu_viet` vẫn giữ từ Việt thật (ví dụ 油 DU, tu_viet "dầu").
   - `char_note` ghi "'dầu' là âm Việt hóa".
   - Chỉ khi chắc mối liên hệ mới thêm `goi_nho` "'dầu' trong tiếng Việt có gốc từ chữ này". Danh sách: 油, 饼, 桶, 哭, 割, 曾, 炒, 煎, 丝, 戴, 妈妈.
   - Không chắc thì `char_note` chỉ ghi "'X' không phải âm Hán Việt".
3. **Tiếng Việt có từ Hán Việt chứa chữ đó** thì lấy âm của từ Việt. Ví dụ: lĩnh vực, chiếm lĩnh, khải hoàn, phẩm hạnh, yên tĩnh, tự lực cánh sinh, cấu kết, khuyết thiếu, ảo tưởng.
4. **Không có từ Việt** thì chọn theo âm tiết pinyin và nghĩa chữ trong từ. Cùng (chữ, pinyin, nghĩa) thì cùng một âm.
   - Ví dụ theo pinyin: 当 dāng/dàng, 调 tiáo/diào.
   - Ví dụ theo nghĩa: 推 đẩy = thôi, suy xét = suy; 领 dẫn = lãnh, nhận/cổ áo = lĩnh.
5. **Âm chỉ có ở hvpinyin** (không có trong Thiều Chửu):
   - Giữ nếu có từ Việt thông dụng chứng thực (lãnh, đơn, đới, tầng, diên, khuếch, đỉnh, bài, gián, nồng…; xem mục 3).
   - Giữ nếu chữ không có mục Thiều Chửu (chữ khẩu ngữ: 搞, 咧, 愣, 啃…).
   - Ngoài hai trường hợp đó thì theo âm Thiều Chửu (đảo, tảo, mai, sát, đinh, hoảng, chàng…).
6. **Từ Việt đọc một âm không có trong nguồn** (资源 tài nguyên, 身份 thân phận, 宗教 tôn giáo…):
   - Giữ âm có nguồn.
   - `tu_viet` ghi từ Việt thật.
   - `char_note` ghi "từ Việt đọc '…' (âm … không có trong nguồn)".
   - Danh sách ở mục 5.

## 2. Chốt các điểm tranh cãi

| Chữ / từ | Chốt | Căn cứ |
|---|---|---|
| 受 | **thụ** (mọi mục) | Thiều Chửu chỉ ghi "thụ". Từ Việt: cảm thụ, hưởng thụ, thụ lý. "Thọ" chỉ có ở hvpinyin. 享受 trước ghi HƯỞNG THỌ, mâu thuẫn với tu_viet "hưởng thụ". |
| 单 dān | **đơn** | Từ Việt: đơn giản, đơn vị, cô đơn, thực đơn (菜单). "Đơn" có ở hvpinyin và Unihan. Thiều Chửu giải nghĩa "Đơn…" nhưng ghi âm đan. |
| 推 | **thôi** khi nghĩa là đẩy (推, 推动, 推广, 推进, 推出, 推迟, 推行, 推销, 推卸, 推移, 推翻, 推辞, 推敲 "thôi xao"); **suy** khi nghĩa là suy xét, tiến cử (推荐, 推测, 推断, 推理, 推算, 推论, 推崇, 推选) | Thiều Chửu: thôi = đẩy lên, dời đi; "có chỗ đọc là suy". Từ Việt: thôi xao; suy luận, suy đoán, suy cử, suy tôn. |
| 当 | dāng → **đương**, dàng → **đáng**. 当天 giữ đương. | Theo pinyin. Từ Việt: đương nhiên, thích đáng, chính đáng, thỏa đáng. 当天 cùng nhóm nghĩa với 当日 và 当晚 (data ghi dāng). |
| 尽 | **tận** (cả jǐn) | 儘 là chữ phái sinh của 盡. hvpinyin ghi 儘 = tận. "Tận" là yếu tố quen trong tiếng Việt. Chỉ đổi một mục: 尽管 TẪN → TẬN. |
| 调 | tiáo → **điều**, diào → **điệu**. Ngoại lệ theo từ Việt (diào mà đọc điều): 调查, 调研, 调动, 调度 | Đã nằm trong HUONG_DAN. Ngoại lệ là các từ Việt: điều tra, điều nghiên, điều động, điều độ. |
| 旋 | **toàn**; riêng 凯旋 đọc **hoàn** | Thiều Chửu: toàn = quay, xoáy (toàn phong, toàn oa). Từ Việt "khải hoàn". |
| 妈 | **ma** | Thiều Chửu: tục gọi mẹ là ma ma 媽媽. "Má" là âm Việt hóa (đưa vào goi_nho). |
| 师傅 | **phó** | Thiều Chửu: sư phó 師傅. "Sư phụ" trong tiếng Việt là 師父. |
| 划 | huá → **hoa** (划算, 划得来, 划不来; nguồn của các mục này chỉ có hoa). huà → **hoạch**. Riêng 划 đứng riêng (nghĩa quẹt, vạch = 劃) → **hoạch**. | Thiều Chửu: 划 hoa = chèo; 劃 hoạch = rạch, vạch. |
| 奖 | **tưởng** (14 mục) | Thiều Chửu chỉ ghi "tưởng" (tưởng lệ). Từ Việt: tưởng thưởng. "Thưởng" là âm của 賞 mà hvpinyin gán lẫn. 中奖 giữ tu_viet "trúng thưởng", có ghi chú. |
| 量 | liáng (đo) → **lương**; liàng → **lượng** | Thiều Chửu: "đo xem dài ngắn gọi là lương". Bốn mục bị đổi: 量, 测量, 衡量, 考量. 商量 giữ "thương lượng" theo từ Việt. |
| 领 | **lãnh** khi nghĩa là dẫn dắt: 领导, 领袖, 领土, 领事, 领先, 带领, 率领, 引领, 领军, 领队, 领会. **lĩnh** khi nghĩa là nhận, cổ áo, nắm được: 领域, 占领, 领悟, 本领, 纲领, 要领, 领取, 申领, 领养, 领略, 白领, 领带 | Cả hai âm đều có nguồn. Từ Việt: lĩnh vực, chiếm lĩnh, lĩnh ngộ, bản lĩnh, cương lĩnh, lĩnh lương. Thiều Chửu: lĩnh = cái cổ, cổ áo. |
| 带 | **đới** (giữ) | Từ Việt: nhiệt đới, ôn đới, hàn đới. Thiều Chửu ghi đái. |
| 安静 | **YÊN TĨNH** | Từ Việt "yên tĩnh". "Yên" có trong Thiều Chửu. |
| 轻松 / 松 | lỏng (鬆) → **tông**; cây thông → **tùng** (松树) | Chọn phồn thể theo nghĩa. |
| 并 | 並 (và, song song) → **tịnh**; 併 (gộp) → **tính**: 合并, 一并, 并购, 并发症 | 并发症 viết 併發症. Từ Việt: thôn tính. |
| 要 | yào → **yếu**, yāo → **yêu** | Đã nằm trong HUONG_DAN. |
| 着 | **trước** (mọi pinyin) | 着 là dạng của 著 (trước = mặc, bám; chấp trước). |
| 综 | **tổng** cho 综合, 综艺; **tông** cho 错综复杂 | Từ Việt "tổng hợp". 错综 (đan xen): Thiều Chửu ghi tông. |
| 找 | **trảo** | Cả hvpinyin và Thiều Chửu đều ghi. |
| 喝 | **hát** | Thiều Chửu: quát; "uống, như hát tửu 喝酒". "Húp/hét" không phải âm Hán Việt. Lưu ý: không phải "hát" (ca). |
| 幻 | **ảo** (cả 6 mục trước ghi huyễn) | Từ Việt: ảo tưởng, ảo giác, ảo ảnh, hư ảo, biến ảo, mộng ảo. Thiều Chửu: "ta quen đọc là ảo". |
| 潮 | thủy triều, ẩm → **triều**; làn sóng, xu hướng → **trào** (潮流, 高潮, 新潮, 热潮) | Từ Việt: trào lưu, cao trào. |
| 挑 | tiāo (gánh, kén chọn) → **thiêu**; tiǎo (khêu) → **khiêu** | Thiều Chửu. |
| 钻 | zuān → **toàn**; zuàn → **toản** | Thiều Chửu: toản = cái khoan; toàn = đâm, dùi. |
| 吃 | **cật** | Thiều Chửu ghi cật cho 吃, "cũng như chữ khiết 喫". 10/11 mục đã dùng cật. |
| 启 | **khải** | "Khởi" là âm của 起. Từ Việt "khởi động" viết 起動 (tu_viet giữ "khởi động", có ghi chú). |

## 3. Âm giữ dù không có trong Thiều Chửu

Các âm dưới đây không có trong bản Thiều Chửu dùng làm nguồn. Vẫn giữ vì có từ Việt chứng thực, hoặc vì chữ không có mục Thiều Chửu.

| Chữ | Âm giữ | Căn cứ (từ Việt / nguồn) |
|---|---|---|
| 领 | lãnh | lãnh đạo, lãnh tụ, lãnh thổ, lãnh sự |
| 单 | đơn | đơn giản, đơn vị, cô đơn, thực đơn |
| 带 | đới | nhiệt đới, ôn đới, hàn đới |
| 延 | diên | diên trì, diên hạn (gia hạn) |
| 层 | tầng | tầng lớp, giai tầng, tầng lầu |
| 份 | phần | cổ phần, phần (suất); 'thân phận' viết 分 |
| 分 | phần | thành phần, phần tử |
| 扩 | khuếch | khuếch đại, khuếch tán, khuếch trương |
| 顶 | đỉnh | đỉnh, tuyệt đỉnh, đỉnh cao |
| 摆 | bài | bài trí, bài binh bố trận |
| 间 | gián | gián tiếp, gián đoạn, gián điệp |
| 浓 | nồng | nồng độ, nồng hậu, nồng nhiệt |
| 潮 | trào | trào lưu, cao trào |
| 仇 | thù | thù hận, báo thù, cừu thù |
| 综 | tổng | tổng hợp (综合) |
| 并 | tính | thôn tính, hợp tính (併) |
| 旋 | hoàn | khải hoàn (凯旋) |
| 叛 | phản | phản nghịch, phản đồ, phản loạn |
| 峡 | hiệp | Tam Hiệp (三峽) |
| 萎 | ủy | ủy mị (萎靡) |
| 饺 | cảo | sủi cảo, há cảo |
| 帅 | soái | nguyên soái, thống soái |
| 玫 | mai | mai khôi (玫瑰) |
| 璃 | lê | pha lê (玻璃) |
| 姆 | mẫu | bảo mẫu (保姆) |
| 迫 | bức | bức thiết, áp bức |
| 勾 | cấu | cấu kết |
| 去 | khử | trừ khử, khử độc, khử trùng |
| 胧 | lung | mông lung (朦朧) |
| 礁 | tiêu | ám tiêu (đá ngầm) |
| 缅 | miến | Miến Điện (緬甸) |
| 侄 | điệt | Thiều Chửu: 侄 mượn làm 姪 điệt |
| 姐 | tỷ | tỷ muội, tỷ tỷ |
| 什 | thậm | 什么 = 甚麼 (thậm) |
| 卡 | ca | phiên âm kǎ (card, calorie) |
| 咖 | ca | phiên âm 咖啡 |
| 呵 | ha | hē: phiên thiết 虎何切 → ha; Thiều Chửu chỉ ghi âm 'a' (tiếng đệm) |
| 哈 | ha | thán từ tượng thanh |
| 橱 | trù | 櫥 = tủ (廚 trù); mục Thiều Chửu 'thụ' là nghĩa khác (như 樹) |
| 吭 | khang | kēng: Thiều Chửu chỉ có hàng/hạng (háng = cổ họng) |

Chữ không có mục Thiều Chửu thì giữ âm hvpinyin (nguồn duy nhất): 搞 cảo, 咧 liệt, 愣 lăng, 溜 lưu, 啤 bia, 乒 binh, 乓 bàng, 嗯 ân, 胳 cách, 捡 kiểm, 嘿 hắc, 叼 điêu, 唬 hổ, 嗦 sách, 啃 khẳng, 嘀 đê, 垮 khỏa, 惦 điếm, 憋 biệt, 挎 khóa, 捂 ngộ, 捅 thống, 掺 sam, 揍 tấu, 暨 kỵ, 沏 thế, 涮 xuyến, 甩 súy, 趴 bát, 蹦 bính. Ngoại lệ: 掰 chỉ có âm Nôm "bẻ", nên đặt `?` và chuyển `needs_review`.

## 4. Bảng quyết định đầy đủ

Bảng này sinh từ `RULES` trong script, gồm 192 quy tắc. Cột "Loại":

- **N**: âm Nôm hoặc Việt hóa, thay bằng âm Hán Việt có nguồn.
- **H**: âm chỉ có ở hvpinyin, không có từ Việt chứng thực, nên theo Thiều Chửu.
- **T**: thống nhất chữ đa âm theo pinyin, nghĩa hoặc từ Việt.

Thứ tự áp dụng: ngoại lệ theo từ, rồi theo pinyin, rồi mặc định. Dấu "—" nghĩa là không có.

Ngoài bảng, `OVERRIDES` trong script sửa văn bản phụ thuộc trực tiếp vào âm: `pt_noi_dung`, `khac_biet`, `tu_viet` của 幻想, `loai` của 冻. `RESOLVE` chuyển các mục needs_review đã quyết sang draft.

| # | Chữ | Mặc định | Theo pinyin | Ngoại lệ theo từ | Loại | Căn cứ |
|---|---|---|---|---|---|---|
| 1 | 受 | thụ | — | — | T | 受=thụ (cảm thụ, hưởng thụ, thụ lý; Thiều Chửu chỉ ghi thụ; 'thọ' chỉ có ở hvpinyin) |
| 2 | 单 | đơn | — | — | T | từ Việt: đơn giản, đơn vị, thực đơn, cô đơn; 'đơn' có ở hvpinyin+Unihan; Thiều Chửu giải nghĩa 'Đơn...' nhưng ghi âm đan |
| 3 | 推 | thôi | — | suy: 推荐、推测、推断、推理、推算、推论、推崇、推选 | T | 推: thôi = đẩy (Thiều Chửu: đẩy lên, dời đi; 推敲 thôi xao); suy = suy xét, suy cử (suy luận, suy đoán, suy cử, suy tôn) |
| 4 | 当 | — | dang1→đương, dang4→đáng, dang5→đáng | đương: 当天 | T | theo pinyin; 当天 giữ đương cùng nhóm 当日/当晚 (nghĩa 'ngay hôm đó') |
| 5 | 尽 | tận | — | — | T | 儘 là chữ phái sinh của 盡; hvpinyin ghi 儘=tận; tận là yếu tố quen (tận lực, tận dụng) |
| 6 | 调 | — | tiao2→điều, diao4→điệu | điều: 调查、调研、调动、调度 | T | 调: tiáo=điều, diào=điệu; điều tra/điều nghiên/điều động/điều độ theo từ Việt |
| 7 | 旋 | toàn | — | hoàn: 凯旋 | T | 旋=toàn (Thiều Chửu: quay, xoáy: toàn phong, toàn oa); 凯旋 theo từ Việt 'khải hoàn' |
| 8 | 妈 | ma | — | — | N | 妈=ma (Thiều Chửu: tục gọi mẹ là ma ma 媽媽); 'má' là âm Việt hóa |
| 9 | 傅 | phó | — | — | T | 傅=phó (Thiều Chửu: sư phó 師傅); 'sư phụ' trong tiếng Việt là 師父 |
| 10 | 划 | — | hua2→hoa, hua4→hoạch | hoạch: 划 | T | 划: huá=hoa (划 chèo; 划算/划得来 nguồn chỉ có hoa), huà=hoạch (劃: kế hoạch); 划 'quẹt, vạch' là 劃 → hoạch |
| 11 | 奖 | tưởng | — | — | N | hvpinyin ghi thưởng (lẫn với 賞); Thiều Chửu chỉ ghi tưởng; 奖赏 = tưởng thưởng |
| 12 | 量 | — | liang2→lương | — | T | 量 liáng (đo) = lương (Thiều Chửu: cân nhắc, đo xem dài ngắn gọi là lương); liàng = lượng |
| 13 | 领 | lãnh | — | lĩnh: 本领、纲领、要领、领域、占领、领悟、领略、领取、申领、领养、白领、领带 | T | cả hai âm có nguồn (lãnh: hvpinyin+Unihan; lĩnh: Thiều Chửu+Wiktionary); chọn theo từ Việt rồi theo nghĩa |
| 14 | 安 | an | — | yên: 安静 | T | 安=an; 安静 theo từ Việt 'yên tĩnh' (yên có trong Thiều Chửu) |
| 15 | 松 | tông | — | tùng: 松树 | T | 松: lỏng (鬆)=tông; cây thông=tùng |
| 16 | 并 | tịnh | — | tính: 合并、一并、并购、并发症 | T | 并: 並 (và, cùng, song song)=tịnh; 併 (gộp)=tính (thôn tính); 并发症=併發症 |
| 17 | 要 | — | yao4→yếu, yao1→yêu | — | T | 要: yào=yếu, yāo=yêu |
| 18 | 着 | trước | — | — | T | 着 (著 zhuó/zháo/zhe)=trước (chấp trước) |
| 19 | 综 | tổng | — | tông: 错综复杂 | T | 综: 综合/综艺 theo từ Việt 'tổng hợp'; 错综 (đan xen) = tông (Thiều Chửu) |
| 20 | 找 | trảo | — | — | T | 找=trảo (hvpinyin+Thiều Chửu) |
| 21 | 喝 | hát | — | — | N | 喝=hát (Thiều Chửu: quát; uống, như hát tửu 喝酒); 'húp/hét' không phải âm Hán Việt |
| 22 | 行 | — | xing2→hành, hang2→hàng | hạnh: 品行 | T | 行: xíng=hành, háng=hàng; 品行 theo từ Việt 'phẩm hạnh' |
| 23 | 面 | diện | — | miến: 面包、面条儿、方便面、面粉 | T | 面: mặt=diện; bột mì (麵)=miến |
| 24 | 重 | — | zhong4→trọng, chong2→trùng | — | T | 重: zhòng=trọng, chóng=trùng |
| 25 | 分 | — | fen1→phân, fen4→phận, fen5→phận | phần: 成分、水分、知识分子; phân: 分量 | T | 分: fēn=phân, fèn=phận; thành phần, thủy phần, phần tử, phân lượng theo từ Việt |
| 26 | 好 | — | hao3→hảo, hao4→hiếu | — | T | 好: hǎo=hảo, hào=hiếu |
| 27 | 中 | — | zhong1→trung, zhong4→trúng | — | T | 中: zhōng=trung, zhòng=trúng |
| 28 | 相 | — | xiang1→tương, xiang4→tướng | — | T | 相: xiāng=tương, xiàng=tướng |
| 29 | 合 | hợp | — | hiệp: 回合 | T | 合=hợp; 回合 'hiệp' (hiệp đấu) theo tiếng Việt |
| 30 | 过 | quá | — | qua: 过、经过、通过、穿过、透过、放过、越过 | T | 过: mặc định quá (quá khứ, quá trình); qua trong kinh qua, thông qua, xuyên qua và nghĩa 'đi xuyên qua' |
| 31 | 会 | — | hui4→hội, kuai4→cối | — | T | 会: huì=hội, kuài=cối |
| 32 | 主 | chủ | — | chúa: 公主、主宰 | T | 主=chủ; công chúa, chúa tể theo từ Việt |
| 33 | 长 | — | chang2→trường, zhang3→trưởng | — | T | 长: cháng=trường, zhǎng=trưởng |
| 34 | 本 | bản | — | bổn: 本分 | T | 本=bản; 本分 theo từ Việt 'bổn phận' |
| 35 | 为 | — | wei2→vi, wei4→vị | — | T | 为: wéi=vi, wèi=vị |
| 36 | 难 | — | nan2→nan, nan5→nan, nan4→nạn | — | T | 难: nán=nan, nàn=nạn |
| 37 | 正 | — | zheng4→chính, zheng1→chinh | — | T | 正: zhèng=chính, zhēng (正月)=chinh |
| 38 | 处 | — | chu4→xứ, chu5→xứ, chu3→xử | — | T | 处: chù=xứ, chǔ=xử |
| 39 | 转 | chuyển | — | — | T | 转=chuyển (chuyển động, vận chuyển) |
| 40 | 数 | — | shu4→số, shu5→số, shu3→sổ | — | T | 数: shù=số, shǔ (đếm)=sổ (Thiều Chửu) |
| 41 | 强 | — | qiang2→cường, jiang4→cường, qiang3→cưỡng | cưỡng: 强制、强加、强占、强行 | T | 强: qiáng=cường, qiǎng=cưỡng; cưỡng chế/cưỡng chiếm và nghĩa 'ép buộc' = cưỡng |
| 42 | 传 | — | chuan2→truyền, zhuan4→truyện | — | T | 传: chuán=truyền, zhuàn=truyện |
| 43 | 应 | — | ying1→ưng, ying4→ứng, ying5→ứng | — | T | 应: yīng=ưng, yìng=ứng |
| 44 | 空 | — | kong1→không, kong4→khống | — | T | 空: kōng=không, kòng=khống |
| 45 | 间 | — | jian1→gian, jian4→gián | — | T | 间: jiān=gian, jiàn=gián (gián tiếp, gián đoạn) |
| 46 | 干 | — | gan1→can, gan4→cán | — | T | 干: gān=can, gàn=cán |
| 47 | 和 | hòa | — | họa: 附和 | T | 和=hòa; 附和 'phụ họa' |
| 48 | 思 | tư | — | tứ: 意思、不好意思、有意思、没意思、构思 | T | 思=tư; ý tứ, cấu tứ = tứ |
| 49 | 乐 | — | le4→lạc, yue4→nhạc | — | T | 乐: lè=lạc, yuè=nhạc |
| 50 | 复 | phục | — | phức: 复印、复杂、重复、错综复杂; phúc: 答复 | T | theo phồn thể; 复合 trong câu nghĩa 'quay lại với nhau' (復合) nên giữ phục |
| 51 | 计 | kế | — | kê: 统计 | T | 计=kế; 统计 'thống kê' |
| 52 | 从 | tòng | — | thung: 从容、从容不迫; tùng: 服从 | T | 从=tòng; thung dung, phục tùng theo từ Việt |
| 53 | 假 | — | jia3→giả, jia4→giá | — | T | 假: jiǎ=giả, jià (nghỉ)=giá |
| 54 | 去 | khứ | — | khử: 除去、去除 | T | 去=khứ; nghĩa 'loại bỏ' = khử (trừ khử, khử độc) |
| 55 | 断 | đoạn | — | đoán: 判断、诊断、当机立断、推断、断定、断然、果断 | T | 断: đứt=đoạn; phán đoán, chẩn đoán, quả đoán = đoán |
| 56 | 称 | — | cheng1→xưng, chen4→xứng | — | T | 称: chēng=xưng, chèn=xứng |
| 57 | 觉 | — | jue2→giác, jiao4→giáo | — | T | 觉: jué=giác, jiào=giáo |
| 58 | 首 | thủ | — | thú: 自首 | T | 首=thủ; 自首 'tự thú' |
| 59 | 折 | chiết | — | triệp: 折、存折 | T | 折叠 (gấp) đáng là triệp nhưng cands của mục chỉ có chiết → giữ chiết |
| 60 | 使 | sử | — | sứ: 使馆、大使、使命、使者、天使 | T | 使: sai khiến=sử; sứ giả=sứ |
| 61 | 兴 | — | xing1→hưng, xing4→hứng | — | T | 兴: xīng=hưng, xìng=hứng |
| 62 | 倒 | đảo | — | — | H | 倒=đảo (Thiều Chửu; 'đáo' chỉ có ở hvpinyin) |
| 63 | 创 | — | chuang4→sáng, chuang1→sang | — | T | 创: chuàng=sáng, chuāng (vết thương)=sang |
| 64 | 少 | — | shao3→thiểu, shao4→thiếu | thiếu: 缺少 | T | 少: shǎo=thiểu, shào=thiếu; 缺少 theo từ Việt 'khuyết thiếu' |
| 65 | 盛 | — | sheng4→thịnh, cheng2→thình | — | T | 盛: shèng=thịnh, chéng=thình |
| 66 | 依 | y | — | ỷ: 依赖 | T | 依=y; 依赖 'ỷ lại' |
| 67 | 营 | doanh | — | dinh: 营养 | T | 营=doanh; 营养 'dinh dưỡng' |
| 68 | 藏 | — | cang2→tàng, zang4→tạng | — | T | 藏: cáng=tàng, zàng=tạng |
| 69 | 住 | trú | — | trụ: 禁不住 | T | 住=trú; bổ ngữ 'giữ vững' trong 禁不住 = trụ |
| 70 | 劳 | lao | — | lạo: 慰劳 | T | 劳=lao; 慰劳 'úy lạo' |
| 71 | 恶 | — | e4→ác, e3→ác, wu4→ố | — | T | 恶: è=ác, wù=ố |
| 72 | 迫 | bách | — | bức: 迫切、压迫 | T | 迫=bách; bức thiết, áp bức theo từ Việt |
| 73 | 占 | — | zhan4→chiếm, zhan1→chiêm | — | T | 占: zhàn=chiếm, zhān=chiêm |
| 74 | 吃 | cật | — | — | T | 吃=cật (Thiều Chửu ghi cật cho 吃, 'cũng như chữ khiết 喫') |
| 75 | 围 | vi | — | — | N | 围=vi (phạm vi, chu vi); 'vây' là âm Việt hóa |
| 76 | 幸 | hạnh | — | hãnh: 侥幸、幸免、幸存 | T | 幸=hạnh; nghĩa 'may mà thoát' = hãnh |
| 77 | 易 | dị | — | dịch: 交易、贸易 | T | 易: dễ=dị; trao đổi=dịch |
| 78 | 背 | bối | — | bội: 背叛、违背 | T | 背: lưng=bối; làm trái=bội |
| 79 | 鲜 | — | xian1→tiên, xian3→tiển | — | T | 鲜: xiān=tiên, xiǎn=tiển |
| 80 | 只 | — | zhi3→chỉ, zhi1→chích | — | T | 只: zhǐ=chỉ, zhī=chích |
| 81 | 散 | tán | — | tản: 散步、散文 | T | 散=tán; tản bộ, tản văn theo từ Việt |
| 82 | 种 | — | zhong3→chủng, zhong4→chúng | — | T | 种: zhǒng=chủng, zhòng (trồng)=chúng |
| 83 | 促 | xúc | — | — | N | 促=xúc (Thiều Chửu); 'thúc' là âm Việt hóa |
| 84 | 启 | khải | — | — | H | 启=khải (Thiều Chửu); 'khởi' là âm của 起 (từ Việt 'khởi động' viết 起動) |
| 85 | 将 | tương | — | tướng: 将军、麻将 | T | 将=tương; tướng quân, mạt chược = tướng |
| 86 | 征 | trưng | — | chinh: 出征、征服、长征 | T | 征: trưng (đặc trưng, trưng cầu); chinh (chinh phục, trường chinh) |
| 87 | 扫 | tảo | — | — | H | 扫=tảo (Thiều Chửu; 'táo' chỉ có ở hvpinyin) |
| 88 | 更 | — | geng1→canh, geng4→cánh | cánh: 自力更生 | T | 更: gēng=canh, gèng=cánh; tự lực cánh sinh |
| 89 | 汇 | hối | — | vựng: 词汇 | T | 汇: 匯=hối; 彙 (từ vựng)=vựng |
| 90 | 症 | — | zheng4→chứng, zheng1→trưng | — | T | 症: zhèng=chứng, zhēng=trưng |
| 91 | 降 | — | jiang4→giáng, xiang2→hàng | — | T | 降: jiàng=giáng, xiáng=hàng |
| 92 | 弹 | — | tan2→đàn, tan5→đàn, dan4→đạn | — | T | 弹: tán=đàn, dàn=đạn |
| 93 | 监 | giám | — | giam: 监狱 | T | 监=giám; nhà giam (监狱)=giam (Thiều Chửu) |
| 94 | 与 | — | yu3→dữ, yu4→dự | — | T | 与: yǔ=dữ, yù=dự |
| 95 | 司 | ti | — | tư: 司令、司法、司空见惯 | T | 司=ti (công ty); tư lệnh, tư pháp theo từ Việt |
| 96 | 埋 | mai | — | — | H | 埋=mai (Thiều Chửu ghi cả pinyin mán; 'man' chỉ có ở hvpinyin) |
| 97 | 幻 | ảo | — | — | T | 幻=ảo (ảo tưởng, ảo giác, ảo ảnh, hư ảo, biến ảo; Thiều Chửu: ta quen đọc là ảo) |
| 98 | 斗 | — | dou4→đấu, dou3→đẩu | — | T | 斗: dòu=đấu, dǒu=đẩu |
| 99 | 朝 | — | zhao1→triêu, chao2→triều | — | T | 朝: zhāo=triêu, cháo=triều |
| 100 | 潮 | triều | — | trào: 潮流、高潮、新潮、热潮 | T | 潮: thủy triều, ẩm=triều; làn sóng, xu hướng=trào (trào lưu, cao trào) |
| 101 | 禁 | — | jin4→cấm, jin1→câm | cấm: 情不自禁 | T | 禁: jìn=cấm, jīn (chịu được)=câm; 情不自禁 theo 'tình bất tự cấm' |
| 102 | 累 | — | lei3→lũy, lei4→lụy, lei2→luy | lụy: 拖累 | T | 累: lěi=lũy (tích lũy), lèi=lụy, léi=luy; 拖累 nghĩa liên lụy |
| 103 | 纵 | túng | — | tung: 纵横、纵深 | T | 纵: buông=túng; dọc=tung |
| 104 | 丑 | xú | — | sửu: 小丑 | T | 丑: 醜 (xấu)=xú; vai hề (丑)=sửu |
| 105 | 丝 | ti | — | — | N | 丝=ti (Thiều Chửu); 'tơ' là âm Việt hóa |
| 106 | 仿 | phỏng | — | phảng: 仿佛 | T | 仿=phỏng; 仿佛 'phảng phất' |
| 107 | 挑 | — | tiao1→thiêu, tiao3→khiêu | — | T | 挑: tiāo (gánh, kén chọn)=thiêu; tiǎo (khêu, khiêu khích)=khiêu (Thiều Chửu) |
| 108 | 武 | vũ | — | võ: 武术、武侠 | T | 武: vũ khí, vũ lực; võ thuật, võ hiệp theo từ Việt |
| 109 | 舍 | — | she3→xả, she4→xá | — | T | 舍: shě=xả, shè=xá |
| 110 | 著 | trứ | — | trước: 著作 | T | 著=trứ; 著作 'trước tác' |
| 111 | 咽 | — | yan1→yết, yan4→yến, ye4→ế | — | T | 咽: yān=yết, yàn=yến, yè=ế |
| 112 | 漂 | — | piao1→phiêu, piao4→phiếu | — | T | 漂: piāo=phiêu, piào=phiếu |
| 113 | 炸 | tạc | — | — | H | 炸=tạc (Thiều Chửu: nổ; đồ ăn nấu dầu, tạc nhục 炸肉) |
| 114 | 箱 | tương | — | — | N | 箱=tương (Thiều Chửu); 'rương' không phải âm Hán Việt |
| 115 | 郁 | uất | — | úc: 浓郁 | T | 郁: 鬱 (u uất)=uất; thơm nồng (郁)=úc |
| 116 | 割 | cát | — | — | N | 割=cát (Thiều Chửu); 'cắt' là âm Việt hóa |
| 117 | 姐 | tỷ | — | thư: 小姐 | T | 姐=tỷ (tỷ muội); 小姐 'tiểu thư' |
| 118 | 慰 | úy | — | ủy: 安慰 | T | 慰=úy (úy lạo, úy vấn); 安慰 lấy ủy (gần 'an ủi') |
| 119 | 晃 | hoảng | — | — | H | 晃=hoảng (Thiều Chửu; 'hoàng' chỉ có ở hvpinyin) |
| 120 | 桥 | kiều | — | — | N | 桥=kiều (Thiều Chửu); 'cầu' không phải âm Hán Việt |
| 121 | 笨 | bổn | — | — | N | 笨=bổn (Thiều Chửu); 'đần' không phải âm Hán Việt |
| 122 | 笼 | lung | — | — | N | 笼=lung (Thiều Chửu); 'lồng' là âm Việt hóa |
| 123 | 缝 | — | feng2→phùng, feng5→phùng, feng4→phúng | — | T | 缝: féng (khâu)=phùng, fèng (khe)=phúng |
| 124 | 钉 | đinh | — | — | H | 钉=đinh (Thiều Chửu; 'đính' chỉ có ở hvpinyin) |
| 125 | 钻 | — | zuan1→toàn, zuan4→toản | — | T | 钻: zuān (dùi, đục)=toàn; zuàn (mũi khoan, kim cương)=toản (Thiều Chửu) |
| 126 | 铺 | — | pu1→phô, pu4→phố | — | T | 铺: pū=phô, pù=phố |
| 127 | 几 | — | ji3→kỷ, ji1→cơ | — | T | 几: jǐ=kỷ, jī=cơ |
| 128 | 勾 | câu | — | cấu: 勾结 | T | 勾=câu; 勾结 theo từ Việt 'cấu kết' |
| 129 | 哭 | khốc | — | — | N | 哭=khốc (Thiều Chửu); 'khóc' là âm Việt hóa |
| 130 | 喷 | phún | — | — | N | 喷=phún (Thiều Chửu); 'phun' không phải âm Hán Việt |
| 131 | 堆 | đôi | — | — | H | 堆=đôi (Thiều Chửu; 'đồi' chỉ có ở hvpinyin) |
| 132 | 戴 | đái | — | — | N | 戴=đái (Thiều Chửu: đội; ái đái); 'đội' là âm Việt hóa |
| 133 | 炒 | sao | — | — | N | 炒=sao (Thiều Chửu); 'xào' là âm Việt hóa |
| 134 | 脏 | — | zang1→tảng, zang4→tạng | — | T | 脏: zāng (bẩn, 髒)=tảng; zàng (nội tạng, 臟)=tạng |
| 135 | 仓 | thương | — | thảng: 仓促 | T | 仓=thương; 仓促 'thảng thốt' |
| 136 | 仔 | — | zi3→tử, zai3→tể | — | T | 仔: zǐ=tử, zǎi=tể |
| 137 | 佛 | — | fu2→phất, fo2→phật | — | T | 佛: fú=phất, fó=phật |
| 138 | 刹 | sát | — | — | H | 刹=sát (Thiều Chửu; 'sa' chỉ có ở hvpinyin) |
| 139 | 卜 | — | bu3→bốc, bo5→bặc | — | T | 卜: bǔ=bốc, bo (萝卜)=bặc |
| 140 | 哨 | sáo | — | — | T | 哨=sáo (Thiều Chửu: sáo tử 哨子 cái còi) |
| 141 | 帖 | thiếp | — | — | N | 帖=thiếp (Thiều Chửu); 'thiệp' là âm Việt hóa |
| 142 | 撒 | — | sa3→tản, sa1→tát | — | T | 撒: sǎ=tản, sā=tát |
| 143 | 歪 | oa | — | — | T | 歪=oa (Thiều Chửu: ta quen đọc là oa) |
| 144 | 滴 | tích | — | — | T | 滴=tích (Thiều Chửu âm chính; thủy tích thạch xuyên) |
| 145 | 煎 | tiên | — | — | N | 煎=tiên (Thiều Chửu); 'chiên' là âm Việt hóa |
| 146 | 油 | du | — | — | N | 油=du (Thiều Chửu); 'dầu' là âm Việt hóa |
| 147 | 饼 | bính | — | — | N | 饼=bính (Thiều Chửu); 'bánh' là âm Việt hóa |
| 148 | 桶 | dũng | — | — | N | 桶=dũng (Thiều Chửu); 'thùng' là âm Việt hóa |
| 149 | 炉 | lô | — | — | N | 炉=lô (Thiều Chửu); 'lò' là âm Việt hóa |
| 150 | 框 | khuông | — | — | N | 框=khuông (Thiều Chửu); 'khung' không phải âm Hán Việt |
| 151 | 粪 | phẩn | — | — | N | 粪=phẩn (Thiều Chửu); 'phân' không phải âm Hán Việt |
| 152 | 爬 | ba | — | — | N | 爬=ba (Thiều Chửu); 'bò' không phải âm Hán Việt |
| 153 | 茄 | gia | — | — | N | 茄=gia (Thiều Chửu); 'cà' không phải âm Hán Việt |
| 154 | 霉 | môi | — | — | N | 霉=môi (Thiều Chửu); 'mốc' không phải âm Hán Việt |
| 155 | 嚏 | đế | — | — | N | 嚏=đế (Thiều Chửu: hắt hơi); 'xì' không phải âm Hán Việt |
| 156 | 椰 | gia | — | — | N | 椰=gia (Thiều Chửu); 'dừa' không phải âm Hán Việt |
| 157 | 爹 | đa | — | — | N | 爹=đa (Thiều Chửu: cha); 'tía' là từ Nam Bộ |
| 158 | 蘸 | trám | — | — | N | 蘸=trám (Thiều Chửu: chấm, thấm nước); 'chấm' không phải âm Hán Việt |
| 159 | 譬 | thí | — | — | N | 譬=thí (thí dụ); 'ví' là âm Việt hóa |
| 160 | 饵 | nhị | — | — | N | 饵=nhị (Thiều Chửu); 'nhử' không phải âm Hán Việt |
| 161 | 赎 | thục | — | — | N | 赎=thục (Thiều Chửu); 'chuộc' là âm Việt hóa |
| 162 | 曾 | tằng | — | — | N | 曾=tằng (Thiều Chửu); 'từng' là âm Việt hóa |
| 163 | 冻 | đống | — | — | N | 冻=đống (Thiều Chửu: chất lỏng đông lại tục gọi là đống) |
| 164 | 歹 | đãi | — | — | N | 歹=đãi (Thiều Chửu: tục đọc là đãi; tồi, xấu) |
| 165 | 咱 | gia | — | — | N | 咱=gia (Thiều Chửu: cha/gia; chọn gia để khỏi lẫn với 'cha'); 'ta' là đại từ thuần Việt |
| 166 | 漱 | sấu | — | — | N | 漱=sấu (Thiều Chửu: súc miệng); 'súc' không phải âm Hán Việt |
| 167 | 橙 | chanh | — | — | H | 橙=chanh (Thiều Chửu) |
| 168 | 讶 | nhạ | — | — | H | 讶=nhạ (Thiều Chửu); từ Việt 'kinh ngạc' viết 驚愕 |
| 169 | 闸 | áp | — | — | T | 闸 (閘)=áp (Thiều Chửu: thủy áp 水閘 đập nước; tục đọc sạp) |
| 170 | 掰 | ? | — | — | N | 掰: nguồn chỉ có âm Nôm 'bẻ' (hvpinyin), không có âm Hán Việt có nguồn |
| 171 | 撞 | chàng | — | — | H | 撞=chàng (Thiều Chửu) |
| 172 | 傻 | sọa | — | — | H | 傻=sọa (Thiều Chửu) |
| 173 | 挣 | tránh | — | — | H | 挣=tránh (Thiều Chửu: 掙 tránh thoát) |
| 174 | 膀 | bàng | — | — | H | 膀=bàng (Thiều Chửu: kiên bàng 肩膀, bàng quang) |
| 175 | 叨 | thao | — | — | H | 叨=thao (Thiều Chửu) |
| 176 | 癌 | nham | — | — | H | 癌=nham (Thiều Chửu: vị nham 胃癌) |
| 177 | 吗 | mạ | — | — | H | 吗=mạ (Thiều Chửu 嗎: tục dùng làm tiếng giúp lời) |
| 178 | 姥 | mỗ | — | — | H | 姥=mỗ (Thiều Chửu: mỗ/mụ) |
| 179 | 怂 | túng | — | — | H | 怂=túng (Thiều Chửu: túng dũng 慫慂) |
| 180 | 惰 | nọa | — | — | H | 惰=nọa (Thiều Chửu: nọa tính 惰性) |
| 181 | 盹 | truân | — | — | H | 盹=truân (Thiều Chửu: đả truân 打盹) |
| 182 | 捶 | chúy | — | — | H | 捶=chúy (Thiều Chửu) |
| 183 | 桩 | thung | — | — | H | 桩=thung (Thiều Chửu 樁) |
| 184 | 煲 | bảo | — | — | H | 煲=bảo (Thiều Chửu: nấu lửa riu riu) |
| 185 | 瞄 | miểu | — | — | H | 瞄=miểu (Thiều Chửu: miểu chuẩn 瞄準) |
| 186 | 腼 | điến | — | — | H | 腼=điến (Thiều Chửu) |
| 187 | 惕 | dịch | — | — | H | 惕=dịch (Thiều Chửu) |
| 188 | 踹 | đoán | — | — | H | 踹=đoán (Thiều Chửu: dọi gót chân) |
| 189 | 阱 | tịnh | — | — | H | 阱=tịnh (Thiều Chửu: hãm tịnh 陷阱 cạm bẫy) |
| 190 | 靶 | bá | — | — | H | 靶=bá (Thiều Chửu: cái đích để bắn) |
| 191 | 椎 | truy | — | — | H | 椎=truy (Thiều Chửu) |
| 192 | 佑 | hữu | — | — | H | 佑=hữu (Thiều Chửu: bảo hữu 保佑) |

## 5. Từ Việt đọc âm không có trong nguồn (hạn chế của nguồn, không tự thêm âm)

Các mục dưới đây giữ âm có nguồn trong `hanviet`. `tu_viet` ghi từ Việt thật, `char_note` ghi "từ Việt đọc '…'" (`GAP_NOTE` trong script):

- **Âm Hán Việt mà nguồn thiếu:**
  - 资源 / 资助: tài (nguồn chỉ có tư)
  - 身份 / 身份证: phận (nguồn chỉ có phần, phân)
  - 宗教 / 宗旨: tôn (nguồn chỉ có tông)
  - 慢性: mãn (nguồn chỉ có mạn)
  - 公平: bằng (nguồn chỉ có bình)
  - 激烈: kịch (nguồn chỉ có kích)
  - 激励: khích (nguồn chỉ có kích)
  - 渗透: thẩm (nguồn chỉ có sấm)
  - 牡丹: đơn (nguồn chỉ có đan)
  - 知识分子: trí (nguồn chỉ có tri)
  - 田径: kinh (nguồn chỉ có kính)
  - 汇聚: hội (nguồn chỉ có hối)
  - 致命: chí (nguồn chỉ có trí)
  - 软弱: nhu (nguồn chỉ có nhuyễn)
- **Âm Việt hóa trong từ Việt:**
  - 安慰: ủi
  - 威风: oai
  - 救命 / 革命 / 性命 / 致命: mạng
  - 模糊: mơ
  - 珠宝: báu
  - 无故 / 缘故: cớ
  - 豆腐: hũ
  - 馒头: màn thầu
- **Từ Việt chứa âm Nôm vừa thay ở R1:** 油 dầu, 饼 bánh, 桶 thùng, 哭 khóc, 割 cắt, 曾 từng, 炒 xào, 煎 chiên, 丝 / 丝毫 tơ, 戴 đội, 框 khung, 桥 cầu, 笨 đần, 粪 phân, 蘸 chấm, 爹 tía, 赎 chuộc, 箱子 rương, 解围 giải vây, 譬如 ví như, 催促 thôi thúc, 督促 đốc thúc. Trong các mục này, `tu_viet` vẫn là từ Việt (cùng gốc), còn `hanviet` là âm Hán Việt.
- **Từ Việt dùng chữ khác:**
  - 中奖: trúng thưởng (賞)
  - 启动: khởi động (起)
  - 惊讶: kinh ngạc (愕)

## 6. Tái lập

```
python -I scripts/r1_apply.py                    # ghi 06_review/fixes_r1_doc_am.tsv
python -I scripts/r1_apply.py --dump-rules       # in bảng mục 4
python -I scripts/r1_apply.py --review <file>    # bảng đối chiếu cũ → mới từng mục
```
