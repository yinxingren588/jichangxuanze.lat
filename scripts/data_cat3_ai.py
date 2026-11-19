# -*- coding: utf-8 -*-
# Category 3: AI 工具与海外服务风控 (20 篇)

AI_FAQS = [
    {
        "id": "faq-51",
        "slug": "chatgpt-access-denied-error-1020",
        "title": "OpenAI / ChatGPT 提示「Access Denied Error 1020」彻底解决指南",
        "category": "ai",
        "categoryLabel": "AI与服务风控",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "访问 chatgpt.com 时遭遇 Cloudflare 弹窗阻断、提示 Error 1020 访问被拒的最全破局方案。",
        "symptoms": [
            "打开 ChatGPT 官网瞬间跳出 Cloudflare 拦截页面，大字显示「Access Denied, Error code 1020」",
            "换了几个节点依然提示无法访问",
            "清除浏览器缓存后依然被拦截"
        ],
        "rootCauses": [
            "当前机场节点的出口 IP 属于廉价机房托管 IP (DataCenter IP)，触发了 Cloudflare 防火墙的高危风控规则",
            "该 IP 在短时间内有大量用户并发访问 OpenAI，被官方标记为滥用并列入临时黑名单",
            "浏览器语言或系统时区被探测为中国大陆（Asia/Shanghai）但出口 IP 在境外产生关联风控"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：必须切换为具有原生住宅/家宽 IP 出口的节点",
                "detail": "在节点列表中挑选标有「原生 IP」、「AI 解锁」或「家宽」的节点（如隐形人或飞猫云的专属 AI 节点）。原生家宽出口被 Cloudflare 视为正常家庭宽带用户，信誉极高，瞬间通过。"
            },
            {
                "stepTitle": "步骤 2：彻底清除 chatgpt.com 的本地 Cookie 与 LocalStorage",
                "detail": "按 F12 打开开发者工具 ->「应用程序 (Application)」->「存储 (Storage)」-> 点击「清除网站数据」，随后使用无痕窗口重新打开。"
            },
            {
                "stepTitle": "步骤 3：关闭浏览器内置的 WebRTC 真实 IP 泄漏",
                "detail": "安装 uBlock Origin 或 WebRTC Control 扩展插件，禁用浏览器底层的 WebRTC 局域网探测，杜绝真实 IP 暴露。"
            }
        ],
        "faqTips": "尽量固定使用同一个优质专线节点登录 ChatGPT，频繁跨国家（刚在香港下一秒切到美国）是触发 OpenAI 封号的主要原因之一。",
        "relatedSlugs": ["chatgpt-unable-to-load-site", "claude-app-unavailable-in-your-region"]
    },
    {
        "id": "faq-52",
        "slug": "chatgpt-unable-to-load-site",
        "title": "ChatGPT 登录页面提示「Unable to load site」一直转圈排查",
        "category": "ai",
        "categoryLabel": "AI与服务风控",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "点击 Log in 登录按钮后页面无限 loading、弹窗 Unable to load site 的排错方案。",
        "symptoms": [
            "输入账号密码后页面一直旋转菊花，长达几分钟没有反应",
            "弹窗提示：Unable to load site. Please try again later.",
            "控制台报错 403 Forbidden 或 CORS policy 跨域阻断"
        ],
        "rootCauses": [
            "分流规则中只将 chatgpt.com 走代理，而 auth0.openai.com 或 tcr9i.chat.openai.com 登录鉴权子域名被漏掉走了国内直连",
            "浏览器广告拦截插件（如 AdGuard）强行拦截了 OpenAI 的 Arkose 人机验证脚本"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：确保分流规则完整覆盖 OpenAI 全套域名",
                "detail": "在客户端规则集中确保包含 GEOSITE:openai 规则组，覆盖包括 auth0、challenges.cloudflare.com 在内的所有鉴权域名。"
            },
            {
                "stepTitle": "步骤 2：临时禁用浏览器广告拦截扩展",
                "detail": "将 chatgpt.com 添加到广告拦截插件的白名单中，确保人机验证模块能正常加载完成。"
            }
        ],
        "faqTips": "如果在 Chrome 下遇到转圈，尝试使用 Edge 浏览器或开启无痕模式往往能快速跳出死循环。",
        "relatedSlugs": ["chatgpt-access-denied-error-1020", "chatgpt-mobile-app-login-loop"]
    },
    {
        "id": "faq-53",
        "slug": "claude-app-unavailable-in-your-region",
        "title": "Claude 3.5 提示「App unavailable in your region」终极绕过方案",
        "category": "ai",
        "categoryLabel": "AI与服务风控",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "Anthropic 旗下 Claude 对地区与节点风控极为严苛，提示区域不可用或账号被封的避坑实战。",
        "symptoms": [
            "访问 claude.ai 提示「App unavailable in your region」",
            "刚注册完账号几分钟内就被强行封禁 (Account suspended)",
            "输入手机号验证时提示当前国家暂不支持"
        ],
        "rootCauses": [
            "使用了香港、俄罗斯等 Anthropic 明确不支持国家地区的节点访问",
            "节点 IP 虽然位于美国，但在 IP2Location 或 MaxMind 数据库中被标记为滥用机房 IP",
            "系统时区与语言设置与代理 IP 物理地理位置严重冲突"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：严禁使用任何香港或澳门节点访问 Claude",
                "detail": "Claude 官方对香港 IP 全面阻断。必须选用正规「美国 (US)」、「日本 (JP)」或「英国 (UK)」的纯物理专线节点。"
            },
            {
                "stepTitle": "步骤 2：修改浏览器系统时区为所选节点时区",
                "detail": "若选用美西节点，将电脑时区临时改为 (UTC-08:00) 太平洋时间，语言首选英文，可极大降低被 Anthropic 风控模型标记的概率。"
            },
            {
                "stepTitle": "步骤 3：选用经过 Claude 原生解锁认证的优质机场",
                "detail": "选用隐形人、大佬云等专门针对 Claude 3.5 部署了纯净住宅出口的机场，从根本上解决地区阻断问题。"
            }
        ],
        "faqTips": "Claude 的风控等级显著高于 ChatGPT，强烈建议不要频繁切换节点，保持一个固定的高质量美区专线访问最安全。",
        "relatedSlugs": ["chatgpt-access-denied-error-1020", "gemini-advanced-country-not-supported"]
    },
    {
        "id": "faq-54",
        "slug": "chatgpt-mobile-app-login-loop",
        "title": "iOS / Android 官方 ChatGPT App 登录死循环与短信验证失败对策",
        "category": "ai",
        "categoryLabel": "AI与服务风控",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "解决在 iPhone 或安卓手机打开官方 ChatGPT App 提示 Something went wrong 无法登录的排错。",
        "symptoms": [
            "点击「Continue with Apple」或「Continue with Google」后页面直接退回初始界面",
            "提示：Something went wrong. Please check your connection and try again.",
            "短信验证码环节无法发送或收不到短信"
        ],
        "rootCauses": [
            "手机客户端只开了系统代理，未代理底层系统组件的 HTTPS 流量",
            "iOS 设备的「语言与地区」设置为中国大陆，被 App 内部的系统 API 探测识别",
            "安卓系统缺少 Google Play Services 基础套件"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：在 iPhone 设置中修改「地区」为美国",
                "detail": "打开 iPhone「设置」->「通用」->「语言与地区」-> 将「地区」改为「美国」，日历改为公历，随后重启手机。"
            },
            {
                "stepTitle": "步骤 2：在小火箭中开启全局代理排查",
                "detail": "初次登录时，在小火箭中临时将全局路由从「配置/规则」改为「代理 (Proxy)」，确保 App 初始化探测流量完全走境外通道。"
            }
        ],
        "faqTips": "登录成功进入聊天界面后，即可将分流模式切回「配置/规则」模式以节省流量。",
        "relatedSlugs": ["chatgpt-access-denied-error-1020", "apple-id-foreign-region-change"]
    },
    {
        "id": "faq-55",
        "slug": "gemini-advanced-country-not-supported",
        "title": "Google Gemini 提示「Gemini is not supported in this country」应对方案",
        "category": "ai",
        "categoryLabel": "AI与服务风控",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "使用 Google Gemini (前 Bard) 遇到地区受限、无法使用高级版 Gemini Advanced 的解决办法。",
        "symptoms": [
            "访问 gemini.google.com 弹出灰色提示：Gemini is not supported in your country yet.",
            "登录 Google 账号后无法开启 Gemini 对话界面"
        ],
        "rootCauses": [
            "节点所在地被判定为不支持的欧盟部分受限制法案地区、或者香港/国内 IP",
            "Google 账号本身的归属地被判定在中国大陆"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：更换为纯正美国 (US) 或日本 (JP) 节点",
                "detail": "Google 官方对自有服务拥有极强的 IP 识别能力，确保节点使用的是纯净无污染的美日出海线路。"
            },
            {
                "stepTitle": "步骤 2：在 Google 账号设置中修改首选语言为 English (US)",
                "detail": "进入 myaccount.google.com ->「个人信息」->「常规网页偏好设置」-> 语言，添加英语为首选语言。"
            }
        ],
        "faqTips": "Gemini 现已整合入 Google Workspace，配合美区谷歌账号使用体验最为完善。",
        "relatedSlugs": ["claude-app-unavailable-in-your-region", "chatgpt-access-denied-error-1020"]
    },
    {
        "id": "faq-56",
        "slug": "poe-ai-vpn-detected-block",
        "title": "Poe AI 提示 VPN 检测阻断与低风控节点推荐方案",
        "category": "ai",
        "categoryLabel": "AI与服务风控",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "在 Quora 旗下 Poe AI 平台与多种机器人对话时频繁提示 VPN 代理异常的对策。",
        "symptoms": [
            "提问后机器人显示抱歉当前网络环境异常",
            "提示：We have detected unusual activity from your IP address",
            "手机客户端无法加载机器人列表"
        ],
        "rootCauses": [
            "Poe 对公共数据中心 IP 进行了频率限制，单个 IP 每小时请求超过阈值后自动限流"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：切换为小众冷门节点",
                "detail": "避开拥挤的热门美西 1 号机房，切换至新加坡或台湾专线节点，降低单 IP 聚合并发。"
            },
            {
                "stepTitle": "步骤 2：使用第三方客户端或 API 接入",
                "detail": "如果网页端受限，可尝试使用其官方 iOS/Android App，App 端的风控判定通常稍宽松。"
            }
        ],
        "faqTips": "Poe 集成了多种主流模型，适合不想单独折腾每个账号的轻度体验用户。",
        "relatedSlugs": ["chatgpt-access-denied-error-1020", "perplexity-ai-cloudflare-challenge"]
    },
    {
        "id": "faq-57",
        "slug": "midjourney-discord-captcha-loop",
        "title": "使用 Midjourney 遇到 Discord 人机验证 (hCaptcha) 死循环解决",
        "category": "ai",
        "categoryLabel": "AI与服务风控",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "在 Discord 中使用 /imagine 生成图片时，每次都强制弹窗让你点红绿灯且无限死循环的排查。",
        "symptoms": [
            "发送提示词后，Discord 弹窗要求进行 hCaptcha 验证码验证",
            "好不容易点完 9 张图片，点击确认又立即刷新出下一套，永远无法通过",
            "控制台网络提示 captcha token invalid"
        ],
        "rootCauses": [
            "节点 IP 被 Cloudflare / hCaptcha 评分为高危爬虫 IP，信誉分过低",
            "浏览器指纹（Canvas / WebGL）被篡改导致防刷机制判定为自动化脚本"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：更换纯净度更高的专线节点",
                "detail": "切换到信誉评分优秀的住宅 IP 节点，高信誉 IP 通常可以直接免跳验证码或者一键勾选秒过。"
            },
            {
                "stepTitle": "步骤 2：登录 Discord 桌面官方独立客户端",
                "detail": "相比网页版，Discord 官方桌面安装包自带完整环境签名，极少频繁触发人机验证死循环。"
            }
        ],
        "faqTips": "如果必须在网页操作，建议登录一个常用的 Google 账号，其浏览行为历史有助于提高验证通过率。",
        "relatedSlugs": ["google-scholar-unusual-traffic-robot", "perplexity-ai-cloudflare-challenge"]
    },
    {
        "id": "faq-58",
        "slug": "github-copilot-proxy-wsl-ide",
        "title": "VS Code / Cursor 中 GitHub Copilot 无法联网的代理配置技巧",
        "category": "ai",
        "categoryLabel": "AI与服务风控",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "解决程序员在 VS Code、Cursor 或 WSL 环境下使用 GitHub Copilot 报错无法连接鉴权服务器的问题。",
        "symptoms": [
            "VS Code 状态栏右下角的 Copilot 小图标出现斜杠或红色感叹号",
            "输出面板提示：GitHub Copilot could not connect to server. Error: getaddrinfo ENOTFOUND",
            "在代码中无法实时补全代码，触发内联代码无反应"
        ],
        "rootCauses": [
            "VS Code 内部的 Node.js 运行时未继承 Windows 系统的 PAC/HTTP 代理设置",
            "Clash 规则分流未将 githubcopilot.com 与 api.github.com 划入 PROXY 组"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：在 VS Code 设置中显式配置 HTTP 代理",
                "detail": "按 Ctrl + , 打开设置，搜索 http.proxy，填入你的本地代理端口 http://127.0.0.1:7890，并将 http.proxySupport 设置为 on。",
                "code": "{\n  \"http.proxy\": \"http://127.0.0.1:7890\",\n  \"http.proxySupport\": \"on\",\n  \"http.proxyStrictSSL\": false\n}"
            },
            {
                "stepTitle": "步骤 2：推荐开启 Clash Verge 的 TUN 模式",
                "detail": "开启 TUN 模式后，虚拟网卡在网络层接管所有进出流量，无需在每个开发工具（VSCode/Git/Docker）中单独配代理，彻底省心。"
            }
        ],
        "faqTips": "国内直连访问 GitHub API 极不稳定，强烈建议为开发工具配置固定的专线加速通道以保障编写效率。",
        "relatedSlugs": ["cursor-ide-ai-network-error", "git-clone-github-ssh-proxy-config"]
    },
    {
        "id": "faq-59",
        "slug": "twitter-x-sensitive-content-sms",
        "title": "Twitter / X 手机短信验证码接收不到与敏感内容无法开启全解",
        "category": "ai",
        "categoryLabel": "AI与服务风控",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "解决国内用户登录推特 (X) 无法收到 +86 短信验证码，以及设置中无法勾选「显示可能包含敏感内容的媒体」的方案。",
        "symptoms": [
            "输入中国大陆 +86 手机号请求验证码，提示发生错误或等了半小时没有任何短信",
            "在 App 内浏览推文，很多图片显示被遮挡，提示「此媒体可能包含敏感内容」，点击无法解锁"
        ],
        "rootCauses": [
            "国内运营商网关对来自 Twitter 国际通道的短信验证码实施了批量拦截与过滤",
            "Twitter 网页版与移动端策略不同，移动端 App 内不允许直接修改敏感内容总开关"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：绑定海外虚拟邮箱或使用身份验证器 (2FA)",
                "detail": "强烈建议使用 Google Authenticator 或 1Password 开启两步验证，彻底摆脱脆弱且易受阻断的短信验证码。"
            },
            {
                "stepTitle": "步骤 2：必须使用电脑网页版修改敏感内容权限",
                "detail": "在浏览器打开 x.com ->「More」->「Settings and privacy」->「Privacy and safety」->「Content you see」-> 勾选「Display media that may contain sensitive content」，随后重启手机 App 即可永久解锁所有内容。"
            }
        ],
        "faqTips": "修改此项设置必须在电脑或手机浏览器打开桌面版网页修改，官方手机客户端内是找不到该勾选项的。",
        "relatedSlugs": ["telegram-connecting-updating-loop", "reddit-blocked-vpn-datacenter"]
    },
    {
        "id": "faq-60",
        "slug": "telegram-connecting-updating-loop",
        "title": "Telegram 桌面端一直显示「Connecting」或「Updating」修复全解",
        "category": "ai",
        "categoryLabel": "AI与服务风控",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "Telegram 电脑端打开后顶部一直转圈显示 Connecting、收不到新消息的排错与内置代理配置。",
        "symptoms": [
            "Telegram 桌面端左下角或顶部常年显示「Connecting...」，无法同步最近聊天记录",
            "能打开 Google 网页，但是 TG 就是转圈连不上",
            "大文件或视频预览下载极其缓慢"
        ],
        "rootCauses": [
            "Telegram 默认采用自研的 MTProto 协议与固定的服务器 IP 建立 Socket 连接，默认不会自动读取 Windows 系统的 HTTP 代理设置",
            "分流规则中未将 Telegram 专有数据中心网段 (ASN 44907 / 62041) 划入代理出站"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：在 Telegram 设置中手动指定本地 SOCKS5 代理",
                "detail": "打开 Telegram「Settings」->「Advanced」->「Connection type」-> 选择「Use custom proxy」-> 添加 SOCKS5 代理，Server 填 127.0.0.1，Port 填 7890（根据你的客户端端口填写）。",
                "code": "Proxy Type: SOCKS5\nServer: 127.0.0.1\nPort: 7890 (或 Clash 混合端口)"
            },
            {
                "stepTitle": "步骤 2：开启 Clash 的 TUN 模式（全局接管最推荐）",
                "detail": "只要开启了 TUN 模式，Telegram 的底层 Socket 流量会被虚拟网卡自动拦截并转发，无需在 TG 软件内做任何繁琐配置。"
            }
        ],
        "faqTips": "如果偶尔连上但收发图片很慢，建议在节点列表中挑选直连香港机房延迟低、带宽大的优质线路。",
        "relatedSlugs": ["clash-tun-mode-virtual-nic-fail", "twitter-x-sensitive-content-sms"]
    },
    {
        "id": "faq-61",
        "slug": "google-scholar-unusual-traffic-robot",
        "title": "Google 学术搜索频繁弹出「异常流量人机验证」终极排查",
        "category": "ai",
        "categoryLabel": "AI与服务风控",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "学术科研人员在查阅 Google Scholar 文献时，每搜一次就弹出一堆验证码让人抓狂的破解之道。",
        "symptoms": [
            "访问 scholar.google.com 弹出提示「我们的系统检测到您的计算机网络中存在异常流量」",
            "完成一次验证后，换一个关键词再次搜索又立刻弹窗",
            "无法批量导出 EndNote / BibTeX 引用文献"
        ],
        "rootCauses": [
            "公用机场节点出口聚集了上百人同时在查询学术资料，且有人使用爬虫脚本高频爬取，导致整个节点 IP 被 Google 标记为高风控机器流量"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：切换到小众专线节点或冷门地区",
                "detail": "避开默认的香港 01、美西 01 这种万人挤爆的节点，切换到英国、德国或新加坡等冷门专线节点，Google 学术的防御敏感度会大幅下降。"
            },
            {
                "stepTitle": "步骤 2：选用纯净独立 IP 或商务专线",
                "detail": "选用大佬云、跨界云等提供纯净商务出海通道的机场，这类线路用户密度低，绝无爬虫脚本污染，查文献畅快无阻。"
            }
        ],
        "faqTips": "经常需要大批量导出文献的学者，务必备用一条纯净专线，避免在关键时刻耽误论文进度。",
        "relatedSlugs": ["chatgpt-access-denied-error-1020", "midjourney-discord-captcha-loop"]
    },
    {
        "id": "faq-62",
        "slug": "openai-api-key-rate-limit-proxy",
        "title": "开发调用 OpenAI API 报 429 或 403 代理网络配置最佳实践",
        "category": "ai",
        "categoryLabel": "AI与服务风控",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "开发者在 Python/Node.js 项目中调用 OpenAI 官方接口时避免 IP 封禁与网络超时的工程指引。",
        "symptoms": [
            "代码报错：openai.APIConnectionError: Connection error.",
            "返回 HTTP 403 Forbidden 或 Country not supported",
            "高并发调用时频繁遇到 429 Rate Limit"
        ],
        "rootCauses": [
            "Python 请求库默认不走 Windows 系统代理",
            "请求发出的出口 IP 处于受限国家地区，直接被 Cloudflare 拦截"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：在代码中显式配置代理客户端",
                "detail": "在初始化 OpenAI SDK 客户端时，显式传入 http_client 或环境变量，确保流量走稳定的香港/美日专线。",
                "code": "import httpx\nfrom openai import OpenAI\n\nclient = OpenAI(\n    api_key=\"your-api-key\",\n    http_client=httpx.Client(\n        proxy=\"http://127.0.0.1:7890\"\n    )\n)"
            },
            {
                "stepTitle": "步骤 2：使用可靠的海外反向代理中转加速",
                "detail": "在生产环境中，推荐使用海外 VPS 搭建 API 反向代理或使用 Cloudflare Worker 中转 base_url，实现免本地代理直连调用。"
            }
        ],
        "faqTips": "开发环境调试建议直接开启 TUN 模式，免去在每一段代码和测试脚本中硬编码代理地址的烦恼。",
        "relatedSlugs": ["pip-conda-npm-proxy-terminal", "chatgpt-access-denied-error-1020"]
    },
    {
        "id": "faq-63",
        "slug": "perplexity-ai-cloudflare-challenge",
        "title": "Perplexity AI 频繁卡在 Cloudflare 验证界面的破局方案",
        "category": "ai",
        "categoryLabel": "AI与服务风控",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "新一代 AI 搜索引擎 Perplexity 访问时一直停留在 Checking your browser 验证界面的解决指南。",
        "symptoms": [
            "页面显示「Just a moment...」并且勾选框打勾后又重新刷新，陷入无限死循环",
            "提示：Verification failed, please try again",
            "无法进入搜索框提问界面"
        ],
        "rootCauses": [
            "Cloudflare Turnstile 人机验证模块通过分析网络往返延迟 (RTT) 与 TCP 握手特征，判定客户端环境异常"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：更换为带有 uTLS 伪装的专线节点",
                "detail": "在客户端中启用 uTLS，将客户端握手特征伪装为最新版的 Google Chrome，提高指纹拟真度。"
            },
            {
                "stepTitle": "步骤 2：尝试在手机 App 端使用",
                "detail": "Perplexity 官方手机 App（iOS/Android）使用专属的 API 鉴权通道，比网页版更容易通过验证。"
            }
        ],
        "faqTips": "使用纯净专线并配合常用登录浏览器，是解决所有 Cloudflare 拦截的终极法宝。",
        "relatedSlugs": ["chatgpt-access-denied-error-1020", "midjourney-discord-captcha-loop"]
    },
    {
        "id": "faq-64",
        "slug": "cursor-ide-ai-network-error",
        "title": "Cursor 代码编辑器 AI 无法连通与设置系统代理方法",
        "category": "ai",
        "categoryLabel": "AI与服务风控",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "爆火的 AI 编程神器 Cursor 无法生成代码、对话一直提示 Connection failed 的一键修复。",
        "symptoms": [
            "按 Ctrl + K 或 Ctrl + L 唤出 AI，生成一半突然报错：Connection failed / Network error",
            "Index 索引代码库时进度条卡在 0% 无法建立连接",
            "Cursor 设置中无法登录 GitHub 账号"
        ],
        "rootCauses": [
            "Cursor 基于 VS Code 魔改，其后端的 AI 补全通信走的是独立的 gRPC / HTTP2 长连接通道，某些旧版代理工具无法处理长连接中断",
            "分流规则未包含 cursor.sh 和 anysphere.co 等核心域名"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：在 Clash 中添加 Cursor 专属分流规则",
                "detail": "在配置文件自定义规则中追加：DOMAIN-SUFFIX,cursor.sh,PROXY 以及 DOMAIN-SUFFIX,anysphere.co,PROXY，确保全部走代理出站。"
            },
            {
                "stepTitle": "步骤 2：开启 Clash Verge Rev 的 TUN 模式（最彻底）",
                "detail": "Cursor 拥有大量后台子进程（cpp、python 语言服务器），开启 TUN 模式从虚拟网卡直接拦截转发，完美解决长连接中断问题。"
            }
        ],
        "faqTips": "Cursor 重度用户推荐选用低延迟的香港或日本 IPLC 专线，代码生成的实时打字流式体验会极其丝滑。",
        "relatedSlugs": ["github-copilot-proxy-wsl-ide", "clash-tun-mode-virtual-nic-fail"]
    },
    {
        "id": "faq-65",
        "slug": "huggingface-model-download-proxy",
        "title": "国内下载 HuggingFace 模型慢或中断的命令行代理设置全攻略",
        "category": "ai",
        "categoryLabel": "AI与服务风控",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "AI 开发者在终端拉取几十 GB 的开源大模型权重文件时，频繁连接重置超时的终极方案。",
        "symptoms": [
            "huggingface-cli download 卡在 0% 或几百 KB/s 龟速下载",
            "下载大文件（如 model.safetensors）几 GB 后报错 ConnectionResetError",
            "transformers 库直接 load_model 报 HTTPSConnectionPool timeout"
        ],
        "rootCauses": [
            "HuggingFace 模型托管于海外 AWS S3 大容量存储，国内直连受到高频丢包与严重限速",
            "Python 的 requests 库默认不会自动读取系统代理设置"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：在终端临时配置环境变量加速",
                "detail": "在运行下载脚本前，在终端中设置全局代理环境变量并启用 hf-mirror 镜像源。",
                "code": "# PowerShell\n$env:HF_ENDPOINT = \"https://hf-mirror.com\"\n$env:http_proxy = \"http://127.0.0.1:7890\"\n$env:https_proxy = \"http://127.0.0.1:7890\"\nhuggingface-cli download --resume-download meta-llama/Llama-2-7b"
            },
            {
                "stepTitle": "步骤 2：搭配大带宽专线节点（如浪网/大佬云）",
                "detail": "下载超大模型动辄几十上百 GB，建议在客户端中选择大带宽储备、不限并发线程的优质节点，跑满千兆带宽。"
            }
        ],
        "faqTips": "使用 --resume-download 参数开启断点续传，即使中途网络微小波动也不会前功尽弃。",
        "relatedSlugs": ["pip-conda-npm-proxy-terminal", "git-clone-github-ssh-proxy-config"]
    },
    {
        "id": "faq-66",
        "slug": "reddit-blocked-vpn-datacenter",
        "title": "Reddit 屏蔽数据中心 IP 导致无法浏览或账号自动锁定解决",
        "category": "ai",
        "categoryLabel": "AI与服务风控",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "海外大论坛 Reddit 升级反爬虫策略后，使用代理访问提示「Blocked by network security」的对策。",
        "symptoms": [
            "打开 Reddit 网页提示：Blocked by network security (You have been blocked from accessing reddit.com)",
            "手机 App 可以看列表，但无法点赞、无法发帖、提示 Sorry try again later",
            "新注册的账号在没有任何违规的情况下直接被 shadowban（影子禁言）"
        ],
        "rootCauses": [
            "Reddit 近期收紧了对大型公共云服务商（如 Linode、DigitalOcean、Vultr）出口 IP 的反抓取限制，将整个网段列入不可信名单"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：更换为原生家庭住宅 IP 节点",
                "detail": "在客户端中切换带有「原生」、「家宽」标签的专线节点，绕过机房 IP 段黑名单检测。"
            },
            {
                "stepTitle": "步骤 2：避免频繁无痕模式登录",
                "detail": "在固定浏览器内保留正常的会话 Cookie，避免每次打开都作为全新的无头浏览器受到重点审查。"
            }
        ],
        "faqTips": "高质量的原生家宽出口对于需要长期在 Reddit、Twitter 等海外社区养号的用户至关重要。",
        "relatedSlugs": ["chatgpt-access-denied-error-1020", "twitter-x-sensitive-content-sms"]
    },
    {
        "id": "faq-67",
        "slug": "pixiv-bypass-dns-blocking",
        "title": "Pixiv (P站) 国内直连阻断与客户端免翻墙 / 分流配置全流程",
        "category": "ai",
        "categoryLabel": "AI与服务风控",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "画师与二次元爱好者访问 Pixiv 插画网站时图片显示破损裂开、无法登录账号的配置技巧。",
        "symptoms": [
            "pixiv.net 网页能打开，但是图片缩略图全部裂开变成灰色小方块",
            "客户端提示 10054 网络错误",
            "即使开着代理，图片加载速度依然极慢"
        ],
        "rootCauses": [
            "Pixiv 的图片静态资源存储在独立的 i.pximg.net 域名下，该 CDN 域名在国内受到了针对性的 SNI 污染和丢包阻断",
            "某些分流规则库仅包含了主站 pixiv.net，遗漏了图片 CDN 域名"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：完善客户端的分流规则，确保图片 CDN 走代理",
                "detail": "在自定义规则中添加：DOMAIN-SUFFIX,pximg.net,PROXY 以及 DOMAIN-SUFFIX,pixiv.net,PROXY，确保所有高清大图全部由境外专线高速拉取。"
            },
            {
                "stepTitle": "步骤 2：选择日本原生节点以获得最佳加载速度",
                "detail": "Pixiv 的服务器机房位于日本东京，选择日本专线节点（如沪日 IPLC）延迟通常低于 40ms，大图几乎瞬间秒开。"
            }
        ],
        "faqTips": "如果使用第三方 Pixiv 客户端（如 Pixiv-Shaft），可在其设置中开启内置 DoH 域名解析。",
        "relatedSlugs": ["bilibili-taiwan-hk-unblock-rule", "clash-verge-custom-rules-override"]
    },
    {
        "id": "faq-68",
        "slug": "bing-copilot-safesearch-locked",
        "title": "微软 Copilot 强制重定向到国内必应及安全搜索锁定解除",
        "category": "ai",
        "categoryLabel": "AI与服务风控",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "打开微软 Copilot 自动跳转到 cn.bing.com、安全搜索被强制锁定为「严格」无法解锁的彻底修复。",
        "symptoms": [
            "访问 copilot.microsoft.com 页面右上角的 Copilot 聊天面板消失",
            "网址被强制重定向为 cn.bing.com",
            "提示：此功能在您的地区暂不可用"
        ],
        "rootCauses": [
            "微软根据浏览器的地理位置定位、Cookie 中的地区代号 (cc=CN) 以及国内 DNS 强制执行了重定向"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：在必应设置中修改国家和地区为美国",
                "detail": "打开 bing.com -> 点击右上角汉堡菜单 ->「设置」->「国家/地区」-> 选择「美国 (当前英语)」，并在安全搜索中选择「中等」或「关闭」。"
            },
            {
                "stepTitle": "步骤 2：在分流规则中将 bing 整体纳入 PROXY 组",
                "detail": "规则添加：DOMAIN-SUFFIX,bing.com,PROXY，防止 DNS 查询返回国内 CDN IP 触发跳转。"
            }
        ],
        "faqTips": "配合 Edge 浏览器自带的侧边栏使用 Copilot 时，建议在系统设置中将默认区域调整为非中国区。",
        "relatedSlugs": ["gemini-advanced-country-not-supported", "chatgpt-access-denied-error-1020"]
    },
    {
        "id": "faq-69",
        "slug": "apple-id-foreign-region-change",
        "title": "美区 / 日区 Apple ID 注册与绑定免税区地址防风控保姆级指南",
        "category": "ai",
        "categoryLabel": "AI与服务风控",
        "readTime": "6 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "苹果用户下载小火箭、ChatGPT 等海外 App 必须拥有的美区 Apple ID 注册要点与防封防退避坑法则。",
        "symptoms": [
            "在 App Store 搜索不到 Shadowrocket 或 ChatGPT 官方正版应用",
            "注册美区账号提示无法完成创建，或购买礼品卡充值后账号被立即停用"
        ],
        "rootCauses": [
            "使用了非纯净节点注册，被苹果风控识别为代理批量创建",
            "填写的账单地址属于高税率州（如加州），导致扣费时产生额外税费且容易触发核验"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：使用美国免税州账单地址",
                "detail": "在填写账单地址时，选择美国五大免税州之一（如俄勒冈州 Oregon、特拉华州 Delaware 或阿拉斯加州），邮编例如 97201，免除每次内购扣税。"
            },
            {
                "stepTitle": "步骤 2：全程保持纯净美国专线节点连接",
                "detail": "在苹果官网 appleid.apple.com 注册时，全程使用纯净美国 IP 访问，付款方式先选「None (无)」，成功后再通过正规渠道购买 App Store 美区礼品卡兑换。"
            }
        ],
        "faqTips": "平时下载完软件后可以切回国区 ID，但千万不要在系统「设置」中登录外区 iCloud，只在「App Store」中登录下载应用最安全！",
        "relatedSlugs": ["shadowrocket-subscription-timeout", "chatgpt-mobile-app-login-loop"]
    },
    {
        "id": "faq-70",
        "slug": "steam-community-error-101-118",
        "title": "Steam 社区 / 个人资料 / 好友列表错误代码 101/118 快速修复与分流",
        "category": "ai",
        "categoryLabel": "AI与服务风控",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "解决电脑 Steam 客户端打开好友列表、创意工坊提示错误代码 -101、-118 的规则分流技巧。",
        "symptoms": [
            "点击 Steam 个人资料或社区创意工坊，黑屏并提示「错误代码：-101 / -118 无法载入网页」",
            "好友列表无法连接网络，一直处于离线状态",
            "游戏本身能玩，唯独社区网页打不开"
        ],
        "rootCauses": [
            "Steam 社区域名 (steamcommunity.com) 在国内遭到严密的 DNS 污染与 HTTPS SNI 阻断",
            "游戏下载流量与网页流量混在一起，导致误走代理白白浪费节点流量"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：在 Clash 中添加 Steam 社区专用分流规则",
                "detail": "在分流规则中将 steamcommunity.com 指向 PROXY 节点，而将游戏下载域名 (steampowered.com / steamcontent.com) 指向 DIRECT 直连，既能秒开社区，下载游戏又能跑满国内千兆宽带！",
                "code": "rules:\n  - DOMAIN-SUFFIX,steamcommunity.com,PROXY\n  - DOMAIN-SUFFIX,steamcontent.com,DIRECT\n  - DOMAIN-SUFFIX,steampowered.com,DIRECT"
            },
            {
                "stepTitle": "步骤 2：刷新本地 hosts 与 DNS 缓存",
                "detail": "在 CMD 运行 ipconfig /flushdns，重启 Steam 客户端即可丝滑进入创意工坊。"
            }
        ],
        "faqTips": "这种动静分离的分流策略是玩 Steam 必须掌握的高级技巧，千万不要用代理去跑几十 GB 的游戏更新。",
        "relatedSlugs": ["bypass-steam-epic-game-download", "error-udp-nat-symmetric-restricted"]
    }
]

print(f"Loaded {len(AI_FAQS)} AI FAQs.")
