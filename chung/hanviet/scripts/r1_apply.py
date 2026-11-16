"""R1 (Opus): thống nhất âm Hán Việt cấp chữ, sinh 06_review/fixes_r1_doc_am.tsv.

Chạy (từ thư mục hanviet):
  python -I scripts/r1_apply.py [--out 06_review/fixes_r1_doc_am.tsv] [--review <scratch.tsv>] [--dump-rules]

Đầu vào: 07_final/merged_v1.jsonl (âm hiện tại), 02_chars/item_hv.jsonl (cands, syl, phồn thể),
04_draft/out/*.tsv + 06_review/fixes_*.tsv trừ fixes_r1* (giá trị 11 cột hiện tại).
Bảng quyết định RULES nhúng dưới đây (cũng in ra markdown bằng --dump-rules).
Ưu tiên chọn âm cho mỗi chữ: w (theo từ, hanzi của mục) > s (theo âm tiết pinyin, từ item_hv.syl) > d (mặc định).
Âm đích phải có trong cands của chữ ở vị trí đó (so reading_key), nếu không thì bỏ qua và báo.
Dòng fix mang đủ 11 cột theo giá trị hiện tại; chỉ đổi hanviet/char_note và, khi cần, pt_noi_dung/khac_biet/
tu_viet/loai/status/review_reason (OVERRIDES, RESOLVE).
"""
import sys, os, json, glob, re, argparse, collections, unicodedata
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
from hv_common import reading_key, display

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COLS = "note_key hanviet nghia_vi loai tu_viet khac_biet pt_kieu pt_noi_dung status review_reason char_note".split()
REVIEWER = "opus:r1_doc_am"

# ---------------------------------------------------------------------------
# BẢNG QUYẾT ĐỊNH
# cat: N = âm Nôm/Việt hóa -> âm HV có nguồn; H = âm chỉ có ở hvpinyin, không có từ Việt chứng thực -> Thiều Chửu;
#      T = thống nhất giữa các lô (chữ đa âm, chọn theo pinyin / nghĩa / từ Việt); G = giữ âm (chỉ ghi để kiểm, không đổi)
# n: lý do ngắn ghi vào char_note
# ---------------------------------------------------------------------------
def R(c, d=None, s=None, w=None, cat="T", n="", why=""):
    return dict(c=c, d=d, s=s or {}, w=w or {}, cat=cat, n=n, why=why or n)

RULES = [
    # ---- điểm tranh cãi nêu trong quy_uoc_doc_am_de_xuat.md ----
    R("受", "thụ", n="受=thụ (cảm thụ, hưởng thụ, thụ lý; Thiều Chửu chỉ ghi thụ; 'thọ' chỉ có ở hvpinyin)"),
    R("单", "đơn", n="单 dān=đơn (đơn giản, cô đơn, thực đơn)", why="từ Việt: đơn giản, đơn vị, thực đơn, cô đơn; 'đơn' có ở hvpinyin+Unihan; Thiều Chửu giải nghĩa 'Đơn...' nhưng ghi âm đan"),
    R("推", "thôi", w={k: "suy" for k in ["推荐", "推测", "推断", "推理", "推算", "推论", "推崇", "推选"]},
      n="推: thôi = đẩy (Thiều Chửu: đẩy lên, dời đi; 推敲 thôi xao); suy = suy xét, suy cử (suy luận, suy đoán, suy cử, suy tôn)"),
    R("当", None, s={"dang1": "đương", "dang4": "đáng", "dang5": "đáng"}, w={"当天": "đương"},
      n="当: dāng=đương (đương nhiên), dàng=đáng (thích đáng, chính đáng)", why="theo pinyin; 当天 giữ đương cùng nhóm 当日/当晚 (nghĩa 'ngay hôm đó')"),
    R("尽", "tận", n="尽=tận (tận lực, tận tình); 儘 jǐn hvpinyin cũng ghi tận", why="儘 là chữ phái sinh của 盡; hvpinyin ghi 儘=tận; tận là yếu tố quen (tận lực, tận dụng)"),
    R("调", None, s={"tiao2": "điều", "diao4": "điệu"}, w={k: "điều" for k in ["调查", "调研", "调动", "调度"]},
      n="调: tiáo=điều, diào=điệu; điều tra/điều nghiên/điều động/điều độ theo từ Việt"),
    R("旋", "toàn", w={"凯旋": "hoàn"}, n="旋=toàn (Thiều Chửu: quay, xoáy: toàn phong, toàn oa); 凯旋 theo từ Việt 'khải hoàn'"),
    R("妈", "ma", cat="N", n="妈=ma (Thiều Chửu: tục gọi mẹ là ma ma 媽媽); 'má' là âm Việt hóa"),
    R("傅", "phó", n="傅=phó (Thiều Chửu: sư phó 師傅); 'sư phụ' trong tiếng Việt là 師父"),
    R("划", None, s={"hua2": "hoa", "hua4": "hoạch"}, w={"划": "hoạch"},
      n="划: huá=hoa (划 chèo; 划算/划得来 nguồn chỉ có hoa), huà=hoạch (劃: kế hoạch); 划 'quẹt, vạch' là 劃 → hoạch"),
    R("奖", "tưởng", cat="N", n="奖=tưởng (Thiều Chửu: tưởng lệ; từ Việt 'tưởng thưởng'); 'thưởng' là âm của 賞",
      why="hvpinyin ghi thưởng (lẫn với 賞); Thiều Chửu chỉ ghi tưởng; 奖赏 = tưởng thưởng"),
    R("量", None, s={"liang2": "lương"}, n="量 liáng (đo) = lương (Thiều Chửu: cân nhắc, đo xem dài ngắn gọi là lương); liàng = lượng"),
    R("领", "lãnh", w={k: "lĩnh" for k in ["本领", "纲领", "要领", "领域", "占领", "领悟", "领略", "领取", "申领", "领养", "白领", "领带"]},
      n="领: lãnh = dẫn dắt (lãnh đạo, lãnh tụ, lãnh thổ); lĩnh = nhận / cổ áo / nắm được (lĩnh vực, chiếm lĩnh, bản lĩnh, lĩnh lương)",
      why="cả hai âm có nguồn (lãnh: hvpinyin+Unihan; lĩnh: Thiều Chửu+Wiktionary); chọn theo từ Việt rồi theo nghĩa"),
    R("安", "an", w={"安静": "yên"}, n="安=an; 安静 theo từ Việt 'yên tĩnh' (yên có trong Thiều Chửu)"),
    R("松", "tông", w={"松树": "tùng"}, n="松: lỏng (鬆)=tông; cây thông=tùng"),
    R("并", "tịnh", w={k: "tính" for k in ["合并", "一并", "并购", "并发症"]},
      n="并: 並 (và, cùng, song song)=tịnh; 併 (gộp)=tính (thôn tính); 并发症=併發症"),
    R("要", None, s={"yao4": "yếu", "yao1": "yêu"}, n="要: yào=yếu, yāo=yêu"),
    R("着", "trước", n="着 (著 zhuó/zháo/zhe)=trước (chấp trước)"),
    R("综", "tổng", w={"错综复杂": "tông"}, n="综: 综合/综艺 theo từ Việt 'tổng hợp'; 错综 (đan xen) = tông (Thiều Chửu)"),
    R("找", "trảo", n="找=trảo (hvpinyin+Thiều Chửu)"),
    R("喝", "hát", cat="N", n="喝=hát (Thiều Chửu: quát; uống, như hát tửu 喝酒); 'húp/hét' không phải âm Hán Việt"),
    # ---- các nhóm trong char_consistency.md: chọn theo pinyin / nghĩa / từ Việt ----
    R("行", None, s={"xing2": "hành", "hang2": "hàng"}, w={"品行": "hạnh"}, n="行: xíng=hành, háng=hàng; 品行 theo từ Việt 'phẩm hạnh'"),
    R("面", "diện", w={k: "miến" for k in ["面包", "面条儿", "方便面", "面粉"]}, n="面: mặt=diện; bột mì (麵)=miến"),
    R("重", None, s={"zhong4": "trọng", "chong2": "trùng"}, n="重: zhòng=trọng, chóng=trùng"),
    R("分", None, s={"fen1": "phân", "fen4": "phận", "fen5": "phận"}, w={**{k: "phần" for k in ["成分", "水分", "知识分子"]}, "分量": "phân"},
      n="分: fēn=phân, fèn=phận; thành phần, thủy phần, phần tử, phân lượng theo từ Việt"),
    R("好", None, s={"hao3": "hảo", "hao4": "hiếu"}, n="好: hǎo=hảo, hào=hiếu"),
    R("中", None, s={"zhong1": "trung", "zhong4": "trúng"}, n="中: zhōng=trung, zhòng=trúng"),
    R("相", None, s={"xiang1": "tương", "xiang4": "tướng"}, n="相: xiāng=tương, xiàng=tướng"),
    R("合", "hợp", w={"回合": "hiệp"}, n="合=hợp; 回合 'hiệp' (hiệp đấu) theo tiếng Việt"),
    R("过", "quá", w={k: "qua" for k in ["过", "经过", "通过", "穿过", "透过", "放过", "越过"]},
      n="过: mặc định quá (quá khứ, quá trình); qua trong kinh qua, thông qua, xuyên qua và nghĩa 'đi xuyên qua'"),
    R("会", None, s={"hui4": "hội", "kuai4": "cối"}, n="会: huì=hội, kuài=cối"),
    R("主", "chủ", w={"公主": "chúa", "主宰": "chúa"}, n="主=chủ; công chúa, chúa tể theo từ Việt"),
    R("长", None, s={"chang2": "trường", "zhang3": "trưởng"}, n="长: cháng=trường, zhǎng=trưởng"),
    R("本", "bản", w={"本分": "bổn"}, n="本=bản; 本分 theo từ Việt 'bổn phận'"),
    R("为", None, s={"wei2": "vi", "wei4": "vị"}, n="为: wéi=vi, wèi=vị"),
    R("难", None, s={"nan2": "nan", "nan5": "nan", "nan4": "nạn"}, n="难: nán=nan, nàn=nạn"),
    R("正", None, s={"zheng4": "chính", "zheng1": "chinh"}, n="正: zhèng=chính, zhēng (正月)=chinh"),
    R("处", None, s={"chu4": "xứ", "chu5": "xứ", "chu3": "xử"}, n="处: chù=xứ, chǔ=xử"),
    R("转", "chuyển", n="转=chuyển (chuyển động, vận chuyển)"),
    R("数", None, s={"shu4": "số", "shu5": "số", "shu3": "sổ"}, n="数: shù=số, shǔ (đếm)=sổ (Thiều Chửu)"),
    R("强", None, s={"qiang2": "cường", "jiang4": "cường", "qiang3": "cưỡng"}, w={k: "cưỡng" for k in ["强制", "强加", "强占", "强行"]},
      n="强: qiáng=cường, qiǎng=cưỡng; cưỡng chế/cưỡng chiếm và nghĩa 'ép buộc' = cưỡng"),
    R("传", None, s={"chuan2": "truyền", "zhuan4": "truyện"}, n="传: chuán=truyền, zhuàn=truyện"),
    R("应", None, s={"ying1": "ưng", "ying4": "ứng", "ying5": "ứng"}, n="应: yīng=ưng, yìng=ứng"),
    R("空", None, s={"kong1": "không", "kong4": "khống"}, n="空: kōng=không, kòng=khống"),
    R("间", None, s={"jian1": "gian", "jian4": "gián"}, n="间: jiān=gian, jiàn=gián (gián tiếp, gián đoạn)"),
    R("干", None, s={"gan1": "can", "gan4": "cán"}, n="干: gān=can, gàn=cán"),
    R("和", "hòa", w={"附和": "họa"}, n="和=hòa; 附和 'phụ họa'"),
    R("思", "tư", w={k: "tứ" for k in ["意思", "不好意思", "有意思", "没意思", "构思"]}, n="思=tư; ý tứ, cấu tứ = tứ"),
    R("乐", None, s={"le4": "lạc", "yue4": "nhạc"}, n="乐: lè=lạc, yuè=nhạc"),
    R("复", "phục", w={**{k: "phức" for k in ["复印", "复杂", "重复", "错综复杂"]}, "答复": "phúc"},
      n="复: 復 (lại, trở lại)=phục; 複 (kép, phức tạp)=phức; 覆 (đáp phúc)=phúc", why="theo phồn thể; 复合 trong câu nghĩa 'quay lại với nhau' (復合) nên giữ phục"),
    R("计", "kế", w={"统计": "kê"}, n="计=kế; 统计 'thống kê'"),
    R("从", "tòng", w={"从容": "thung", "从容不迫": "thung", "服从": "tùng"}, n="从=tòng; thung dung, phục tùng theo từ Việt"),
    R("假", None, s={"jia3": "giả", "jia4": "giá"}, n="假: jiǎ=giả, jià (nghỉ)=giá"),
    R("去", "khứ", w={"除去": "khử", "去除": "khử"}, n="去=khứ; nghĩa 'loại bỏ' = khử (trừ khử, khử độc)"),
    R("断", "đoạn", w={k: "đoán" for k in ["判断", "诊断", "当机立断", "推断", "断定", "断然", "果断"]}, n="断: đứt=đoạn; phán đoán, chẩn đoán, quả đoán = đoán"),
    R("称", None, s={"cheng1": "xưng", "chen4": "xứng"}, n="称: chēng=xưng, chèn=xứng"),
    R("觉", None, s={"jue2": "giác", "jiao4": "giáo"}, n="觉: jué=giác, jiào=giáo"),
    R("首", "thủ", w={"自首": "thú"}, n="首=thủ; 自首 'tự thú'"),
    R("折", "chiết", w={k: "triệp" for k in ["折", "存折"]}, n="折: bẻ, gãy=chiết; gấp (摺)=triệp", why="折叠 (gấp) đáng là triệp nhưng cands của mục chỉ có chiết → giữ chiết"),
    R("使", "sử", w={k: "sứ" for k in ["使馆", "大使", "使命", "使者", "天使"]}, n="使: sai khiến=sử; sứ giả=sứ"),
    R("兴", None, s={"xing1": "hưng", "xing4": "hứng"}, n="兴: xīng=hưng, xìng=hứng"),
    R("倒", "đảo", cat="H", n="倒=đảo (Thiều Chửu; 'đáo' chỉ có ở hvpinyin)"),
    R("创", None, s={"chuang4": "sáng", "chuang1": "sang"}, n="创: chuàng=sáng, chuāng (vết thương)=sang"),
    R("少", None, s={"shao3": "thiểu", "shao4": "thiếu"}, w={"缺少": "thiếu"}, n="少: shǎo=thiểu, shào=thiếu; 缺少 theo từ Việt 'khuyết thiếu'"),
    R("盛", None, s={"sheng4": "thịnh", "cheng2": "thình"}, n="盛: shèng=thịnh, chéng=thình"),
    R("依", "y", w={"依赖": "ỷ"}, n="依=y; 依赖 'ỷ lại'"),
    R("营", "doanh", w={"营养": "dinh"}, n="营=doanh; 营养 'dinh dưỡng'"),
    R("藏", None, s={"cang2": "tàng", "zang4": "tạng"}, n="藏: cáng=tàng, zàng=tạng"),
    R("住", "trú", w={"禁不住": "trụ"}, n="住=trú; bổ ngữ 'giữ vững' trong 禁不住 = trụ"),
    R("劳", "lao", w={"慰劳": "lạo"}, n="劳=lao; 慰劳 'úy lạo'"),
    R("恶", None, s={"e4": "ác", "e3": "ác", "wu4": "ố"}, n="恶: è=ác, wù=ố"),
    R("迫", "bách", w={"迫切": "bức", "压迫": "bức"}, n="迫=bách; bức thiết, áp bức theo từ Việt"),
    R("占", None, s={"zhan4": "chiếm", "zhan1": "chiêm"}, n="占: zhàn=chiếm, zhān=chiêm"),
    R("吃", "cật", n="吃=cật (Thiều Chửu ghi cật cho 吃, 'cũng như chữ khiết 喫')"),
    R("围", "vi", cat="N", n="围=vi (phạm vi, chu vi); 'vây' là âm Việt hóa"),
    R("幸", "hạnh", w={k: "hãnh" for k in ["侥幸", "幸免", "幸存"]}, n="幸=hạnh; nghĩa 'may mà thoát' = hãnh"),
    R("易", "dị", w={"交易": "dịch", "贸易": "dịch"}, n="易: dễ=dị; trao đổi=dịch"),
    R("背", "bối", w={"背叛": "bội", "违背": "bội"}, n="背: lưng=bối; làm trái=bội"),
    R("鲜", None, s={"xian1": "tiên", "xian3": "tiển"}, n="鲜: xiān=tiên, xiǎn=tiển"),
    R("只", None, s={"zhi3": "chỉ", "zhi1": "chích"}, n="只: zhǐ=chỉ, zhī=chích"),
    R("散", "tán", w={"散步": "tản", "散文": "tản"}, n="散=tán; tản bộ, tản văn theo từ Việt"),
    R("种", None, s={"zhong3": "chủng", "zhong4": "chúng"}, n="种: zhǒng=chủng, zhòng (trồng)=chúng"),
    R("促", "xúc", cat="N", n="促=xúc (Thiều Chửu); 'thúc' là âm Việt hóa"),
    R("启", "khải", cat="H", n="启=khải (Thiều Chửu); 'khởi' là âm của 起 (từ Việt 'khởi động' viết 起動)"),
    R("将", "tương", w={"将军": "tướng", "麻将": "tướng"}, n="将=tương; tướng quân, mạt chược = tướng"),
    R("征", "trưng", w={"出征": "chinh", "征服": "chinh", "长征": "chinh"}, n="征: trưng (đặc trưng, trưng cầu); chinh (chinh phục, trường chinh)"),
    R("扫", "tảo", cat="H", n="扫=tảo (Thiều Chửu; 'táo' chỉ có ở hvpinyin)"),
    R("更", None, s={"geng1": "canh", "geng4": "cánh"}, w={"自力更生": "cánh"}, n="更: gēng=canh, gèng=cánh; tự lực cánh sinh"),
    R("汇", "hối", w={"词汇": "vựng"}, n="汇: 匯=hối; 彙 (từ vựng)=vựng"),
    R("症", None, s={"zheng4": "chứng", "zheng1": "trưng"}, n="症: zhèng=chứng, zhēng=trưng"),
    R("降", None, s={"jiang4": "giáng", "xiang2": "hàng"}, n="降: jiàng=giáng, xiáng=hàng"),
    R("弹", None, s={"tan2": "đàn", "tan5": "đàn", "dan4": "đạn"}, n="弹: tán=đàn, dàn=đạn"),
    R("监", "giám", w={"监狱": "giam"}, n="监=giám; nhà giam (监狱)=giam (Thiều Chửu)"),
    R("与", None, s={"yu3": "dữ", "yu4": "dự"}, n="与: yǔ=dữ, yù=dự"),
    R("司", "ti", w={"司令": "tư", "司法": "tư", "司空见惯": "tư"}, n="司=ti (công ty); tư lệnh, tư pháp theo từ Việt"),
    R("埋", "mai", cat="H", n="埋=mai (Thiều Chửu ghi cả pinyin mán; 'man' chỉ có ở hvpinyin)"),
    R("幻", "ảo", n="幻=ảo (ảo tưởng, ảo giác, ảo ảnh, hư ảo, biến ảo; Thiều Chửu: ta quen đọc là ảo)"),
    R("斗", None, s={"dou4": "đấu", "dou3": "đẩu"}, n="斗: dòu=đấu, dǒu=đẩu"),
    R("朝", None, s={"zhao1": "triêu", "chao2": "triều"}, n="朝: zhāo=triêu, cháo=triều"),
    R("潮", "triều", w={k: "trào" for k in ["潮流", "高潮", "新潮", "热潮"]}, n="潮: thủy triều, ẩm=triều; làn sóng, xu hướng=trào (trào lưu, cao trào)"),
    R("禁", None, s={"jin4": "cấm", "jin1": "câm"}, w={"情不自禁": "cấm"}, n="禁: jìn=cấm, jīn (chịu được)=câm; 情不自禁 theo 'tình bất tự cấm'"),
    R("累", None, s={"lei3": "lũy", "lei4": "lụy", "lei2": "luy"}, w={"拖累": "lụy"}, n="累: lěi=lũy (tích lũy), lèi=lụy, léi=luy; 拖累 nghĩa liên lụy"),
    R("纵", "túng", w={"纵横": "tung", "纵深": "tung"}, n="纵: buông=túng; dọc=tung"),
    R("丑", "xú", w={"小丑": "sửu"}, n="丑: 醜 (xấu)=xú; vai hề (丑)=sửu"),
    R("丝", "ti", cat="N", n="丝=ti (Thiều Chửu); 'tơ' là âm Việt hóa"),
    R("仿", "phỏng", w={"仿佛": "phảng"}, n="仿=phỏng; 仿佛 'phảng phất'"),
    R("挑", None, s={"tiao1": "thiêu", "tiao3": "khiêu"}, n="挑: tiāo (gánh, kén chọn)=thiêu; tiǎo (khêu, khiêu khích)=khiêu (Thiều Chửu)"),
    R("武", "vũ", w={"武术": "võ", "武侠": "võ"}, n="武: vũ khí, vũ lực; võ thuật, võ hiệp theo từ Việt"),
    R("舍", None, s={"she3": "xả", "she4": "xá"}, n="舍: shě=xả, shè=xá"),
    R("著", "trứ", w={"著作": "trước"}, n="著=trứ; 著作 'trước tác'"),
    R("咽", None, s={"yan1": "yết", "yan4": "yến", "ye4": "ế"}, n="咽: yān=yết, yàn=yến, yè=ế"),
    R("漂", None, s={"piao1": "phiêu", "piao4": "phiếu"}, n="漂: piāo=phiêu, piào=phiếu"),
    R("炸", "tạc", cat="H", n="炸=tạc (Thiều Chửu: nổ; đồ ăn nấu dầu, tạc nhục 炸肉)"),
    R("箱", "tương", cat="N", n="箱=tương (Thiều Chửu); 'rương' không phải âm Hán Việt"),
    R("郁", "uất", w={"浓郁": "úc"}, n="郁: 鬱 (u uất)=uất; thơm nồng (郁)=úc"),
    R("割", "cát", cat="N", n="割=cát (Thiều Chửu); 'cắt' là âm Việt hóa"),
    R("姐", "tỷ", w={"小姐": "thư"}, n="姐=tỷ (tỷ muội); 小姐 'tiểu thư'"),
    R("慰", "úy", w={"安慰": "ủy"}, n="慰=úy (úy lạo, úy vấn); 安慰 lấy ủy (gần 'an ủi')"),
    R("晃", "hoảng", cat="H", n="晃=hoảng (Thiều Chửu; 'hoàng' chỉ có ở hvpinyin)"),
    R("桥", "kiều", cat="N", n="桥=kiều (Thiều Chửu); 'cầu' không phải âm Hán Việt"),
    R("笨", "bổn", cat="N", n="笨=bổn (Thiều Chửu); 'đần' không phải âm Hán Việt"),
    R("笼", "lung", cat="N", n="笼=lung (Thiều Chửu); 'lồng' là âm Việt hóa"),
    R("缝", None, s={"feng2": "phùng", "feng5": "phùng", "feng4": "phúng"}, n="缝: féng (khâu)=phùng, fèng (khe)=phúng"),
    R("钉", "đinh", cat="H", n="钉=đinh (Thiều Chửu; 'đính' chỉ có ở hvpinyin)"),
    R("钻", None, s={"zuan1": "toàn", "zuan4": "toản"}, n="钻: zuān (dùi, đục)=toàn; zuàn (mũi khoan, kim cương)=toản (Thiều Chửu)"),
    R("铺", None, s={"pu1": "phô", "pu4": "phố"}, n="铺: pū=phô, pù=phố"),
    R("几", None, s={"ji3": "kỷ", "ji1": "cơ"}, n="几: jǐ=kỷ, jī=cơ"),
    R("勾", "câu", w={"勾结": "cấu"}, n="勾=câu; 勾结 theo từ Việt 'cấu kết'"),
    R("哭", "khốc", cat="N", n="哭=khốc (Thiều Chửu); 'khóc' là âm Việt hóa"),
    R("喷", "phún", cat="N", n="喷=phún (Thiều Chửu); 'phun' không phải âm Hán Việt"),
    R("堆", "đôi", cat="H", n="堆=đôi (Thiều Chửu; 'đồi' chỉ có ở hvpinyin)"),
    R("戴", "đái", cat="N", n="戴=đái (Thiều Chửu: đội; ái đái); 'đội' là âm Việt hóa"),
    R("炒", "sao", cat="N", n="炒=sao (Thiều Chửu); 'xào' là âm Việt hóa"),
    R("脏", None, s={"zang1": "tảng", "zang4": "tạng"}, n="脏: zāng (bẩn, 髒)=tảng; zàng (nội tạng, 臟)=tạng"),
    R("仓", "thương", w={"仓促": "thảng"}, n="仓=thương; 仓促 'thảng thốt'"),
    R("仔", None, s={"zi3": "tử", "zai3": "tể"}, n="仔: zǐ=tử, zǎi=tể"),
    R("佛", None, s={"fu2": "phất", "fo2": "phật"}, n="佛: fú=phất, fó=phật"),
    R("刹", "sát", cat="H", n="刹=sát (Thiều Chửu; 'sa' chỉ có ở hvpinyin)"),
    R("卜", None, s={"bu3": "bốc", "bo5": "bặc"}, n="卜: bǔ=bốc, bo (萝卜)=bặc"),
    R("哨", "sáo", n="哨=sáo (Thiều Chửu: sáo tử 哨子 cái còi)"),
    R("帖", "thiếp", cat="N", n="帖=thiếp (Thiều Chửu); 'thiệp' là âm Việt hóa"),
    R("撒", None, s={"sa3": "tản", "sa1": "tát"}, n="撒: sǎ=tản, sā=tát"),
    R("歪", "oa", n="歪=oa (Thiều Chửu: ta quen đọc là oa)"),
    R("滴", "tích", n="滴=tích (Thiều Chửu âm chính; thủy tích thạch xuyên)"),
    R("煎", "tiên", cat="N", n="煎=tiên (Thiều Chửu); 'chiên' là âm Việt hóa"),
    # ---- âm Nôm / Việt hóa khác (am_khong_thieuchuu_sau_soan.tsv) ----
    R("油", "du", cat="N", n="油=du (Thiều Chửu); 'dầu' là âm Việt hóa"),
    R("饼", "bính", cat="N", n="饼=bính (Thiều Chửu); 'bánh' là âm Việt hóa"),
    R("桶", "dũng", cat="N", n="桶=dũng (Thiều Chửu); 'thùng' là âm Việt hóa"),
    R("炉", "lô", cat="N", n="炉=lô (Thiều Chửu); 'lò' là âm Việt hóa"),
    R("框", "khuông", cat="N", n="框=khuông (Thiều Chửu); 'khung' không phải âm Hán Việt"),
    R("粪", "phẩn", cat="N", n="粪=phẩn (Thiều Chửu); 'phân' không phải âm Hán Việt"),
    R("爬", "ba", cat="N", n="爬=ba (Thiều Chửu); 'bò' không phải âm Hán Việt"),
    R("茄", "gia", cat="N", n="茄=gia (Thiều Chửu); 'cà' không phải âm Hán Việt"),
    R("霉", "môi", cat="N", n="霉=môi (Thiều Chửu); 'mốc' không phải âm Hán Việt"),
    R("嚏", "đế", cat="N", n="嚏=đế (Thiều Chửu: hắt hơi); 'xì' không phải âm Hán Việt"),
    R("椰", "gia", cat="N", n="椰=gia (Thiều Chửu); 'dừa' không phải âm Hán Việt"),
    R("爹", "đa", cat="N", n="爹=đa (Thiều Chửu: cha); 'tía' là từ Nam Bộ"),
    R("蘸", "trám", cat="N", n="蘸=trám (Thiều Chửu: chấm, thấm nước); 'chấm' không phải âm Hán Việt"),
    R("譬", "thí", cat="N", n="譬=thí (thí dụ); 'ví' là âm Việt hóa"),
    R("饵", "nhị", cat="N", n="饵=nhị (Thiều Chửu); 'nhử' không phải âm Hán Việt"),
    R("赎", "thục", cat="N", n="赎=thục (Thiều Chửu); 'chuộc' là âm Việt hóa"),
    R("曾", "tằng", cat="N", n="曾=tằng (Thiều Chửu); 'từng' là âm Việt hóa"),
    R("冻", "đống", cat="N", n="冻=đống (Thiều Chửu: chất lỏng đông lại tục gọi là đống)"),
    R("歹", "đãi", cat="N", n="歹=đãi (Thiều Chửu: tục đọc là đãi; tồi, xấu)"),
    R("咱", "gia", cat="N", n="咱=gia (Thiều Chửu: cha/gia; chọn gia để khỏi lẫn với 'cha'); 'ta' là đại từ thuần Việt"),
    R("漱", "sấu", cat="N", n="漱=sấu (Thiều Chửu: súc miệng); 'súc' không phải âm Hán Việt"),
    R("橙", "chanh", cat="H", n="橙=chanh (Thiều Chửu)"),
    R("讶", "nhạ", cat="H", n="讶=nhạ (Thiều Chửu); từ Việt 'kinh ngạc' viết 驚愕"),
    R("闸", "áp", n="闸 (閘)=áp (Thiều Chửu: thủy áp 水閘 đập nước; tục đọc sạp)"),
    R("掰", "?", cat="N", n="掰: nguồn chỉ có âm Nôm 'bẻ' (hvpinyin), không có âm Hán Việt có nguồn"),
    # ---- âm chỉ có ở hvpinyin, không có từ Việt chứng thực -> Thiều Chửu ----
    R("撞", "chàng", cat="H", n="撞=chàng (Thiều Chửu)"),
    R("傻", "sọa", cat="H", n="傻=sọa (Thiều Chửu)"),
    R("挣", "tránh", cat="H", n="挣=tránh (Thiều Chửu: 掙 tránh thoát)"),
    R("膀", "bàng", cat="H", n="膀=bàng (Thiều Chửu: kiên bàng 肩膀, bàng quang)"),
    R("叨", "thao", cat="H", n="叨=thao (Thiều Chửu)"),
    R("癌", "nham", cat="H", n="癌=nham (Thiều Chửu: vị nham 胃癌)"),
    R("吗", "mạ", cat="H", n="吗=mạ (Thiều Chửu 嗎: tục dùng làm tiếng giúp lời)"),
    R("姥", "mỗ", cat="H", n="姥=mỗ (Thiều Chửu: mỗ/mụ)"),
    R("怂", "túng", cat="H", n="怂=túng (Thiều Chửu: túng dũng 慫慂)"),
    R("惰", "nọa", cat="H", n="惰=nọa (Thiều Chửu: nọa tính 惰性)"),
    R("盹", "truân", cat="H", n="盹=truân (Thiều Chửu: đả truân 打盹)"),
    R("捶", "chúy", cat="H", n="捶=chúy (Thiều Chửu)"),
    R("桩", "thung", cat="H", n="桩=thung (Thiều Chửu 樁)"),
    R("煲", "bảo", cat="H", n="煲=bảo (Thiều Chửu: nấu lửa riu riu)"),
    R("瞄", "miểu", cat="H", n="瞄=miểu (Thiều Chửu: miểu chuẩn 瞄準)"),
    R("腼", "điến", cat="H", n="腼=điến (Thiều Chửu)"),
    R("惕", "dịch", cat="H", n="惕=dịch (Thiều Chửu)"),
    R("踹", "đoán", cat="H", n="踹=đoán (Thiều Chửu: dọi gót chân)"),
    R("阱", "tịnh", cat="H", n="阱=tịnh (Thiều Chửu: hãm tịnh 陷阱 cạm bẫy)"),
    R("靶", "bá", cat="H", n="靶=bá (Thiều Chửu: cái đích để bắn)"),
    R("椎", "truy", cat="H", n="椎=truy (Thiều Chửu)"),
    R("佑", "hữu", cat="H", n="佑=hữu (Thiều Chửu: bảo hữu 保佑)"),
]

# Âm giữ dù không có trong Thiều Chửu (chỉ ghi nhận, không đổi; kiểm tra là đang dùng thống nhất)
KEEP = [
    ("领", "lãnh", "lãnh đạo, lãnh tụ, lãnh thổ, lãnh sự"), ("单", "đơn", "đơn giản, đơn vị, cô đơn, thực đơn"),
    ("带", "đới", "nhiệt đới, ôn đới, hàn đới"), ("延", "diên", "diên trì, diên hạn (gia hạn)"),
    ("层", "tầng", "tầng lớp, giai tầng, tầng lầu"), ("份", "phần", "cổ phần, phần (suất); 'thân phận' viết 分"),
    ("分", "phần", "thành phần, phần tử"), ("扩", "khuếch", "khuếch đại, khuếch tán, khuếch trương"),
    ("顶", "đỉnh", "đỉnh, tuyệt đỉnh, đỉnh cao"), ("摆", "bài", "bài trí, bài binh bố trận"),
    ("间", "gián", "gián tiếp, gián đoạn, gián điệp"), ("浓", "nồng", "nồng độ, nồng hậu, nồng nhiệt"),
    ("潮", "trào", "trào lưu, cao trào"), ("仇", "thù", "thù hận, báo thù, cừu thù"),
    ("综", "tổng", "tổng hợp (综合)"), ("并", "tính", "thôn tính, hợp tính (併)"), ("旋", "hoàn", "khải hoàn (凯旋)"),
    ("叛", "phản", "phản nghịch, phản đồ, phản loạn"), ("峡", "hiệp", "Tam Hiệp (三峽)"), ("萎", "ủy", "ủy mị (萎靡)"),
    ("饺", "cảo", "sủi cảo, há cảo"), ("帅", "soái", "nguyên soái, thống soái"), ("玫", "mai", "mai khôi (玫瑰)"),
    ("璃", "lê", "pha lê (玻璃)"), ("姆", "mẫu", "bảo mẫu (保姆)"), ("迫", "bức", "bức thiết, áp bức"),
    ("勾", "cấu", "cấu kết"), ("去", "khử", "trừ khử, khử độc, khử trùng"), ("胧", "lung", "mông lung (朦朧)"),
    ("礁", "tiêu", "ám tiêu (đá ngầm)"), ("缅", "miến", "Miến Điện (緬甸)"), ("侄", "điệt", "Thiều Chửu: 侄 mượn làm 姪 điệt"),
    ("姐", "tỷ", "tỷ muội, tỷ tỷ"), ("什", "thậm", "什么 = 甚麼 (thậm)"), ("卡", "ca", "phiên âm kǎ (card, calorie)"),
    ("咖", "ca", "phiên âm 咖啡"), ("呵", "ha", "hē: phiên thiết 虎何切 → ha; Thiều Chửu chỉ ghi âm 'a' (tiếng đệm)"),
    ("哈", "ha", "thán từ tượng thanh"), ("橱", "trù", "櫥 = tủ (廚 trù); mục Thiều Chửu 'thụ' là nghĩa khác (như 樹)"),
    ("吭", "khang", "kēng: Thiều Chửu chỉ có hàng/hạng (háng = cổ họng)"),
]

# Sửa các trường văn bản phụ thuộc trực tiếp vào âm (khóa: hanzi của mục). "char_note+" = nối thêm vào char_note.
GN = "'{w}' trong tiếng Việt có gốc từ chữ này"
OVERRIDES = {
    "幻想": {"tu_viet": "ảo tưởng", "khac_biet": ""},
    "推": {"pt_kieu": "goi_nho", "pt_noi_dung": "như thôi xao (推敲, cân nhắc câu chữ); 'suy' trong suy luận, suy cử cũng là chữ này", "khac_biet": ""},
    "冻": {"loai": "khong_giup", "pt_kieu": "goi_nho", "pt_noi_dung": "gần 'đông' trong đông lạnh, đông đá"},
    "量": {"pt_noi_dung": "gần 'lường' trong đo lường; danh từ (liàng) đọc lượng: trọng lượng"},
    "奖": {"pt_noi_dung": "như tưởng thưởng, tưởng lệ; 'thưởng' trong giải thưởng là chữ 賞", "khac_biet": ""},
    "奖励": {"pt_noi_dung": "奖 tưởng (khen thưởng) + 励 lệ (gắng sức, khích lệ) → thưởng để khích lệ (tưởng lệ)"},
    "中奖": {"char_note+": "từ Việt 'trúng thưởng' dùng chữ 賞 thưởng"},
    "领取": {"pt_noi_dung": "领 lĩnh (nhận, như lĩnh lương) + 取 thủ (lấy) → nhận lấy"},
    "申领": {"pt_noi_dung": "申 thân (xin) + 领 lĩnh (nhận, như lĩnh lương)"},
    "并发症": {"pt_noi_dung": "并 tính (gộp, kèm theo) + 发 phát (xảy ra) + 症 chứng (bệnh) → bệnh phát sinh kèm theo"},
    "哨": {"pt_kieu": "goi_nho", "pt_noi_dung": "哨子 sáo tử = cái còi (Thiều Chửu); đồn gác 'tiền tiêu' cũng là chữ này"},
    "喝彩": {"pt_noi_dung": "喝 hát (hô lớn) + 彩 thái (màu sắc, tiếng khen) → hô khen"},
    "喷": {"pt_noi_dung": "như (đá) phún xuất; gần 'phun' (phun nước) trong tiếng Việt"},
    "钉": {"pt_noi_dung": "như cái đinh, đóng đinh"},
    "妈妈": {"pt_noi_dung": GN.format(w="má") + " (má = mẹ)"},
    "油": {"pt_kieu": "goi_nho", "pt_noi_dung": GN.format(w="dầu")},
    "饼": {"pt_kieu": "goi_nho", "pt_noi_dung": GN.format(w="bánh")},
    "桶": {"pt_kieu": "goi_nho", "pt_noi_dung": GN.format(w="thùng")},
    "哭": {"pt_kieu": "goi_nho", "pt_noi_dung": GN.format(w="khóc")},
    "割": {"pt_kieu": "goi_nho", "pt_noi_dung": GN.format(w="cắt")},
    "曾": {"pt_kieu": "goi_nho", "pt_noi_dung": GN.format(w="từng")},
    "炒": {"pt_kieu": "goi_nho", "pt_noi_dung": GN.format(w="xào")},
    "煎": {"pt_kieu": "goi_nho", "pt_noi_dung": GN.format(w="chiên")},
    "丝": {"pt_kieu": "goi_nho", "pt_noi_dung": GN.format(w="tơ")},
    "戴": {"pt_kieu": "goi_nho", "pt_noi_dung": GN.format(w="đội") + " (đội mũ)"},
    # mục needs_review chỉ vì chọn âm, không đổi hanviet: ghi quyết định
    "师傅": {"char_note+": "R1: 傅=phó (Thiều Chửu: sư phó 師傅); 'sư phụ' trong tiếng Việt viết 師父"},
    "划": {"char_note+": "R1: 划 nghĩa quẹt, vạch = 劃 hoạch; 划 chèo, 划算/划得来 = hoa"},
    "寻找": {"char_note+": "R1: 找=trảo (hvpinyin + Thiều Chửu)"},
    "推荐": {"char_note+": "R1: 推 nghĩa tiến cử = suy (suy cử)"},
    "资源": {"char_note+": "R1: giữ TƯ theo nguồn; từ Việt đọc 'tài nguyên' (âm tài không có trong nguồn)"},
    "身份": {"char_note+": "R1: giữ PHẦN theo nguồn; từ Việt đọc 'thân phận' (âm phận của 份 không có trong nguồn)"},
    "崭新": {"char_note+": "R1: 崭=tiệm (Thiều Chửu: tiệm tân 嶄新 mới tinh)"},
    "扮演": {"char_note+": "R1: 扮=ban (Thiều Chửu: đả ban 打扮)"},
    "一并": {"char_note+": "R1: 一并 = 一併 → tính"},
    "划得来": {"char_note+": "R1: 划 huá=hoa (nguồn chỉ có hoa)"},
    "划算": {"char_note+": "R1: 划 huá=hoa (nguồn chỉ có hoa)"},
    "周旋": {"char_note+": "R1: 旋=toàn (Thiều Chửu: quay, xoáy)"},
    "旋律": {"char_note+": "R1: 旋=toàn (Thiều Chửu: quay, xoáy)"},
    "旋涡": {"char_note+": "R1: 旋=toàn (Thiều Chửu: toàn oa 旋渦 nước xoáy)"},
    "沉着": {"char_note+": "R1: 着 (著 zhuó)=trước"},
    "沮丧": {"char_note+": "R1: 沮 jǔ=trở (Thiều Chửu: bại hoại, tan nát)"},
    "错综复杂": {"char_note+": "R1: 综 (đan xen)=tông (Thiều Chửu)"},
    "拴": {"char_note+": "R1: 拴=thuyên; Thiều Chửu nghĩa 2: buộc (thuyên mã 拴馬 buộc ngựa) — khớp nghĩa câu, tc_char chỉ cắt nghĩa 1"},
}
# Mục needs_review mà lý do chỉ là chọn âm, đã quyết: hanzi -> lý do mới ("" = chuyển draft)
RESOLVE = {k: "" for k in ["喝", "吃喝玩乐", "喝彩", "师傅", "划", "寻找", "推荐", "炸", "资源", "身份", "刹车", "崭新",
                           "扮演", "一并", "划得来", "划算", "周旋", "哨", "好歹", "旋律", "旋涡", "歹徒", "沉着", "沮丧",
                           "错综复杂", "闸", "拴"]}
RESOLVE["堆砌"] = "nghĩa từ cần xác nhận (âm 堆 đã chốt đôi ở R1)"

# Từ Việt đọc một âm KHÔNG có trong nguồn (hạn chế của nguồn; không tự thêm âm): hanzi -> âm thiếu.
# Giữ hanviet theo nguồn; nếu char_note chưa có "từ Việt" thì ghi thêm.
GAP_NOTE = {
    "公平": "bằng", "激烈": "kịch", "资源": "tài", "资助": "tài", "身份": "phận", "身份证": "phận", "宗教": "tôn",
    "宗旨": "tôn", "慢性": "mãn", "渗透": "thẩm", "牡丹": "đơn", "知识分子": "trí", "激励": "khích", "田径": "kinh",
    "汇聚": "hội", "致命": "chí, mạng", "软弱": "nhu", "安慰": "ủi", "威风": "oai", "救命": "mạng", "革命": "mạng",
    "性命": "mạng", "模糊": "mơ", "珠宝": "báu", "无故": "cớ", "缘故": "cớ", "豆腐": "hũ", "馒头": "màn, thầu",
}


def read_rows(path):
    with open(path, encoding="utf-8", newline="") as f:
        lines = f.read().split("\n")
    h = lines[0].rstrip("\r").split("\t")
    for l in lines[1:]:
        l = l.rstrip("\r")
        if l.strip():
            yield dict(zip(h, l.split("\t")))


def load_jsonl(p):
    with open(p, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def split_top(text):
    """Tách theo ';' ở mức ngoài ngoặc ( ) [ ] " "."""
    out, buf, depth, q = [], [], 0, False
    for ch in text or "":
        if ch in "([":
            depth += 1
        elif ch in ")]":
            depth = max(0, depth - 1)
        elif ch in '"“”':
            q = not q if ch == '"' else (ch == "“")
        if ch == ";" and depth == 0 and not q:
            out.append("".join(buf)); buf = []
        else:
            buf.append(ch)
    out.append("".join(buf))
    return out


def case_like(src, new):
    if src.isupper():
        return new.upper()
    if src[:1].isupper():
        return new[:1].upper() + new[1:]
    return new


def replace_mentions(text, forms, old, new):
    """Đổi 'chữ âm_cũ' -> 'chữ âm_mới' trong văn bản (chữ giản hoặc phồn)."""
    if not text:
        return text
    pat = re.compile("(" + "|".join(map(re.escape, forms)) + r")(\s*[=:]?\s*)(" + re.escape(old) + r")(?![\wÀ-ỹ])", re.I)
    return pat.sub(lambda m: m.group(1) + m.group(2) + case_like(m.group(3), new), text)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(BASE, "06_review", "fixes_r1_doc_am.tsv"))
    ap.add_argument("--review")
    ap.add_argument("--dump-rules", action="store_true")
    a = ap.parse_args()

    if a.dump_rules:
        print("| # | Chữ | Mặc định | Theo pinyin | Ngoại lệ theo từ | Loại | Căn cứ |")
        print("|---|---|---|---|---|---|---|")
        for i, r in enumerate(RULES, 1):
            s = ", ".join(f"{k}→{v}" for k, v in r["s"].items())
            wg = collections.defaultdict(list)
            for k, v in r["w"].items():
                wg[v].append(k)
            w = "; ".join(f"{v}: {'、'.join(ks)}" for v, ks in wg.items())
            print(f"| {i} | {r['c']} | {r['d'] or '—'} | {s or '—'} | {w or '—'} | {r['cat']} | {r['why']} |")
        return

    merged = load_jsonl(os.path.join(BASE, "07_final", "merged_v1.jsonl"))
    ihv = {x["note_key"]: x for x in load_jsonl(os.path.join(BASE, "02_chars", "item_hv.jsonl"))}
    raw = {}
    for p in sorted(glob.glob(os.path.join(BASE, "04_draft", "out", "*.tsv"))):
        for r in read_rows(p):
            raw[r["note_key"]] = r
    for p in sorted(glob.glob(os.path.join(BASE, "06_review", "fixes_*.tsv"))):
        if os.path.basename(p).startswith("fixes_r1"):
            continue
        for r in read_rows(p):
            raw[r["note_key"]] = r

    rule_of = {r["c"]: r for r in RULES}
    stats = collections.Counter()
    per_rule = collections.defaultdict(set)
    skipped = []
    out_rows = []
    review = []
    for m in merged:
        k = m["note_key"]
        iv = ihv[k]
        cur = {c: raw[k].get(c, "") for c in COLS}
        cur["hanviet"] = m["hanviet"]
        new = dict(cur)
        toks = m["hanviet"].split()
        changes = []   # (char, old, new, note)
        for i, ic in enumerate(iv["chars"]):
            c = ic["char"]
            r = rule_of.get(c)
            if not r:
                continue
            tgt = r["w"].get(m["hanzi"]) or r["s"].get(ic.get("syl")) or r["d"]
            if not tgt:
                continue
            old = toks[i]
            if tgt == "?":
                if old != "?":
                    changes.append((c, old, "?", r["n"]))
                    toks[i] = "?"
                continue
            if old != "?" and reading_key(old) == reading_key(tgt):
                continue
            cands = {reading_key(cd["reading"]) for cd in ic.get("cands", [])}
            if reading_key(tgt) not in cands:
                skipped.append((k, m["hanzi"], c, old, tgt))
                continue
            toks[i] = display(tgt).upper()
            changes.append((c, old, tgt, r["n"]))
        if changes:
            new["hanviet"] = " ".join(toks)
            forms_of = {}
            for i, ic in enumerate(iv["chars"]):
                forms_of.setdefault(ic["char"], {ic["char"], *(ic.get("trad") or [])})
            for c, old, tgt, note in changes:
                if tgt == "?":
                    continue
                for f in ("pt_noi_dung", "khac_biet"):
                    new[f] = replace_mentions(new[f], forms_of[c], display(old.lower()), display(tgt))
            # char_note: bỏ các đoạn cũ nói về chữ đã đổi, thêm ghi chú R1
            chg_chars = {c for c, *_ in changes}
            forms = set().union(*(forms_of[c] for c in chg_chars))
            segs = [s.strip() for s in split_top(cur["char_note"]) if s.strip()]
            olds = [display(o.lower()) for _, o, t, _ in changes if t != "?"]
            pat_old = re.compile(r"(?<![\wÀ-ỹ])(" + "|".join(map(re.escape, olds)) + r")(?![\wÀ-ỹ])", re.I) if olds else None
            keep = [s for s in segs if not any(f in s for f in forms)
                    and not (pat_old and pat_old.search(s)) and not re.search(r"\bpre\b", s)]
            r1 = []
            for c, old, tgt, note in changes:
                if note not in r1:
                    r1.append(note)
            new["char_note"] = "; ".join(["R1: " + " | ".join(r1)] + keep)
            for c, old, tgt, note in changes:
                per_rule[c].add(k)
                stats[(rule_of[c]["cat"], c, display(old.lower()), tgt)] += 1
            if any(t == "?" for _, _, t, _ in changes):
                new["status"] = "needs_review"
                rs = [r for _, _, t, r in changes if t == "?"]
                new["review_reason"] = "; ".join(x for x in [cur["review_reason"]] + rs if x)
        # overrides theo hanzi
        ov = OVERRIDES.get(m["hanzi"]) or OVERRIDES.get(k)
        if ov:
            for f, v in ov.items():
                if f == "char_note+":
                    new["char_note"] = (new["char_note"] + "; " + v) if new["char_note"] else v
                else:
                    new[f] = v or ""
        if m["hanzi"] in GAP_NOTE and "từ Việt" not in new["char_note"]:
            tv = new["tu_viet"] or ("thân phận" if m["hanzi"] == "身份证" else "")
            gn = f"R1: từ Việt đọc '{tv}' (âm {GAP_NOTE[m['hanzi']]} không có trong nguồn; giữ âm có nguồn)"
            new["char_note"] = (new["char_note"] + "; " + gn) if new["char_note"] else gn
        if m["hanzi"] in RESOLVE or k in RESOLVE:
            reason = RESOLVE.get(m["hanzi"], RESOLVE.get(k))
            if reason:
                new["status"], new["review_reason"] = "needs_review", reason
            else:
                new["status"], new["review_reason"] = "draft", ""
        if any(new[c] != cur[c] for c in COLS):
            out_rows.append(new)
            review.append((m["hanzi"], m.get("word_pinyin", ""), cur, new))

    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    with open(a.out, "w", encoding="utf-8", newline="\n") as f:
        f.write("\t".join(COLS + ["reviewer"]) + "\n")
        for r in out_rows:
            vals = [str(r[c]).replace("\t", " ").replace("\n", " ") for c in COLS]
            f.write("\t".join(vals + [REVIEWER]) + "\n")
    if a.review:
        with open(a.review, "w", encoding="utf-8", newline="\n") as f:
            for hz, wp, cur, new in review:
                diffs = [f"{c}: {cur[c]!s} => {new[c]!s}" for c in COLS if c != "note_key" and cur[c] != new[c]]
                ctx = f"loai={new['loai']} tv={new['tu_viet']} pt={new['pt_noi_dung']} kb={new['khac_biet']}"
                f.write(f"{hz}\t{wp}\t{new['note_key']}\t" + " || ".join(diffs) + "\t" + ctx + "\n")
    print(f"dòng fix: {len(out_rows)}; mục đổi âm: {len(set().union(*per_rule.values())) if per_rule else 0}")
    cat_items = collections.defaultdict(set)
    for c, ks in per_rule.items():
        cat_items[rule_of[c]["cat"]] |= ks
    print("theo loại quy tắc:", {c: len(v) for c, v in sorted(cat_items.items())})
    print("theo chữ:", ", ".join(f"{c}:{len(v)}" for c, v in sorted(per_rule.items(), key=lambda t: -len(t[1]))))
    for key, n in sorted(stats.items()):
        print("  ", key, n)
    if skipped:
        print("BỎ QUA (âm đích không có trong cands):")
        for s in skipped:
            print("  ", s)


if __name__ == "__main__":
    main()
