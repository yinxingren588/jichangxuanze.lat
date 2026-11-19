# -*- coding: utf-8 -*-
# Category 7: 底层协议与加密技术科普 (15 篇)

PROTOCOLS_FAQS = [
    {
        "id": "faq-121",
        "slug": "shadowsocks-vs-trojan-vs-vless",
        "title": "Shadowsocks、Trojan、Vless 协议本质区别与适用场景横评",
        "category": "protocols",
        "categoryLabel": "底层协议技术",
        "readTime": "6 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "从密码学原理、抗审查机制和运行性能开销，深度拆解三大主流代理协议的技术内核。",
        "symptoms": [
            "面对节点列表中琳琅满目的 SS、Trojan、Vless 协议不知道它们有什么区别",
            "不知道哪种协议在晚高峰看 4K 速度最快、延迟最低"
        ],
        "rootCauses": [
            "不同协议诞生的时代背景和设计目标不同：Shadowsocks 追求极致轻量无握手延迟；Trojan 追求完美模拟标准 HTTPS 伪装；Vless 追求轻量无状态与模块化解耦"
        ],
        "solutions": [
            {
                "stepTitle": "协议 1：Shadowsocks (SS) —— 专线环境下的性能之王",
                "detail": "设计极其纯粹，没有复杂的多层包装，直接采用高效的对称加密（如 AEAD-2022 / AES-128-GCM）。在走内网 IPLC 专线时，SS 的加解密开销最低、CPU 占用最小、延迟最低，是打游戏和看 4K 跑分的首选！"
            },
            {
                "stepTitle": "协议 2：Trojan —— 经典 HTTPS 伪装者",
                "detail": "直接伪装成标准的互联网 HTTPS 网页流量（监听 443 端口并配置真实 SSL 证书）。防火墙看它就像普通网购或查资料，在公网直连或普通隧道中继下具有极高的存活率。"
            },
            {
                "stepTitle": "协议 3：Vless (搭配 Reality) —— 新一代抗审查天花板",
                "detail": "本身不包含冗余加密逻辑，完全依托底层传输层（如 TLS 1.3）保障安全，结合 Reality 技术借用海外真实大厂证书，完全不需要自己申请域名，是当前公网抗阻断的最强形态。"
            }
        ],
        "faqTips": "如果你的机场走的是纯 IPLC 专线，优先选 Shadowsocks 性能最爆棚；如果走公网中继，优先选 Trojan 或 Vless。",
        "relatedSlugs": ["vless-reality-anti-censorship-how-it-works", "hysteria-2-udp-protocol-deep-dive"]
    },
    {
        "id": "faq-122",
        "slug": "hysteria-2-udp-protocol-deep-dive",
        "title": "Hysteria 2 协议为什么弱网起飞快？底层原理与劣势全方位剖析",
        "category": "protocols",
        "categoryLabel": "底层协议技术",
        "readTime": "6 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "深入解读基于魔改 QUIC / UDP 的 Hysteria 2 (歇斯底里) 协议如何在丢包 30% 环境下跑满百兆宽带的秘密。",
        "symptoms": [
            "在某些极其劣化的弱网 Wi-Fi 下，普通 TCP 节点全部断流，而 Hysteria 2 却能流畅看 1080P",
            "晚高峰个别地区运营商对 Hysteria 2 出现限速"
        ],
        "rootCauses": [
            "传统 TCP 协议遇到丢包会触发「拥塞避免机制」，自动将发送窗口减半并等待重传，导致速率暴跌；而 Hysteria 2 基于 UDP 构建，采用了专有的 Brutal 拥塞控制算法，即使公网存在 20%~30% 的丢包，依然以恒定目标速率持续发包，配合前向纠错 (FEC)，实现逆风起飞！"
        ],
        "solutions": [
            {
                "stepTitle": "优势：弱网与跨国高丢包线路的绝对救星",
                "detail": "在校园网、移动 4G/5G 弱信号、或晚高峰普通公网中继遭遇恶劣丢包时，Hysteria 2 能让网页秒开、视频无感加载。"
            },
            {
                "stepTitle": "劣势与对策：注意运营商对 UDP 的 QoS 限制",
                "detail": "部分地区运营商由于讨厌这种暴力发包行为，在晚高峰会对 UDP 实施严厉的单向限速。遇到此类情况，开启 Hysteria 2 的「端口跳跃 (Port Hopping)」或切换回 TCP IPLC 专线即可化解。"
            }
        ],
        "faqTips": "Hysteria 2 是近年来代理协议领域最具颠覆性的技术突破之一，暮光加速、微风网络等主流品牌已全面标配支持。",
        "relatedSlugs": ["error-hysteria2-udp-rate-limit", "tuic-protocol-quic-advantages"]
    },
    {
        "id": "faq-123",
        "slug": "vless-reality-anti-censorship-how-it-works",
        "title": "Vless-Reality 借用大厂证书原理：为什么它号称当前最强抗封锁",
        "category": "protocols",
        "categoryLabel": "底层协议技术",
        "readTime": "6 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "揭秘 Xray 团队创造的 Reality 协议如何彻底告别域名购买与证书申请，实现真假难辨的完美伪装。",
        "symptoms": [
            "听说 Reality 协议很强，但不知道它是如何做到不买域名、不申请证书却拥有最高等级安全加密的"
        ],
        "rootCauses": [
            "传统伪装协议（Trojan / VMess+TLS）必须由机场主购买域名并向 Let's Encrypt 申请 SSL 证书，审查系统只要顺藤摸瓜查询证书颁发历史和域名解析，就能轻易发现猫腻；而 Reality 彻底打破了这一模式。"
        ],
        "solutions": [
            {
                "stepTitle": "核心机理 1：偷天换日借用大厂真实证书 (SNI Borrowing)",
                "detail": "Reality 节点的服务端在握手时直接借用苹果 (apple.com)、微软 (microsoft.com) 或雅虎等真正全球科技巨头的正规合法证书。审查系统在探测时，拿到的就是苹果官方的真证书，完全无法封锁！"
            },
            {
                "stepTitle": "核心机理 2：独创的 ShortID 与客户端私钥身份校验",
                "detail": "只有持正确 ShortID 秘钥的真实客户端发出的请求，服务端才会接纳并解密代理流量；而如果是防火墙发出的主动嗅探探测，服务端会直接原封不动地将流量透传转发给真正的苹果官网，彻底迷惑防火墙！"
            }
        ],
        "faqTips": "Reality 真正实现了从逻辑层面免疫 GFW 的主动探测识别，是目前公网代理最先进的技术形态。",
        "relatedSlugs": ["error-502-bad-gateway-reality", "shadowsocks-vs-trojan-vs-vless"]
    },
    {
        "id": "faq-124",
        "slug": "tuic-protocol-quic-advantages",
        "title": "TUIC 协议基于标准 QUIC 的性能优势与高丢包线路测试对比",
        "category": "protocols",
        "categoryLabel": "底层协议技术",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "分析基于 IETF 标准 QUIC 协议构建的 TUIC 协议在 0-RTT 握手、多路复用与头部阻塞消除上的技术亮点。",
        "symptoms": [
            "客户端支持 TUIC 协议，想知道它与 Hysteria 2 和传统 TCP 相比有何区别"
        ],
        "rootCauses": [
            "传统 TCP 协议存在「队头阻塞 (Head-of-Line Blocking)」问题，一个数据包丢了整个连接都要停下来等待重传；而基于 QUIC 的 TUIC 在单个 UDP 连接内实现了完全独立的并发流，互不影响！"
        ],
        "solutions": [
            {
                "stepTitle": "优势 1：0-RTT 极速握手连接",
                "detail": "对于曾经建立过连接的服务端，TUIC 支持 0-RTT 直接发送应用层数据，点开网页的瞬间无需等待任何三次握手，首包延迟达到物理极限。"
            },
            {
                "stepTitle": "优势 2：天然模拟 HTTP/3 合法流量",
                "detail": "TUIC 严格遵守 IETF 官方 QUIC 规范标准，在公网线路上表现为极其标准的合规 HTTP/3 流量，比激进发包的协议更具隐蔽性。"
            }
        ],
        "faqTips": "Sing-box 核心对 TUIC 提供了原生的顶级支持，搭配优质落地机使用体验非常出色。",
        "relatedSlugs": ["hysteria-2-udp-protocol-deep-dive", "error-quic-blocked-fallback-tcp"]
    },
    {
        "id": "faq-125",
        "slug": "vmess-vs-vless-why-deprecated",
        "title": "为什么主流机场正逐步淘汰 VMess 协议？技术架构进化深度解析",
        "category": "protocols",
        "categoryLabel": "底层协议技术",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "回顾翻墙协议历史，详解为什么统治一时的 VMess 正在被更轻量安全的 Vless 全面取代。",
        "symptoms": [
            "发现新买的机场订阅里 VMess 协议越来越少，全变成了 Vless、Trojan 和 SS"
        ],
        "rootCauses": [
            "VMess 协议由 V2Ray 团队在多年前设计，为了在未加密的公网中传输，设计了复杂的对称加密与严格的时间戳机制。随着互联网全面普及 TLS 1.3，VMess 内部的重复加密造成了严重的 CPU 算力浪费，且历史实现曾出现过被学术论文披露的认证漏洞"
        ],
        "solutions": [
            {
                "stepTitle": "Vless 的革命性精简：去掉双重加密",
                "detail": "Vless (VMess Less) 顾名思义就是「去掉了多余包袱的 VMess」。它不依赖死板的 90 秒时间对齐，完全将加密工作托付给外层的标准 TLS/Reality，握手开销降低 50% 以上。"
            },
            {
                "stepTitle": "协议演进历程：SS -> VMess -> Vless/Trojan -> Reality/Hysteria2",
                "detail": "机场行业正在完成新一轮协议技术换代，逐步淘汰老旧复杂的 VMess 是提升全网并发吞吐的必然结果。"
            }
        ],
        "faqTips": "老旧客户端如果不支持 Vless，建议尽快迁移至活跃维护的 Clash Verge Rev 或 Sing-box。",
        "relatedSlugs": ["error-clock-skew-system-time", "shadowsocks-vs-trojan-vs-vless"]
    },
    {
        "id": "faq-126",
        "slug": "gfw-sni-blocking-and-ech-solution",
        "title": "什么是 SNI 阻断？ECH (Encrypted Client Hello) 如何对抗审查机制",
        "category": "protocols",
        "categoryLabel": "底层协议技术",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "科普现代网络审查的核心杀手锏「SNI 嗅探阻断」原理，以及下一代技术 ECH 的抗审查曙光。",
        "symptoms": [
            "访问部分未完全被封锁 IP 的网站，刚发起 HTTPS 握手瞬间就被直接切断"
        ],
        "rootCauses": [
            "在标准 HTTPS TLS 握手最开始的 Client Hello 阶段，客户端必须发送 SNI (Server Name Indication) 告诉服务器自己要访问哪个域名。这一步在传统 TLS 1.3 中是完全「明文」的！GFW 只要在主干网嗅探到包含 youtube.com 等明文字符，立刻发送 RST 实施阻断！"
        ],
        "solutions": [
            {
                "stepTitle": "当前解决方案：代理协议在本地先进行全套加密封装",
                "detail": "客户端通过 Shadowsocks/Vless 将整个 TLS 握手包整体作为内层载荷加密后再发给境外节点，GFW 看到的只是一串随机乱码，根本看不到里面的真实 SNI。"
            },
            {
                "stepTitle": "未来终极方案：ECH (加密客户端问候) 协议原生普及",
                "detail": "IETF 推动的 ECH 标准通过将初始 SNI 利用公钥在 DNS 层完成预加密，未来即使不通过代理，明文阻断也将彻底成为历史。"
            }
        ],
        "faqTips": "这也是为什么单纯修改电脑 DNS 并不能真正翻墙的原因，因为哪怕 DNS 没被污染，随后的明文 SNI 握手依然会被 GFW 当场抓获。",
        "relatedSlugs": ["error-sni-mismatch-tls", "error-tcp-rst-injection-gfw"]
    },
    {
        "id": "faq-127",
        "slug": "tcp-bbr-congestion-control-speedup",
        "title": "Linux 拥塞控制算法 BBR 对外网翻墙测速的显著加速效果原理",
        "category": "protocols",
        "categoryLabel": "底层协议技术",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "Google 研发的 BBR 拥塞控制算法如何将跨国高丢包、高延迟长肥管道的下载速度提升数倍。",
        "symptoms": [
            "同一个节点在开启 BBR 加速后，YouTube 4K 播放跑分直接从 20,000 Kbps 飙升到 150,000+ Kbps"
        ],
        "rootCauses": [
            "传统的 CUBIC 算法将「数据包丢失」作为网络拥塞的唯一信号，一旦公网出现轻微物理丢包，CUBIC 会立刻主动大幅降低发包速度；而跨国公网丢包通常只是路由抖动而非真正信道拥塞，导致传统算法永远跑不满带宽！"
        ],
        "solutions": [
            {
                "stepTitle": "BBR 原理：基于最大带宽 (BtlBw) 和最小延迟 (RTprop) 建模",
                "detail": "Google BBR 不再盲目将丢包视为拥塞，而是通过测量实际传输带宽与往返延迟，精准计算出管道的最大承载能力，以物理极限速率持续灌满链路！"
            },
            {
                "stepTitle": "优秀机场标配：全节点内核开启 BBRv3 / BBRplus",
                "detail": "正规专业机场的每一台中继与落地服务器，都在底层 Linux 内核中默认编译启用了 BBR 算法，这也是其在晚高峰依然能输出数百兆速率的核心秘诀之一。"
            }
        ],
        "faqTips": "如果自己有海外 VPS，在终端运行一行命令开启 BBR 是提升网络速度最简单有效的方法。",
        "relatedSlugs": ["hysteria-2-udp-protocol-deep-dive", "error-connection-reset-by-peer"]
    },
    {
        "id": "faq-128",
        "slug": "websocket-vs-grpc-transport-layer",
        "title": "WebSocket、gRPC 与 HTTP/2 底层传输层性能深度对比",
        "category": "protocols",
        "categoryLabel": "底层协议技术",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "梳理主流代理协议常见的传输层载体优劣，在 CDN 穿透与极致性能之间找到最佳平衡。",
        "symptoms": [
            "配置节点时在 WS、gRPC、TCP 传输协议之间纠结不知道哪个性能更好"
        ],
        "rootCauses": [
            "不同的传输协议设计初衷不同：WebSocket 兼容所有标准 Web 反向代理与 CDN；gRPC 采用 HTTP/2 多路复用和 Protobuf 二进制序列化，多并发下延迟更低"
        ],
        "solutions": [
            {
                "stepTitle": "对比 1：纯 TCP / RAW —— 性能最高、延迟最低（专线首选）",
                "detail": "没有任何多余的中间封装协议，数据直接通过原生 TCP Socket 发送，开销为 0。在 IPLC 专线中 100% 推荐使用纯 TCP。"
            },
            {
                "stepTitle": "对比 2：gRPC —— 多并发长连接性能卓越",
                "detail": "基于 HTTP/2 实现，单个 TCP 连接内可以并发传输几百个子流，在大规模高并发网页请求时抗丢包和性能明显优于老旧的 WebSocket。"
            },
            {
                "stepTitle": "对比 3：WebSocket (WS) —— CDN 穿透兼容性最强",
                "detail": "唯一的不可替代价值在于完美兼容 Cloudflare 等几乎所有主流 CDN 平台的免费反代与 WebSocket 升级转发，适合极端防封锁备用。"
            }
        ],
        "faqTips": "追求极致测速选 TCP/RAW；追求多路复用选 gRPC；追求走免费 CDN 优选 IP 救砖选 WS。",
        "relatedSlugs": ["error-ws-bad-handshake-403", "vless-reality-anti-censorship-how-it-works"]
    },
    {
        "id": "faq-129",
        "slug": "iplc-vs-iepl-technical-difference",
        "title": "IPLC 国际专线与 IEPL 国际以太网专线的真正技术差异与成本真相",
        "category": "protocols",
        "categoryLabel": "底层协议技术",
        "readTime": "6 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "揭开机场宣传中最常出现的两个核心技术名词神秘面纱，为什么专线能够真正做到「永不被墙」。",
        "symptoms": [
            "看到机场宣传「全节点 IPLC 物理专线」或「金融级 IEPL 内网专线」不明白具体区别"
        ],
        "rootCauses": [
            "二者在底层电信运营商的实现协议层级不同：IPLC (International Private Leased Circuit) 是二层/三层物理专租线路；IEPL (International Ethernet Private Line) 是基于以太网标准的点对点专线"
        ],
        "solutions": [
            {
                "stepTitle": "共同特质（核心价值）：完全不经过 GFW 国家防火墙！",
                "detail": "不管是 IPLC 还是 IEPL，都是企业向中国电信/联通/移动直接租用的物理级跨境专网光纤。数据从深圳/上海的内网机房直接直通香港/日本内网机房，根本不接入公共互联网国际出口，物理上完美绕开 GFW！"
            },
            {
                "stepTitle": "细微差别：IEPL 组网更灵活、抖动更低",
                "detail": "IEPL 基于现代以太网封装，延展性更好、网络延迟抖动更加平滑（通常低于 1ms），常见于对时延要求苛刻的跨国金融证券交易；IPLC 则更老牌成熟。"
            },
            {
                "stepTitle": "成本真相：高昂带宽决定了它不可能白菜价",
                "detail": "真正的 IPLC/IEPL 带宽成本是普通公网 VPS 的数十倍，认准隐形人、大佬云这类真专线品牌，切勿轻信几块钱的假虚标专线。"
            }
        ],
        "faqTips": "只要是真正的物理专线，敏感时期完全就是平时状态，完全感受不到任何封锁波动。",
        "relatedSlugs": ["bgp-multi-line-tunnel-relay-explained", "why-never-buy-multi-year-package"]
    },
    {
        "id": "faq-130",
        "slug": "bgp-multi-line-tunnel-relay-explained",
        "title": "BGP 隧道中继为什么能降低晚高峰丢包？入口与出口架构原理解密",
        "category": "protocols",
        "categoryLabel": "底层协议技术",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "剖析主流中高端机场普遍采用的「国内多入口 BGP 智能分流 + 境外落地机」双层架构优势。",
        "symptoms": [
            "好奇为什么普通直连节点一到晚高峰直接死翘翘，而经过 BGP 隧道中转的节点依然能跑 500M"
        ],
        "rootCauses": [
            "国内普通宽带（尤其是移动和广电）直接访问境外服务器必须经过极其拥挤的公网国际出口关口局；而 BGP 中继架构彻底改变了数据路由拓扑"
        ],
        "solutions": [
            {
                "stepTitle": "第一步：国内 BGP 多线秒级接入 (用户 -> 机场国内入口)",
                "detail": "你的电信/联通/移动流量首先连接到机场部署在广州、上海或北京的国内高防机房。机房拥有 BGP 动态路由，三网直连延迟极低（通常只有 10~25ms），完全不丢包！"
            },
            {
                "stepTitle": "第二步：专线/隧道极速出境 (机场国内入口 -> 境外落地机)",
                "detail": "国内机房收到流量后，通过内部专线或优质大带宽隧道直接将数据运送到香港或日本落地机，随后在境外当地公网完成目标网站访问并原路回传。"
            }
        ],
        "faqTips": "BGP 入口就像高铁专用通道，将最容易丢包的「跨境出境段」交由企业级专线代劳，体验当然天差地别。",
        "relatedSlugs": ["iplc-vs-iepl-technical-difference", "anycast-routing-in-airport-nodes"]
    },
    {
        "id": "faq-131",
        "slug": "anycast-routing-in-airport-nodes",
        "title": "Anycast 广播路由在机场智能分流中的应用与超低就近接入优势",
        "category": "protocols",
        "categoryLabel": "底层协议技术",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "科普大型高阶机场如何利用 Anycast 技术实现全国各地用户自动连入离自己物理距离最近的入口机房。",
        "symptoms": [
            "不管身在广东、北京还是四川，连接同一个订阅节点名称，测速延迟都奇迹般地保持在 20ms 以内"
        ],
        "rootCauses": [
            "Anycast（任播）技术：多个分布在不同地理位置的服务器机房对外广播完全相同的同一个 IP 地址，互联网底层路由器会根据 BGP 路由表自动将用户的流量导向物理跳数最短、网络质量最佳的最近机房！"
        ],
        "solutions": [
            {
                "stepTitle": "优势 1：全国就近接入，免除手动挑选入口的烦恼",
                "detail": "南方用户自动进入广州机房，北方用户自动进入北京机房，华东用户自动进入上海机房，省去在节点列表中手动翻找「广移/沪联」的繁琐。"
            },
            {
                "stepTitle": "优势 2：毫秒级自动故障容灾转移",
                "detail": "当某一个入口机房因突发故障离线时，全球 BGP 路由会自动在几秒钟内将后续流量无感切换到邻近的健康机房，用户甚至感觉不到任何掉线。"
            }
        ],
        "faqTips": "具备 Anycast 入口调度能力的机场（如闪跃、飞V）在架构成熟度与抗灾容灾能力上均处于行业第一梯队。",
        "relatedSlugs": ["bgp-multi-line-tunnel-relay-explained", "iplc-vs-iepl-technical-difference"]
    },
    {
        "id": "faq-132",
        "slug": "full-cone-nat-type-for-gaming",
        "title": "NAT 1 (Full Cone) 对主机联机与 P2P 下载的关键作用及测试方法",
        "category": "protocols",
        "categoryLabel": "底层协议技术",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "主机与 PC 玩家为什么一定要认准带有 Full Cone NAT 属性的节点才能畅快联机对战。",
        "symptoms": [
            "打外服使命召唤搜不到人，联机提示 NAT 严格 (Strict)",
            "任天堂 Switch 联机报错代码 2618-0516 无法加入对局"
        ],
        "rootCauses": [
            "NAT 类型从好到差分为 4 类：NAT 1 (全锥型 Full Cone)、NAT 2 (受限锥型)、NAT 3 (端口受限)、NAT 4 (对称型)。主机联机和语音通话要求客户端之间必须能够互相直接打洞穿透，如果代理节点是对称型 NAT，穿透率几乎为 0！"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：使用 NatTypeTester 工具检测当前节点 NAT 类型",
                "detail": "在开启代理的状态下运行开源小工具 NatTypeTester。如果结果显示为「FullCone」即为完美状态；若显示「SymmetricNAT」则代表该节点不适合用于游戏联机。"
            },
            {
                "stepTitle": "步骤 2：在客户端开启 UDP 转发并选择游戏专线",
                "detail": "确保节点配置中开启了 udp: true，并选择带有「游戏专线」、「全锥形」标识的优质节点。"
            }
        ],
        "faqTips": "真正的游戏专线不仅看 Ping 延迟高低，NAT 类型是否为 Full Cone 更是决定能否顺利进房间的关键基石。",
        "relatedSlugs": ["error-udp-nat-symmetric-restricted", "lan-share-proxy-switch-ps5-xbox"]
    },
    {
        "id": "faq-133",
        "slug": "dns-over-https-doh-vs-dot-clash",
        "title": "DoH (DNS over HTTPS) 与 DoT 在防劫持中的实战配置指南",
        "category": "protocols",
        "categoryLabel": "底层协议技术",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "掌握加密 DNS 协议技术，彻底杜绝本地运营商 HTTP 劫持、弹窗广告与 DNS 污染。",
        "symptoms": [
            "访问某些正常网页经常莫名其妙弹出右下角运营商推送的宽带广告",
            "境外冷门网站被解析到了 127.0.0.1 反诈黑洞 IP"
        ],
        "rootCauses": [
            "传统的 DNS 查询基于明文 UDP 53 端口传输，中间网络设备不仅可以随时窥探你在访问什么网站，还可以肆无忌惮地篡改解析返回结果"
        ],
        "solutions": [
            {
                "stepTitle": "技术方案：升级为经过 TLS 加密的 DoH (443端口)",
                "detail": "DNS over HTTPS 将 DNS 查询打包在标准 HTTPS 报文中，伪装成普通网页访问，外界完全无法窃听或篡改解析内容。"
            },
            {
                "stepTitle": "在 Clash 配置中配置国内外分离的加密 DoH 上游",
                "detail": "国内域名使用阿里/腾讯 DoH，海外域名使用 Cloudflare/Google DoH：",
                "code": "dns:\n  enable: true\n  nameserver:\n    - https://dns.alidns.com/dns-query\n    - https://doh.pub/dns-query\n  fallback:\n    - https://1.1.1.1/dns-query\n    - https://8.8.8.8/dns-query"
            }
        ],
        "faqTips": "在客户端开启 TUN 模式配合 DoH，整机所有软件的域名解析均处于全密态保护之下。",
        "relatedSlugs": ["dns-leak-detection-fix", "clash-tun-fake-ip-vs-redir-host"]
    },
    {
        "id": "faq-134",
        "slug": "traffic-camouflage-obfs-mechanisms",
        "title": "流量伪装 (Obfuscation) 机制：TLS、WebRTC 与视频流混淆原理解密",
        "category": "protocols",
        "categoryLabel": "底层协议技术",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "剖析审查系统如何利用机器学习深度包检测 (DPI) 识别代理特征，以及混淆技术如何以假乱真。",
        "symptoms": [
            "好奇为什么代理流量能够瞒过防火墙的逐包深度检测 (DPI) 审查"
        ],
        "rootCauses": [
            "如果仅仅对数据进行加密，密文在统计学上呈现高熵 (High Entropy) 特征，审查系统很容易识别出「这是一段非正常的加密翻墙流」并进行阻断；而伪装技术将加密数据封装为标准应用层协议，使其符合正常网络规律。"
        ],
        "solutions": [
            {
                "stepTitle": "伪装层次 1：TLS 握手伪装 (uTLS / Chrome 指纹)",
                "detail": "模拟真实 Chrome 浏览器的 Client Hello 扩展列表、密码套件顺序，让审查模型判定其为一次正规的人类网页访问。"
            },
            {
                "stepTitle": "伪装层次 2：应用载荷伪装 (HTTP/2、WebRTC 实时语音)",
                "detail": "将数据切片混淆为 WebRTC 视频会议推流包，在流媒体大爆发时代，海量视频包特征极其庞大，审查系统不敢随意全局一刀切阻断。"
            }
        ],
        "faqTips": "不断升级伪装拟真度是开源社区对抗审查长期演进的核心智慧结晶。",
        "relatedSlugs": ["error-tls-handshake-timeout", "vless-reality-anti-censorship-how-it-works"]
    },
    {
        "id": "faq-135",
        "slug": "shadowsocks-2022-specification-upgrade",
        "title": "Shadowsocks 2022 新规范带来了哪些安全加固与抗重放防御",
        "category": "protocols",
        "categoryLabel": "底层协议技术",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "全面解读 Shadowsocks 协议自 2022 年大重构后，如何解决长达数年的主动探测与重放攻击隐患。",
        "symptoms": [
            "看到某些节点类型为 ss-2022、采用 blake3-aes-128-gcm 加密方式"
        ],
        "rootCauses": [
            "原版 Shadowsocks 缺乏严格的会话时序认证，GFW 可以截获用户发出的历史握手包并在几分钟后向服务端重新发送（主动探测攻击），观察服务端的响应行为从而 100% 确认该 IP 就是翻墙服务器"
        ],
        "solutions": [
            {
                "stepTitle": "升级 1：引入严格的时间戳校验与重放过滤器 (Sliding Window)",
                "detail": "SS-2022 在握手头部强制包含了时间戳和基于 BLAKE3 算法的单向哈希，任何重复收到或时间偏差的数据包会被直接静默丢弃，主动探测攻击彻底失效。"
            },
            {
                "stepTitle": "升级 2：定长握手头部与响应伪装",
                "detail": "消除了任何由数据包长度差异带来的指纹特征泄漏，使握手报文在物理形态上完全等同于不可预测的真随机白噪声。"
            }
        ],
        "faqTips": "SS-2022 是经典 Shadowsocks 协议在新时代重获新生的重大升级，兼具顶级性能与现代密码学安全。",
        "relatedSlugs": ["shadowsocks-vs-trojan-vs-vless", "error-cipher-not-supported"]
    }
]

print(f"Loaded {len(PROTOCOLS_FAQS)} protocols FAQs.")
