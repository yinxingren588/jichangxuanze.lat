# -*- coding: utf-8 -*-
# Category 6: 订阅与节点维护管理 (15 篇)

SUBSCRIPTION_FAQS = [
    {
        "id": "faq-106",
        "slug": "subscription-update-error-solutions",
        "title": "机场订阅更新失败报 500、404 或超时终极排错与备用短链",
        "category": "subscription",
        "categoryLabel": "订阅与节点管理",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "详细分析客户端点击刷新订阅时频繁出现 HTTP 500、404、Empty Content 报错的处理方案。",
        "symptoms": [
            "点击刷新订阅按钮，弹窗提示：Update subscription failed (status 500 / 404 / 502)",
            "原有的节点列表瞬间被清空，导致彻底无法上网",
            "订阅日志显示：response body is not a valid YAML/Base64"
        ],
        "rootCauses": [
            "机场对应的订阅分发域名遭到了国内 DNS 污染或被国家防火墙加入 SNI 阻断黑名单",
            "用户套餐已经到期或者月流量已完全耗尽，机场后台自动切断了订阅接口的鉴权",
            "机场主正在维护升级后端数据库或迁移节点服务器"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：第一步登录机场用户中心检查套餐状态",
                "detail": "使用手机或任意可用网络登录机场后台官网，确认你的会员订阅是否处于「有效 (Active)」状态，确认剩余流量是否大于 0。"
            },
            {
                "stepTitle": "步骤 2：获取机场提供的防封锁「备用订阅链接」",
                "detail": "很多靠谱机场在用户后台仪表盘提供了「备用节点链接」或支持一键生成免污染短链，复制新链接替换客户端中的旧 URL 即可立即刷新成功。"
            },
            {
                "stepTitle": "步骤 3：在客户端开启「代理状态下更新订阅」",
                "detail": "只要列表中还有一个能勉强连通的节点，先开启代理，再点击更新订阅。此时请求将由海外节点中转，直接绕过国内所有阻断。"
            }
        ],
        "faqTips": "刷新订阅前建议在客户端右键备份当前的旧配置文件，即使更新失败也不会发生节点全部消失的尴尬局面。",
        "relatedSlugs": ["shadowrocket-subscription-timeout", "all-nodes-turn-red-suddenly"]
    },
    {
        "id": "faq-107",
        "slug": "subconverter-remote-token-leak",
        "title": "为什么绝不建议用公共在线订阅转换平台？自建订阅转换与防泄露",
        "category": "subscription",
        "categoryLabel": "订阅与节点管理",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "揭秘网上免费公共 Subconverter 订阅转换平台的偷节点、盗取 Token 与流量盗刷黑产内幕。",
        "symptoms": [
            "使用网上搜到的免费在线订阅转换后，第二天发现机场流量被莫名奇妙消耗了几百 GB",
            "在异地登录记录中看到来自未知 IP 的大量节点并发连接",
            "机场后台提示账号因为异常多地并发被系统临时封禁"
        ],
        "rootCauses": [
            "部分不良公共在线订阅转换平台在后端脚本中直接把你的原版订阅链接 (包含 Token 秘钥) 私自记录在数据库中，转手挂到发卡网作为廉价节点池倒卖！"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：优先使用客户端内置的原生转换核心",
                "detail": "现代客户端（Clash Verge Rev、Mihomo Party、小火箭）均已内置原生的协议转换解析器，直接导入原始订阅即可，完全不需要借助任何第三方外部转换网站！"
            },
            {
                "stepTitle": "步骤 2：如果必须转换，推荐使用本地 Docker 离线自建",
                "detail": "在本地电脑或私人 NAS 上直接运行官方开源的 subconverter Docker 镜像，转换过程完全在局域网内完成，绝不向外暴露任何 Token。",
                "code": "docker run -d --name subconverter -p 25500:25500 tindy2013/subconverter:latest"
            },
            {
                "stepTitle": "步骤 3：怀疑泄露时立即在机场后台重置订阅链接",
                "detail": "如果曾在不明公共转换站粘贴过链接，立即进入机场后台点击「重置订阅链接」，旧 Token 即刻作废，保障账户资产安全。"
            }
        ],
        "faqTips": "把带有完整秘钥的订阅链接粘贴到公共第三方网站，相当于把家门钥匙直接挂在公开论坛上，务必养成良好安全意识。",
        "relatedSlugs": ["traffic-drain-fast-background-leaks", "how-to-spot-scam-airports"]
    },
    {
        "id": "faq-108",
        "slug": "nodes-have-ping-but-cannot-browse",
        "title": "节点测速延迟几十毫秒但网页打不开的根本原因与排查",
        "category": "subscription",
        "categoryLabel": "订阅与节点管理",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "分析为什么测速全部显示低延迟绿灯，但实际访问 Google、YouTube 却连不上的假连通现象。",
        "symptoms": [
            "在客户端点击测速，香港节点显示 35ms，日本节点显示 50ms 全部绿油油",
            "但在浏览器里输入 www.google.com 却一直加载甚至提示无法连接",
            "测速显示正常但微信外网图片都发不出去"
        ],
        "rootCauses": [
            "所谓的 35ms 只是客户端到机场「国内中继/入口服务器」的 TCP Ping 延迟，并不代表从入口机房到境外落地节点之间的全链路通畅！",
            "机场的境外落地机器被封锁或后端代理服务已经宕机，但国内入口服务器依然在正常坚挺回复 Ping 探测报文（典型的空包中继）",
            "本地 Windows 系统代理开关未真正开启，浏览器根本没有将请求发给 Clash"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：排查系统代理是否真正生效",
                "detail": "按 Win + I 打开 Windows 设置 ->「网络和 Internet」->「代理」，检查「使用代理服务器」是否已开启，地址是否指向 127.0.0.1:7890。"
            },
            {
                "stepTitle": "步骤 2：在客户端内切换真实的测速 URL",
                "detail": "将客户端的测试地址改为一个真正的端到端境外网页，例如 http://www.google.com/generate_204，这种端到端测试才能准确反映全链路是否真正通畅。"
            },
            {
                "stepTitle": "步骤 3：选用真正全节点直通的 IPLC 纯专线",
                "detail": "公网中继容易出现入口好、出口断的假冒伪劣现象；认准真正全链路监控的 IPLC 专线（如隐形人、大佬云）彻底告别假测速。"
            }
        ],
        "faqTips": "记住：低 Ping 只能说明你家到机场入口很近，不等于机场出口能够顺利连接全世界，端到端实际打开网页才是唯一真理。",
        "relatedSlugs": ["error-dial-tcp-timeout-10000ms", "all-nodes-turn-red-suddenly"]
    },
    {
        "id": "faq-109",
        "slug": "all-nodes-turn-red-suddenly",
        "title": "节点突然全部变红不可用是机场跑路还是节点维护？如何准确鉴别",
        "category": "subscription",
        "categoryLabel": "订阅与节点管理",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "手把手教你在 2 分钟内精准鉴别当前是由于遭遇大审查节点临时被拔线、还是机场跑路的四步排查法。",
        "symptoms": [
            "今天开机后发现订阅列表里原本好几十个节点全部变红，全部测速超时",
            "官方 Telegram 群组被开启了全员禁言",
            "机场官网打不开或者显示 Cloudflare 521/522 错误"
        ],
        "rootCauses": [
            "正常情况：遇到敏感时期或者上游大型机房断电事故，导致多地中继入口同时离线，通常在 2~6 小时内修复",
            "跑路情况：机场主因低价超售资金链断裂、被上游追缴服务器欠费跑路，或者群组解散官网清空"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：第一步访问机场官方 Telegram 频道（看最新公告）",
                "detail": "正规靠谱的机场在遇到故障时，都会在第一时间（5~15 分钟内）在 Telegram 官方频道发布通知，说明是机房光纤被挖断还是入口迁移，并给出预计修复时间。"
            },
            {
                "stepTitle": "步骤 2：观察官网主页是否依然存活并能登录后台",
                "detail": "如果官网依然能正常访问、工单系统可以正常提交，说明大概率只是节点服务器在做紧急容灾迁移，切勿惊慌。"
            },
            {
                "stepTitle": "步骤 3：立即启用你的第二家「备用机场」无缝办公",
                "detail": "这也是为什么永远要备用一条不同线路机场的原因，立刻切换备用节点，工作与娱乐不受丝毫耽误。"
            }
        ],
        "faqTips": "如果 Telegram 频道被注销、官网直接域名解析不存在超过 24 小时没有任何解释，基本可以确认跑路，建议及时止损。",
        "relatedSlugs": ["why-never-buy-multi-year-package", "backup-airport-strategy-redundancy"]
    },
    {
        "id": "faq-110",
        "slug": "why-never-buy-multi-year-package",
        "title": "为什么绝不建议购买一次性多年付套餐？防跑路生存法则大揭秘",
        "category": "subscription",
        "categoryLabel": "订阅与节点管理",
        "readTime": "6 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "从机场行业商业逻辑、高防专线成本与法律风险，深度揭秘为什么「月付/季付」是普通用户的最硬核护城河。",
        "symptoms": [
            "看到某些新开机场打出「三年付只要 99 元送 500G 专线」的诱人广告蠢蠢欲动",
            "买了一年付套餐，结果用到第二个月机场就关门大吉失联"
        ],
        "rootCauses": [
            "庞氏超售骗局：新开机场租借廉价月租 VPS，通过极低的多年付预收款迅速吸纳几十万现金，随后一旦服务器到期无力支付高昂的续费账单，机场主直接卷款跑路换皮重新开新站！",
            "物理专线极高成本：正规合规的 IPLC 物理专线每个 Gbps 带宽每个月的成本高达数万元，绝不可能有「三年几十块钱」还能保证高峰期稳定不卡顿的物理逻辑！"
        ],
        "solutions": [
            {
                "stepTitle": "黄金铁律 1：初次尝试任何新机场，必须且只买「月付」",
                "detail": "即使年付折扣再诱人，首次体验也必须先买一个月付套餐，在晚上 8~10 点的晚高峰真实检验其 4K 播放与丢包表现。"
            },
            {
                "stepTitle": "黄金铁律 2：即使是运营 3 年以上的老牌机场，最多只买「年付」",
                "detail": "对口碑极佳的老品牌，购买年付享受 8 折优惠是合情合理的，但坚决不要碰任何「两年付、三年付、永久传家宝」套餐！"
            }
        ],
        "faqTips": "记住：你在意的是他那点超额折扣，不良机场主盯上的却是你的全部本金！保持月付/季付，永远拥有随时用脚投票的自由。",
        "relatedSlugs": ["how-to-spot-scam-airports", "backup-airport-strategy-redundancy"]
    },
    {
        "id": "faq-111",
        "slug": "airport-vs-self-built-vps-comparison",
        "title": "机场节点与自己买海外 VPS 搭建科学上网深度横评 (谁更稳定划算？)",
        "category": "subscription",
        "categoryLabel": "订阅与节点管理",
        "readTime": "6 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "从金钱成本、抗封锁能力、晚高峰带宽、维护时间与流媒体解锁等 5 大维度，全面对比自建与专业机场的优劣。",
        "symptoms": [
            "纠结是自己买搬瓦工、Linode、Oracle 搭建，还是直接购买成熟的机场专线服务",
            "自建 VPS IP 经常被墙，换一次 IP 要花 8 美元心力交瘁"
        ],
        "rootCauses": [
            "个人自建通常只能买到普通公网直连 VPS，走公网国际出口，晚高峰受到严重丢包压制，且单个 IP 一旦被防火墙识别就是 100% 彻底报废；而专业机场拥有多入口 BGP 智能调度、内网 IPLC 物理专线与几百台落地机组成的强大容灾矩阵。"
        ],
        "solutions": [
            {
                "stepTitle": "维度 1：晚高峰速度与抗审查（机场完胜）",
                "detail": "个人买不起动辄每月几万元的商业 IPLC 专线，自建直连一到特殊时期或晚高峰就断流；专业机场走物理专线不过墙，稳如泰山。"
            },
            {
                "stepTitle": "维度 2：流媒体与 AI 解锁（机场完胜）",
                "detail": "自建机房 IP（如 DigitalOcean）100% 被 OpenAI 和 Netflix 识别阻断；机场配置了专门的原生家宽池进行动态分流解锁。"
            },
            {
                "stepTitle": "维度 3：性价比与时间成本（机场完胜）",
                "detail": "自建 VPS 最便宜也要 $5/月 (约 ¥35)，还要自己折腾代码、对付被墙；而同等价位已能购买顶级 IPLC 专线机场，省去无数折腾时间。"
            }
        ],
        "faqTips": "结论：除非有特定的海外私有独立固定 IP 或远程服务器运维需求，日常查资料、看视频、用 AI，直接选优质专线机场在各方面均呈碾压之势。",
        "relatedSlugs": ["why-never-buy-multi-year-package", "iplc-vs-iepl-technical-difference"]
    },
    {
        "id": "faq-112",
        "slug": "traffic-drain-fast-background-leaks",
        "title": "为什么机场流量消耗异常飞快？排查后台偷跑流量的元凶",
        "category": "subscription",
        "categoryLabel": "订阅与节点管理",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "明明没看几个视频，几天内 100G 流量就见了底？全面排查系统后台自动偷跑境外流量的黑手。",
        "symptoms": [
            "刚买的月付 200GB 套餐，才用了一个星期后台就提示流量只剩 10%",
            "手机或电脑即使静置未操作，客户端连接日志仍然在持续跳动几十 KB/s 的上传下载"
        ],
        "rootCauses": [
            "误开启了「全局代理 (Global)」，导致国内百度网盘下载、Steam 游戏更新、迅雷 P2P 全部走了代理",
            "网盘类软件（iCloud、OneDrive、Google Drive、Dropbox）在后台疯狂同步相册与大文件",
            "在节点列表中长时间使用了 3.0x 或 5.0x 的高倍率节点进行大文件下载"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：排查并确保处于「规则模式 (Rule)」",
                "detail": "在客户端中核实当前处于规则模式，杜绝国内大流量软件消耗境外配额。"
            },
            {
                "stepTitle": "步骤 2：检查当前连接的节点倍率",
                "detail": "注意节点名称后是否标注了「x3.0」或「x5.0」等倍率标识。如果在 3 倍率节点下看了一个 10GB 的 4K 电影，实际扣除的流量是 30GB！日常看长视频建议选用 1.0x 或 0.5x 经济节点。"
            },
            {
                "stepTitle": "步骤 3：在客户端连接面板中按「下载流量」排序排查",
                "detail": "在 Clash Verge Rev 的「连接 (Connections)」面板中，点击「下载」列头降序排列，一眼抓出是哪个进程（如 OneDrive.exe）正在疯狂消耗流量，并将其单独划为直连。"
            }
        ],
        "faqTips": "如果使用了公共在线订阅转换，也可能是 Token 泄露被他人盗刷，必要时在机场后台点击重置订阅。",
        "relatedSlugs": ["subconverter-remote-token-leak", "node-multiplier-billing-explained"]
    },
    {
        "id": "faq-113",
        "slug": "how-to-spot-scam-airports",
        "title": "如何在 3 分钟内识别虚假宣传、随时跑路的野鸡机场？",
        "category": "subscription",
        "categoryLabel": "订阅与节点管理",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "掌握科学上网老鸟的「照妖镜」法则，快速识破虚标专线与即将跑路野鸡站的四大破绽。",
        "symptoms": [
            "在某些不知名论坛或小红书看到有人疯狂刷屏推广某家极其便宜的机场",
            "界面粗制滥造，没有任何官方说明文档"
        ],
        "rootCauses": [
            "野鸡机场通常是一两个人使用免费开源面板（如 V2board、SSPanel）搭建，租用几台超售小鸡，以低价为饵圈一波钱就跑"
        ],
        "solutions": [
            {
                "stepTitle": "破绽 1：价格违背物理常识（几块钱号称无限流量 IPLC 专线）",
                "detail": "IPLC 物理专线是实打实的昂贵商业带宽，如果一家机场号称「9.9 元一个月不限流量全专线」，100% 是用廉价普通公网直连挂羊头卖狗肉的虚标货！"
            },
            {
                "stepTitle": "破绽 2：查域名的 Whois 注册时间",
                "detail": "通过 whois.chinaz.com 查询其官网域名注册时间。如果域名才刚注册不到 1 个月，必须保持高度警惕，绝不买长期套餐。"
            },
            {
                "stepTitle": "破绽 3：看 Telegram 官方社群的活跃度与氛围",
                "detail": "正规老牌机场群内有上千活跃真实用户交流技术，管理团队态度专业；野鸡机场群内往往全员禁言，或者只有几个机器人自导自演发好评。"
            }
        ],
        "faqTips": "认准经过长期监控实测、口碑积累 2~3 年以上的老牌团队（如本站实测推荐的 14 个品牌）是避开跑路的最省心方案。",
        "relatedSlugs": ["why-never-buy-multi-year-package", "all-nodes-turn-red-suddenly"]
    },
    {
        "id": "faq-114",
        "slug": "airport-telegram-group-safety-tips",
        "title": "机场 Telegram 交流群防被骗、防隐私泄露与群规常识",
        "category": "subscription",
        "categoryLabel": "订阅与节点管理",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "进入机场官方 TG 交流群时防止遭遇假客服私信诈骗、隐藏手机号防开盒的安全守则。",
        "symptoms": [
            "刚进群在群里提问了一句「节点连不上」，立刻有头像和名字一模一样的高仿管理人员私信你要求发订阅链接或微信扫码转账",
            "Telegram 账号无故被盗或收到境外骚扰电话"
        ],
        "rootCauses": [
            "骗子长期潜伏在大型机场群组内，使用自动化脚本监控带问号的提问，随后高仿官方头像实施私信诈骗；TG 默认未隐藏 +86 手机号导致真实身份泄露"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：第一步在 TG 隐私设置中彻底隐藏手机号",
                "detail": "打开 Telegram「Settings」->「Privacy and Security」->「Phone number」-> 选择「Nobody (任何人不可见)」，下方的「谁能通过手机号找到我」设为「My Contacts」。"
            },
            {
                "stepTitle": "步骤 2：牢记铁律：任何主动私信你的所谓「管理员/客服」100% 是骗子！",
                "detail": "正规机场官方管理团队绝不会主动私信任何普通用户索要密码、订阅链接或要求额外转账。遇到主动私信直接点击 Report Spam 并拉黑屏蔽。"
            },
            {
                "stepTitle": "步骤 3：群内严禁发送完整的订阅 URL 截图",
                "detail": "截图提问时必须用马赛克完全遮挡住你的订阅 URL 和二维码，防止他人盗取你的节点配额。"
            }
        ],
        "faqTips": "遇到技术故障，优先在机场官网提交正规 Support Ticket（支持工单），这是最安全、最直接的官方通道。",
        "relatedSlugs": ["subconverter-remote-token-leak", "telegram-connecting-updating-loop"]
    },
    {
        "id": "faq-115",
        "slug": "subscription-link-custom-user-agent",
        "title": "机场屏蔽默认客户端 UA 导致订阅无法更新的自定义 UA 技巧",
        "category": "subscription",
        "categoryLabel": "订阅与节点管理",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "解决部分机场服务端为了防爬虫恶意刷接口，屏蔽了部分小众客户端 User-Agent 的技巧。",
        "symptoms": [
            "同一个订阅链接在手机小火箭里更新正常，但在电脑特定客户端里更新直接报 403 Forbidden",
            "控制台提示：User-Agent blocked by server"
        ],
        "rootCauses": [
            "机场服务端的安全防火墙配置了 UA 过滤白名单，未将部分新兴或小众客户端的默认请求头纳入其中"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：在客户端订阅设置中自定义 User-Agent",
                "detail": "进入 Clash Verge Rev ->「订阅」-> 右键该订阅选择「编辑配置」-> 找到「User-Agent」输入框，填入标准的通用小火箭或 Clash UA：",
                "code": "# 推荐伪装的通用标准 UA：\nClashMeta\n或\nShadowrocket/1990 CFNetwork/1410.0.3 Darwin/22.6.0"
            },
            {
                "stepTitle": "步骤 2：保存并再次点击更新订阅",
                "detail": "修改 UA 保存后，服务端会将请求识别为标准的小火箭或官方 Clash，立即放行订阅数据下发。"
            }
        ],
        "faqTips": "自定义 UA 是解决各类客户端订阅导入报 403 错误的杀手锏秘籍。",
        "relatedSlugs": ["subscription-update-error-solutions", "shadowrocket-subscription-timeout"]
    },
    {
        "id": "faq-116",
        "slug": "node-multiplier-billing-explained",
        "title": "机场节点倍率（0.5x、1.0x、3.0x、5.0x）到底是什么意思？如何省流量",
        "category": "subscription",
        "categoryLabel": "订阅与节点管理",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "搞懂节点倍率的真实扣费逻辑，教你如何用同等套餐看双倍时长的 4K 视频。",
        "symptoms": [
            "看到节点名字后面带有 0.1x、0.5x、1.0x、3.0x 不知该怎么选",
            "用了几天 3.0x 节点，后台流量直接飞快蒸发"
        ],
        "rootCauses": [
            "倍率是机场对不同成本路线的定价杠杆：实际扣除流量 = 你的真实物理流量 × 节点倍率"
        ],
        "solutions": [
            {
                "stepTitle": "倍率类型 1：0.5x / 0.8x 经济型节点 —— 刷视频与大下载首选",
                "detail": "你实际下载了 10GB 视频，后台只从你账户中扣除 5GB 流量！非常适合追剧、挂机下载或轻度刷网页，相当于流量凭空翻倍！"
            },
            {
                "stepTitle": "倍率类型 2：1.0x 标准型节点 —— 日常主力平衡之选",
                "detail": "实打实的 1:1 扣费，通常是机场性价比最高的普通专线线路，性能与消耗最均衡。"
            },
            {
                "stepTitle": "倍率类型 3：3.0x / 5.0x 旗舰高防专线 —— 重要商务与电竞专享",
                "detail": "走最昂贵、成本最高的金融级专网，通常延迟极低且全天 0 丢包。适合重要越洋电话会议、关键考试抢票或游戏排位赛，日常看长视频切勿常驻使用。"
            }
        ],
        "faqTips": "平时看 YouTube 推荐挂 0.5x~1.0x 节点，重要生产力时刻切 3.0x 极速专线，精打细算最聪明。",
        "relatedSlugs": ["traffic-drain-fast-background-leaks", "why-never-buy-multi-year-package"]
    },
    {
        "id": "faq-117",
        "slug": "backup-airport-strategy-redundancy",
        "title": "双机场冷备与热备策略：如何搭建永不失联的网络高可用容灾体系",
        "category": "subscription",
        "categoryLabel": "订阅与节点管理",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "外贸办公、跨境出海与科研刚需用户必备的容灾冗余体系搭建指南。",
        "symptoms": [
            "主力机场突然遇到上游机房故障维护 2 小时，手头正在进行的跨国商务会议被紧急打断",
            "手里只有一家机场，一旦出问题就彻底两眼一抹黑"
        ],
        "rootCauses": [
            "任何网络服务（哪怕是微软、亚马逊云）都有 99.9% 之外的那 0.1% 故障率，单点依赖是所有生产力崩溃的根源"
        ],
        "solutions": [
            {
                "stepTitle": "黄金组合方案：「一条主力包月专线」+「一个不限时长按量计费包」",
                "detail": "日常主力选择稳定、大带宽的高质量包月专线（如隐形人或大佬云）；同时购买一个几块钱或几十块钱、流量永久不过期的「不限时按量计费套餐」（如无忧链接或时空立方）作为常驻备用。"
            },
            {
                "stepTitle": "步骤 2：在客户端中将两家订阅同时导入",
                "detail": "在 Clash Verge Rev 中同时勾选两家订阅，在同一个节点列表中即可看到两家机场的所有节点，主力遇到维护瞬间无缝切换备用，整个团队工作完全不中断！"
            }
        ],
        "faqTips": "按量计费的备用包平时不用一分钱不扣，关键时刻就是救命稻草，是每个专业选手的标配。",
        "relatedSlugs": ["why-never-buy-multi-year-package", "all-nodes-turn-red-suddenly"]
    },
    {
        "id": "faq-118",
        "slug": "airport-reset-traffic-billing-cycle",
        "title": "机场每月流量重置日期与按周期结账常见误区澄清",
        "category": "subscription",
        "categoryLabel": "订阅与节点管理",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "搞清楚你的流量到底是在自然月 1 号重置，还是在每次扣款账单日重置的防超额常识。",
        "symptoms": [
            "以为每个月 1 号会自动刷新 200G 流量，结果 1 号打开依然提示流量耗尽",
            "不知道自己剩余流量还有几天有效"
        ],
        "rootCauses": [
            "大部分机场采用「订单周期重置制」而非「自然月制」：如果你是在 1 月 18 日购买的月付套餐，流量重置时间是每月的 18 日，而不是 2 月 1 日！"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：在机场后台查看「下一次重置日期 (Next Reset Date)」",
                "detail": "登录机场用户仪表盘，在流量圆环图下方明确标注了精确到小时的重置时间戳。"
            },
            {
                "stepTitle": "步骤 2：流量见底但距离重置还有多天的应急方案",
                "detail": "如果提前耗尽了流量，正规机场后台通常提供「提前重置流量包」或「临时充值附加流量包」，花费几元钱即可立即刷新本月配额，无需重复购买新套餐。"
            }
        ],
        "faqTips": "合理规划每月的下载和看剧配额，避免在账单周期最后几天出现断粮尴尬。",
        "relatedSlugs": ["node-multiplier-billing-explained", "traffic-drain-fast-background-leaks"]
    },
    {
        "id": "faq-119",
        "slug": "speedtest-bandwidth-waste-warning",
        "title": "为什么在机场测速测几十次会导致几十上百G流量瞬间蒸发？",
        "category": "subscription",
        "categoryLabel": "订阅与节点管理",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "科普 Speedtest 与一键全节点跑分脚本的流量黑洞真相，告别无意义的测速焦虑。",
        "symptoms": [
            "用测速脚本把列表里的 50 个节点挨个跑了一遍测速，回头一看后台发现蒸发了 80GB 流量"
        ],
        "rootCauses": [
            "Speedtest 测速的物理原理：为了测出你的极限带宽，客户端会向境外服务器并发拉取海量垃圾数据包并塞满整个千兆通道。在 1000M 宽带下，测一个节点短短 15 秒钟就要消耗 1.5GB~2GB 的真实物理流量！测试 50 个节点，直接消耗 100GB 流量！"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：杜绝高频全量跑分，日常使用以延迟测试为主",
                "detail": "在客户端点击闪电图标（仅发送几字节的 Ping 握手包探测毫秒延迟），这种延迟测试几乎完全不消耗任何流量。"
            },
            {
                "stepTitle": "步骤 2：用真实使用场景检验，替代冷冰冰的跑分",
                "detail": "只要打开 YouTube 4K 视频能秒开、拖拽进度条不卡顿，就说明当前节点带宽完全充沛，毫无必要专门去跑满速测速浪费流量。"
            }
        ],
        "faqTips": "流量是买来看视频办公的，不是拿来给测速服务器刷数据的，克制测速瘾是省流量第一步。",
        "relatedSlugs": ["traffic-drain-fast-background-leaks", "nodes-have-ping-but-cannot-browse"]
    },
    {
        "id": "faq-120",
        "slug": "airport-refund-policy-chargeback",
        "title": "机场购买后无法使用能否退款？工单协商与争议申诉指南",
        "category": "subscription",
        "categoryLabel": "订阅与节点管理",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "遇到新买的机场完全连不上或服务质量严重与宣传不符时的正规退款沟通与维权渠道。",
        "symptoms": [
            "刚买完发现当地运营商对该机场完全无法连通，要求退款被客服置之不理",
            "不知道各家服务商的退款保障时间窗口"
        ],
        "rootCauses": [
            "网络代理产品属于数字虚拟商品，大部分机场在服务条款 (ToS) 中明确规定「一经售出概不退款」或仅支持「24 小时内流量未超 5G 无理由退款」"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：仔细阅读该机场的服务条款 (ToS) 与退款政策",
                "detail": "查看官网底部的 Terms of Service，确认其是否提供 24 小时或 3 天内的退款保障期。"
            },
            {
                "stepTitle": "步骤 2：礼貌提交详细工单 (Ticket) 进行协商",
                "detail": "在工单中详细描述本地测试情况（附带 ping 截图和客户端日志），说明由于本地网络特殊原因确实无法连接，申请原路退回或退回站内余额。"
            },
            {
                "stepTitle": "步骤 3：防范风险的最好办法永远是「先买月付」",
                "detail": "花十几块钱买月付即使遇到水土不服损失也极小，切勿一上来就为了省几块钱买大几百的年付。"
            }
        ],
        "faqTips": "正规老牌机场对于合理的用户技术原因退款通常支持工单扣除少量手续费原路退还，购买前认准信誉品牌最关键。",
        "relatedSlugs": ["why-never-buy-multi-year-package", "how-to-spot-scam-airports"]
    }
]

print(f"Loaded {len(SUBSCRIPTION_FAQS)} subscription FAQs.")
