# COVID19
**Django+Pyecharts 搭建的新冠肺炎疫情监控面板**

### 其中用到了 Mysql “世界各国中英文对照”(zh2en) 表
```sql
create table zh2en
(
    英文 varchar(100) null,
    中文 varchar(20)  null
);

INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Afghanistan', '阿富汗');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Alaska(U.S.A)', '阿拉斯加');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Albania', '阿尔巴尼亚');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Algeria', '阿尔及利亚');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Andorra', '安道尔');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Angola', '安哥拉');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Anguilla I.', '安圭拉岛英)');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Antigua and Barbuda', '安提瓜和巴布达');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Argentina', '阿根廷');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Armenia', '亚美尼亚');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Aruba I.', '阿鲁巴岛');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Ascension', '阿森松(英)');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Australia', '澳大利亚');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Austria', '奥地利');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Azerbaijan', '阿塞拜疆');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Bahrain', '巴林');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Bangladesh', '孟加拉');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Barbados', '巴巴多斯');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Belarus', '白俄罗斯');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Belgium', '比利时');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Belize', '伯利兹');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Benin', '贝宁');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Bermuda Is.', '百慕大群岛(英)');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Bhutan', '不丹');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Bolivia', '玻利维亚');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Bosnia and Herz.', '波黑');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Botswana', '博茨瓦纳');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Brazil', '巴西');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Bulgaria', '保加利亚');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Burkina Faso', '布基纳法索');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Burundi', '布隆迪');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Cameroon', '喀麦隆');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Canada', '加拿大');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Canaries Is.', '加那利群岛');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Cape Verde', '佛得角');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Cayman Is.', '开曼群岛(英)');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Central African Rep.', '中非共和国');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Chad', '乍得');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Chile', '智利');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Christmas I.', '圣诞岛');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Cocos I.', '科科斯岛');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Colombia', '哥伦比亚');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Commonwealth of The Bahamas', '巴哈马国');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Commonwealth of dominica', '多米尼克国');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Comoro', '科摩罗');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Dem. Rep. Congo', '刚果（金）');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Cook IS.', '科克群岛(新)');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Costa Rica', '哥斯达黎加');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Croatia', '克罗地亚');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Cuba', '古巴');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Cyprus', '塞浦路斯');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Czech Rep.', '捷克');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Denmark', '丹麦');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Diego Garcia I.', '迪戈加西亚岛');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Djibouti', '吉布提');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Dominican Rep.', '多米尼加共和国');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Ecuador', '厄瓜多尔');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Egypt', '埃及');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('El Salvador', '萨尔瓦多');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Eq. Guinea', '赤道几内亚');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Eritrea', '厄立特里亚');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Estonia', '爱沙尼亚');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Ethiopia', '埃塞俄比亚');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Falkland Is.', '福克兰群岛');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Faroe Is.', '法罗群岛(丹)');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Fiji', '斐济');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Finland', '芬兰');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('France', '法国');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('French Guiana', '法属圭亚那');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('French Polynesia', '法属波里尼西亚');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Gabon', '加蓬');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Gambia', '冈比亚');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Georgia', '格鲁吉亚');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Germany', '德国');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Ghana', '加纳');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Gibraltar', '直布罗陀(英)');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Greece', '希腊');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Greenland', '格陵兰岛');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Grenada', '格林纳达');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Guadeloupe I.', '瓜德罗普岛(法)');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Guam', '关岛(美)');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Guatemala', '危地马拉');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Guinea', '几内亚');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Guinea-bissau', '几内亚比绍');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Guyana', '圭亚那');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Haiti', '海地');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Hawaii', '夏威夷');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Honduras', '洪都拉斯');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Hungary', '匈牙利');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Iceland', '冰岛');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('India', '印度');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Indonesia', '印度尼西亚');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Iran', '伊朗');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Iraq', '伊拉克');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Ireland', '爱尔兰');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Israel', '以色列');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Italy', '意大利');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Ivory Coast', '科特迪瓦');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Jamaica', '牙买加');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Japan', '日本本土');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Jordan', '约旦');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Kazakhstan', '哈萨克斯坦');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Kenya', '肯尼亚');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Kiribati', '基里巴斯');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Korea(dpr of)', '朝鲜');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Korea', '韩国');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Kuwait', '科威特');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Kyrgyzstan', '吉尔吉斯斯坦');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Latvia', '拉脱维亚');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Lebanon', '黎巴嫩');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Lesotho', '莱索托');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Liberia', '利比里亚');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Libya', '利比里亚');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Liechtenstein', '列支敦士登');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Lithuania', '立陶宛');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Luxembourg', '卢森堡');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Macedonia', '北马其顿');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Madagascar', '马达加斯加');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Malawi', '马拉维');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Malaysia', '马来西亚');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Maldive', '马尔代夫');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Mali', '马里');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Malta', '马耳他');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Mariana Is.', '马里亚纳群岛');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Marshall Is.', '马绍尔群岛');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Martinique', '马提尼克(法)');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Mauritania', '毛里塔尼亚');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Mauritius', '毛里求斯');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Mayotte I.', '马约特岛');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Mexico', '墨西哥');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Micronesia', '密克罗尼西亚(美)');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Midway I.', '中途岛(美)');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Moldova', '摩尔多瓦');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Monaco', '摩纳哥');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Mongolia', '蒙古');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Montserrat I.', '蒙特塞拉特岛(英)');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Morocco', '摩洛哥');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Mozambique', '莫桑比克');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Myanmar', '缅甸');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Namibia', '纳米比亚');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Nauru', '瑙鲁');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Nepal', '尼泊尔');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Netherlands', '荷兰');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Netherlandsantilles Is.', '荷属安的列斯群岛');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('New Caledonia Is.', '新喀里多尼亚群岛(法)');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('New Zealand', '新西兰');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Nicaragua', '尼加拉瓜');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Niger', '尼日尔');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Nigeria', '尼日利亚');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Niue I.', '纽埃岛(新)');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Norfolk I,', '诺福克岛(澳)');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Norway', '挪威');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Oman', '阿曼');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Palau', '帕劳(美)');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Panama', '巴拿马');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Papua New Guinea', '巴布亚新几内亚');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Paraguay', '巴拉圭');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Peru', '秘鲁');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Philippines', '菲律宾');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Poland', '波兰');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Portugal', '葡萄牙');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Pakistan', '巴基斯坦');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Puerto Rico', '波多黎各(美)');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Qatar', '卡塔尔');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Reunion I.', '留尼汪岛');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Romania', '罗马尼亚');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Russia', '俄罗斯');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Rwanda', '卢旺达');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Samoa,Eastern', '东萨摩亚(美)');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Samoa,Western', '西萨摩亚');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('San.Marino', '圣马力诺');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('San.Pierre And Miquelon I.', '圣皮埃尔岛及密克隆岛');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('San.Tome And Principe', '圣多美和普林西比');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Saudi Arabia', '沙特阿拉伯');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Senegal', '塞内加尔');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Seychelles', '塞舌尔');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Singapore', '新加坡');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Slovakia', '斯洛伐克');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Slovenia', '斯洛文尼亚');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Solomon Is.', '所罗门群岛');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Somalia', '索马里');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('South Africa', '南非');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Spain', '西班牙');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Sri Lanka', '斯里兰卡');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('St.Christopher and Nevis', '圣克里斯托弗和尼维斯');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('St.Helena', '圣赫勒拿');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('St.Lucia', '圣卢西亚');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('St.Vincent I.', '圣文森特岛(英)');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Sudan', '苏丹');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Suriname', '苏里南');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Swaziland', '斯威士兰');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Sweden', '瑞典');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Switzerland', '瑞士');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Syria', '叙利亚');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Tajikistan', '塔吉克斯坦');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Tanzania', '坦桑尼亚');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Thailand', '泰国');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('The United Arab Emirates', '阿拉伯联合酋长国');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Togo', '多哥');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Tokelau Is.', '托克劳群岛(新)');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Tonga', '汤加');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Trinidad and Tobago', '特立尼达和多巴哥');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Tunisia', '突尼斯');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Turkey', '土耳其');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Turkmenistan', '土库曼斯坦');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Turks and Caicos Is.', '特克斯和凯科斯群岛');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Tuvalu', '图瓦卢');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('United States', '美国');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Uganda', '乌干达');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Ukraine', '乌克兰');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('United Kingdom', '英国');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Uruguay', '乌拉圭');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Uzbekistan', '乌兹别克斯坦');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Vanuatu', '瓦努阿图');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Vatican', '梵蒂冈');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Venezuela', '委内瑞拉');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Vietnam', '越南');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Virgin Is.', '维尔京群岛(英)');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Virgin Is. and St.Croix I.', '维尔京群岛和圣罗克伊');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Wake I.', '威克岛(美)');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Wallis And Futuna Is.', '瓦里斯和富士那群岛(');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Western sahara', '西撒哈拉');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Yemen', '也门');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Yugoslavia', '南斯拉夫');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Zaire', '扎伊尔');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Zambia', '赞比亚');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Zanzibar', '韩国');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Zimbabwe', '津巴布韦');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('P.R.C.', '中华人民共和国');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('China', '中国');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Cambodia', '柬埔寨');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Lao PDR', '老挝');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Montenegro', '黑山');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Serbia', '塞尔维亚');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Congo', '刚果（布）');
INSERT INTO covid19.zh2en (英文, 中文) VALUES ('Sierra Leone', '塞拉利昂');

```