# Báo cáo R1: thống nhất âm Hán Việt cấp chữ

*Reviewer R1, model **Opus**, 16/11/2026. R1 không soạn các mục này.*

Sản phẩm:
- `06_review/quy_uoc_doc_am_chot.md`: quy ước chốt, bảng quyết định đầy đủ.
- `06_review/fixes_r1_doc_am.tsv`: 218 dòng, reviewer `opus:r1_doc_am`.
- `scripts/r1_apply.py`: script sinh fixes, chạy lại được.

## 1. Số liệu chính

| Chỉ số | Giá trị |
|---|---|
| Quy tắc trong bảng `RULES` | 192: N 39, H 33, T 120 |
| Quy tắc thực sự làm đổi âm ít nhất một mục | 95 chữ |
| Âm được ghi nhận giữ dù không có trong Thiều Chửu (`KEEP`) | 40 |
| Dòng fix | 218 |
| Mục đổi âm (`hanviet`) | 186 |
| Mục chỉ đổi `char_note` / `status` / văn bản | 32 |
| Lỗi validator trên các dòng fixes_r1 | 0 |

Các lỗi còn lại trong out (15) là lỗi cũ, đã được fixes_r0 xử lý.

Merge thử (`--expect 10898 --drafted-by-map`) ra đủ 10.898 dòng. Có 232 mục mang fix (r0 + r1). `status`: 10.886 draft, 12 needs_review.

### Số mục đổi âm theo loại quy tắc

- **N, âm Nôm / Việt hóa → âm Hán Việt có nguồn: 87 mục.**
  - 奖 thưởng→tưởng 14; 油 dầu→du 13; 箱 rương→tương 4; 曾 từng→tằng 4; 喝 húp/hét→hát 3
  - 饼 bánh→bính 3; 冻 đông→đống 3; 丝 tơ→ti 3; 妈 má→ma 2 mục (3 chữ)
  - Mỗi chữ sau 2 mục: 戴 đội→đái, 桶 thùng→dũng, 喷 phun→phún, 笼 lồng→lung, 促 thúc→xúc, 炉 lò→lô, 框 khung→khuông, 粪 phân→phẩn, 歹 tồi→đãi
  - Mỗi chữ sau 1 mục: 哭 khóc→khốc, 爬 bò→ba, 桥 cầu→kiều, 笨 đần→bổn, 炒 xào→sao, 茄 cà→gia, 割 cắt→cát, 霉 mốc→môi, 嚏 xì→đế, 椰 dừa→gia, 煎 chiên→tiên, 爹 tía→đa, 蘸 chấm→trám, 围 vây→vi, 譬 ví→thí, 饵 nhử→nhị, 赎 chuộc→thục, 帖 thiệp→thiếp, 咱 ta→gia, 漱 súc→sấu
  - 掰 bẻ→`?` (needs_review)
- **H, âm chỉ có ở hvpinyin, không có từ Việt chứng thực → Thiều Chửu: 46 mục.**
  - 撞 tràng→chàng 4; 晃 hoàng→hoảng 3; 姥 lão→mỗ 2 mục
  - Mỗi chữ sau 2 mục: 倒 đáo→đảo, 傻 xọa→sọa, 叨 đao→thao, 堆 đồi→đôi, 挣 tranh→tránh, 膀 bảng→bàng, 癌 ngai→nham
  - Mỗi chữ sau 1 mục: 佑 hựu→hữu, 刹 sa→sát, 吗 ma→mạ, 启 khởi→khải, 埋 man→mai, 怂 tủng→túng, 惕 thích→dịch, 惰 đọa→nọa, 扫 táo→tảo, 捶 chủy→chúy, 桩 trang→thung, 椎 chuy→truy, 橙 tranh→chanh, 炸 trác→tạc, 煲 bao→bảo, 盹 độn→truân, 瞄 miêu→miểu, 腼 điển→điến, 讶 ngạc→nhạ, 踹 soại→đoán, 钉 đính→đinh, 阱 tỉnh→tịnh, 靶 bả→bá
- **T, thống nhất chữ đa âm: 53 mục.**
  - 推 suy→thôi 10; 领 lãnh→lĩnh 9; 幻 huyễn→ảo 6; 量 lượng→lương 4; 受 thọ→thụ 3
  - Mỗi chữ sau 2 mục: 单 đan→đơn, 挑 khiêu→thiêu, 钻 toản→toàn
  - Mỗi chữ sau 1 mục: 尽 tẫn→tận, 吃 khiết→cật, 哨 tiếu→sáo, 少 thiểu→thiếu (缺少), 并 tịnh→tính (并发症), 旋 hoàn→toàn (盘旋), 歪 oai→oa, 滴 trích→tích, 潮 triều→trào (热潮), 脏 tang→tảng, 转 chuyến→chuyển, 迫 bách→bức (压迫), 数 số→sổ (倒数), 去 khứ→khử (去除), 闸 ?→áp

Các mục chỉ đổi văn bản hoặc trạng thái (32):
- 27 mục needs_review được giải (mục 4).
- Thêm `char_note` "từ Việt đọc '…'" cho các mục ở mục 3.
- Sửa `pt_noi_dung` / `khac_biet` / `tu_viet` phụ thuộc trực tiếp vào âm. Ví dụ: 幻想 tu_viet "huyễn tưởng"→"ảo tưởng"; 推 bỏ khac_biet về "suy"; 冻 yeu_to→khong_giup vì "đống" không có từ Việt.
- Mỗi chữ đổi âm trong `pt_noi_dung` được script tự thay theo mẫu "chữ âm_cũ" → "chữ âm_mới". Ví dụ "领 lãnh (nhận)" → "领 lĩnh (nhận)".

## 2. Âm giữ dù không có trong Thiều Chửu (căn cứ)

Có từ Việt thông dụng chứng thực:

| Chữ | Âm giữ | Từ Việt chứng thực |
|---|---|---|
| 领 | lãnh | lãnh đạo, lãnh tụ, lãnh thổ, lãnh sự |
| 单 | đơn | đơn giản, đơn vị, cô đơn, thực đơn |
| 带 | đới | nhiệt đới, ôn đới, hàn đới |
| 延 | diên | diên trì, diên hạn |
| 层 | tầng | tầng lớp, giai tầng |
| 份 | phần | cổ phần |
| 分 | phần | thành phần, phần tử, thủy phần |
| 扩 | khuếch | khuếch đại, khuếch tán |
| 顶 | đỉnh | đỉnh cao, tuyệt đỉnh |
| 摆 | bài | bài trí, bài binh bố trận |
| 间 | gián | gián tiếp, gián đoạn, gián điệp |
| 浓 | nồng | nồng độ, nồng hậu |
| 潮 | trào | trào lưu, cao trào |
| 仇 | thù | thù hận, báo thù |
| 综 | tổng | tổng hợp |
| 并 | tính | thôn tính |
| 旋 | hoàn | khải hoàn |
| 叛 | phản | phản nghịch, phản đồ |
| 峡 | hiệp | Tam Hiệp |
| 萎 | ủy | ủy mị |
| 饺 | cảo | sủi cảo, há cảo |
| 帅 | soái | nguyên soái |
| 玫 | mai | mai khôi |
| 璃 | lê | pha lê |
| 姆 | mẫu | bảo mẫu |
| 迫 | bức | bức thiết, áp bức |
| 勾 | cấu | cấu kết |
| 去 | khử | trừ khử, khử trùng |
| 胧 | lung | mông lung |
| 礁 | tiêu | ám tiêu |
| 缅 | miến | Miến Điện |
| 姐 | tỷ | tỷ muội |
| 侄 | điệt | Thiều Chửu: "mượn làm chữ điệt 姪" |

Giữ vì lý do khác:
- 什 thậm: 什么 = 甚麼.
- 卡 ca, 咖 ca: phiên âm.
- 呵 ha: phiên thiết 虎何切; Thiều Chửu chỉ ghi âm "a" (tiếng đệm).
- 哈 ha: thán từ tượng thanh.
- 橱 trù: mục Thiều Chửu "thụ" là nghĩa khác.
- 吭 khang: Thiều Chửu chỉ có âm của háng.
- 30 chữ khẩu ngữ không có mục Thiều Chửu: giữ âm hvpinyin, xem quy ước mục 3.

Sau R1, merge thử còn 70 nhóm (chữ, âm) / 205 mục dùng âm không có Thiều Chửu. Trước R1 là 146 nhóm / 341 mục. Tất cả 70 nhóm còn lại đều thuộc các danh sách giữ ở trên.

## 3. Từ Việt đọc âm không có trong nguồn (hạn chế của nguồn)

Giữ âm có nguồn. `tu_viet` = từ Việt thật. `char_note` ghi "từ Việt đọc '…'".

- **Âm Hán Việt nguồn thiếu (17 mục):**
  - 资源, 资助: tài
  - 身份, 身份证: phận
  - 宗教, 宗旨: tôn
  - 慢性: mãn
  - 公平: bằng
  - 激烈: kịch
  - 激励: khích
  - 渗透: thẩm
  - 牡丹: đơn
  - 知识分子: trí
  - 田径: kinh
  - 汇聚: hội
  - 致命: chí
  - 软弱: nhu
- **Âm Việt hóa trong từ Việt (11 mục):**
  - 安慰: ủi
  - 威风: oai
  - 救命, 革命, 性命, 致命: mạng
  - 模糊: mơ
  - 珠宝: báu
  - 无故, 缘故: cớ
  - 豆腐: hũ
  - 馒头: màn thầu
- **Âm Nôm vừa thay ở R1:** `tu_viet` vẫn là từ Việt cùng gốc. Các mục: 油 dầu, 饼 bánh, 桶 thùng, 哭 khóc, 割 cắt, 曾 từng, 炒 xào, 煎 chiên, 丝 tơ, 丝毫 tơ hào, 戴 đội, 框 khung, 桥 cầu, 笨 đần, 粪 phân, 蘸 chấm, 爹 tía, 赎 chuộc, 箱子 rương, 解围 giải vây, 譬如 ví như, 催促 thôi thúc, 督促 đốc thúc, 微波炉 lò vi ba.
- **Từ Việt dùng chữ khác:**
  - 中奖: trúng thưởng (賞)
  - 启动: khởi động (起)
  - 惊讶: kinh ngạc (愕)

## 4. Mục needs_review

Trước R1 có 38 mục needs_review. Sau R1 còn 12.

**Đã giải, chuyển sang draft (27 mục, lý do cũ chỉ là chọn âm):**

| Mục | Âm chốt / cách giải |
|---|---|
| 喝, 吃喝玩乐, 喝彩 | hát |
| 师傅 | phó |
| 划 | hoạch (劃) |
| 划得来, 划算 | hoa |
| 寻找 | trảo |
| 推荐 | suy |
| 炸 | tạc |
| 刹车 | sát |
| 崭新 | tiệm (Thiều Chửu: tiệm tân) |
| 扮演 | ban (Thiều Chửu: đả ban) |
| 一并 | tính |
| 周旋, 旋律, 旋涡 | toàn |
| 哨 | sáo |
| 好歹, 歹徒 | đãi |
| 沉着 | trước |
| 沮丧 | trở |
| 错综复杂 | tông |
| 闸 | áp (Thiều Chửu: thủy áp 水閘) |
| 拴 | thuyên (Thiều Chửu nghĩa 2: buộc, thuyên mã 拴馬) |
| 资源, 身份 | giữ âm theo nguồn; từ Việt ghi trong char_note |

**Còn lại (12 mục):**
- 11 mục mà lý do không phải chọn âm, hoặc chưa đủ căn cứ để chọn: 感冒, 一切, 十分, 先天, 克制, 兹, 坎坷, 大名鼎鼎, 把手, 夯实 (夯 không có Thiều Chửu; hvpinyin cho hãng/kháng), 堆砌.
  - 堆砌: âm đã chốt là đôi; giữ needs_review vì nghĩa từ cần xác nhận, lý do đã cập nhật.
- Mới: 掰 `?`, vì nguồn chỉ có âm Nôm "bẻ".

## 5. Khác biệt có chủ đích còn lại sau thống nhất

Chạy `char_consistency.py` trên bản merge thử:
- Nhóm (chữ, pinyin) có từ 2 âm: 85 → 57.
- Chữ có từ 2 âm: 140 → 107.

Kiểm tự động (đối chiếu từng chữ trong từng mục với bảng `RULES`): **0 mục lệch quy tắc**, và **không còn chữ nhiều âm nào nằm ngoài bảng**.

57 nhóm còn lại đều là ngoại lệ theo từ Việt hoặc theo nghĩa, ghi trong bảng. Mỗi dòng dưới đây ghi âm chính, rồi các từ dùng âm khác:

- 面 mian4: diện; miến (bột mì): 面包, 面条儿, 方便面, 面粉
- 行 xing2: hành; hạnh: 品行
- 合: hợp; hiệp: 回合
- 过 guo4: quá; qua: 经过, 通过, 穿过, 透过, 放过, 越过
- 主: chủ; chúa: 公主, 主宰
- 本: bản; bổn: 本分
- 安: an; yên: 安静
- 领: lãnh (dẫn dắt); lĩnh (12 từ: nhận / cổ áo / nắm được)
- 强 qiang2: cường; cưỡng: 强制, 强加, 强占, 强行
- 复: phục; phức (複): 复印, 复杂, 重复, 错综复杂; phúc: 答复
- 推: thôi; suy: 8 từ suy xét / tiến cử
- 从: tòng; thung: 从容, 从容不迫; tùng: 服从
- 计: kế; kê: 统计
- 断: đoạn; đoán: 判断, 诊断, 推断, 果断, 断定, 断然, 当机立断
- 去: khứ; khử: 去除, 除去
- 思 si1: tư; tứ: 构思
- 思 si5: tứ; tư: 心思 (tâm tư)
- 首: thủ; thú: 自首
- 使: sử; sứ: 使馆, 大使, 使命, 使者, 天使
- 折 zhe2: chiết; triệp (摺): 折, 存折
- 依: y; ỷ: 依赖
- 营: doanh; dinh: 营养
- 住: trú; trụ: 禁不住
- 分 fen4: phận; phần: 成分, 水分, 知识分子; phân: 分量
- 劳: lao; lạo: 慰劳
- 少 shao3: thiểu; thiếu: 缺少
- 迫: bách; bức: 迫切, 压迫
- 并: tịnh; tính (併): 合并, 一并, 并发症, 并购
- 幸: hạnh; hãnh: 侥幸, 幸免, 幸存
- 易: dị; dịch: 交易, 贸易
- 当 dang4: đáng; đương: 当天
- 调 diao4: điệu; điều: 调查, 调研, 调动, 调度
- 征: trưng; chinh: 出征, 征服, 长征
- 散: tán; tản: 散步
- 汇: hối; vựng: 词汇
- 将: tương; tướng: 将军
- 监: giám; giam: 监狱
- 背 bei4: bối; bội: 背叛, 违背
- 更 geng1: canh; cánh: 自力更生
- 松: tông; tùng: 松树
- 潮: trào: 潮流, 高潮, 新潮, 热潮; triều: 潮湿, 潮, 潮水
- 纵: túng; tung: 纵横, 纵深
- 丑: xú; sửu: 小丑
- 仿: phỏng; phảng: 仿佛
- 旋: toàn; hoàn: 凯旋
- 武: vũ; võ: 武术, 武侠
- 著: trứ; trước: 著作
- 司: tư: 司令, 司法, 司空见惯; ti: 公司, 司机
- 郁: uất; úc: 浓郁
- 划 hua2: hoa; hoạch: 划 (劃 quẹt)
- 慰: úy; ủy: 安慰
- 累 lei3: lũy; lụy: 拖累
- 勾: câu; cấu: 勾结
- 禁 jin1: câm; cấm: 情不自禁
- 综: tổng; tông: 错综复杂
- 仓: thương; thảng: 仓促
- 姐 jie5: tỷ; thư: 小姐

**Lệch duy nhất có chủ đích do giới hạn nguồn:** 折叠 (gấp) đáng đọc triệp như 折 và 存折, nhưng `cands` của mục này chỉ có "chiết", nên giữ CHIẾT.

## 6. Điểm R1 không chắc (để anh / Codex xem)

1. **奖 tưởng thay cho thưởng (14 mục).**
   - Căn cứ: Thiều Chửu chỉ ghi tưởng; "thưởng" vốn là 賞.
   - Đổi lại, người học quen "giải thưởng", nên TƯỞNG HỌC KIM… có thể lạ tai.
   - Nếu anh muốn ưu tiên độ quen, có thể đảo về thưởng (âm có nguồn hvpinyin). Chỉ cần sửa một dòng trong `RULES`.
2. **推 tách thôi / suy theo nghĩa.** Có 10 mục đổi suy→thôi. "Thôi" chỉ quen trong "thôi xao". Phương án khác là SUY cho tất cả: đơn giản hơn nhưng sai nghĩa gốc.
3. **量 liáng → lương (4 mục).** Thiều Chửu rõ. Tuy vậy tiếng Việt hiện đại ít dùng âm "lương" cho 量.
4. **领: lĩnh cho nghĩa "nhận" và "cổ áo".** Các mục 领取, 申领, 领养, 领带, 白领 đổi sang lĩnh. Tiếng Việt miền Nam vẫn nói "lãnh lương".
5. **Chọn giữa hai âm Thiều Chửu cho chữ khẩu ngữ, không có từ Việt kiểm chứng:**
   - 咱 gia: chọn thay cho "cha" để khỏi lẫn nghĩa.
   - 姥 mỗ: mụ cũng có nguồn.
   - 踹 đoán: sủy cũng có nguồn.
   - 椎 truy: 颈椎. "Chùy" không có trong cands.
   - 歪 oa
   - 滴 tích: Thiều Chửu nói "ta quen đọc trích".
   - 哨 sáo
6. **Âm hvpinyin thay bằng Thiều Chửu:** 吗 mạ, 撞 chàng, 晃 hoảng, 挣 tránh, 钉 đinh, 刹 sát.
   - Các âm "ma, tràng, hoàng, tranh, đính, sa" có thể là âm đọc hiện đại theo pinyin mà hvpinyin thu từ từ điển mới.
   - R1 chọn Thiều Chửu vì không tìm được từ Việt chứng thực.
7. **Âm giữ chưa thật chắc:**
   - 呵 ha, 哈 ha: Thiều Chửu ghi a, cáp.
   - 吭 khang
   - 什 thậm
   - 缅 miến cho 缅怀: "Miến Điện" chứng thực âm, nhưng không chứng thực nghĩa này. Thiều Chửu ghi miễn.
   - 侄 điệt
   - 迫 bức
8. **Thêm goi_nho "'X' trong tiếng Việt có gốc từ chữ này"** cho 11 mục: 油 dầu, 饼 bánh, 桶 thùng, 哭 khóc, 割 cắt, 曾 từng, 炒 xào, 煎 chiên, 丝 tơ, 戴 đội, 妈妈 má.
   - Đây là các cặp thường được dẫn trong tài liệu về âm Hán Việt cổ / Việt hóa.
   - R1 không có nguồn từ nguyên cụ thể trong 01_sources. Nếu muốn chặt, có thể bỏ.
9. **`loai` của các mục Nôm vẫn giữ `cung_dung` với `tu_viet` là từ Việt cùng gốc.** Ví dụ 油 DU / dầu, 箱子 TƯƠNG TỬ / rương.
   - R1 làm vậy để thay đổi ít nhất, theo cách xử lý 资源.
   - R2/R3 có thể cân nhắc hạ xuống `ghep_nghia` / `khong_giup`, vì "dầu" không phải từ Hán Việt theo nghĩa chặt.
10. **R1 không đụng các nhóm sau** vì không thuộc phạm vi "chữ có ≥2 âm / âm không Thiều Chửu":
    - Chữ dùng một âm thống nhất nhưng có thể sai trên toàn bộ.
    - Các lệch do đảo trật tự từ Việt: 语言 / ngôn ngữ, 简单 / đơn giản…; đây không phải lỗi âm.
