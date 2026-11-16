# R3: phân tích toàn cục trên `07_final/merged_v2.jsonl`

*Reviewer opus:r2_set_sample_02 (model: Opus), 16/11/2026. Chỉ phân tích, **không sửa** mục nào ngoài tập set_sample_02. Điều phối quyết việc sửa cả nhóm.*

Nguồn: `07_final/merged_v2.jsonl` (10.898 mục). Script tạm nằm trong scratchpad (`work/hanviet_review/set_sample_02/glob_*.py`, `cls.py`). Các nhận định "quen / không quen với người Việt" là đánh giá của reviewer, chưa được người thẩm định.

## Tóm tắt

| Kiểm | Kết quả | Đề nghị |
|---|---|---|
| (a) Thành ngữ/cụm 4 chữ gắn `cung_dung` | 87/458 mục 4 chữ. A (quen thật) 33, B (sách vở, nhiều người hiểu) 27, **C (thổi phồng rõ) 27** | Hạ 27 mục C về `ghep_nghia`; xem lại 27 mục B |
| Tỷ lệ `cung_dung` của mục 4 chữ theo lô | Lệch rất mạnh: 07b 49%, 08b 46%, 12b 46%, 13b 60%, trong khi 10a 3%, 11a 0%, 13a 0%, 14b 0% | Lỗi hệ thống theo lô; nên chuẩn hóa cùng một ngưỡng |
| (b) Cặp từ cùng chữ, `loai` mâu thuẫn | 0 cặp trùng hanzi khác loai. 35 cặp đối nghĩa (上/下, 男/女…) khác loai, trong đó **6 cặp mâu thuẫn rõ**, 4 cặp nên xem lại, còn lại có lý do | Sửa 6 cặp, xem 4 cặp |
| (c) `pt_noi_dung` có khẳng định nguồn gốc/từ nguyên | 79 + 77 lượt khớp từ khóa, phần lớn là nghĩa chữ ("gốc" = 本/原) hay âm "tích/phạn". Khẳng định nguồn gốc thật: **5 mục trong pt** (2 sai rõ) + 6 mục trong `khac_biet`/`nghia_vi` | Xóa/sửa 5 mục pt; xem 6 mục còn lại |

## (a) Thành ngữ / cụm 4 chữ gắn `cung_dung`

Phân bố `loai` của 458 mục có 4 chữ Hán: ghep_nghia 367, **cung_dung 87**, khong_giup 3, ten_rieng 1.

Tiêu chí: TIEU_CHUAN + HUONG_DAN_REVIEW: "Thành ngữ chỉ là `cung_dung` nếu dạng Hán Việt đó quen với người Việt".

- **A**: dạng Hán Việt quen trong tiếng Việt hiện đại (nhất cử nhất động, bán tín bán nghi, lực bất tòng tâm…) hoặc thuật ngữ (kinh tế thị trường, chủ nghĩa xã hội).
- **B**: có trong tiếng Việt viết, người có học hiểu được, nhưng hiếm trong lời nói. Có vài mục mà tiếng Việt quen một biến thể khác.
- **C**: người Việt bình thường không dùng dạng Hán Việt này. Tiếng Việt thường nói bằng thành ngữ thuần Việt khác, hoặc diễn giải. Đây là thổi phồng.

Theo người soạn:
- Nhóm C: sonnet:batch_07b 13, 08a 4, 08b 4, 13b 3, 09b 2, 11b 1. Toàn bộ là Sonnet.
- Các mục do Opus soạn (hard_02, hard_03) đều thuộc nhóm A.

**Tỷ lệ gắn `cung_dung` của mục 4 chữ theo lô:**

| Lô | Tỷ lệ |
|---|---|
| 07b | 20/41 (49%) |
| 08a | 7/26 (27%) |
| 08b | 12/26 (46%) |
| 09b | 8/23 (35%) |
| 12b | 6/13 (46%) |
| 13b | 9/15 (60%) |
| 09a | 2/29 (7%) |
| 10a | 1/32 (3%) |
| 10b | 3/39 (8%) |
| 11a | 0/30 |
| 13a | 0/26 |
| 14b | 0/29 |

Đây là chênh lệch theo người soạn, không theo độ khó của từ. Ngược lại, ở các lô 0%, vài mục loại A có thể đã bị **đánh thấp**. Điều phối nên quét ngược mục 4 chữ `ghep_nghia` của các lô 0–10% để tìm thành ngữ quen như "nhất cử lưỡng tiện" hay "tự cấp tự túc". Phần quét ngược này chưa làm.

#### Nhóm C: thổi phồng rõ, đề nghị ghep_nghia (bỏ tu_viet; có thể thêm goi_nho nêu cách nói Việt) — 27 mục

| note_key | hanzi | hanviet | tu_viet | drafted_by | ghi chú |
|---|---|---|---|---|---|
| zh:hskstory-hsk7:1792758600000 | 一丝不苟 | NHẤT TI BẤT CẨU | nhất ti bất cẩu | sonnet:batch_07b |  |
| zh:hskstory-hsk7:1792758600056 | 一概而论 | NHẤT KHÁI NHI LUẬN | nhất khái nhi luận | sonnet:batch_07b |  |
| zh:hskstory-hsk7:1792758600058 | 一毛不拔 | NHẤT MAO BẤT BẠT | nhất mao bất bạt | sonnet:batch_07b | tiếng Việt nói 'vắt cổ chày ra nước' |
| zh:hskstory-hsk7:1792758600062 | 一筹莫展 | NHẤT TRÙ MẠC TRIỂN | nhất trù mạc triển | sonnet:batch_07b |  |
| zh:hskstory-hsk7:1792758600072 | 一言不发 | NHẤT NGÔN BẤT PHÁT | nhất ngôn bất phát | sonnet:batch_07b |  |
| zh:hskstory-hsk7:1792758600078 | 一针见血 | NHẤT CHÂM KIẾN HUYẾT | nhất châm kiến huyết | sonnet:batch_07b | tiếng Việt nói 'nói trúng tim đen' |
| zh:hskstory-hsk7:1792758600082 | 一鼓作气 | NHẤT CỔ TÁC KHÍ | nhất cổ tác khí | sonnet:batch_07b |  |
| zh:hskstory-hsk7:1792758600182 | 不以为然 | BẤT DĨ VI NHIÊN | bất dĩ vi nhiên | sonnet:batch_07b |  |
| zh:hskstory-hsk7:1792758600196 | 不厌其烦 | BẤT YẾM KỲ PHIỀN | bất yếm kỳ phiền | sonnet:batch_07b |  |
| zh:hskstory-hsk7:1792758600252 | 不知所措 | BẤT TRI SỞ THỐ | bất tri sở thố | sonnet:batch_07b |  |
| zh:hskstory-hsk7:1792758600256 | 不约而同 | BẤT ƯỚC NHI ĐỒNG | bất ước nhi đồng | sonnet:batch_07b |  |
| zh:hskstory-hsk7:1792758600260 | 不翼而飞 | BẤT DỰC NHI PHI | bất dực nhi phi | sonnet:batch_07b |  |
| zh:hskstory-hsk7:1792758600270 | 不言而喻 | BẤT NGÔN NHI DỤ | bất ngôn nhi dụ | sonnet:batch_07b |  |
| zh:hskstory-hsk7:1792758600496 | 争先恐后 | TRANH TIÊN KHỦNG HẬU | tranh tiên khủng hậu | sonnet:batch_08a |  |
| zh:hskstory-hsk7:1792758600532 | 井底之蛙 | TỈNH ĐỂ CHI OA | tỉnh để chi oa | sonnet:batch_08a | tiếng Việt nói 'ếch ngồi đáy giếng' |
| zh:hskstory-hsk7:1792758600534 | 亡羊补牢 | VONG DƯƠNG BỔ LAO | vong dương bổ lao | sonnet:batch_08a | tiếng Việt nói 'mất bò mới lo làm chuồng' |
| zh:hskstory-hsk7:1792758600720 | 众志成城 | CHÚNG CHÍ THÀNH THÀNH | chúng chí thành thành | sonnet:batch_08a |  |
| zh:hskstory-hsk7:1792758601360 | 冰天雪地 | BĂNG THIÊN TUYẾT ĐỊA | băng thiên tuyết địa | sonnet:batch_08b |  |
| zh:hskstory-hsk7:1792758601806 | 勇往直前 | DŨNG VÃNG TRỰC TIỀN | dũng vãng trực tiền | sonnet:batch_08b |  |
| zh:hskstory-hsk7:1792758601850 | 化险为夷 | HÓA HIỂM VI DI | hóa hiểm vi di | sonnet:batch_08b |  |
| zh:hskstory-hsk7:1792758601870 | 千方百计 | THIÊN PHƯƠNG BÁCH KẾ | thiên phương bách kế | sonnet:batch_08b | tiếng Việt nói 'trăm phương nghìn kế' |
| zh:hskstory-hsk7:1792758603004 | 大惊小怪 | ĐẠI KINH TIỂU QUÁI | đại kinh tiểu quái | sonnet:batch_09b |  |
| zh:hskstory-hsk7:1792758603318 | 守株待兔 | THỦ CHU ĐÃI THỎ | ôm cây đợi thỏ | sonnet:batch_09b | tu_viet 'ôm cây đợi thỏ' là câu dịch thuần Việt, không phải dạng Hán Việt |
| zh:hskstory-hsk7:1792758605976 | 束手无策 | THÚC THỦ VÔ SÁCH | thúc thủ vô sách | sonnet:batch_11b |  |
| zh:hskstory-hsk7:1792758608802 | 自然而然 | TỰ NHIÊN NHI NHIÊN | tự nhiên nhi nhiên | sonnet:batch_13b |  |
| zh:hskstory-hsk7:1792758609260 | 见多识广 | KIẾN ĐA THỨC QUẢNG | kiến đa thức quảng | sonnet:batch_13b |  |
| zh:hskstory-hsk7:1792758609326 | 触目惊心 | XÚC MỤC KINH TÂM | xúc mục kinh tâm | sonnet:batch_13b |  |

#### Nhóm B: có trong văn viết/sách vở, nhiều người Việt hiểu nhưng ít dùng; điều phối cân nhắc (đề nghị: giữ cung_dung chỉ khi dạng HV thật sự quen, còn lại ghep_nghia) — 27 mục

| note_key | hanzi | hanviet | tu_viet | drafted_by | ghi chú |
|---|---|---|---|---|---|
| zh:hskstory-hsk6:1792758600990 | 多才多艺 | ĐA TÀI ĐA NGHỆ | đa tài đa nghệ | sonnet:batch_06a |  |
| zh:hskstory-hsk7:1792758600034 | 一心一意 | NHẤT TÂM NHẤT Ý | nhất tâm nhất ý | sonnet:batch_07b |  |
| zh:hskstory-hsk7:1792758600094 | 万无一失 | VẠN VÔ NHẤT THẤT | vạn vô nhất thất | sonnet:batch_07b |  |
| zh:hskstory-hsk7:1792758600262 | 不耻下问 | BẤT SỈ HẠ VẤN | bất sỉ hạ vấn | sonnet:batch_07b |  |
| zh:hskstory-hsk7:1792758600272 | 不辞而别 | BẤT TỪ NHI BIỆT | bất từ nhi biệt | sonnet:batch_07b |  |
| zh:hskstory-hsk7:1792758600430 | 举一反三 | CỬ NHẤT PHẢN TAM | cử nhất phản tam | sonnet:batch_08a |  |
| zh:hskstory-hsk7:1792758600676 | 以身作则 | DĨ THÂN TÁC TẮC | dĩ thân tác tắc | sonnet:batch_08a |  |
| zh:hskstory-hsk7:1792758600796 | 似是而非 | TỰ THỊ NHI PHI | tự thị nhi phi | sonnet:batch_08a |  |
| zh:hskstory-hsk7:1792758601648 | 刻舟求剑 | KHẮC CHU CẦU KIẾM | khắc chu cầu kiếm | sonnet:batch_08b |  |
| zh:hskstory-hsk7:1792758601672 | 前无古人 | TIỀN VÔ CỔ NHÂN | tiền vô cổ nhân | sonnet:batch_08b |  |
| zh:hskstory-hsk7:1792758601840 | 包罗万象 | BAO LA VẠN TƯỢNG | bao la vạn tượng | sonnet:batch_08b |  |
| zh:hskstory-hsk7:1792758602992 | 大公无私 | ĐẠI CÔNG VÔ TƯ | đại công vô tư | sonnet:batch_09b | tiếng Việt quen 'chí công vô tư' |
| zh:hskstory-hsk7:1792758603286 | 孤陋寡闻 | CÔ LẬU QUẢ VĂN | cô lậu quả văn | sonnet:batch_09b |  |
| zh:hskstory-hsk7:1792758604618 | 成家立业 | THÀNH GIA LẬP NGHIỆP | thành gia lập nghiệp | sonnet:batch_10b | tiếng Việt quen 'thành gia lập thất' |
| zh:hskstory-hsk7:1792758605902 | 朝三暮四 | TRIÊU TAM MỘ TỨ | triêu tam mộ tứ | sonnet:batch_11b |  |
| zh:hskstory-hsk7:1792758607198 | 犹豫不决 | DO DỰ BẤT QUYẾT | do dự bất quyết | sonnet:batch_12a |  |
| zh:hskstory-hsk7:1792758607506 | 皆大欢喜 | GIAI ĐẠI HOAN HỶ | giai đại hoan hỷ | sonnet:batch_12b |  |
| zh:hskstory-hsk7:1792758607572 | 目中无人 | MỤC TRUNG VÔ NHÂN | mục trung vô nhân | sonnet:batch_12b | tiếng Việt quen 'mục hạ vô nhân' |
| zh:hskstory-hsk7:1792758607710 | 知足常乐 | TRI TÚC THƯỜNG LẠC | tri túc thường lạc | sonnet:batch_12b |  |
| zh:hskstory-hsk7:1792758607804 | 礼尚往来 | LỄ THƯỢNG VÃNG LAI | lễ thượng vãng lai | sonnet:batch_12b |  |
| zh:hskstory-hsk7:1792758607982 | 突如其来 | ĐỘT NHƯ KỲ LAI | đột như kỳ lai | sonnet:batch_12b |  |
| zh:hskstory-hsk7:1792758608806 | 自相矛盾 | TỰ TƯƠNG MÂU THUẪN | tự mâu thuẫn | sonnet:batch_13b | tu_viet 'tự mâu thuẫn' là dạng rút gọn |
| zh:hskstory-hsk7:1792758609020 | 萍水相逢 | BÌNH THỦY TƯƠNG PHÙNG | bình thủy tương phùng | sonnet:batch_13b |  |
| zh:hskstory-hsk7:1792758609202 | 袖手旁观 | TỤ THỦ BÀNG QUAN | tụ thủ bàng quan | sonnet:batch_13b |  |
| zh:hskstory-hsk7:1792758609252 | 见义勇为 | KIẾN NGHĨA DŨNG VI | kiến nghĩa dũng vi | sonnet:batch_13b |  |
| zh:hskstory-hsk7:1792758609256 | 见利忘义 | KIẾN LỢI VONG NGHĨA | kiến lợi vong nghĩa | sonnet:batch_13b |  |
| zh:hskstory-hsk7:1792758609746 | 足智多谋 | TÚC TRÍ ĐA MƯU | túc trí đa mưu | sonnet:batch_14a |  |

#### Nhóm A: quen thuộc thật, giữ cung_dung — 33 mục

| note_key | hanzi | hanviet | tu_viet | drafted_by | ghi chú |
|---|---|---|---|---|---|
| zh:hskstory-hsk6:1792758601920 | 未成年人 | VỊ THÀNH NIÊN NHÂN | vị thành niên | opus:hard_02 | thuật ngữ |
| zh:hskstory-hsk7:1792758600004 | 一举一动 | NHẤT CỬ NHẤT ĐỘNG | nhất cử nhất động | sonnet:batch_07b |  |
| zh:hskstory-hsk7:1792758600036 | 一成不变 | NHẤT THÀNH BẤT BIẾN | nhất thành bất biến | sonnet:batch_07b |  |
| zh:hskstory-hsk7:1792758600250 | 不知不觉 | BẤT TRI BẤT GIÁC | bất tri bất giác | sonnet:batch_07b |  |
| zh:hskstory-hsk7:1792758601210 | 全心全意 | TOÀN TÂM TOÀN Ý | toàn tâm toàn ý | sonnet:batch_08b |  |
| zh:hskstory-hsk7:1792758601478 | 出口成章 | XUẤT KHẨU THÀNH CHƯƠNG | xuất khẩu thành chương | sonnet:batch_08b |  |
| zh:hskstory-hsk7:1792758601708 | 力不从心 | LỰC BẤT TÒNG TÂM | lực bất tòng tâm | opus:hard_02 |  |
| zh:hskstory-hsk7:1792758601864 | 千军万马 | THIÊN QUÂN VẠN MÃ | thiên quân vạn mã | sonnet:batch_08b |  |
| zh:hskstory-hsk7:1792758601866 | 千变万化 | THIÊN BIẾN VẠN HÓA | thiên biến vạn hóa | sonnet:batch_08b |  |
| zh:hskstory-hsk7:1792758601878 | 半信半疑 | BÁN TÍN BÁN NGHI | bán tín bán nghi | sonnet:batch_08b |  |
| zh:hskstory-hsk7:1792758602576 | 喜怒哀乐 | HỶ NỘ AI LẠC | hỉ nộ ai lạc | sonnet:batch_09a | tu_viet viết 'hỉ' lệch với hanviet 'HỶ' |
| zh:hskstory-hsk7:1792758602642 | 四通八达 | TỨ THÔNG BÁT ĐẠT | tứ thông bát đạt | sonnet:batch_09a |  |
| zh:hskstory-hsk7:1792758602994 | 大同小异 | ĐẠI ĐỒNG TIỂU DỊ | đại đồng tiểu dị | sonnet:batch_09b |  |
| zh:hskstory-hsk7:1792758603048 | 天经地义 | THIÊN KINH ĐỊA NGHĨA | thiên kinh địa nghĩa | sonnet:batch_09b |  |
| zh:hskstory-hsk7:1792758603054 | 天长地久 | THIÊN TRƯỜNG ĐỊA CỬU | thiên trường địa cửu | sonnet:batch_09b |  |
| zh:hskstory-hsk7:1792758603386 | 实事求是 | THỰC SỰ CẦU THỊ | thực sự cầu thị | sonnet:batch_09b |  |
| zh:hskstory-hsk7:1792758603672 | 居安思危 | CƯ AN TƯ NGUY | cư an tư nguy | opus:hard_03 |  |
| zh:hskstory-hsk7:1792758603788 | 市场经济 | THỊ TRƯỜNG KINH TẾ | kinh tế thị trường | sonnet:batch_10a | thuật ngữ, không phải thành ngữ |
| zh:hskstory-hsk7:1792758604486 | 惊天动地 | KINH THIÊN ĐỘNG ĐỊA | kinh thiên động địa | sonnet:batch_10b |  |
| zh:hskstory-hsk7:1792758604490 | 惊心动魄 | KINH TÂM ĐỘNG PHÁCH | kinh tâm động phách | sonnet:batch_10b |  |
| zh:hskstory-hsk7:1792758605454 | 改邪归正 | CẢI TÀ QUY CHÍNH | cải tà quy chính | opus:hard_03 |  |
| zh:hskstory-hsk7:1792758606126 | 根深蒂固 | CĂN THÂM ĐẾ CỐ | thâm căn cố đế | sonnet:batch_11b | tu_viet đảo thành 'thâm căn cố đế' (đúng tiếng Việt) |
| zh:hskstory-hsk7:1792758606418 | 汗马功劳 | HÃN MÃ CÔNG LAO | công lao hãn mã | opus:hard_03 | tu_viet 'công lao hãn mã' (đảo, đúng) |
| zh:hskstory-hsk7:1792758606832 | 滔滔不绝 | THAO THAO BẤT TUYỆT | thao thao bất tuyệt | sonnet:batch_12a |  |
| zh:hskstory-hsk7:1792758607212 | 独一无二 | ĐỘC NHẤT VÔ NHỊ | độc nhất vô nhị | sonnet:batch_12a |  |
| zh:hskstory-hsk7:1792758607290 | 理所当然 | LÝ SỞ ĐƯƠNG NHIÊN | lý sở đương nhiên | opus:hard_03 |  |
| zh:hskstory-hsk7:1792758607500 | 百科全书 | BÁCH KHOA TOÀN THƯ | bách khoa toàn thư | sonnet:batch_12b | thuật ngữ |
| zh:hskstory-hsk7:1792758607706 | 知识分子 | TRI THỨC PHẦN TỬ | phần tử trí thức | opus:hard_03 | thuật ngữ |
| zh:hskstory-hsk7:1792758607812 | 社会主义 | XÃ HỘI CHỦ NGHĨA | chủ nghĩa xã hội | opus:hard_03 | thuật ngữ |
| zh:hskstory-hsk7:1792758608778 | 自力更生 | TỰ LỰC CÁNH SINH | tự lực cánh sinh | opus:hard_03 |  |
| zh:hskstory-hsk7:1792758608926 | 苦尽甘来 | KHỔ TẬN CAM LAI | khổ tận cam lai | sonnet:batch_13b |  |
| zh:hskstory-hsk7:1792758609644 | 资本主义 | TƯ BẢN CHỦ NGHĨA | chủ nghĩa tư bản | opus:hard_03 | thuật ngữ |
| zh:hskstory-hsk7:1792758609800 | 身不由己 | THÂN BẤT DO KỶ | thân bất do kỷ | sonnet:batch_14a |  |

## (b) Cặp từ cùng chữ có `loai` mâu thuẫn

Phương pháp:
1. Tìm mục trùng hanzi mà khác `loai`: **0 cặp**.
2. Tìm cặp 2 chữ thay một chữ bằng chữ đối nghĩa hoặc cùng trường nghĩa (上/下, 前/后, 男/女, 内/外, 正/反, 轻/重, 早/晚, 父/母…; khoảng 65 cặp chữ), có `loai` khác nhau giữa cung_dung / khac_dung / ghep_nghia / yeu_to / khong_giup: **35 cặp**.
3. Tìm cặp hậu tố 儿/子 hoặc từ láy so với chữ đơn: không có mâu thuẫn đáng kể.

Phần lớn 35 cặp khác nhau là có lý do, vì từ Việt chỉ có một vế. Ví dụ: 东西/东北, 主人/客人, 有关/无关, 天上/天下, 先天/后天.

### Mâu thuẫn rõ: đề nghị sửa

| # | Cặp | Hiện tại | Vấn đề | Đề nghị |
|---|---|---|---|---|
| 1 | 上游 `zh:hskstory-hsk7:1792758600120` / 下游 `zh:hskstory-hsk7:1792758600154` | 上游 khac_dung (thượng du), 下游 cung_dung (hạ du) | Có căn cứ một phần: "thượng du" tiếng Việt là miền núi, còn "hạ du" có dùng cho vùng hạ lưu (tin lũ). Nhưng 下游 còn nghĩa "khâu sau (chuỗi sản xuất), đứng chót", và "hạ du" không phải cách nói phổ biến cho "hạ lưu" | 下游 → khac_dung hoặc ghep_nghia, tu_viet/goi_nho nêu "hạ lưu". Hai mục cùng lô 07b nên viết song song |
| 2 | 伯父 `zh:hskstory-hsk7:1792758600776` / 伯母 `zh:hskstory-hsk7:1792758600774` | 伯父 cung_dung (bá phụ), 伯母 ghep_nghia | "Bá phụ" và "bá mẫu" cùng mức (văn kiếm hiệp, xưng hô cổ). Không lý do gì một vế cung_dung | 伯父 → ghep_nghia (hoặc cả hai khac_dung với khac_biet "chỉ gặp trong truyện dịch") |
| 3 | 男人 `zh:hskstory-hsk3:1792758600682` / 女人 `zh:hskstory-hsk3:1792758600336` | 男人 ghep_nghia, 女人 cung_dung (nữ nhân) | "Nữ nhân" không phải từ Việt thông dụng (chỉ gặp trong truyện dịch, giọng đùa); cùng mức với "nam nhân" | 女人 → ghep_nghia |
| 4 | 早年 `zh:hskstory-hsk7:1792758605734` / 晚年 `zh:hskstory-hsk7:1792758605824` | 早年 ghep_nghia, 晚年 cung_dung (vãn niên) | "Vãn niên" rất sách vở; người Việt nói "tuổi già, về già, những năm cuối đời" | 晚年 → ghep_nghia. 早年 đã sửa nghĩa trong fixes_r2_set_sample_02 |
| 5 | 轻视 `zh:hskstory-hsk7:1792758609856` / 重视 `zh:hskstory-hsk4:1792758601856` | 轻视 cung_dung (khinh thị), 重视 ghep_nghia | Tiếng Việt có cả "khinh thị" và "trọng thị". Nhưng "trọng thị" Việt là đón tiếp long trọng, tôn kính, khác 重视 "coi trọng" | 重视 → khac_dung, tu_viet "trọng thị", khac_biet nêu chỗ khác |
| 6 | 长期 `zh:hskstory-hsk5:1792758602966` / 短期 `zh:hskstory-hsk5:1792758602244` | 长期 cung_dung (trường kỳ), 短期 ghep_nghia | "Trường kỳ" Việt gắn với "kháng chiến trường kỳ", sắc thái văn chương. Nghĩa "dài hạn" (vay dài hạn) tiếng Việt nói "dài hạn". Chưa hẳn sai, nhưng lệch với cách nói hiện đại | 长期 → khac_dung (khac_biet: tiếng Việt "trường kỳ" chủ yếu trong "kháng chiến trường kỳ"; nghĩa dài hạn nói "dài hạn"), hoặc giữ cung_dung kèm goi_nho "dài hạn" |

### Nên xem lại (có lý do một phần)

| Cặp | Hiện tại | Ghi chú |
|---|---|---|
| 上级 `zh:hskstory-hsk6:1792758600044` / 下级 `zh:hskstory-hsk7:1792758600158` | cung_dung / khac_dung | Hợp lý ("hạ cấp" Việt hay mang nghĩa kém chất lượng). Giữ; chỉ cần khac_biet bớt khẳng định "giáng cấp" |
| 正面 `zh:hskstory-hsk6:1792758602048` / 反面 `zh:hskstory-hsk7:1792758602074` / 负面 `zh:hskstory-hsk6:1792758603068` | cung_dung / khac_dung / ghep_nghia | 正面 Trung có cả nghĩa "tích cực" (正面影响), "chính diện" Việt không có nghĩa này. Nếu câu ví dụ là nghĩa tích cực thì 正面 nên khac_dung, song song với 反面 |
| 上台 `zh:hskstory-hsk6:1792758600036` / 下台 `zh:hskstory-hsk7:1792758600142` | khac_dung / ghep_nghia | "Hạ đài" Việt hiếm; có thể chấp nhận. Chỉ nên viết goi_nho song song |
| 尺 `zh:hskstory-hsk6:1792758601212` | cung_dung, tu_viet "thước", hanviet XÍCH | tu_viet không phải từ Hán Việt của mục (thước ≠ xích). Theo quy ước R1 về âm Việt hóa, nên ghi rõ trong char_note; xem lại loai (yeu_to/khac_dung) |

## (c) Khẳng định nguồn gốc / điển tích trong `pt_noi_dung`

Tìm theo từ khóa: gốc, xuất xứ, điển, bắt nguồn, nguồn gốc, vốn là, nguyên nghĩa, thời xưa, cổ đại, tương truyền, câu chuyện, tên sách và triều đại, mượn từ, tiếng Anh/Nhật/Phạn…
- Lượt quét 1 khớp 79 mục, lượt 2 khớp 77 mục.
- Phần lớn là **dương tính giả**: "gốc" là nghĩa chữ 本/原/根 (bản gốc, căn nguyên); "tích", "phạn", "khổng" là âm Hán Việt.
- Không mục nào có trường `tu_nguyen`.
- R1b đã viết lại các câu "'X' có gốc từ chữ này" thành "gợi nhớ…".

### Khẳng định nguồn gốc thật trong `pt_noi_dung`: đề nghị sửa

| note_key | hanzi | pt hiện tại (trích) | Vấn đề | Đề nghị |
|---|---|---|---|---|
| zh:hskstory-hsk3:1792758600536 | 方便面 | "面 miến (mì; 'mì' tiếng Việt bắt nguồn từ chữ này)" | Từ nguyên không nguồn; 面 không thuộc danh sách R1 được phép ghi gốc. Mục này qua dieu_phoi_r0 nhưng không qua r1b. (Bản merge đã đúng âm PHƯƠNG TIỆN MIẾN; out gốc batch_01b còn E_HV_COUNT, nhưng fix r0 đã ghi đè.) | Đổi thành "gợi nhớ: 'mì' trong tiếng Việt (liên tưởng)" hoặc bỏ |
| zh:hskstory-hsk1:1792758600504 | 要 | "(nghĩa gốc: quan trọng)" | **Sai**: nghĩa gốc của 要 là "eo" (腰), không phải "quan trọng" | Bỏ ngoặc "nghĩa gốc" |
| zh:hskstory-hsk3:1792758600848 | 角 | "nghĩa gốc là góc (như 'tam giác')" | **Sai**: nghĩa gốc của 角 là "sừng" | Đổi "nghĩa 'góc' như 'tam giác'" |
| zh:hskstory-hsk6:1792758603320 | 酷 | "(nghĩa gốc là cực độ, tàn ác)" | Khẳng định "nghĩa gốc" không nguồn (Thiều Chửu chỉ ghi nghĩa tàn ác; rất) | Đổi "nghĩa Hán Việt: tàn ác, quá mức" |
| zh:hskstory-hsk7:1792758611086 | 麻 | "như ma túy (vốn chỉ chất làm tê mê)" | "vốn chỉ" là khẳng định lịch sử | Đổi "麻 = tê, như 'ma túy', 'ma tê'" |

### Mức nhẹ: trong `khac_biet` / `nghia_vi` (ngoài phạm vi pt, ghi để tham khảo)

| note_key | hanzi | Trích | Ghi chú |
|---|---|---|---|
| zh:hskstory-hsk1:1792758600084 | 他 | "'tha'… có nghĩa gốc là 'khác'; nghĩa đại từ… là cách dùng hiện đại" | Khẳng định lịch sử ngữ nghĩa không nguồn; nên viết "'tha' trong 'tha nhân, tha hương' nghĩa là 'khác'" |
| zh:hskstory-hsk6:1792758601966 | 枪 | "(cũng là nghĩa gốc của chữ)" | Bỏ ngoặc |
| zh:hskstory-hsk6:1792758603320 | 酷 | "nghĩa 'ngầu' là mượn từ tiếng Anh 'cool'" | Phổ biến, chấp nhận được; có thể đổi "dùng như tiếng Anh 'cool'" |
| zh:hskstory-hsk7:1792758607464 | 症结 | nghia_vi "nghĩa gốc: khối cứng trong bụng" | Có thể giữ (Đông y), hoặc đổi "cũng: (Đông y) khối cứng trong bụng" |
| zh:hskstory-hsk7:1792758608718 | 脉络 | "Tiếng Trung nghĩa gốc 'mạch máu'" | Đổi "nghĩa đen" |
| zh:hskstory-hsk7:1792758601940 | 卡车 | pt "卡 ca (phiên âm 'car')" | Hay được nêu nhưng không có nguồn trong dự án; mức thấp |

Các mục nêu điển/truyện như 曰 ("tử viết"), 姐姐/吩咐 ("trong truyện dịch"), 刹那 (phiên âm tiếng Phạn), 漫画/主人公 (cùng chữ với tiếng Nhật) là nhận xét cách dùng hoặc sự thật phổ biến, không cần sửa.

## Liên hệ với mẫu set_sample_02 (169 mục HSK7-9, Sonnet lô 10a–14b)

Ngoài thành ngữ, mẫu cho thấy lỗi `loai` theo **hai chiều** với từ 2 chữ:
- **Thổi phồng cung_dung** cho từ Việt rất sách vở hoặc khác nghĩa: 海藻 hải tảo, 瓦解 ngõa giải, 褒贬 bao biếm, 解体 giải thể (Việt: giải thể tổ chức), 降临 giáng lâm (Việt: thần thánh giáng xuống).
- **Đánh thấp** (ghep_nghia) cho từ Việt thông dụng: 检讨 kiểm thảo, 生前 sinh tiền, 虚幻 hư ảo, 随身 tùy thân.
- Liên từ gắn ghep_nghia thay vì hu_tu (非但), lệch với 不但/不仅/不光.

Ước lượng: khoảng 6% mục 2 chữ của các lô Sonnet 10–14 có `loai` lệch giữa cung_dung và ghep_nghia/khac_dung (9/144 trong mẫu), chia gần đều hai chiều. Vì không có hướng lệch chung, không thể sửa hàng loạt bằng quy tắc. Muốn sửa thì phải rà theo danh sách từ Việt (ví dụ đối chiếu `tu_viet`/hanviet với một từ điển tiếng Việt).
