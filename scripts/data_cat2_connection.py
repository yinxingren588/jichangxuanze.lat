# -*- coding: utf-8 -*-
# Category 2: 连接报错与网络诊断 (25 篇)

CONNECTION_FAQS = [
    {
        "id": "faq-26",
        "slug": "error-tls-handshake-timeout",
        "title": "节点频繁报错「TLS handshake timeout」握手超时根源剖析与解决",
        "category": "connection",
        "categoryLabel": "网络连接报错",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "分析 Clash / Xray 日志中频繁出现 TLS 握手超时、无法建立安全传输通道的根本原因及排查方案。",
        "symptoms": [
            "客户端日志大量出现：connect: TLS handshake timeout",
            "节点在测速列表显示绿色延迟，但访问具体外网网页时加载十几秒最终报错",
            "某些 Trojan 或 Shadowsocks-TLS 节点断断续续"
        ],
        "rootCauses": [
            "GFW 防火墙对特定 TLS 握手包（特别是未经混淆的标准 Client Hello）进行了 SNI 阻断或丢包干扰",
            "客户端电脑的系统时间与服务器真实 UTC 时间误差超过 60 秒，导致证书有效期校验超时",
            "机场落地服务器的 TLS 证书过期或 Let's Encrypt 证书自动续签失败"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：第一步同步系统网络时间（90% 的诱因）",
                "detail": "按 Win + I 打开 Windows 设置 ->「时间和语言」->「日期和时间」，点击「立即同步」，确保系统时间与国家授时中心秒级同步。"
            },
            {
                "stepTitle": "步骤 2：切换为支持 uTLS 浏览器伪装的内核",
                "detail": "在 Clash Verge Rev 中切换为 Mihomo 核心，并在设置中开启 uTLS（如 Chrome / Safari 指纹伪装），有效躲避 GFW 对握手特征的主动探测过滤。"
            },
            {
                "stepTitle": "步骤 3：更换同机场其他 IPLC 内网专线节点",
                "detail": "真正的 IPLC 专线走物理内网不过墙，完全不受公网 TLS 阻断影响，可立即恢复顺畅连接。"
            }
        ],
        "faqTips": "如果所有节点都报 TLS 错误，请优先检查本地宽带是否被运营商开启了单向阻断，尝试用手机 5G 热点测试对比即可快速定位。",
        "relatedSlugs": ["error-clock-skew-system-time", "error-certificate-verify-failed"]
    },
    {
        "id": "faq-27",
        "slug": "error-connection-reset-by-peer",
        "title": "连接突然中断并提示「connection reset by peer」排错全解",
        "category": "connection",
        "categoryLabel": "网络连接报错",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "排查网络连接建立后突然被对端重置 (TCP RST)、网页加载一半中断报错的实用指南。",
        "symptoms": [
            "看 YouTube 4K 视频看到一半突然缓冲转圈，控制台提示 connection reset by peer",
            "下载大文件（如 GitHub Release、HuggingFace 模型）几百兆后突然连接断开无法续传",
            "特定敏感域名一访问立刻触发长达 3 分钟的无响应"
        ],
        "rootCauses": [
            "GFW 在检测到未加密或特征明显的境外敏感流量时，双向注入伪造的 TCP RST 重置报文",
            "机场中继入口到落地机之间的链路发生瞬时抖动或单边断网",
            "服务器端并发连接数达到上限，防火墙主动掐断非活跃会话"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：排查是否误开启了「直连 (Direct)」导致撞墙",
                "detail": "检查分流规则，确保目标海外域名没有被误划入 DIRECT 直连规则。如果直连访问被封锁域名，必然会被 GFW 发送 RST 报文直接阻断。"
            },
            {
                "stepTitle": "步骤 2：在客户端中开启 TCP 并发与保持活跃",
                "detail": "在 Clash 配置中开启 keep-alive 与 tcp-concurrent，增加链路连接的健壮性并快速故障切换。"
            },
            {
                "stepTitle": "步骤 3：选择纯物理内网 IPLC 专线",
                "detail": "公网隧道中继在敏感时期常受 RST 干扰，建议切换至隐形人等走物理专线的节点彻底杜绝伪造重置包。"
            }
        ],
        "faqTips": "TCP RST 注入是防火墙最经典的阻断手法，只要流量走完整的全加密专线通道，GFW 根本无法窥探报文内容，也就无法实施注入。",
        "relatedSlugs": ["error-tcp-rst-injection-gfw", "error-eof-proxy-closed"]
    },
    {
        "id": "faq-28",
        "slug": "error-eof-proxy-closed",
        "title": "客户端日志大量出现「EOF」错误意味着什么？如何根治",
        "category": "connection",
        "categoryLabel": "网络连接报错",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "详细解析代理客户端输出中频繁看到的 proxy connect error: EOF 含义与彻底解决方法。",
        "symptoms": [
            "日志窗口频繁刷出「read tcp 127.0.0.1:xxx->...: read: connection reset by peer / EOF」",
            "网页加载失败并显示白屏，过几秒再次刷新又恢复正常",
            "Telegram 或海外游戏频繁重连"
        ],
        "rootCauses": [
            "EOF 代表 End of File（文件结尾），在网络层表示服务端没有发送任何预期数据就突然单方面关闭了 Socket 连接",
            "机场节点被瞬时超载打满，后端代理核心自动重启",
            "运营商 NAT 网关超时，自动回收了长时间无流量的空闲连接"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：排查是否处于晚高峰极端拥堵期",
                "detail": "如果在每晚 20:00~23:00 集中出现 EOF，说明该节点的出口带宽已被其他大流量用户打满，建议切换到负载较低的备选节点。"
            },
            {
                "stepTitle": "步骤 2：调整客户端 TCP 保持活跃间隔",
                "detail": "缩短客户端的 Keep-Alive 探测间隔至 15~30 秒，防止中间 NAT 路由器提前掐死连接。"
            }
        ],
        "faqTips": "偶发的单次 EOF 属于正常公网丢包现象，只有当连续高频刷屏且导致网页无法打开时才需要介入排查。",
        "relatedSlugs": ["error-connection-reset-by-peer", "error-dial-tcp-timeout-10000ms"]
    },
    {
        "id": "faq-29",
        "slug": "error-certificate-verify-failed",
        "title": "报错「SSL: CERTIFICATE_VERIFY_FAILED」证书验证失败排错",
        "category": "connection",
        "categoryLabel": "网络连接报错",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "访问外网或运行 Python/Node 脚本时频繁出现 SSL 证书自签名错误、证书不可信的原因与处理方案。",
        "symptoms": [
            "Python 请求报错：ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED]",
            "浏览器访问 Google 提示「您的连接不是私密连接」NET::ERR_CERT_AUTHORITY_INVALID",
            "git clone 报 fatal: unable to access ... SSL certificate problem"
        ],
        "rootCauses": [
            "客户端开启了 MitM 解密抓包功能，但未将生成的私有 CA 证书导入系统受信任根证书颁发机构",
            "公司内网深信服或网络行为管理防火墙正在进行中间人流量解密劫持",
            "机场节点配置了错误的 skip-cert-verify: false 且节点使用的证书已过期"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：在客户端配置中开启跳过证书验证（应急）",
                "detail": "如果节点本身的伪装域名证书存在小问题，在 Clash 配置的对应节点下方添加 skip-cert-verify: true 即可跳过校验。",
                "code": "proxies:\n  - name: \"香港 01 节点\"\n    type: trojan\n    server: xxx.com\n    port: 443\n    skip-cert-verify: true"
            },
            {
                "stepTitle": "步骤 2：排查本地杀毒软件的「HTTPS 流量扫描」",
                "detail": "进入卡巴斯基、ESET 或某些国产安全卫士，临时关闭其内置的「扫描加密连接/HTTPS 检测」功能，防止其插入伪造证书。"
            }
        ],
        "faqTips": "切勿在生产服务器环境中随意全局关闭 SSL 校验，应优先定位是哪一个中间件注入了伪造证书。",
        "relatedSlugs": ["quantumult-x-mitm-cert-untrusted", "error-tls-handshake-timeout"]
    },
    {
        "id": "faq-30",
        "slug": "error-dial-tcp-timeout-10000ms",
        "title": "节点测速全部显示 Timeout 10000ms 终极排查六步法",
        "category": "connection",
        "categoryLabel": "网络连接报错",
        "readTime": "6 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "解决打开客户端点击测速时所有节点全红、全部显示 Timeout 超时的最完整排查指南。",
        "symptoms": [
            "点击延迟测试后，全部几十个节点无一例外全部显示 Timeout 或 10000ms",
            "原本昨天还能正常使用，今天打开一个外网网页都加载不出来",
            "切换不同国家地区节点毫无反应"
        ],
        "rootCauses": [
            "机场订阅域名被墙或机场服务商整体更换了解密密钥/端口",
            "本地电脑系统时间严重不同步",
            "本地 Windows 防火墙或第三方网络防护直接将客户端内核拉入了入站黑名单",
            "国内宽带 DNS 发生故障，根本无法解析节点服务器的初始 IP 地址"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：同步系统北京时间（最常见）",
                "detail": "前往 Windows 设置强制同步系统时间。时间只要差了 1 分钟以上，现代 VMess/Vless 加密握手协议会直接判定为重放攻击而拒绝连接。"
            },
            {
                "stepTitle": "步骤 2：重新更新一次订阅链接",
                "detail": "机场可能由于受到攻击或故障转移，全面更换了后端节点接入点。在订阅面板点击刷新订阅，拉取最新的节点配置。"
            },
            {
                "stepTitle": "步骤 3：更换客户端内置测速 URL",
                "detail": "有些机场屏蔽了默认的 Google 204 测速地址，进入设置将测速地址改为 http://cp.cloudflare.com/generate_204 再次测试。"
            }
        ],
        "faqTips": "如果手机连 5G 热点测试所有节点是绿的，但连家里 Wi-Fi 全红，说明家里宽带运营商或路由器设置存在拦截，可尝试重启光猫更新外网 IP。",
        "relatedSlugs": ["nodes-have-ping-but-cannot-browse", "all-nodes-turn-red-suddenly"]
    },
    {
        "id": "faq-31",
        "slug": "error-io-timeout-dns-resolve",
        "title": "访问外网报错「i/o timeout」且域名解析为 0.0.0.0 故障处理",
        "category": "connection",
        "categoryLabel": "网络连接报错",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "解决 Clash Fake-IP 模式下 DNS 冲突导致目标域名解析为 0.0.0.0 或无法完成首包交互的排错。",
        "symptoms": [
            "浏览器提示 ERR_NAME_NOT_RESOLVED 或 ERR_CONNECTION_TIMED_OUT",
            "ping 目标网站直接显示来自 0.0.0.0 或 198.18.0.x 的响应超时",
            "Clash 日志中出现 dial tcp: lookup xxx.com: i/o timeout"
        ],
        "rootCauses": [
            "Clash 内置 DNS 配置的 nameserver 上游 DNS 地址在国内无法联通",
            "Windows 本地 DNS 缓存堆积损坏",
            "本地路由器开启了 DNS 重定向或防劫持功能，阻断了 53 端口 UDP 流量"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：刷新本地 Windows DNS 缓存",
                "detail": "打开 CMD 运行 ipconfig /flushdns 命令清空本地堆积的过期映射缓存。",
                "code": "ipconfig /flushdns"
            },
            {
                "stepTitle": "步骤 2：优化 Clash 内置 DNS 上游服务器",
                "detail": "在配置文件的 dns 部分，将国内 nameserver 设置为国内权威公共 DNS（如 223.5.5.5 和 119.29.29.29），境外 fallback 设置为 https://1.1.1.1/dns-query。"
            }
        ],
        "faqTips": "Fake-IP 模式下解析出 198.18.x.x 是完全正常的内部保留虚拟 IP，核心会将其映射到远端真实服务器，无需惊慌。",
        "relatedSlugs": ["clash-tun-fake-ip-vs-redir-host", "dns-leak-detection-fix"]
    },
    {
        "id": "faq-32",
        "slug": "error-ws-bad-handshake-403",
        "title": "WebSocket 节点提示「WebSocket bad handshake: 403 Forbidden」解决",
        "category": "connection",
        "categoryLabel": "网络连接报错",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "使用 VMess+WS 或 Vless+WS 协议时报 HTTP 403 握手拒绝的排查方案。",
        "symptoms": [
            "日志反复提示：websocket: bad handshake with status 403 Forbidden",
            "节点一直转圈，完全没有任何下行流量产生",
            "仅在使用 Cloudflare CDN 优选节点时出现该问题"
        ],
        "rootCauses": [
            "客户端配置中的 Host 请求头或 Path 路径与服务端 Nginx/Caddy 的反向代理配置不一致",
            "Cloudflare WAF 防火墙将该 IP 判定为恶意爬虫并拦截了 WebSocket 升级请求",
            "机场服务端的反代回源证书失效"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：检查 ws-opts 里的 path 和 headers",
                "detail": "查看节点配置，确保 path（如 /my-ws-path）前导斜杠完整，且 Host 请求头与服务端的伪装域名绝对完全一致。"
            },
            {
                "stepTitle": "步骤 2：更新订阅获取最新的 CDN 回源路径",
                "detail": "机场可能会因防封需要定时轮换 WebSocket 分流路径，重新拉取一次订阅即可自动匹配新路径。"
            }
        ],
        "faqTips": "随着新一代 Vless-Reality 和 Hysteria 2 的普及，传统的 WebSocket+TLS 方案因握手延迟偏高已逐渐退居备用地位。",
        "relatedSlugs": ["vless-reality-anti-censorship-how-it-works", "error-tls-handshake-timeout"]
    },
    {
        "id": "faq-33",
        "slug": "error-502-bad-gateway-reality",
        "title": "Reality / Vless 节点提示 502 Bad Gateway 目标伪装站异常排查",
        "category": "connection",
        "categoryLabel": "网络连接报错",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "连接 Vless-Reality 节点时提示 502 错误或无法连通伪装站的处理方案。",
        "symptoms": [
            "连接日志显示 received HTTP/1.1 502 Bad Gateway",
            "节点无法握手，无法通过伪装站点借用证书",
            "Reality 节点偶发性大面积失联"
        ],
        "rootCauses": [
            "机场服务端借用的外部目标网站（如 www.apple.com、www.microsoft.com）对来源 SNI 进行了风控阻断",
            "节点配置的 ShortID 或 PublicKey 公钥不匹配"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：更新订阅同步最新的 Reality 目标伪装站列表",
                "detail": "机场管理员通常会轮换更优质、更低风控的海外大厂伪装目标网站，更新订阅即可解决。"
            },
            {
                "stepTitle": "步骤 2：检查本地客户端版本是否过低",
                "detail": "Xray 1.8.0 之前版本对某些 Reality TLS 1.3 扩展支持不全，建议升级至最新稳定版 Xray 或 Mihomo 核心。"
            }
        ],
        "faqTips": "Reality 协议本身不会被 GFW 特征识别，502 多数属于服务端与伪装目标站之间的反代链路配置问题。",
        "relatedSlugs": ["vless-reality-anti-censorship-how-it-works", "error-sni-mismatch-tls"]
    },
    {
        "id": "faq-34",
        "slug": "error-hysteria2-udp-rate-limit",
        "title": "Hysteria 2 节点被运营商 QoS 限制甚至丢包 90% 处理对策",
        "category": "connection",
        "categoryLabel": "网络连接报错",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "针对部分省份运营商（如某些地区移动或广电）对 UDP 协议暴力 QoS 限速导致 Hysteria 2 瘫痪的应对方案。",
        "symptoms": [
            "白天使用 Hysteria 2 节点下行可以跑满，一到晚上 8 点后速度直接跌至几百 Kbps",
            "丢包率飙升至 80%~90%，视频严重卡顿",
            "改用传统的 Shadowsocks 或 Trojan 协议反而能跑出正常速度"
        ],
        "rootCauses": [
            "当地城域网宽带运营商在晚高峰对未知境外 UDP 流量实施了强制 QoS 队列惩罚或严格限速",
            "Hysteria 2 的默认发包拥塞算法与当地宽带 MTU 不适配"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：开启并使用端口跳跃 (Port Hopping)",
                "detail": "Hysteria 2 支持配置一个端口范围（例如 20000-40000），客户端定期动态切换通信端口，避免长时间固定单端口被运营商 QoS 规则抓包盯上。"
            },
            {
                "stepTitle": "步骤 2：调整客户端上传与下载带宽参数",
                "detail": "不要盲目将 up_mbps 设得过高，根据你的实际家庭上行宽带（如 50M 或 100M）如实填写，避免过度激进发包触发运营商惩罚。"
            },
            {
                "stepTitle": "步骤 3：高峰期切换为走物理内网的 IPLC 专线",
                "detail": "IPLC 内网专线走企业私网隧道，完全不走普通公网 UDP，根本不存在运营商 QoS 问题。"
            }
        ],
        "faqTips": "Hysteria 2 极度适合在弱网或普通轻度拥堵时起飞，但若遇到运营商无差别绞杀 UDP 时，TCP 专线仍然是不可替代的稳定基石。",
        "relatedSlugs": ["hysteria-2-udp-protocol-deep-dive", "error-udp-nat-symmetric-restricted"]
    },
    {
        "id": "faq-35",
        "slug": "dns-leak-detection-fix",
        "title": "什么是 DNS 泄漏？如何使用 Extended Test 检测并彻底修复",
        "category": "connection",
        "categoryLabel": "网络连接报错",
        "readTime": "6 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "深入剖析 DNS 泄漏带来的隐私暴露与翻墙失效风险，手把手教你配置防泄漏与无污染加密 DNS。",
        "symptoms": [
            "在 dnsleaktest.com 进行扩展测试，发现列表中赫然出现了本地中国电信/联通/移动的 DNS 服务器",
            "即使开着代理，某些海外网站依然弹窗提示「检测到你的真实物理位置在大连/广州/北京」",
            "访问特定未被直接屏蔽的海外小众网站经常被解析到反诈拦截页面"
        ],
        "rootCauses": [
            "操作系统默认优先使用网卡设定的本地运营商 DNS 进行域名首轮解析",
            "客户端分流规则中未开启针对 DNS 查询的强制远端代理转发",
            "Windows 系统的「智能多宿主名称解析 (Smart Multi-Homed Name Resolution)」特性在所有网卡上并发发送 DNS 查询"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：在线访问 dnsleaktest.com 进行 Standard / Extended Test",
                "detail": "在开启代理的状态下打开 dnsleaktest.com，点击「Extended Test」。如果测试结果只有美国/香港等境外机房 DNS，说明安全；若出现任何中国境内的 ISP，即为存在泄漏。"
            },
            {
                "stepTitle": "步骤 2：在 Clash 配置中开启 Fake-IP 与严格路由",
                "detail": "在 dns 配置段中，将 mode 设为 fake-ip，并在 tun 模块中开启 strict-route: true，禁止系统绕过虚拟网卡向物理网卡发送 DNS 请求。"
            },
            {
                "stepTitle": "步骤 3：组策略彻底禁用 Windows 智能多宿主名称解析",
                "detail": "按 Win + R 运行 gpedit.msc，定位至「计算机配置 -> 管理模板 -> 网络 -> DNS 客户端」，双击「关闭智能多宿主名称解析」并设置为「已启用」。"
            }
        ],
        "faqTips": "彻底解决 DNS 泄漏不仅关乎上网隐私安全，也是流畅解锁 Netflix 与 ChatGPT 防止被标记为国内用户的关键一步。",
        "relatedSlugs": ["ipv6-bypass-leak-proxy", "clash-tun-fake-ip-vs-redir-host"]
    },
    {
        "id": "faq-36",
        "slug": "ipv6-bypass-leak-proxy",
        "title": "IPv6 导致流量绕过代理直连甚至真实 IP 暴露修复指南",
        "category": "connection",
        "categoryLabel": "网络连接报错",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "国内光猫普遍开通 IPv6 后，境外支持 IPv6 的网站绕过客户端代理直连撞墙或泄露国内原生地址的防护。",
        "symptoms": [
            "访问 ipleak.net 时，IPv4 显示为香港/美国代理 IP，而下面的 IPv6 赫然显示出本地联通/电信的原生 IPv6 地址",
            "访问支持双栈的海外网站（如 Google、YouTube）极其缓慢甚至提示无法访问",
            "流媒体平台判定用户在中国大陆并拒绝播放"
        ],
        "rootCauses": [
            "大多数机场节点只提供纯 IPv4 出口，未对 IPv6 流量进行封装与路由转发",
            "Windows 默认优先走 IPv6 路由直连，流量根本没有进入 Clash 的代理通道"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：在 Clash 客户端设置中全局禁用 IPv6 解析",
                "detail": "进入 Clash Verge Rev 设置 -> 在「通用设置」或「DNS 设置」中，确保「IPv6」总开关处于关闭状态，强制所有域名只返回 A 记录走 IPv4 代理。"
            },
            {
                "stepTitle": "步骤 2：在电脑物理网卡属性中取消勾选 IPv6 协议（最稳妥）",
                "detail": "按 Win + R 运行 ncpa.cpl，右键当前正在使用的以太网或 Wi-Fi 网卡 ->「属性」-> 在列表中取消勾选「Internet 协议版本 6 (TCP/IPv6)」并点击确定。"
            }
        ],
        "faqTips": "对于日常科学上网，关闭本地 IPv6 不会对正常上网产生任何负面影响，反而能避开大量的路由泄漏与 CDN 识别坑。",
        "relatedSlugs": ["dns-leak-detection-fix", "chatgpt-access-denied-error-1020"]
    },
    {
        "id": "faq-37",
        "slug": "error-connect-exceeded-deadline",
        "title": "Clash 日志提示「connect: context deadline exceeded」排查方案",
        "category": "connection",
        "categoryLabel": "网络连接报错",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "客户端在建立 TCP 连接时超过了设定的最大等待超时时间的原因排查。",
        "symptoms": [
            "日志频繁显示：dial tcp xxx: connect: context deadline exceeded",
            "网页一直在转菊花，直到几十秒后才报错断开",
            "特定节点在测速时直接被判定为超时丢弃"
        ],
        "rootCauses": [
            "客户端到机场入口服务器之间的物理网络丢包率极高，SYN 握手包多次重发无果",
            "机场对应的入口 IP 遭到 DDOS 攻击或当地机房正在维护",
            "本地路由器的 MTU 设置过小或 MSS 协商异常"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：在客户端切换不同的入口线路",
                "detail": "选择标有不同入口（例如 广移、沪联、京德）的节点，避开当前发生故障的单点入口机房。"
            },
            {
                "stepTitle": "步骤 2：排查本地宽带物理丢包",
                "detail": "打开 CMD，运行 ping 223.5.5.5 -t，观察连续 20 个数据包是否有规律性丢包；若丢包严重，可尝试重启家用光猫重新分配公网 IP。"
            }
        ],
        "faqTips": "deadline exceeded 本质上就是建立连接超时，多属于中间网络运营商物理链路故障或入口机房受攻击。",
        "relatedSlugs": ["error-dial-tcp-timeout-10000ms", "error-tls-handshake-timeout"]
    },
    {
        "id": "faq-38",
        "slug": "error-cipher-not-supported",
        "title": "Shadowsocks 加密方式不被内核支持（如 chacha20 报错）处理",
        "category": "connection",
        "categoryLabel": "网络连接报错",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "老旧机场使用已被弃用的旧加密方式或客户端内核不兼容导致节点无法加载的解决。",
        "symptoms": [
            "启动核心提示：cipher [xxx] is not supported",
            "导入订阅后部分特定节点被标记为 invalid 并自动隐藏",
            "连接时提示 unsupported encryption method"
        ],
        "rootCauses": [
            "老旧的 Shadowsocks 流密码（如 chacha20、rc4-md5、aes-256-cfb）因不具备 AEAD 认证防篡改能力，已被现代 Mihomo/Xray 内核安全机制弃用",
            "节点配置字段名称混淆拼写错误"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：切换为兼容老旧协议的专用内核",
                "detail": "在客户端内核管理中临时切换为 Clash 原生兼容核心，或者使用 v2rayN 作为应急过渡。"
            },
            {
                "stepTitle": "步骤 2：建议升级更换采用现代 AEAD 协议的优质机场",
                "detail": "现代主流机场已全面采用 aes-256-gcm、2022-blake3-aes-128-gcm 或 Vless-Reality 等全新安全协议，彻底淘汰了不安全的明文流密码。"
            }
        ],
        "faqTips": "坚持使用已被破译特征的旧加密方式不仅连接极不稳定，更容易被防火墙针对性识别断流。",
        "relatedSlugs": ["shadowsocks-vs-trojan-vs-vless", "shadowsocks-2022-specification-upgrade"]
    },
    {
        "id": "faq-39",
        "slug": "error-udp-nat-symmetric-restricted",
        "title": "节点 UDP 变 Restricted 导致外服联机打游戏卡死的排错对策",
        "category": "connection",
        "categoryLabel": "网络连接报错",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "主机与 PC 玩家使用代理加速外服游戏时，NAT 类型显示为严格或对称型导致搜不到房间的排查指南。",
        "symptoms": [
            "Switch 或 PS5 网络测试显示 NAT 类型为 NAT-D / NAT-F 或 严格 (Strict)",
            "Apex Legends、使命召唤或怪物猎人联机经常掉线、无法加入好友队伍",
            "游戏中开启麦克风语音聊天没有任何声音"
        ],
        "rootCauses": [
            "所选机场节点本身未开启 Full Cone NAT 支持，或其服务端禁用了 UDP 流量转发",
            "客户端开启了系统代理，但游戏流量直接走底层的原始 Socket 无法被 HTTP 代理截获"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：使用客户端自带的 NAT 类型检测工具筛选节点",
                "detail": "在节点列表中挑选标有「游戏专线」、「Full Cone」或「游戏加速」的节点，这些节点通常配置了独立公网出口与 Cone NAT 支持。"
            },
            {
                "stepTitle": "步骤 2：必须在客户端开启「TUN 模式」",
                "detail": "普通系统代理只支持 TCP 网页流量，游戏联机必须在 Clash Verge Rev 中开启「TUN 模式」，接管完整的 UDP 握手数据包。"
            }
        ],
        "faqTips": "对游戏联机有高要求的玩家，强烈建议使用灵动云等带有极低延迟香港/日本游戏物理专线的节点。",
        "relatedSlugs": ["full-cone-nat-type-for-gaming", "lan-share-proxy-switch-ps5-xbox"]
    },
    {
        "id": "faq-40",
        "slug": "error-remote-host-closed-connection",
        "title": "远程服务器主动关闭连接排错与节点被阻断状态诊断",
        "category": "connection",
        "categoryLabel": "网络连接报错",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "客户端频繁提示 remote host closed connection 导致下载与播放频繁卡死的分析与解决。",
        "symptoms": [
            "正在浏览网页突然提示连接已由远程主机关闭",
            "测速软件刚跑到峰值瞬间掉零",
            "客户端日志提示 connection reset by foreign host"
        ],
        "rootCauses": [
            "目标海外服务器的防火墙检测到来自该机场出口 IP 的并发连接数异常（例如短时间内数百个并发爬虫），触发了限频防御",
            "中间防火墙检测到了异常阻断特征，在半路上阻断了 TCP 握手"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：更换机场的其他国家或冷门备用节点",
                "detail": "香港和美西的 01 号热门节点往往聚集了海量用户，容易触发海外服务器风控；改选日本 02 或新加坡节点体验通常更好。"
            },
            {
                "stepTitle": "步骤 2：调低本地下载软件的最大并发线程数",
                "detail": "使用 IDM 或多线程下载工具时，将线程数从 32 调低至 8，避免被海外服务端防刷系统误判封锁。"
            }
        ],
        "faqTips": "避开人满为患的第一位主力节点是每个科学上网老玩家的日常经验秘诀。",
        "relatedSlugs": ["error-connection-reset-by-peer", "error-eof-proxy-closed"]
    },
    {
        "id": "faq-41",
        "slug": "error-too-many-open-files-ulimit",
        "title": "高并发下载时报错「too many open files」系统句柄上限解决",
        "category": "connection",
        "categoryLabel": "网络连接报错",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "在 macOS / Linux 桌面或软路由上高并发跑外网下载时，Clash 核心崩溃或提示文件描述符超限的解决。",
        "symptoms": [
            "打开多个网页或使用下载工具时，Clash 突然停止响应",
            "终端控制台报错：socket: too many open files",
            "新的网络请求全部被挂起无法建立连接"
        ],
        "rootCauses": [
            "macOS 或 Linux 系统默认的单个进程允许打开的文件描述符 (ulimit -n) 限制较低（通常为 256 或 1024），在高并发代理下迅速耗尽"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：在终端临时调高当前环境的 ulimit 上限",
                "detail": "运行 ulimit -n 65535 将文件句柄上限放大到 65535。",
                "code": "ulimit -n 65535"
            },
            {
                "stepTitle": "步骤 2：永久修改系统配置文件",
                "detail": "在 /etc/security/limits.conf 文件中追加 soft nofile 65535 和 hard nofile 65535 永久生效。"
            }
        ],
        "faqTips": "Windows 系统的句柄管理机制不同，通常极少遇到该报错，该问题多发生在 macOS 开发者或 Linux/软路由用户身上。",
        "relatedSlugs": ["openwrt-openclash-double-routing-crash", "linux-desktop-system-wide-proxy-clash"]
    },
    {
        "id": "faq-42",
        "slug": "error-sni-mismatch-tls",
        "title": "TLS SNI 与伪装域名不一致导致握手被拒绝排查",
        "category": "connection",
        "categoryLabel": "网络连接报错",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "分析节点配置中的 SNI (Server Name Indication) 字段与真实证书证书名不符导致的连接阻断。",
        "symptoms": [
            "提示 tls: bad certificate 或 remote certificate is invalid for given name",
            "修改了订阅中的节点名称后无法连通",
            "自建节点或手动修改配置后无法上网"
        ],
        "rootCauses": [
            "客户端发送的 Client Hello 中的 SNI 扩展名与服务端 Nginx 绑定的 SSL 证书 Common Name 不匹配"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：更新官方原生订阅，勿手动修改 sni 属性",
                "detail": "直接拉取机场后台的原始配置，不要擅自修改 node-options 中的 sni 或 servername 字段。"
            },
            {
                "stepTitle": "步骤 2：开启 skip-cert-verify 作为临时排查验证",
                "detail": "临时开启 skip-cert-verify: true 验证是否确由证书域名校验引起。"
            }
        ],
        "faqTips": "正确的 SNI 是现代 TLS 伪装能在大流量特征审查下安全存活的关键所在。",
        "relatedSlugs": ["error-tls-handshake-timeout", "vless-reality-anti-censorship-how-it-works"]
    },
    {
        "id": "faq-43",
        "slug": "error-proxy-authentication-required-407",
        "title": "提示 HTTP 407 Proxy Authentication Required 认证失败解决",
        "category": "connection",
        "categoryLabel": "网络连接报错",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "浏览器打开外网网页弹出登录窗口要求输入代理用户名密码，或报 407 错误的处理全解。",
        "symptoms": [
            "浏览器弹出弹窗：「代理服务器需要用户名和密码」",
            "网页提示 HTTP Error 407: Proxy Authentication Required",
            "无法跳过登录窗口直接上网"
        ],
        "rootCauses": [
            "本地客户端开启了混合端口认证功能，并设置了自定义的账号密码",
            "局域网内部署了企业级上网行为审计代理，强行插入了二次认证"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：在 Clash 设置中清空或重置混合端口认证",
                "detail": "进入 Clash Verge Rev 设置 ->「代理设置」，检查「认证 (Authentication)」项是否填写了内容，将其清空并保存即可免密使用。"
            },
            {
                "stepTitle": "步骤 2：检查系统环境变量中的 http_proxy",
                "detail": "检查环境变量中是否残留了带有旧账密的代理变量（如 http://user:pass@127.0.0.1:7890），将其修正或删除。"
            }
        ],
        "faqTips": "个人电脑使用本地代理完全不需要设置认证，保持默认的无密码模式体验最顺畅。",
        "relatedSlugs": ["clash-verge-mixed-port-conflict", "curl-wget-terminal-proxy-environment"]
    },
    {
        "id": "faq-44",
        "slug": "error-trojan-password-hash-mismatch",
        "title": "Trojan 密码哈希不匹配或 TLS ALPN 协商失败排查",
        "category": "connection",
        "categoryLabel": "网络连接报错",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "针对 Trojan 协议节点连接时提示 password authentication failed 或 ALPN 握手失败的对策。",
        "symptoms": [
            "客户端日志显示：[Trojan] authenticate failed: invalid password hash",
            "Trojan 节点延迟测速正常，但实际收发流量均为 0",
            "TLS 握手阶段提示 no application protocol negotiated"
        ],
        "rootCauses": [
            "密码字符串中包含未正确转义的特殊符号，导致计算 SHA224 哈希值出现偏差",
            "客户端 ALPN 配置强制指定为 h2，而服务端仅配置了 http/1.1 支持"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：直接通过订阅链接全量导入，切勿手工抄写密码",
                "detail": "Trojan 采用 SHA224 算法将密码转为 56 位十六进制摘要，手动复制极易遗漏字符，务必使用机场一键订阅导入。"
            },
            {
                "stepTitle": "步骤 2：在节点配置中允许默认 ALPN 协商",
                "detail": "配置中的 alpn 字段建议同时包含 [\"h2\", \"http/1.1\"]，让客户端与服务端自适应协商最快协议。"
            }
        ],
        "faqTips": "Trojan 协议对标准 HTTPS 模拟非常逼真，配置严谨度极高，必须严格对齐服务端参数。",
        "relatedSlugs": ["shadowsocks-vs-trojan-vs-vless", "error-tls-handshake-timeout"]
    },
    {
        "id": "faq-45",
        "slug": "error-clock-skew-system-time",
        "title": "系统时间与网络时间误差超过 90 秒导致 VMess 彻底断连深度剖析",
        "category": "connection",
        "categoryLabel": "网络连接报错",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "详解为什么电脑或手机时间不准会导致科学上网全军覆没的底层安全密码学机制与秒级自愈。",
        "symptoms": [
            "明明网络正常、订阅也是最新购买的，所有 VMess 节点连上全部超时打不开网页",
            "日志显示：Invalid user request / timestamp expired",
            "修改完主板电池或跨时区后突然所有节点断网"
        ],
        "rootCauses": [
            "VMess 协议为了抵御重放攻击 (Replay Attack)，在客户端与服务端之间严格强制校验动态时间戳。协议规定：若双方时间误差绝对值超过 90 秒，服务器将直接静默丢弃所有认证包，视同伪造黑客攻击！"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：在系统设置中启用「自动设置时间」并立即同步",
                "detail": "无论是 Windows、macOS 还是手机，必须在系统设置中将「自动设置时间」开启，并点击「立即同步」。",
                "code": "# Windows PowerShell 管理员强制同步时间命令\nw32tm /resync"
            },
            {
                "stepTitle": "步骤 2：切换为对时间无死板要求的 Vless-Reality 或 Hysteria 2 协议",
                "detail": "新一代协议已经淘汰了脆弱的时间戳强校验机制，改用现代非对称加密证书握手，对时间轻微误差更加包容稳定。"
            }
        ],
        "faqTips": "记住这个黄金铁律：只要发现全部节点突然毫无征兆一起超时，90% 都是系统时间偏差导致的，对时后瞬间满血复活！",
        "relatedSlugs": ["error-tls-handshake-timeout", "error-dial-tcp-timeout-10000ms"]
    },
    {
        "id": "faq-46",
        "slug": "error-routing-loop-detected",
        "title": "Clash 日志提示「routing loop detected」死循环回环阻断排错",
        "category": "connection",
        "categoryLabel": "网络连接报错",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "开启 TUN 模式或自建网关时流量陷入死循环自我回环导致机器直接断网的处理。",
        "symptoms": [
            "日志疯狂刷屏：routing loop detected, packet dropped",
            "开启 TUN 瞬间整机断网，CPU 占用率飙升到 100%",
            "客户端频繁弹窗提示核心已紧急停止"
        ],
        "rootCauses": [
            "TUN 模式将整机默认网关重定向到了 Clash 虚拟网卡，而发往机场服务器节点的出站流量本身未被排除在 TUN 之外，导致节点通信流量又被捕获进了 TUN，形成无限套娃死循环！"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：在 TUN 配置中正确开启 auto-route 与严格路由",
                "detail": "使用 Mihomo 官方推荐的 TUN 标准配置，内核会自动将机场服务器 IP 加入系统物理网卡的直连旁路名单中。"
            },
            {
                "stepTitle": "步骤 2：检查自定义规则是否将代理服务器本身指向了 PROXY",
                "detail": "检查 rules 规则，确保没有把机场节点的域名或 IP 错误地写成走 PROXY 策略，节点域名必须直连。"
            }
        ],
        "faqTips": "TUN 模式通过虚拟网卡接管底层，配置路由表时切忌手动胡乱修改系统默认网关跃点数。",
        "relatedSlugs": ["clash-tun-mode-virtual-nic-fail", "openwrt-openclash-double-routing-crash"]
    },
    {
        "id": "faq-47",
        "slug": "error-stun-test-failed",
        "title": "STUN 测试失败导致无法穿透 P2P 与海外语音通话掉线排错",
        "category": "connection",
        "categoryLabel": "网络连接报错",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "针对使用 Discord、Telegram 语音或打外服游戏时频繁掉线、STUN 测试超时的应对方案。",
        "symptoms": [
            "Discord 语音频道一直显示「RTC Connecting」或「No Route」进不去频道",
            "P2P 联机游戏无法穿透好友房主内网",
            "STUN 测试客户端报告 NAT Mapping Failure"
        ],
        "rootCauses": [
            "节点禁用了 UDP 或者经过了多层对称式 NAT 转化，阻断了 STUN 探测响应",
            "分流规则中未将 Discord 的语音媒体服务器网段加入代理策略"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：开启 Clash 的 UDP 转发总开关",
                "detail": "在客户端配置的对应节点属性中，确保 udp: true 处于开启状态。"
            },
            {
                "stepTitle": "步骤 2：在分流规则中添加专门的 Discord 与 WebRTC 规则",
                "detail": "确保使用的分流规则库包含最新的 Discord 与 Google STUN (stun.l.google.com) 专用规则。"
            }
        ],
        "faqTips": "对于语音开黑玩家，建议优先选用具备 Full Cone NAT 属性的高端专线节点以获得最流畅通话体验。",
        "relatedSlugs": ["error-udp-nat-symmetric-restricted", "full-cone-nat-type-for-gaming"]
    },
    {
        "id": "faq-48",
        "slug": "error-mtu-packet-fragmentation",
        "title": "MTU 过大引起分片丢包导致的网页加载白屏与排查指南",
        "category": "connection",
        "categoryLabel": "网络连接报错",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "解决特定网络环境下网页只能加载前半部分、上传附件中断的 MTU 路径最大传输单元适配问题。",
        "symptoms": [
            "微信能发文字但发不出图片",
            "访问轻量级文字页面很快，一旦访问大图片网页就无限加载甚至白屏",
            "网络测速上传几乎为 0"
        ],
        "rootCauses": [
            "物理宽带是 PPPoE 拨号（基础 MTU 为 1492），代理协议再包裹一层 50~100 字节的隧道包头后，总报文超过 1500 字节，在途中被不可分片标志 (DF) 路由器直接丢弃！"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：使用 ping 测试找到本地无丢包的最大 MTU",
                "detail": "在 CMD 中执行 ping -f -l 1400 www.baidu.com，如果提示需要拆分，则逐步调小数字，直到不提示拆分且不丢包为止。",
                "code": "ping -f -l 1400 www.baidu.com"
            },
            {
                "stepTitle": "步骤 2：在客户端 TUN 设置中将 MTU 调整为安全值 1360~1400",
                "detail": "在 Clash 或 Sing-box 的 TUN 配置中指定 mtu: 1380，彻底消除链路分片丢包现象。"
            }
        ],
        "faqTips": "适当降低 MTU 虽然会牺牲微小的报文有效载荷比例，但换来的是极端复杂的公网链路下绝不卡死、永不断流的稳定性。",
        "relatedSlugs": ["sing-box-inbound-tun-mtu", "error-tls-handshake-timeout"]
    },
    {
        "id": "faq-49",
        "slug": "error-tcp-rst-injection-gfw",
        "title": "遇到 GFW TCP RST 报文注入伪装阻断的深度识别与规避方案",
        "category": "connection",
        "categoryLabel": "网络连接报错",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "揭秘国家防火墙旁路监听机制如何通过伪造 TCP RST 重置包实施阻断，以及专线如何实现物理免疫。",
        "symptoms": [
            "访问特定未被完全封 IP 的海外网站，初次连接正常，浏览 2 秒后突然中断",
            "Wireshark 抓包可以看到连续收到多个 TTL 跳数异常的 RST 标志数据包",
            "随后目标网站在接下来的几分钟内完全不可访问"
        ],
        "rootCauses": [
            "公网光纤经过 GFW 旁路监听设备时，检测到了未加密的 HTTP 敏感词或明文 TLS SNI，GFW 会迅速向通信两端伪造发送 TCP RST 报文，强行掐断正在建立的连接"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：全量流量必须在离开本地电脑前完成高强度加密",
                "detail": "确保客户端规则分流完善，凡是海外未备案网站一律走代理节点出境，本地发出的每一个数据包都处于 Shadowsocks/Trojan 的强加密保护之下。"
            },
            {
                "stepTitle": "步骤 2：选用 IPLC/IEPL 国际专线从物理层规避",
                "detail": "IPLC/IEPL 走的是国内运营商向香港/日本铺设的物理内网专线光纤，在物理链路上根本不接入 GFW 审查机房，从源头彻底消除了 RST 注入风险。"
            }
        ],
        "faqTips": "直连翻墙在当今环境下几乎是百分之百会被 RST 注入阻断的，规范的专线架构是长期稳定翻墙的唯一解。",
        "relatedSlugs": ["error-connection-reset-by-peer", "iplc-vs-iepl-technical-difference"]
    },
    {
        "id": "faq-50",
        "slug": "error-quic-blocked-fallback-tcp",
        "title": "浏览器 QUIC (HTTP/3) 协议被阻断导致网页卡死终极优化",
        "category": "connection",
        "categoryLabel": "网络连接报错",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "解决 Chrome / Edge 访问 YouTube 或 Google 默认使用 QUIC (UDP 443) 遭遇运营商阻断卡顿的问题。",
        "symptoms": [
            "Chrome 访问 YouTube 首页加载速度极慢，但一旦刷新几次换成普通 TCP 又变快",
            "控制台网络面板显示协议为 h3 或 quic 时速度极慢",
            "视频经常在刚播放 5 秒后严重卡顿"
        ],
        "rootCauses": [
            "Google 大量服务默认启用基于 UDP 的 HTTP/3 (QUIC) 协议，而国内运营商对境外 443 端口 UDP 流量进行无差别限速或丢包"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：在 Chrome / Edge 浏览器中直接禁用 QUIC 协议",
                "detail": "在浏览器地址栏输入 chrome://flags，搜索 Experimental QUIC protocol，将其从 Default 改为「Disabled」，重启浏览器强制回退到极速的 TCP TLS 1.3 链路。"
            },
            {
                "stepTitle": "步骤 2：在 Clash 分流规则中丢弃 443 端口 UDP 流量",
                "detail": "在规则列表中添加 REJECT 规则：AND,((DST-PORT,443),(NETWORK,UDP)),REJECT，强制所有客户端自动回退到流畅的 TCP 通道。"
            }
        ],
        "faqTips": "禁用 QUIC 几乎不会影响视频画质，反而能彻底解决 UDP 劣化带来的初期缓冲假死现象。",
        "relatedSlugs": ["error-hysteria2-udp-rate-limit", "error-udp-nat-symmetric-restricted"]
    }
]

print(f"Loaded {len(CONNECTION_FAQS)} connection FAQs.")
