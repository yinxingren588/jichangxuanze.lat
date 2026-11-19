# -*- coding: utf-8 -*-
# Category 8: 跨平台设备与硬件终端专病 (15 篇)

HARDWARE_FAQS = [
    {
        "id": "faq-136",
        "slug": "windows-11-system-proxy-auto-tampered",
        "title": "Windows 11 系统代理开关被其他软件反复篡改锁定彻底解决",
        "category": "hardware",
        "categoryLabel": "多端设备与系统专病",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "排查电脑中恶意加速器、网盘客户端或流氓插件在后台强制劫持 Windows 代理注册表的根除方案。",
        "symptoms": [
            "明明关闭了 Clash，几秒钟后代理开关又莫名其妙自己打开，指向一个奇怪的本地端口（如 127.0.0.1:10809 或 8080）",
            "国内微信百度瞬间断网，必须手动去设置里不断关闭代理",
            "修改注册表后重启电脑又被恢复"
        ],
        "rootCauses": [
            "某些第三方游戏加速器、老旧安卓模拟器、极速下载器在后台运行了静默守护进程，硬编码循环检测并强行覆盖注册表 ProxyEnable 键值"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：排查可疑的后台自启动常驻服务",
                "detail": "打开任务管理器 ->「启动」选项卡，禁用所有不认识的开机自启程序；按 Win + R 运行 services.msc，检查是否有残留的第三方代理服务。"
            },
            {
                "stepTitle": "步骤 2：对 Windows 代理注册表键值设置「拒绝写入」权限（强效绝杀）",
                "detail": "按 Win + R 运行 regedit，定位到：HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings，右键该项选择「权限」->「高级」-> 限制受限用户的「设置数值」权限，防止任何流氓软件再次擅自篡改。"
            },
            {
                "stepTitle": "步骤 3：在日常中开启 Clash 的 TUN 模式",
                "detail": "TUN 模式完全绕过 Windows 的传统注册表代理体系，彻底免疫此类系统级代理篡改。"
            }
        ],
        "faqTips": "如果刚卸载过某些游戏加速器，建议重启前执行一次 netsh winsock reset 重置网络套接字。",
        "relatedSlugs": ["clash-verge-system-proxy-reset", "clash-tun-mode-virtual-nic-fail"]
    },
    {
        "id": "faq-137",
        "slug": "macos-network-extension-authorization-blocked",
        "title": "macOS 提示「系统扩展已被阻止」无法接管流量修复指南",
        "category": "hardware",
        "categoryLabel": "多端设备与系统专病",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "苹果 Mac 用户在初次安装 Clash Verge Rev 或 Surge 开启增强模式时，macOS 弹窗拦截驱动授权的解决。",
        "symptoms": [
            "开启增强模式或 TUN 时弹窗提示：系统扩展已被阻止 (System Extension Blocked)",
            "无法在网络偏好设置中看到虚拟网卡",
            "状态栏客户端图标闪烁报错"
        ],
        "rootCauses": [
            "macOS (Sonoma / Sequoia) 具备极其严格的 SIP 系统完整性保护机制，任何内核级或网络扩展 (Network Extension) 必须由用户亲自在系统设置中手动解锁授权"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：前往系统设置的「隐私与安全性」中手动点击允许",
                "detail": "打开 Mac「系统设置」->「隐私与安全性」-> 向下滑动到「安全性」区域，会看到一行黄底文字：「来自开发者 xxx 的系统软件已被阻止载入」，点击右侧的「允许」按钮并输入 Mac 开机密码确认授权。"
            },
            {
                "stepTitle": "步骤 2：在网络面板中信任新添加的 VPN 配置",
                "detail": "系统弹出提示「xxx 想要添加 VPN 配置」，果断点击「允许」，完成驱动加载注册。"
            }
        ],
        "faqTips": "这是苹果系统的标准安全防护流程，每个 Mac 用户初次配置网络扩展工具时都需要进行一次授权。",
        "relatedSlugs": ["clash-tun-mode-virtual-nic-fail", "linux-desktop-system-wide-proxy-clash"]
    },
    {
        "id": "faq-138",
        "slug": "ios-vpn-auto-disconnect-standby",
        "title": "iPhone 锁屏待机后代理经常自动断开重连的省电冲突解决",
        "category": "hardware",
        "categoryLabel": "多端设备与系统专病",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "苹果 iPhone 用户锁屏息屏十几分钟后，小火箭或 Loon 自动断开、推送消息收不到的解决全解。",
        "symptoms": [
            "点亮屏幕发现状态栏小 VPN 标志才刚刚重新弹出来，显示正在重新连接",
            "锁屏期间 Telegram 或海外邮件没有任何消息推送通知",
            "频繁在 Wi-Fi 和蜂窝移动网络切换时断连"
        ],
        "rootCauses": [
            "iOS 系统的「低电量模式」或休眠策略会在锁屏后强行切断后台常驻的网络扩展以节省电量",
            "Wi-Fi 在休眠时自动关闭了与路由器的信令保活"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：关闭 iOS「低电量模式」并允许后台刷新",
                "detail": "进入 iPhone「设置」->「电池」-> 确保关闭「低电量模式」；进入「通用」->「后台 App 刷新」，确保小火箭处于允许刷新状态。"
            },
            {
                "stepTitle": "步骤 2：在小火箭设置中开启「随网络切换自动重连」",
                "detail": "进入 Shadowrocket「设置」-> 开启「自动连接」与「随网络切换重新连接」，确保从 Wi-Fi 走到户外切为 5G 时无感续接。"
            }
        ],
        "faqTips": "小火箭基于 iOS 原生 NetworkExtension 框架开发，内存占用通常低于 15MB，常驻后台耗电微乎其微，无需刻意关闭。",
        "relatedSlugs": ["v2rayng-battery-optimization-kill", "shadowrocket-subscription-timeout"]
    },
    {
        "id": "faq-139",
        "slug": "android-private-dns-conflict-proxy",
        "title": "Android 手机系统「私人 DNS」与科学上网软件冲突排错指南",
        "category": "hardware",
        "categoryLabel": "多端设备与系统专病",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "安卓手机（小米/三星/一加）开启了系统自带的 Private DNS 后，导致所有代理软件完全打不开网页的解决。",
        "symptoms": [
            "开启 v2rayNG 或 Clash 后手机状态栏提示「无法连接到互联网」",
            "打开任何网页提示 DNS_PROBE_FINISHED_BAD_CONFIG",
            "必须在手机系统设置里把私人 DNS 关掉才能上网"
        ],
        "rootCauses": [
            "Android 原生的「私人 DNS (Private DNS)」采用 DoT 协议强制向固定主机名发起 TLS 握手，而代理客户端的 VPN 虚拟网卡在尝试劫持 853 端口时产生死锁冲突"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：在手机设置中将私人 DNS 设为「关闭」或「自动」",
                "detail": "打开安卓手机「设置」->「连接与共享」->「私人 DNS」-> 勾选「关闭」即可。域名防污染和加密解析完全交由客户端内置的 Clash DNS 代劳，性能更好。"
            },
            {
                "stepTitle": "步骤 2：在客户端内开启 Fake-IP 模式",
                "detail": "Fake-IP 模式会直接接管所有 DNS 解析流程，彻底解决系统底层 DoT 与代理冲突问题。"
            }
        ],
        "faqTips": "很多安卓用户折腾半天连不上，最后发现就是因为系统里偷偷开了一个不可用的私人 DNS 导致的，关闭后秒通。",
        "relatedSlugs": ["dns-leak-detection-fix", "clash-tun-fake-ip-vs-redir-host"]
    },
    {
        "id": "faq-140",
        "slug": "apple-tv-tvos-surge-clash-proxy",
        "title": "Apple TV (tvOS 17+) 安装 Quantumult X / Surge 终极看片方案",
        "category": "hardware",
        "categoryLabel": "多端设备与系统专病",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "苹果电视盒子自 tvOS 17 开放原生 VPN 接口后，在电视上直接安装圈 X、Surge 或 Loon 看 4K 原盘大片的终极方案。",
        "symptoms": [
            "以往在 Apple TV 上看 Netflix / YouTube 必须折腾软路由或复杂网关",
            "不知道如何在 tvOS 系统的 App Store 下载代理软件"
        ],
        "rootCauses": [
            "tvOS 17 之前系统原生不支持 VPN 协议栈，tvOS 17 之后苹果官方全面开放，主流工具均已推出原生 TV 版客户端"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：在 Apple TV 的 App Store 登录美区 Apple ID",
                "detail": "进入电视设置 ->「用户与账户」-> 添加并切换为你已购买过圈 X、Surge 或 Loon 的美区 Apple ID。"
            },
            {
                "stepTitle": "步骤 2：在 TV 版 App Store 直接搜索下载客户端",
                "detail": "下载并安装 Quantumult X (TV 版) 或 Surge (tvOS 版)，打开后手机扫描电视屏幕上的二维码即可一键同步手机上的机场订阅！"
            },
            {
                "stepTitle": "步骤 3：在设置中开启「随 Apple TV 开机自动连接」",
                "detail": "开启后，电视每次开机自动后台静默代理，直接使用遥控器点开 YouTube 4K、Netflix 丝滑秒播！"
            }
        ],
        "faqTips": "tvOS 原生客户端的出现彻底终结了为了电视买软路由的时代，稳定性大幅跃升。",
        "relatedSlugs": ["surge-enhanced-mode-router-gateway", "netflix-only-originals-fix"]
    },
    {
        "id": "faq-141",
        "slug": "android-tv-box-clash-remote-control",
        "title": "索尼电视 / 小米盒子安装 Clash 遥控器无法操作与旁路由选型",
        "category": "hardware",
        "categoryLabel": "多端设备与系统专病",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "在安卓智能电视、外贸电视盒子上使用标准手机版 APK 导致遥控器无法点击按钮的应对。",
        "symptoms": [
            "把手机版 Clash 安装包通过 U 盘装到电视上后，遥控器光标无法移动到开关按钮上",
            "界面横竖屏错乱，画面被拉伸变形"
        ],
        "rootCauses": [
            "手机版 APK 是为触屏交互设计的，缺乏 Android TV 专有的遥控器焦点 (Focus) 交互规范"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：必须下载专门针对电视 TV 适配的专用版客户端",
                "detail": "认准专为电视大屏开发的开源客户端（如 Clash for Android TV 版、Karing TV 版或 v2rayNG TV 版），界面完美支持方向键与确定键。"
            },
            {
                "stepTitle": "步骤 2：应急方案：使用蓝牙鼠标或手机遥控器触控板",
                "detail": "给电视插入一个普通的无线鼠标，或者在手机上安装遥控器 App 开启鼠标指针模式进行一次性配置。"
            }
        ],
        "faqTips": "电视端一旦配置好订阅并开启开机自启，之后只需日常使用即可，极少需要频繁修改设置。",
        "relatedSlugs": ["apple-tv-tvos-surge-clash-proxy", "lan-share-proxy-switch-ps5-xbox"]
    },
    {
        "id": "faq-142",
        "slug": "harmonyos-next-proxy-compatibility",
        "title": "华为鸿蒙系统 (HarmonyOS) 代理软件安装与纯血鸿蒙前瞻",
        "category": "hardware",
        "categoryLabel": "多端设备与系统专病",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "华为手机用户在 HarmonyOS 4.x 及纯血鸿蒙 HarmonyOS NEXT 下配置科学上网的现状与指引。",
        "symptoms": [
            "华为手机安装第三方 APK 提示高风险应用并强制拦截",
            "关心未来升级纯血鸿蒙后还能否继续使用科学上网工具"
        ],
        "rootCauses": [
            "华为纯血鸿蒙 NEXT 彻底剥离了 Linux 内核与安卓 AOSP 代码，无法直接运行传统的 Android .apk 安装包"
        ],
        "solutions": [
            {
                "stepTitle": "针对 HarmonyOS 4.x / 现有鸿蒙系统：关闭纯净模式安装",
                "detail": "进入「设置」->「系统和更新」-> 关闭「纯净模式」，或者在安装提示风险时点击「继续安装」输入指纹即可正常使用 v2rayNG 或 Clash。"
            },
            {
                "stepTitle": "针对纯血鸿蒙 NEXT：通过路由器或局域网代理托管",
                "detail": "未来升级纯血鸿蒙且未有原生客户端适配前，建议通过电脑端开启「允许局域网连接」或家庭软路由让华为手机免客户端享受加速。"
            }
        ],
        "faqTips": "现有搭载 HarmonyOS 4 的华为设备完全具备 Android 兼容层，正常使用主流客户端毫无障碍。",
        "relatedSlugs": ["v2rayng-battery-optimization-kill", "lan-share-proxy-switch-ps5-xbox"]
    },
    {
        "id": "faq-143",
        "slug": "linux-desktop-system-wide-proxy-clash",
        "title": "Ubuntu / Debian Linux 桌面环境下系统全局代理最佳配置",
        "category": "hardware",
        "categoryLabel": "多端设备与系统专病",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "Linux 极客与开发者在 GNOME / KDE 桌面环境中实现系统设置、终端命令与 GUI 应用统一代理。",
        "symptoms": [
            "在 Linux 下运行了 Clash 核心，Firefox 浏览器可以翻墙但 Chrome 或终端依然无法联网"
        ],
        "rootCauses": [
            "Linux 各个工具生态割裂：GNOME 桌面代理只影响部分 GUI 软件，终端工具只认环境变量，内核流量需要 iptables/nftables 接管"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：直接使用 Clash Verge Rev 的 Linux 官方包并开启 TUN",
                "detail": "从 GitHub 下载 clash-verge_x.x.x_amd64.deb 安装，使用 sudo 启动并开启 TUN 模式，Mihomo 会自动通过 nftables 接管整机全流量！"
            },
            {
                "stepTitle": "步骤 2：在 /etc/environment 中注入全局代理环境变量",
                "detail": "在配置文件末尾写入代理地址，保证所有终端命令行程序开箱即用：",
                "code": "http_proxy=\"http://127.0.0.1:7890/\"\nhttps_proxy=\"http://127.0.0.1:7890/\"\nno_proxy=\"localhost,127.0.0.1,localaddress,.localdomain.com\""
            }
        ],
        "faqTips": "TUN 模式是目前解决 Linux 多应用网络割裂的最完美现代方案，强烈推荐开启。",
        "relatedSlugs": ["clash-tun-mode-virtual-nic-fail", "curl-wget-terminal-proxy-environment"]
    },
    {
        "id": "faq-144",
        "slug": "synology-nas-docker-proxy-download",
        "title": "群晖 Synology NAS Docker 与套件中心联网慢走代理配置",
        "category": "hardware",
        "categoryLabel": "多端设备与系统专病",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "解决群晖 NAS 套件中心刷新不出来、Container Manager (Docker) 无法下载海外容器镜像的问题。",
        "symptoms": [
            "群晖套件中心提示「联机失败，请检查网络设置」",
            "拉取海外 Docker 镜像卡死在 Downloading",
            "Cloud Sync 无法同步 Google Drive 或 OneDrive"
        ],
        "rootCauses": [
            "群晖 DSM 系统默认未配置系统级网络代理"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：在群晖控制面板中直接配置局域网代理",
                "detail": "打开 DSM「控制面板」->「网络」->「常规」选项卡 -> 勾选「通过代理服务器连接」-> 填入局域网内开着代理的电脑 IP（如 192.168.1.100）和端口 7890，点击应用。"
            },
            {
                "stepTitle": "步骤 2：套件中心与系统更新即刻恢复秒开",
                "detail": "配置完成后，套件中心和 Container Manager 会自动通过局域网代理高速下载所需套件与镜像。"
            }
        ],
        "faqTips": "大文件下载完成后，可随时在控制面板中取消勾选代理，恢复纯内网直连状态。",
        "relatedSlugs": ["docker-daemon-pull-images-proxy", "lan-share-proxy-switch-ps5-xbox"]
    },
    {
        "id": "faq-145",
        "slug": "steam-deck-gaming-mode-proxy-clash",
        "title": "Steam Deck 掌机在 Gaming 游戏模式下后台常驻运行 Clash 加速",
        "category": "hardware",
        "categoryLabel": "多端设备与系统专病",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "手把手教你在 Steam Deck 掌机原生系统 (SteamOS) 部署全自动翻墙，加速 Steam 商店与游戏更新。",
        "symptoms": [
            "Steam Deck 掌机进入商店一直转圈报错无法进入",
            "外服 Apex 或怪物猎人联机延迟极高容易掉线",
            "切换到桌面模式配置好代理，一回到游戏模式又失效"
        ],
        "rootCauses": [
            "SteamOS 基于 Arch Linux 构建，只读根文件系统保护导致常规安装重启后被抹除"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：在桌面模式使用 Flatpak 安装 Clash Verge",
                "detail": "切换到桌面模式 (Desktop Mode)，在 Discover 软件中心搜索并安装 Clash Verge Rev Flatpak 封装版。"
            },
            {
                "stepTitle": "步骤 2：开启服务模式并设置开机自启 systemd 守护服务",
                "detail": "导入机场订阅并开启 TUN 模式，TUN 模式会作为虚拟网卡直接驻留在操作系统网络栈底层，即使切换回掌机游戏模式依然完美常驻生效！"
            }
        ],
        "faqTips": "Steam Deck 配备香港专线后，在被窝里随时逛商店、秒连好友房间开黑体验极佳。",
        "relatedSlugs": ["lan-share-proxy-switch-ps5-xbox", "steam-community-error-101-118"]
    },
    {
        "id": "faq-146",
        "slug": "kindle-kobo-ereader-proxy-sync",
        "title": "Kindle 与 Kobo 电子书阅读器走代理同步海外书库设置指南",
        "category": "hardware",
        "categoryLabel": "多端设备与系统专病",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "水墨屏阅读器同步亚马逊美区 Kindle 商店或乐天 Kobo 书库的网络打通指南。",
        "symptoms": [
            "Kindle 登录美区 Amazon 账号时提示无法连接到服务器",
            "Kobo 电子书商店一直在同步中无法下载已购图书"
        ],
        "rootCauses": [
            "电子书水墨屏系统功能精简，缺乏直接安装 VPN 应用的能力"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：利用电脑开启局域网代理共享",
                "detail": "在电脑 Clash 中开启「允许局域网连接」，在 Kindle 连上同一个 Wi-Fi 后，长按该 Wi-Fi 选择「修改网络」-> 开启代理并填入电脑 IP 与 7890 端口。"
            },
            {
                "stepTitle": "步骤 2：同步完成后关闭代理节省电量",
                "detail": "电子书同步完毕后将 Wi-Fi 代理关闭，避免长时间开启增加墨水屏设备的待机功耗。"
            }
        ],
        "faqTips": "或者直接利用手机热点翻墙分享给阅读器，便携且免去配置路由器的麻烦。",
        "relatedSlugs": ["lan-share-proxy-switch-ps5-xbox", "smart-home-iot-bypass-proxy"]
    },
    {
        "id": "faq-147",
        "slug": "vr-meta-quest-3-sidequest-proxy",
        "title": "Meta Quest 3 / Pico 4 VR 一体机科学上网与游戏联机方案",
        "category": "hardware",
        "categoryLabel": "多端设备与系统专病",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "VR 玩家初次激活 Meta Quest 3、下载 Beat Saber 联机歌单的保姆级穿透指南。",
        "symptoms": [
            "Quest 3 首次开机佩戴提示无网络连接无法完成初始系统更新与配对",
            "Meta Quest Store 商店无法加载应用列表"
        ],
        "rootCauses": [
            "Quest 3 系统基于 Android 开源底层构建，初次开机强依赖 Oculus/Meta 服务器激活"
        ],
        "solutions": [
            {
                "stepTitle": "方案 A：使用电脑开热点配合 TUN 模式（开机激活最推荐）",
                "detail": "在笔记本电脑上开启 Clash Verge TUN 模式，然后开启 Windows 移动热点；Quest 3 连接该热点即可实现全局透明翻墙，轻松完成初始固件更新激活！"
            },
            {
                "stepTitle": "方案 B：激活后通过 SideQuest 侧载安装安卓版 Clash APK",
                "detail": "激活进入系统后，通过 SideQuest 将 APK 安装进头显，在「未知来源」中即可直接用手柄点击运行开启代理。"
            }
        ],
        "faqTips": "VR 游戏对延迟极其敏感，玩外服联机时强烈建议搭配香港或日本 IPLC 专线以防眩晕和卡顿。",
        "relatedSlugs": ["lan-share-proxy-switch-ps5-xbox", "error-udp-nat-symmetric-restricted"]
    },
    {
        "id": "faq-148",
        "slug": "smart-home-iot-bypass-proxy",
        "title": "避免小米 / 米家 / 涂鸦智能家居设备误走代理导致离线的规则",
        "category": "hardware",
        "categoryLabel": "多端设备与系统专病",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "在全屋软路由部署透明代理时，防止扫地机器人、智能门锁、摄像头莫名其妙频繁掉线离线。",
        "symptoms": [
            "软路由开启代理后，米家 App 里多款智能灯具显示离线",
            "小爱同学经常提示「网络连接出现问题」"
        ],
        "rootCauses": [
            "智能家居硬件使用的私有长连接心跳通道被代理核心强制接管拦截，导致与国内云端心跳超时"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：在路由器中通过 MAC / IP 地址设立「智能设备直连绕过名单」",
                "detail": "在 OpenClash 或旁路由访问控制中，将全家所有智能家居设备的局域网 IP（或通过固定 DHCP 分配）加入「不走核心直连白名单」。"
            },
            {
                "stepTitle": "步骤 2：添加米家与涂鸦全系云平台直连域名规则",
                "detail": "在 rules 中加入 DOMAIN-SUFFIX,mi.com,DIRECT 和 DOMAIN-SUFFIX,tuya.com,DIRECT。"
            }
        ],
        "faqTips": "智能家居全部排除在代理之外是保证家庭智能网络稳固不折腾的基本底线。",
        "relatedSlugs": ["openwrt-openclash-double-routing-crash", "bypass-private-lan-ip-clash"]
    },
    {
        "id": "faq-149",
        "slug": "ipad-split-view-proxy-rules",
        "title": "iPadOS 分屏多任务办公场景下 Safari 与文献查阅的分流规则优化",
        "category": "hardware",
        "categoryLabel": "多端设备与系统专病",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "iPad 生产力玩家边开微信写笔记、边在 Safari 查阅海外文献时的无缝分流调优。",
        "symptoms": [
            "在 iPad 上分屏使用微信和海外学术网站，微信收发文件变得极慢"
        ],
        "rootCauses": [
            "iPad 端的 Shadowrocket 或 Loon 分流规则未细化，国内通讯与海外科研流量混杂"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：在小火箭中使用精细化的规则配置分组",
                "detail": "规则模式选用「配置」，并确保国内应用 (CN) 指向 DIRECT 直连，海外学术域名指向高速学术专线。"
            },
            {
                "stepTitle": "步骤 2：在控制中心添加一键切换快捷小组件",
                "detail": "利用 iOS 快捷指令添加小火箭开关组件，在不需要查资料时轻触即可关闭代理省电。"
            }
        ],
        "faqTips": "iPad 搭配规则分流，完全可以实现微信秒发、海外 Google 文献秒开的无缝混合办公体验。",
        "relatedSlugs": ["domestic-speed-slow-when-proxy-on", "shadowrocket-node-group-auto-test"]
    },
    {
        "id": "faq-150",
        "slug": "carplay-in-car-screen-proxy-network",
        "title": "CarPlay 与 Android 车机系统安装代理软件导航与流媒体播放指南",
        "category": "hardware",
        "categoryLabel": "多端设备与系统专病",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "在特斯拉、造车新势力或通用 Android 大屏车机上播放海外 Spotify、YouTube 音乐的技巧。",
        "symptoms": [
            "车机连上手机热点后，车机自带的高德/百度地图导航提示网络受阻",
            "在车机端使用第三方浏览器无法播放海外音乐"
        ],
        "rootCauses": [
            "车载车机默认流量卡走的是受限的车联网专网通道，无法直接建立境外代理隧道"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：利用手机无线 CarPlay / 热点作为代理跳板",
                "detail": "iPhone 开启代理后连接无线 CarPlay，车机端屏幕映射的 Spotify 会直接继承手机端的科学上网链路，车载地图导航则依然走国内直连，互不冲突！"
            },
            {
                "stepTitle": "步骤 2：开放式 Android 车机（如比亚迪、吉利等）可直接侧载 APK",
                "detail": "在开放车机上通过应用市场安装 v2rayNG，设置「分应用代理」仅勾选媒体播放软件，确保不影响车辆本身的远程车控与 OTA 升级。"
            }
        ],
        "faqTips": "车机系统关乎驾驶安全，严禁对核心行车仪表及辅助驾驶网络做任何全局代理接管，仅限制在娱乐 App 即可。",
        "relatedSlugs": ["spotify-change-country-gray-songs", "v2rayng-battery-optimization-kill"]
    }
]

print(f"Loaded {len(HARDWARE_FAQS)} hardware FAQs.")
