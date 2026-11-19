# -*- coding: utf-8 -*-
# Category 1: 客户端与软件配置疑难 (25 篇)

CLIENT_FAQS = [
    {
        "id": "faq-1",
        "slug": "clash-verge-service-mode-error",
        "title": "Clash Verge Rev 提示「Service Mode Not Installed」服务模式无法安装彻底解决方案",
        "category": "client",
        "categoryLabel": "客户端配置",
        "readTime": "6 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "详细排查 Windows 与 macOS 下 Clash Verge Rev 提示服务模式未就绪或安装报错，导致 TUN 虚拟网卡无法接管系统全局流量的问题。",
        "symptoms": [
            "点击安装服务模式后弹窗报错「Install Service Failed」",
            "服务模式图标常年为灰色或黄色感叹号，无法变为绿色勾选状态",
            "开启 TUN 模式提示需要先以服务模式运行"
        ],
        "rootCauses": [
            "系统安全杀毒软件（360、火绒、Windows Defender）拦截了后台注册系统服务的操作",
            "Clash Verge Rev 安装路径包含中文字符或非标准权限目录",
            "旧版本 Clash 遗留的 clash-core-service 注册表项冲突未清理干净"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：以管理员身份彻底重启 Clash Verge Rev",
                "detail": "右键点击任务栏退出 Clash Verge Rev，在桌面图标上右键选择「以管理员身份运行」，赋予完整的系统服务注册提权权限。"
            },
            {
                "stepTitle": "步骤 2：手动执行服务模式安装批处理脚本",
                "detail": "进入安装目录（通常为 C:\\Program Files\\Clash Verge Rev 或 %LOCALAPPDATA%\\Programs\\Clash Verge Rev），找到 resources\\clash-verge-service.exe，右键以管理员身份运行 install.bat。",
                "code": "cd \"C:\\Program Files\\Clash Verge Rev\\resources\"\n.\\clash-verge-service.exe install\n.\\clash-verge-service.exe start"
            },
            {
                "stepTitle": "步骤 3：清理 Windows 服务注册残留",
                "detail": "若依然报错，打开 PowerShell（管理员），运行 sc.exe delete clash_verge_service 清理残留服务，重启电脑后再次点击客户端内的一键安装即可成功。",
                "code": "Stop-Service -Name \"clash_verge_service\" -ErrorAction SilentlyContinue\nsc.exe delete \"clash_verge_service\""
            }
        ],
        "faqTips": "如果是在公司域控或学校受限电脑中，受限组策略可能会完全禁止创建非官方驱动服务，此时建议使用普通「系统代理」模式替代 TUN 模式。",
        "relatedSlugs": ["clash-tun-mode-virtual-nic-fail", "clash-verge-system-proxy-reset"]
    },
    {
        "id": "faq-2",
        "slug": "clash-tun-mode-virtual-nic-fail",
        "title": "开启 TUN 模式提示虚拟网卡适配器初始化失败 (Wintun.dll 缺失/驱动签名阻断)",
        "category": "client",
        "categoryLabel": "客户端配置",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "解决在 Windows 10/11 中启用 TUN 虚拟网卡时出现 Adapter Init Failed、wintun.dll 缺失或代码 52 驱动数字签名阻断问题。",
        "symptoms": [
            "开启 TUN 模式瞬间网络中断，客户端日志弹出「create tun interface: wintun create adapter failed」",
            "设备管理器中网络适配器出现黄色感叹号虚拟网卡",
            "系统提示「Windows 无法验证此设备所需驱动程序的数字签名 (代码 52)」"
        ],
        "rootCauses": [
            "Windows 11 安全中心开启了「内核隔离（内存完整性）」，阻断了老旧第三方虚拟网卡加载",
            "缺少微软官方最新的 C++ 运行库与 Wintun 核心动态链接库",
            "网络适配器堆栈被其他 VPN/加速器残留的 TAP-Windows 网卡占满"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：更换为 Meta (Mihomo) 最新自研内核",
                "detail": "进入 Clash Verge 设置 -> 内核选择，切换为「Mihomo 内核」。Meta 内核直接内置了最新的官方 Wintun 驱动规范，无需依赖传统不稳定的 TAP 网卡。"
            },
            {
                "stepTitle": "步骤 2：检查 Windows 安全中心的内核隔离开关",
                "detail": "打开「Windows 安全中心」->「设备安全性」->「核心隔离详细信息」，若提示不兼容驱动，先临时关闭内核隔离并重启电脑。"
            },
            {
                "stepTitle": "步骤 3：重置网络堆栈并修复 Winsock",
                "detail": "以管理员身份打开 CMD 或 PowerShell，执行网络重置命令，彻底刷新系统适配器注册表。",
                "code": "netsh winsock reset\nnetsh int ip reset"
            }
        ],
        "faqTips": "TUN 模式可以直接接管终端命令行、不走系统代理的海外游戏和桌面应用，是目前最推荐的全局接管方案。",
        "relatedSlugs": ["clash-verge-service-mode-error", "hiddify-next-windows-driver-error"]
    },
    {
        "id": "faq-3",
        "slug": "mihomo-party-startup-crash",
        "title": "Mihomo Party 启动闪退或界面白屏无响应终极排查",
        "category": "client",
        "categoryLabel": "客户端配置",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "新一代极美代理客户端 Mihomo Party 启动后白屏、黑屏、直接崩溃闪退的原因与配置重置方案。",
        "symptoms": [
            "双击快捷方式后窗口一闪而过，任务管理器无进程残留",
            "客户端窗口打开后一片空白，无法渲染节点列表与侧边栏",
            "提示「GPU Process Crashed Too Many Times」"
        ],
        "rootCauses": [
            "Electron 框架与某些独立显卡驱动硬件加速冲突",
            "缓存配置文件 config.yaml 损坏，存在未转义的特殊字符导致 YAML 解析器崩溃",
            "端口被本地其他代理软件（如 v2rayN、老 Clash）占用"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：禁用 GPU 硬件加速启动",
                "detail": "右键桌面 Mihomo Party 快捷方式，选择「属性」，在目标路径最后追加空格和 --disable-gpu 参数，然后点击确定重启。",
                "code": "\"C:\\Program Files\\Mihomo Party\\Mihomo Party.exe\" --disable-gpu"
            },
            {
                "stepTitle": "步骤 2：清理本地损坏的运行时缓存目录",
                "detail": "按 Win + R 运行 %APPDATA%\\mihomo-party，将 cache 和 local-storage 文件夹重命名或删除，重新打开软件即可重新生成纯净配置文件。"
            }
        ],
        "faqTips": "Mihomo Party 是开源社区近年来 UI 最现代化的客户端之一，若遇频繁白屏建议在客户端设置中常驻关闭「硬件加速」选项。",
        "relatedSlugs": ["clash-verge-mixed-port-conflict", "clash-nyanpasu-core-stopped"]
    },
    {
        "id": "faq-4",
        "slug": "sing-box-config-json-syntax-error",
        "title": "Sing-box 客户端解析 config.json 语法报错与格式快速修复",
        "category": "client",
        "categoryLabel": "客户端配置",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "解析 Sing-box 客户端在导入第三方通用订阅时提示 invalid json format、outbound type unknown 等核心配置报错排查。",
        "symptoms": [
            "点击启动提示「parse config: json: cannot unmarshal string into Go struct」",
            "订阅链接导入后节点解析为 0 个，控制台红字提示 schema violation",
            "切换配置后核心自动关闭"
        ],
        "rootCauses": [
            "机场返回的是 Clash YAML 格式，而直接粘贴到了 Sing-box 原生 JSON 导入框中",
            "Sing-box 版本快速迭代，老版本字段（如 inbound 里的 sniff）在新版中被重构为 route.sniff",
            "JSON 文件中存在中文全角逗号、多余结尾逗号或缺少花括号"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：确认订阅类型是否为 Sing-box 专属订阅",
                "detail": "登录机场后台，必须复制标有「Sing-box 订阅」的链接，切勿将 Clash 订阅直接当作 Sing-box 配置粘贴。"
            },
            {
                "stepTitle": "步骤 2：使用在线 JSON Linter 验证语法有效性",
                "detail": "将 config.json 全文粘贴至 jsonlint.com 进行语法校验，自动标红定位多余的逗号或缺失的双引号并一键格式化修复。"
            },
            {
                "stepTitle": "步骤 3：升级 Sing-box 核心至 1.9+ 或 1.10+ 最新稳定版",
                "detail": "检查客户端使用的 sing-box 核心版本，确保与机场提供的最新协议规范保持一致。"
            }
        ],
        "faqTips": "Sing-box 的优势在于资源开销极小且原生支持 Hysteria 2 与 TUIC 协议，如果不想手调 JSON，建议使用图形化壳子（如 Karing 或 GUI.for.SingBox）。",
        "relatedSlugs": ["sing-box-inbound-tun-mtu", "karing-client-multi-protocol-setup"]
    },
    {
        "id": "faq-5",
        "slug": "shadowrocket-subscription-timeout",
        "title": "iOS 小火箭 (Shadowrocket) 订阅更新一直转圈提示 Timeout 解决",
        "category": "client",
        "categoryLabel": "客户端配置",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "苹果 iPhone/iPad 用户在 Shadowrocket 下拉更新订阅链接时，一直转圈并弹出「Network Request Timeout」超时的解决全解。",
        "symptoms": [
            "在首页下拉刷新订阅，进度条转动超过 30 秒最终提示请求超时",
            "节点更新时间停留在数天前，无法获取最新的可用节点列表",
            "连上家里 Wi-Fi 无法更新，切换到 4G/5G 数据网络依然失败"
        ],
        "rootCauses": [
            "机场订阅服务器域名被国内本地 DNS 污染阻断无法解析",
            "iOS 系统网络权限中禁用了小火箭的「无线局域网与蜂窝网络」",
            "客户端当前未开启代理，而该订阅域名本身位于境外阻断名单中"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：开启现有任意存活节点后再点击更新订阅",
                "detail": "只要列表中还有一个能勉强连通的备用节点，先点击开启小火箭代理，再在首页下拉刷新订阅。此时订阅请求将走境外代理通道，直接绕过国内阻断。"
            },
            {
                "stepTitle": "步骤 2：更换小火箭内置 DNS 节点",
                "detail": "进入小火箭「设置」->「DNS」-> 修改为 223.5.5.5 或 119.29.29.29，同时添加备用境外 DNS 1.1.1.1，防止域名解析失败。"
            },
            {
                "stepTitle": "步骤 3：登录机场后台获取备用订阅转换域名",
                "detail": "进入机场后台用户中心，很多优质机场提供了防污染备用订阅链接或短链服务，将其重新导入小火箭替换即可。"
            }
        ],
        "faqTips": "强烈建议在小火箭「设置」->「订阅」中打开「打开时更新」与「自动后台更新」开关，确保节点时刻保持最新。",
        "relatedSlugs": ["shadowrocket-nodes-missing", "shadowrocket-node-group-auto-test"]
    },
    {
        "id": "faq-6",
        "slug": "v2rayng-battery-optimization-kill",
        "title": "Android v2rayNG 在后台被系统杀掉断网处理 (小米/华为/OPPO/vivo)",
        "category": "client",
        "categoryLabel": "客户端配置",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "安卓手机锁屏待机或切换应用数分钟后，v2rayNG VPN 图标自动消失并断开外网连接的保活设置全攻略。",
        "symptoms": [
            "手机息屏十分钟后，微信海外推送或 Telegram 接收不到任何消息",
            "解锁手机发现通知栏顶部的小钥匙 VPN 图标已消失",
            "重新打开 v2rayNG 提示服务已停止运行"
        ],
        "rootCauses": [
            "国产定制 Android 系统（HyperOS、鸿蒙、ColorOS、OriginOS）极致激进的后台电池优化策略",
            "未开启「允许自启动」与「允许关联启动」权限",
            "未给 v2rayNG 锁定后台多任务卡片"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：将电池优化设置为「无限制/不优化」",
                "detail": "长按 v2rayNG 图标 -> 应用信息 -> 省电策略/电池优化 -> 勾选「无限制」（允许在后台常驻运行，不限制后台活动）。"
            },
            {
                "stepTitle": "步骤 2：多任务卡片加锁并允许自启动",
                "detail": "在手机多任务管理界面中，按住 v2rayNG 卡片向下拉动，点击「小锁」图标加锁；同时在手机权限管理中打开「允许自启动」开关。"
            },
            {
                "stepTitle": "步骤 3：在软件内开启常驻通知栏",
                "detail": "打开 v2rayNG -> 设置 -> 勾选「显示常驻通知」，通过 Android 系统原生前台服务保活机制避免被内存回收机制清理。"
            }
        ],
        "faqTips": "如果系统版本较高，还可在系统设置的「VPN」选项中，点击 v2rayNG 后方的齿轮图标，勾选「始终开启的 VPN」以达到系统级守护。",
        "relatedSlugs": ["harmonyos-next-proxy-compatibility", "android-private-dns-conflict-proxy"]
    },
    {
        "id": "faq-7",
        "slug": "quantumult-x-mitm-cert-untrusted",
        "title": "Quantumult X 抓包与 MitM CA 证书未信任报错彻底解决",
        "category": "client",
        "categoryLabel": "客户端配置",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "iOS 圈 X (Quantumult X) 开启 HTTPS 解密重写与脚本时，提示证书未信任、无法解密流量的实操指引。",
        "symptoms": [
            "配置完去广告重写规则后，目标 App 提示网络不可用或无法建立安全连接",
            "圈 X 日志大量提示「MitM Handshake failed: certificate untrusted」",
            "Safari 访问网页提示「此网站证书不受信任」"
        ],
        "rootCauses": [
            "在圈 X 中生成了自签名 CA 证书并下载了描述文件，但在 iOS 系统中未进行最终的信任授权",
            "证书有效期已过，或重新安装圈 X 后未重新生成唯一专属证书",
            "重写主机名 (hostname) 列表包含过于宽泛的泛域名通配符导致全网证书冲突"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：圈 X 内生成并安装证书",
                "detail": "进入圈 X 核心设置 -> MitM -> 点击「生成证书」-> 点击「配置证书」-> 跳转到 Safari 允许下载描述文件。"
            },
            {
                "stepTitle": "步骤 2：在 iOS 系统设置中安装描述文件",
                "detail": "打开 iPhone「设置」-> 顶部出现「已下载描述文件」-> 点击「安装」并输入手机锁屏密码完成安装。"
            },
            {
                "stepTitle": "步骤 3：关键一步：进入系统完全信任根证书",
                "detail": "打开 iPhone「设置」->「通用」->「关于本机」-> 滑到最底部点击「证书信任设置」-> 在针对根证书启用完全信任下，找到 Quantumult X 并「开启绿色开关」。"
            }
        ],
        "faqTips": "如果只需要普通的科学上网看视频查资料，完全不需要开启 MitM 功能；MitM 仅在需要去应用内置广告或跑自动打卡脚本时才需开启。",
        "relatedSlugs": ["shadowrocket-subscription-timeout", "surge-rule-set-import-fail"]
    },
    {
        "id": "faq-8",
        "slug": "clash-for-windows-legacy-migration",
        "title": "Clash for Windows (CFW) 停更后安全迁移到 Clash Verge Rev 全流程",
        "category": "client",
        "categoryLabel": "客户端配置",
        "readTime": "6 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "手把手指导如何安全停用已停更的老旧 CFW，平滑迁移订阅与自定义规则至活跃维护的 Clash Verge Rev 客户端。",
        "symptoms": [
            "继续使用老旧 CFW 经常遇到新协议（如 Hysteria 2、Vless-Reality）无法识别报错",
            "老版本 Electron 存在已披露的安全执行漏洞",
            "无法使用现代高分辨率缩放与 Windows 11 暗黑主题"
        ],
        "rootCauses": [
            "原 CFW 开发者于 2023 年底停止维护并删库，内核永久停留在旧版 Clash Premium",
            "新一代主流机场全面转向 Mihomo (Meta) 内核，旧客户端不再兼容新规则集语法"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：从 GitHub 官方发布页下载 Clash Verge Rev",
                "detail": "认准官方活跃分支 clash-verge-rev/clash-verge-rev，在 Releases 中下载 Clash.Verge_x.x.x_x64-setup.exe 安装包。"
            },
            {
                "stepTitle": "步骤 2：彻底退出并卸载旧版 CFW",
                "detail": "先在老 CFW 设置中关闭「System Proxy」和「Start with Windows」，随后退出并卸载，防止两者在 7890 端口上产生抢占冲突。"
            },
            {
                "stepTitle": "步骤 3：在 Verge 中导入原订阅并开启 TUN 模式",
                "detail": "打开 Clash Verge Rev，在「订阅」页面粘贴你的机场订阅链接，点击导入即可无缝继承全部节点，同时享受更强大的 Meta 核心加速。"
            }
        ],
        "faqTips": "Clash Verge Rev 现已成为 Windows / macOS / Linux 桌面端最主流的通用主力客户端，拥有极佳的稳定性和活跃的社区更新。",
        "relatedSlugs": ["clash-verge-service-mode-error", "clash-meta-alpha-core-update"]
    },
    {
        "id": "faq-9",
        "slug": "surge-rule-set-import-fail",
        "title": "Surge 规则集 (RULE-SET) 远程更新失败与本地镜像缓存策略",
        "category": "client",
        "categoryLabel": "客户端配置",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "macOS/iOS 平台顶级代理工具 Surge 更新外部规则列表时出现 Fetching rule-set failed 的优化策略。",
        "symptoms": [
            "Surge 日志中频繁刷红提示「Rule-set [xxx] failed to load, using cached version」",
            "规则列表因长时间拉取失败导致分流策略错乱，国内网站被误走代理",
            "手动点击重新加载规则长时间卡在 0%"
        ],
        "rootCauses": [
            "引用的 GitHub Raw 规则地址直接访问国内 DNS 遭到污染或速率限制",
            "外部规则集 URL 链接由于上游作者改名或删库导致 404 Not Found",
            "Surge 的 update-interval 间隔过短被 GitHub API 频率限制"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：给 GitHub 规则地址添加加速镜像前缀",
                "detail": "编辑 Surge 配置文件，在 raw.githubusercontent.com 规则 URL 前添加常用的加速反代前缀（如 ghproxy.net）。"
            },
            {
                "stepTitle": "步骤 2：在 Surge 规则集后指定代理策略走境外出站",
                "detail": "在 RULE-SET 定义行最后指定 update-interval 并在 policy 中明确走代理节点更新，例如：RULE-SET,https://...,DIRECT,update-interval=86400。"
            }
        ],
        "faqTips": "尽量选用大维护团队维护的多合一规则集库（如 Loyalsoldier），避免引用年久失修的个人零散规则链接。",
        "relatedSlugs": ["quantumult-x-mitm-cert-untrusted", "surge-enhanced-mode-router-gateway"]
    },
    {
        "id": "faq-10",
        "slug": "clash-verge-mixed-port-conflict",
        "title": "Clash 混合端口 7890 提示「Port Already in Use」端口冲突解决",
        "category": "client",
        "categoryLabel": "客户端配置",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "启动客户端时核心报错，提示 7890 或 9090 端口已被其他进程占用导致代理无法正常监听。",
        "symptoms": [
            "Clash 核心启动日志标红：listen tcp 127.0.0.1:7890: bind: address already in use",
            "虽然界面打开了，但是系统代理开关打开后依然无法科学上网",
            "外部控制端口 9090 冲突导致 Web UI 无法连接"
        ],
        "rootCauses": [
            "后台有未退出的残留 Clash 进程（如任务管理器中的 clash-meta.exe 僵尸进程）",
            "同时开启了其他代理工具（v2rayN、QQ加速器、网易云解锁等）占用了默认 7890 端口",
            "Windows Hyper-V 动态端口范围保留占用了 7890 端口"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：排查并结束占用 7890 端口的进程",
                "detail": "以管理员身份打开 CMD，运行 netstat -ano | findstr 7890 查找占用该端口的 PID 进程号，然后在任务管理器中结束对应进程。",
                "code": "netstat -ano | findstr 7890\ntaskkill /F /PID <查询到的PID>"
            },
            {
                "stepTitle": "步骤 2：直接在客户端设置中更换默认端口",
                "detail": "如果不想排查其他软件，直接进入 Clash Verge Rev 设置 ->「混合端口 (Mixed Port)」，将其从 7890 修改为 7892 或 10808，点击保存即可立刻恢复正常。"
            }
        ],
        "faqTips": "如果修改了端口，终端或其他手动设置过 http_proxy=127.0.0.1:7890 的脚本也需要同步更新对应端口号。",
        "relatedSlugs": ["clash-verge-service-mode-error", "clash-nyanpasu-core-stopped"]
    },
    {
        "id": "faq-11",
        "slug": "loon-plugin-parser-error",
        "title": "iOS Loon 插件与订阅转换解析失败应对方案",
        "category": "client",
        "categoryLabel": "客户端配置",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "iOS 平台高阶工具 Loon 导入第三方插件时提示 Parser Error 无法加载插件脚本的修复指南。",
        "symptoms": [
            "导入外部 .plugin 文件时提示「Plugin syntax invalid」",
            "开启插件后特定海外网站直接报 500 错误打不开",
            "订阅配置中的 Script 脚本无法从 GitHub 下载"
        ],
        "rootCauses": [
            "插件引用的外部 JS 脚本地址在国内网络环境下无法直连拉取",
            "Loon 版本较低，插件使用了新版专有的 arguments 参数特性",
            "插件与当前的 MitM 证书状态不匹配"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：确保已正确安装并完全信任 Loon CA 证书",
                "detail": "进入 Loon 设置 -> 配置证书 -> 安装并前往 iPhone 系统设置开启完全信任。"
            },
            {
                "stepTitle": "步骤 2：在插件配置中启用走代理下载脚本",
                "detail": "在 Loon 节点列表中先挑选一个正常的可用节点，确保网络整体处于代理状态后再点击插件界面的「重新加载插件脚本」。"
            }
        ],
        "faqTips": "Loon 拥有强大的节点管理能力，日常使用建议仅保留必要的流媒体解锁检测插件，精简冗余脚本以提升响应速度。",
        "relatedSlugs": ["quantumult-x-mitm-cert-untrusted", "shadowrocket-subscription-timeout"]
    },
    {
        "id": "faq-12",
        "slug": "nekoray-singbox-core-switch",
        "title": "NekoBox / NekoRay 切换 Sing-box 内核与 Xray 内核崩溃问题",
        "category": "client",
        "categoryLabel": "客户端配置",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "针对桌面端 NekoRay 在 Sing-box 核心与 Xray 核心之间切换时提示 core stopped unexpectedly 的排查。",
        "symptoms": [
            "在设置中切换 Core 为 sing-box 后，点击启动立即闪退",
            "日志提示「sing-box core not found in directory」",
            "某些新协议在 Xray 核心下提示 unsupported protocol"
        ],
        "rootCauses": [
            "NekoRay 根目录没有下载匹配的 sing-box-core 独立执行文件",
            "旧版订阅规则包含 Xray 专有 routing 字段，Sing-box 无法向下兼容解析",
            "系统杀毒软件将解压的 sing-box.exe 误判并隔离"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：手动下载完整核心包覆盖",
                "detail": "前往 NekoRay 官方发布页，务必下载带有「-with-core」后缀的完整版本，或者手动下载最新 sing-box.exe 放置到软件根目录下。"
            },
            {
                "stepTitle": "步骤 2：重置路由设置",
                "detail": "进入「基本设置」->「路由设置」，点击「恢复默认设置」，自动适配当前选定内核的标准路由策略。"
            }
        ],
        "faqTips": "NekoRay 是少数在 Windows/Linux 上原生同时支持 Xray 和 Sing-box 的优秀客户端，适合协议极客深度定制。",
        "relatedSlugs": ["sing-box-config-json-syntax-error", "v2rayn-core-path-not-found"]
    },
    {
        "id": "faq-13",
        "slug": "clash-verge-script-override-error",
        "title": "Clash Verge Rev 扩展脚本 Script Override 报错 syntax error 修复",
        "category": "client",
        "categoryLabel": "客户端配置",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "用户在 Clash Verge Rev 中使用 JavaScript 进行配置预处理脚本 (Script / Merge) 覆盖时报错的修复步骤。",
        "symptoms": [
            "点击刷新订阅后提示「Merge script error: ReferenceError: main is not defined」",
            "自定义的 rules 规则没有生效，全部节点配置变为空白",
            "控制台输出 Uncaught SyntaxError: Unexpected token"
        ],
        "rootCauses": [
            "Clash Verge Rev 已经全面采用现代 ESModule 标准，旧版的 CommonJS `module.exports = main` 语法不再支持",
            "JavaScript 脚本中访问了不存在的字段引发空指针异常",
            "规则数组拼接使用了 push 却没有做前置存在性检查"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：按照最新规范定义 main 入口函数",
                "detail": "确保脚本结构严格遵循官方规范：function main(config, profileName) { return config; }，并在最后 export default main;",
                "code": "function main(config, profileName) {\n  // 确保 rules 存在\n  if (!config.rules) config.rules = [];\n  config.rules.unshift(\"DOMAIN-SUFFIX,google.com,PROXY\");\n  return config;\n}\n\n// 必须使用 export 导出\nexport default main;"
            },
            {
                "stepTitle": "步骤 2：利用客户端内置的预览功能单步调试",
                "detail": "在「扩展脚本」编辑面板中，点击右上角的「预览」按钮，查看当前脚本转换后的实时配置 YAML 输出，确认是否有 syntax 抛错。"
            }
        ],
        "faqTips": "如果对 JavaScript 语法不熟悉，建议直接使用更简单的 YAML 键值替换方式（Merge 配置），直观且不易出错。",
        "relatedSlugs": ["clash-verge-service-mode-error", "clash-meta-alpha-core-update"]
    },
    {
        "id": "faq-14",
        "slug": "shadowrocket-nodes-missing",
        "title": "小火箭导入订阅后节点列表为空，或只显示一个 Direct 节点排查",
        "category": "client",
        "categoryLabel": "客户端配置",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "新手使用 iOS 小火箭导入机场提供的链接后，首页没有任何节点出现，只有默认 Direct/Proxy 分组的解决办法。",
        "symptoms": [
            "扫码或导入 URL 成功，但小火箭列表中没有香港、日本等具体节点名称",
            "点击连接后直接报「No active proxy server available」",
            "订阅名称后显示 0 bytes / 0 servers"
        ],
        "rootCauses": [
            "复制的并不是节点订阅链接，而是机场后台的登录网址或普通官网 URL",
            "机场订阅被防火墙拦截，返回了 403/502 错误网页源码，小火箭无法将其解析为节点格式",
            "导入时类型选择错误（例如把 Base64 订阅强制选成了 Trojan 独立协议）"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：检查复制链接是否以 http/https 开头且带有 token/code",
                "detail": "标准订阅链接通常类似于 https://xxx.com/api/v1/client/subscribe?token=...，若复制成了官网主页则完全无法解析。"
            },
            {
                "stepTitle": "步骤 2：直接在 Safari 浏览器中打开该订阅链接验证",
                "detail": "将该链接粘贴到手机 Safari 中访问，如果页面下载了一个文本文件或显示了一长串加密字符，说明链接有效；如果显示 Cloudflare 拦截或 404，说明链接已被阻断，需联系机场客服获取新域名。"
            },
            {
                "stepTitle": "步骤 3：在小火箭中选择「Subscribe (订阅)」类型导入",
                "detail": "点击右上角加号，类型一定要选择「Subscribe」，而不是单节点协议，粘贴后点击右上角完成即可刷新出全部节点。"
            }
        ],
        "faqTips": "现在大部分优质机场（如隐形人、暮光等）都支持在用户后台直接点击「一键导入小火箭」，无需手动复制粘贴链接。",
        "relatedSlugs": ["shadowrocket-subscription-timeout", "shadowrocket-node-group-auto-test"]
    },
    {
        "id": "faq-15",
        "slug": "hiddify-next-windows-driver-error",
        "title": "Hiddify Next 在 Windows 下提示 wintun.dll 缺失处理",
        "category": "client",
        "categoryLabel": "客户端配置",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "开源跨平台客户端 Hiddify Next 开启 TUN 模式时报错 Wintun driver failure 解决方法。",
        "symptoms": [
            "在 Hiddify Next 切换为 VPN 模式提示「Cannot install virtual interface」",
            "日志提示 LoadLibrary wintun.dll failed (error 126)",
            "系统未弹出网络配置更改授权窗口"
        ],
        "rootCauses": [
            "绿色便携免安装版在移动解压时丢失了位于 bin/ 目录下的 wintun 驱动动态库",
            "第三方杀毒软件误拦截了驱动文件的临时加载"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：下载官方标准 MSI / Setup 安装包",
                "detail": "尽量避免使用单可执行便携版，下载官方提供的 .msi 安装包，安装程序会自动向 Windows System32 注册所需驱动。"
            },
            {
                "stepTitle": "步骤 2：手动补充官方 Wintun 动态链接库",
                "detail": "从 wintun.net 官方开源仓库下载对应平台（x64 或 arm64）的 wintun.dll，拷贝进 Hiddify 安装目录即可立即解决。"
            }
        ],
        "faqTips": "Hiddify Next 优势在于多协议整合极简设计，界面美观，也是目前非常值得推荐的通用客户端之一。",
        "relatedSlugs": ["clash-tun-mode-virtual-nic-fail", "sing-box-config-json-syntax-error"]
    },
    {
        "id": "faq-16",
        "slug": "clash-meta-alpha-core-update",
        "title": "手动升级 Clash Verge 的 Mihomo (Meta) 内核至最新 Alpha 版本",
        "category": "client",
        "categoryLabel": "客户端配置",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "教你如何手动替换 Clash Verge Rev 中的 Mihomo 核心文件，抢先体验最新协议特性与性能修复。",
        "symptoms": [
            "客户端稳定版发布滞后，无法使用最新的 Hysteria 2 端口跳跃或新分流特性",
            "老核心在某些高带宽并发场景下 CPU 占用过高",
            "某些新特性被机场要求必须在 Mihomo 1.18+ 以上才可支持"
        ],
        "rootCauses": [
            "客户端发行版打包的通常是稳定的 Release 内核，更新周期慢于核心开发者的日常迭代"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：从 MetaCubeX 官方仓库下载最新 Alpha 内核",
                "detail": "前往 github.com/MetaCubeX/mihomo/releases，在预发布版本中找到与系统架构匹配的压缩包（如 mihomo-windows-amd64-alpha-xxxx.zip）。"
            },
            {
                "stepTitle": "步骤 2：解压并重命名覆盖客户端核心文件",
                "detail": "退出客户端，进入 Clash Verge 数据目录（设置 -> 内核 -> 点击打开内核目录），将下载的文件重命名为 clash-meta.exe（或 mihomo.exe）替换原文件，随后重启客户端即可。"
            }
        ],
        "faqTips": "替换前建议将原内核备份为 clash-meta-old.exe，以便遇到 Alpha 尝鲜版不稳定时随时一键回退。",
        "relatedSlugs": ["clash-verge-service-mode-error", "clash-for-windows-legacy-migration"]
    },
    {
        "id": "faq-17",
        "slug": "flclash-cross-platform-sync",
        "title": "FlClash 跨平台客户端在 Linux / Android 同步配置报错修复",
        "category": "client",
        "categoryLabel": "客户端配置",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "使用 Flutter 构建的多平台客户端 FlClash 配置文件同步或局域网导入报错排错。",
        "symptoms": [
            "通过 WebDAV 同步配置时提示 401 Unauthorized 或 404",
            "Android 手机无法扫描桌面端生成的局域网同步二维码",
            "保存自定义规则后没有在节点列表体现"
        ],
        "rootCauses": [
            "移动端与电脑端不在同一个局域网网段，或电脑端开启了防火墙阻断了入站探测",
            "WebDAV 服务地址末尾缺少斜杠 / 导致路径拼接异常"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：排查局域网防火墙规则",
                "detail": "确保电脑与手机连接在同一个家庭 Wi-Fi 频段（切勿一台在访客网络另一台在主网），并在电脑防火墙中允许 FlClash 入站。"
            },
            {
                "stepTitle": "步骤 2：直接使用订阅链接手动添加",
                "detail": "若局域网二维码识别困难，推荐直接在手机端微信或浏览器中通过复制机场订阅链接导入，更加稳定直接。"
            }
        ],
        "faqTips": "FlClash 界面极其现代简洁，适合追求全平台（手机、平板、电脑）UI 风格统一的用户。",
        "relatedSlugs": ["clash-verge-service-mode-error", "stash-icloud-sync-conflict"]
    },
    {
        "id": "faq-18",
        "slug": "clash-verge-system-proxy-reset",
        "title": "每次关机重启后 Windows 系统代理开关自动开启/残留代理排查",
        "category": "client",
        "categoryLabel": "客户端配置",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "关机或非正常关闭 Clash 后，电脑重启无法上网，浏览器提示「无法连接到代理服务器」的根本解决办法。",
        "symptoms": [
            "电脑开机后不打开代理软件连微信、百度都打不开，提示代理错误",
            "每次进入 Windows 设置手动关掉代理，过几分钟又被自动打开",
            "日志频繁显示 127.0.0.1:7890 拒绝连接"
        ],
        "rootCauses": [
            "Windows 关机前 Clash 未执行正常的反注册退出流程，导致注册表中 ProxyEnable 依然标记为 1",
            "后台有其他流氓软件（某些网盘加速、浏览器插件）锁定了注册表代理键值",
            "开启了开机自启但在服务启动前系统就尝试访问网络"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：在客户端中正常「关闭系统代理」并安全退出",
                "detail": "养成习惯：电脑关机或不需要代理时，先在客户端主界面手动将「系统代理」开关置为关闭状态，再右键任务栏图标选择「退出」。"
            },
            {
                "stepTitle": "步骤 2：一键重置 Windows 注册表代理开关",
                "detail": "在 PowerShell 中运行以下一行命令，强制将注册表代理标记清零，立即恢复国内直连上网能力。",
                "code": "Set-ItemProperty -Path 'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings' -Name ProxyEnable -Value 0"
            }
        ],
        "faqTips": "若经常遇到此问题，建议在 Clash Verge Rev 设置中开启「TUN 模式」替代「系统代理模式」，TUN 模式由系统虚拟网卡管理，关机时绝不残留任何代理注册表垃圾。",
        "relatedSlugs": ["clash-verge-service-mode-error", "windows-11-system-proxy-auto-tampered"]
    },
    {
        "id": "faq-19",
        "slug": "clash-nyanpasu-core-stopped",
        "title": "Clash Nyanpasu 启动后核心自动停止 (Core Stopped) 修复指南",
        "category": "client",
        "categoryLabel": "客户端配置",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "二次元风格客户端 Clash Nyanpasu 在启动内核时提示 Core Stopped 且日志为空的快速修复。",
        "symptoms": [
            "点击启动核心，状态栏短暂变绿后又立即变红变为 Core Stopped",
            "控制台没有任何网络日志输出",
            "切换不同的订阅后依然无法唤醒核心"
        ],
        "rootCauses": [
            "用户订阅配置文件中包含了 Mihomo 当前版本无法解析的特殊字符（如未转义的表情符号或冒号）",
            "运行内存受限或防护软件强制结束了后台子进程"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：新建一个纯净空白 Profile 配置文件排查",
                "detail": "在 Profiles 页面新建一个空的默认配置并启用，如果核心能成功启动，说明核心本身正常，问题出在特定机场的订阅 YAML 内容中。"
            },
            {
                "stepTitle": "步骤 2：检查订阅 YAML 的编码格式",
                "detail": "确保订阅文件保存为 UTF-8 无 BOM 格式，避免非标准字符导致 YAML 解析器直接中止退出。"
            }
        ],
        "faqTips": "如果排查复杂，建议直接切换至主流稳定的 Clash Verge Rev，兼容性更广，社区文档也更完善。",
        "relatedSlugs": ["clash-verge-mixed-port-conflict", "mihomo-party-startup-crash"]
    },
    {
        "id": "faq-20",
        "slug": "stash-icloud-sync-conflict",
        "title": "iOS / Mac 平台 Stash 配置文件 iCloud 云同步冲突与版本恢复",
        "category": "client",
        "categoryLabel": "客户端配置",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "Stash 客户端在 iPhone 和 Mac 之间通过 iCloud 同步分流规则时提示冲突或配置回滚的应对方案。",
        "symptoms": [
            "在 Mac 端添加的规则在手机上被旧版本覆盖",
            "Stash 设置中 iCloud 状态显示「Sync Pending」甚至报错",
            "节点分组被重置为初始状态"
        ],
        "rootCauses": [
            "多台设备在断网状态下同时修改了配置，导致苹果 iCloud 产生分支版本冲突",
            "iCloud 空间已满或手机处于低电量模式暂停了后台数据同步"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：在 Stash 中导出本地副本备份",
                "detail": "在修改重大规则前，先在 Stash「配置」页面选择「导出配置为本地文件」，保存好应急备份。"
            },
            {
                "stepTitle": "步骤 2：强制在文件 App 中处理 iCloud 冲突文件",
                "detail": "打开 iPhone「文件」App -> iCloud 云盘 -> Stash 文件夹，如果看到标有 (1) 或 Conflict 后缀的文件，删除旧文件并保留最新的一份。"
            }
        ],
        "faqTips": "Stash 是 iOS / Mac 生态中深度适配 Clash 规则体系的高颜值利器，支持 Siri 捷径与磁贴小组件，非常适合果粉全家桶。",
        "relatedSlugs": ["surge-rule-set-import-fail", "shadowrocket-subscription-timeout"]
    },
    {
        "id": "faq-21",
        "slug": "karing-client-multi-protocol-setup",
        "title": "新兴多平台客户端 Karing 配置多协议订阅与分流规则指南",
        "category": "client",
        "categoryLabel": "客户端配置",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "跨 iOS / Android / Windows / Mac 的新兴客户端 Karing 零门槛导入订阅与分流调优全流程。",
        "symptoms": [
            "初次使用不知如何配置多协议聚合订阅",
            "节点延迟测试全部超时或无法智能分流",
            "需要实现国内直连、海外代理、AI 专属节点的自动化策略"
        ],
        "rootCauses": [
            "Karing 基于 Sing-box 核心构建，需要根据规则集自动匹配 routing 策略"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：添加订阅源",
                "detail": "打开 Karing -> 点击右上角加号 -> 选择「添加订阅」-> 粘贴机场提供的 Clash 或 Sing-box 订阅链接即可自动识别并解析节点。"
            },
            {
                "stepTitle": "步骤 2：选择智能路由分流模式",
                "detail": "在主界面路由策略中选择「绕过大陆 (Bypass CN)」或「规则模式 (Rule)」，保证国内应用直连不受任何影响。"
            }
        ],
        "faqTips": "Karing 已经在各大平台官方应用商店（如 App Store、Google Play）直接上架，对于没有美区 Apple ID 的朋友是极佳的免费选择。",
        "relatedSlugs": ["sing-box-config-json-syntax-error", "clash-for-windows-legacy-migration"]
    },
    {
        "id": "faq-22",
        "slug": "clash-verge-dark-mode-font-blur",
        "title": "Clash Verge Rev 4K 高分屏字体模糊与暗黑模式适配优化",
        "category": "client",
        "categoryLabel": "客户端配置",
        "readTime": "3 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "在 2K / 4K 高分辨率显示屏下使用 Clash Verge 界面字体发虚或暗黑模式对比度不舒服的调节技巧。",
        "symptoms": [
            "在高 DPI 缩放（如 150%、200%）下文字有重影或锯齿",
            "夜间使用亮色界面刺眼，开启暗黑模式后部分节点文字无法看清"
        ],
        "rootCauses": [
            "Windows 缩放 DPI 未交由应用程序自主渲染",
            "未启用现代 Webview2 / 自定义主题引擎"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：修改高 DPI 覆盖设置",
                "detail": "右键桌面快捷方式 ->「属性」->「兼容性」->「更改高 DPI 设置」-> 勾选「替代高 DPI 缩放行为」并选择「应用程序」。"
            },
            {
                "stepTitle": "步骤 2：在客户端内切换主题与字体",
                "detail": "进入 Clash Verge Rev 设置 ->「界面设置」-> 选择「跟随系统暗黑模式」，并在自定义字体中填入 Microsoft YaHei UI 或 Inter。"
            }
        ],
        "faqTips": "最新的 Clash Verge Rev 采用现代 Web 技术重构，界面的高刷新率与字体清晰度均大幅领先老款 CFW。",
        "relatedSlugs": ["clash-for-windows-legacy-migration", "mihomo-party-startup-crash"]
    },
    {
        "id": "faq-23",
        "slug": "sing-box-inbound-tun-mtu",
        "title": "Sing-box 自定义 TUN 入站 MTU 调优防止网页卡死与高丢包",
        "category": "client",
        "categoryLabel": "客户端配置",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "针对 Sing-box 开启虚拟网卡后大文件传输慢、网页加载一半突然卡住的 MTU 调优实战。",
        "symptoms": [
            "普通文字网页秒开，但打开图片很多的大型网站长时间白屏",
            "测速下行很高，但上传文件或发送邮件附件直接超时",
            "日志中经常看到 packet too large, fragmentation required 提示"
        ],
        "rootCauses": [
            "默认 MTU 设为 1500，加上外层代理协议（如 Vless/Hysteria）加密封装包头后超过了物理网卡上限，导致链路层发生严重分片甚至丢包"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：打开 Sing-box config.json 的 inbound 配置",
                "detail": "在 inbounds 数组中找到 type 为 tun 的配置对象，添加或修改 mtu 字段。"
            },
            {
                "stepTitle": "步骤 2：推荐将 MTU 调整为 9000（局域网）或 1400（公网防分片）",
                "detail": "针对常规公网科学上网，推荐将 MTU 设为 1400 或 1350，预留充足的协议包头缓冲区。",
                "code": "{\n  \"type\": \"tun\",\n  \"inet4_address\": \"172.19.0.1/30\",\n  \"auto_route\": true,\n  \"strict_route\": true,\n  \"mtu\": 1400\n}"
            }
        ],
        "faqTips": "如果使用 Hysteria 2 协议，适当调小 MTU 能够大幅改善晚高峰在移动宽带等劣化网络下的网页秒开体验。",
        "relatedSlugs": ["error-mtu-packet-fragmentation", "sing-box-config-json-syntax-error"]
    },
    {
        "id": "faq-24",
        "slug": "shadowrocket-node-group-auto-test",
        "title": "小火箭设置定时自动测速与最优延迟节点自动切换策略",
        "category": "client",
        "categoryLabel": "客户端配置",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "教你在 iPhone 小火箭中配置 URL-Test 自动优选策略组，遇到节点临时断连无需手动切换。",
        "symptoms": [
            "正在看视频时当前节点突然维护断流，必须手动打开小火箭一个个测速换节点",
            "不知道列表中哪个香港或日本节点此刻延迟最低"
        ],
        "rootCauses": [
            "默认使用的是手动单选节点策略，缺乏动态健康检查探测"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：创建 Auto URL-Test 服务器分组",
                "detail": "进入小火箭「服务器」列表 -> 点击右上角加号 -> 类型选择「URL Test」-> 自定义一个名称（如 自动优选专线）。"
            },
            {
                "stepTitle": "步骤 2：添加候选节点与健康检查参数",
                "detail": "在成员列表中勾选常用的 3~5 个优质专线节点，测试 URL 填入 http://www.gstatic.com/generate_204，间隔填入 300 秒，容差设为 50ms。"
            }
        ],
        "faqTips": "自动优选建议仅添加同一家机场的同级别专线节点，切勿将普通直连节点与高端 IPLC 混合，以免自动跳到低速直连节点。",
        "relatedSlugs": ["shadowrocket-subscription-timeout", "shadowrocket-nodes-missing"]
    },
    {
        "id": "faq-25",
        "slug": "v2rayn-core-path-not-found",
        "title": "v2rayN 提示 Xray / V2Ray 核心路径不存在或没有执行权限彻底解决",
        "category": "client",
        "categoryLabel": "客户端配置",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "Windows 经典工具 v2rayN 启动报错「未找到核心文件，请检查 bin 目录」的排错指南。",
        "symptoms": [
            "双击打开 v2rayN 弹出红框：System.Exception: 核心启动失败，未在 bin 目录下找到 xray.exe",
            "订阅可以更新，但无法启动服务，无法开启系统代理"
        ],
        "rootCauses": [
            "解压时未将整个文件夹完全解压，或者单独把 v2rayN.exe 拖到了桌面上",
            "Windows Defender 误将 xray.exe 移到了隔离区"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：右键完整解压整个压缩包",
                "detail": "务必将下载的 zip 包「全部解压缩」到非 C 盘 Program Files 的普通目录（如 D:\\v2rayN-With-Core），不要在压缩包内直接双击运行。"
            },
            {
                "stepTitle": "步骤 2：从软件菜单一键下载更新核心",
                "detail": "进入 v2rayN 顶部菜单 ->「检查更新」-> 点击「下载 Xray-Core」，程序会自动连接官方源解压到 bin 目录下。"
            }
        ],
        "faqTips": "现代网络环境下，建议优先使用 Clash Verge Rev，在多节点路由分流和内存管理上比传统的 v2rayN 更加省心易用。",
        "relatedSlugs": ["nekoray-singbox-core-switch", "clash-for-windows-legacy-migration"]
    }
]

print(f"Loaded {len(CLIENT_FAQS)} client FAQs.")
