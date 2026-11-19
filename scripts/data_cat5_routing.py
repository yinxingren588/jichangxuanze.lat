# -*- coding: utf-8 -*-
# Category 5: 系统分流与局域网网络穿透 (20 篇)

ROUTING_FAQS = [
    {
        "id": "faq-86",
        "slug": "domestic-speed-slow-when-proxy-on",
        "title": "开启代理后国内微信/百度/淘宝/京东极慢排查与加速优化",
        "category": "routing",
        "categoryLabel": "系统分流与穿透",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "新手最常遇到的痛点：开启科学上网后外网秒开了，但国内微信发不出去、淘宝打不开的彻底优化。",
        "symptoms": [
            "打开代理软件后，微信电脑版发送图片一直转圈",
            "淘宝、京东、B站首页加载极其缓慢，视频只能看 360P 标清",
            "网易云音乐提示因版权限制无法在当前地区播放"
        ],
        "rootCauses": [
            "客户端被错误地设置成了「全局模式 (Global)」，导致国内淘宝微信流量全部绕道香港/美国再绕回国内，延迟暴增且白白浪费机场流量",
            "分流规则中缺失了针对中国大陆域名与 IP 段的 GEOIP:CN / GEOSITE:CN 直连规则",
            "DNS 解析发生严重污染，国内域名被解析到了境外无 CDN 的远端服务器"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：必须且务必将客户端切换为「规则模式 (Rule)」",
                "detail": "在 Clash Verge Rev、Mihomo 或小火箭中，将运行模式从「全局 (Global)」切换为「规则 (Rule)」。在规则模式下，只有被封锁的境外网站走代理，国内所有流量自动原速直连！"
            },
            {
                "stepTitle": "步骤 2：优化 DNS 分流配置（国内域名国内解析）",
                "detail": "在客户端配置中，确保 default-nameserver 和 nameserver 包含国内权威 DNS（223.5.5.5 和 119.29.29.29），让国内网站解析到离你家最近的本地 CDN 机房。"
            },
            {
                "stepTitle": "步骤 3：更新 GeoIP / GeoSite 官方大陆白名单数据库",
                "detail": "在客户端设置中点击更新 GeoIP 数据库，确保最新的中国企业网段不会被误杀判定为境外流量。"
            }
        ],
        "faqTips": "规则模式是科学上网最科学、最优雅的常驻方案，日常挂着不用关，国内国外两不误。",
        "relatedSlugs": ["global-vs-rule-vs-direct-difference", "clash-tun-fake-ip-vs-redir-host"]
    },
    {
        "id": "faq-87",
        "slug": "lan-share-proxy-switch-ps5-xbox",
        "title": "将电脑代理局域网共享给 Switch / PS5 / Xbox 主机下载联机加速",
        "category": "routing",
        "categoryLabel": "系统分流与穿透",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "无需购买额外的主机加速盒，利用手头 Windows / Mac 电脑为游戏主机提供满速下载与 NAT 优化的保姆级教程。",
        "symptoms": [
            "Switch 商店 eShop 一直打不开报错 2811-7503",
            "PS5 游戏下载只有几百 KB/s，更新大补丁需要十几天",
            "Xbox 联机 NAT 类型显示为严格或不可用"
        ],
        "rootCauses": [
            "游戏主机默认不具备直接安装 Clash/Sing-box 等第三方开源代理客户端的能力"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：在电脑端开启「允许局域网连接 (Allow LAN)」",
                "detail": "打开 Clash Verge Rev 设置 -> 勾选「允许局域网连接 (Allow LAN)」，记录下电脑本机的局域网 IP（如 192.168.1.100）和混合端口（通常为 7890）。"
            },
            {
                "stepTitle": "步骤 2：在游戏主机中手动配置网络代理",
                "detail": "在 Switch/PS5 的网络设置中，选择当前 Wi-Fi ->「更改设置」-> 将「代理服务器 (Proxy)」改为「使用」->「服务器地址」填入电脑的局域网 IP（192.168.1.100），「端口号」填入 7890，保存连接即可！"
            },
            {
                "stepTitle": "步骤 3：在电脑防火墙中允许 7890 端口入站",
                "detail": "如果主机连接测试失败，在 Windows 防火墙中添加一条允许入站规则，放行 TCP 7890 端口即可畅通无阻。"
            }
        ],
        "faqTips": "下载游戏时，在电脑客户端选择不限速的大带宽专线节点，Switch/PS5 即可轻松跑满家庭百兆宽带。",
        "relatedSlugs": ["error-udp-nat-symmetric-restricted", "bypass-steam-epic-game-download"]
    },
    {
        "id": "faq-88",
        "slug": "global-vs-rule-vs-direct-difference",
        "title": "全局代理 (Global)、规则分流 (Rule) 与直连 (Direct) 本质区别深度解析",
        "category": "routing",
        "categoryLabel": "系统分流与穿透",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "一文彻底搞懂代理客户端核心的三大分流工作模式，什么场景下该用哪种模式的终极指南。",
        "symptoms": [
            "不知道平时应该常驻哪种模式最省流量、速度最快",
            "不小心选了全局模式导致微信掉线或流量飞速耗尽",
            "选了直连模式以为在翻墙结果连 Google 都打不开"
        ],
        "rootCauses": [
            "模式概念混淆不清：规则 (Rule) 相当于智能导航，全局 (Global) 相当于一刀切全部出境，直连 (Direct) 相当于彻底不走代理"
        ],
        "solutions": [
            {
                "stepTitle": "模式 1：规则模式 (Rule) —— 99% 场景下的日常唯一首选",
                "detail": "智能判断目标域名。命中黑名单/海外域名的自动走代理节点；命中白名单/国内域名的自动走国内直连。完全不用手动干预，速度最快、最省流量。"
            },
            {
                "stepTitle": "模式 2：全局模式 (Global) —— 仅用于小众冷门网站应急排错",
                "detail": "不管访问什么网站（哪怕是百度），全部强行打包发往当前选中的海外节点。仅在遇到极冷门小众海外网站未被规则库收录、打不开时，临时开启测试排查。"
            },
            {
                "stepTitle": "模式 3：直接连接 (Direct) —— 相当于完全关闭代理功能",
                "detail": "所有流量均不通过任何境外节点，直接从你的物理网卡发出，相当于没有打开科学上网软件。"
            }
        ],
        "faqTips": "记住日常永远保持在「规则模式 (Rule)」即可，省心、极速、无感加速。",
        "relatedSlugs": ["domestic-speed-slow-when-proxy-on", "clash-verge-custom-rules-override"]
    },
    {
        "id": "faq-89",
        "slug": "openwrt-openclash-double-routing-crash",
        "title": "软路由 OpenClash 开启后断网或与主路由 DHCP 冲突终极排错",
        "category": "routing",
        "categoryLabel": "系统分流与穿透",
        "readTime": "6 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "在 OpenWrt 软路由 / 旁路由中部署 OpenClash 常见的大陆白名单失效、网关死锁与断网处理。",
        "symptoms": [
            "软路由安装并启动 OpenClash 后，整屋设备瞬间无法上网",
            "后台不断报错：Can not resolve github.com / Core stopped",
            "局域网内部设备互 ping 丢包率高达 50%"
        ],
        "rootCauses": [
            "旁路由开启了自身的 DHCP 服务器，导致局域网内存在两个 DHCP 发生 IP 冲突",
            "防火墙自定义规则中没有添加正确的 MASQUERADE 伪装规则，导致上行数据包回包路径混乱",
            "DNS 53 端口被系统默认的 Dnsmasq 占死，OpenClash 无法接管"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：旁路由务必关闭自身 DHCP 并设置网关指向主路由",
                "detail": "在 OpenWrt「网络」->「接口」->「LAN」->「DHCP 服务器」，勾选「忽略此接口」（彻底关闭 DHCP）；网关和 DNS 均填入主路由 IP（如 192.168.1.1）。"
            },
            {
                "stepTitle": "步骤 2：在 OpenWrt 防火墙添加经典的 IP 伪装规则",
                "detail": "进入「网络」->「防火墙」->「自定义规则」，在末尾添加以下一行规则并重启防火墙：",
                "code": "iptables -t nat -A POSTROUTING -o br-lan -j MASQUERADE"
            },
            {
                "stepTitle": "步骤 3：运行模式优先选择「Meta-TUN (Fake-IP)」模式",
                "detail": "OpenClash 高级设置中，将运行模式切换为 Meta 内核的 TUN 混合模式，兼容性与吞吐性能最佳。"
            }
        ],
        "faqTips": "软路由配置复杂，如果只是个人电脑或手机使用，直接安装单机版 Clash Verge Rev 体验往往比折腾软路由更省心稳定。",
        "relatedSlugs": ["clash-tun-fake-ip-vs-redir-host", "surge-enhanced-mode-router-gateway"]
    },
    {
        "id": "faq-90",
        "slug": "clash-verge-custom-rules-override",
        "title": "如何在 Clash Verge Rev 中添加自定义直连与代理规则 (完整语法示范)",
        "category": "routing",
        "categoryLabel": "系统分流与穿透",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "教你通过扩展配置 (Merge / Script) 自主添加指定网站走直连、特定内网 IP 走代理的高级技巧。",
        "symptoms": [
            "公司内部办公系统或特定校园网域名被误判走了代理导致无法登录",
            "想让某个小众海外生肉漫画网站固定走日本高速专线"
        ],
        "rootCauses": [
            "通用公共订阅的规则库不可能覆盖全网所有私有或小众域名，需要个性化前置规则覆盖"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：新建一个 Merge 类型的订阅扩展",
                "detail": "打开 Clash Verge Rev ->「订阅」-> 在顶部点击「新建」-> 类型选择「Merge」，命名为「我的自定义分流规则」。"
            },
            {
                "stepTitle": "步骤 2：按标准语法编写前置规则并置顶",
                "detail": "在 rules 列表顶部添加你的特定域名规则。Clash 是自上而下匹配的，写在最顶部的规则拥有最高优先级！",
                "code": "prepend-rules:\n  # 让公司内部域名绝对直连\n  - DOMAIN-SUFFIX,company-internal.com,DIRECT\n  - IP-CIDR,192.168.0.0/16,DIRECT,no-resolve\n  # 让特定学术网站强制走代理专线\n  - DOMAIN-SUFFIX,sciencedirect.com,PROXY\n  - DOMAIN-KEYWORD,torrent,REJECT"
            },
            {
                "stepTitle": "步骤 3：右键启用并保存",
                "detail": "在扩展配置列表中，右键该条目点击「启用」，随后右键你的机场订阅点击「刷新」，自定义规则即刻永久生效！"
            }
        ],
        "faqTips": "建议优先使用 prepend-rules（前置规则），防止自定义规则被机场自带的基础规则淹没在底部失效。",
        "relatedSlugs": ["clash-verge-script-override-error", "bypass-private-lan-ip-clash"]
    },
    {
        "id": "faq-91",
        "slug": "campus-network-port-blocking-bypass",
        "title": "校园网或公司内网封锁非 80/443 端口代理的突破方案",
        "category": "routing",
        "categoryLabel": "系统分流与穿透",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "在大学校园网、医院或严格企业网络中，只放行 Web 端口、封死全部非常规端口的高效突破手段。",
        "symptoms": [
            "在普通家里宽带用得好好的节点，到了大学宿舍或公司内网后所有节点全部报 Timeout 超时",
            "用手机热点可以正常翻墙，切换到校园网有线/无线瞬间瘫痪",
            "网络管理中心开启了严格的防火墙端口白名单机制"
        ],
        "rootCauses": [
            "企业或高校的防火墙配置了严格的安全策略，仅允许目的端口为 80 (HTTP) 和 443 (HTTPS) 的连接流出，而大部分机场节点的公网端口是 10000~60000 的随机高位端口"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：在节点列表中挑选目标端口为 443 的专用节点",
                "detail": "观察节点列表中的端口号，挑选使用 Trojan 或 Vless 且端口标明为 443 的节点。防火墙会将其直接视为合法的标准 HTTPS 网页流量予以放行。"
            },
            {
                "stepTitle": "步骤 2：选用支持多端口复用或端口转发的优质机场",
                "detail": "优秀的机场（如飞V、隐形人）通常提供专用的「443 穿透专线」或支持全端口复用，专为校园网与严苛内网环境设计。"
            }
        ],
        "faqTips": "在学校宿舍连不上千万别以为是机场跑路了，优先看一眼节点端口是不是被校园网防火墙给掐了。",
        "relatedSlugs": ["error-dial-tcp-timeout-10000ms", "error-tls-handshake-timeout"]
    },
    {
        "id": "faq-92",
        "slug": "wsl2-ubuntu-windows-proxy-setup",
        "title": "Windows 11 WSL2 子系统共享宿主机 Clash 代理一键配置脚本",
        "category": "routing",
        "categoryLabel": "系统分流与穿透",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "开发者在 Windows WSL2 (Ubuntu) 命令行中运行 apt update、git clone 极速共享主机代理的配置。",
        "symptoms": [
            "Windows 宿主机网页可以正常秒开 Google，但 WSL2 终端里运行 git clone 动辄超时卡死",
            "设置了 export http_proxy=http://127.0.0.1:7890 提示 Connection refused"
        ],
        "rootCauses": [
            "WSL2 采用独立的 Hyper-V 虚拟机架构，WSL 内部的 127.0.0.1 指的是 WSL 自己内部，并不是 Windows 宿主机的 IP！"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：确保 Windows 客户端开启「Allow LAN (允许局域网连接)」",
                "detail": "在 Clash Verge Rev 中开启「允许局域网连接」，使宿主机端口允许来自虚拟子网网段的请求。"
            },
            {
                "stepTitle": "步骤 2：在 WSL2 的 ~/.bashrc 中写入自动提取宿主机 IP 脚本",
                "detail": "在 WSL 终端中运行 nano ~/.bashrc，在文件末尾追加以下快捷函数：",
                "code": "# 自动获取 WSL2 对应的 Windows 宿主机网关 IP 并设置代理\nfunction set_proxy() {\n  host_ip=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}')\n  export http_proxy=\"http://${host_ip}:7890\"\n  export https_proxy=\"http://${host_ip}:7890\"\n  export all_proxy=\"socks5://${host_ip}:7890\"\n  echo \"[+] Proxy set to ${host_ip}:7890\"\n}\n\nfunction unset_proxy() {\n  unset http_proxy https_proxy all_proxy\n  echo \"[-] Proxy cleared.\"\n}"
            },
            {
                "stepTitle": "步骤 3：source 生效并一行命令开启",
                "detail": "运行 source ~/.bashrc，之后每次需要翻墙只需在终端输入 set_proxy 回车，立即享受千兆极速代理！"
            }
        ],
        "faqTips": "最新的 Windows 11 已支持 WSL 镜像网络模式 (Mirrored Mode)，开启镜像模式后 WSL2 与 Windows 完全共享同一个 localhost，更加无脑丝滑。",
        "relatedSlugs": ["git-clone-github-ssh-proxy-config", "pip-conda-npm-proxy-terminal"]
    },
    {
        "id": "faq-93",
        "slug": "docker-daemon-pull-images-proxy",
        "title": "Docker 国内镜像大面积失效与配置代理拉取镜像指南",
        "category": "routing",
        "categoryLabel": "系统分流与穿透",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "针对目前国内各大 Docker 镜像源大面积下线停服，导致 docker pull 报超时失败的工程配置。",
        "symptoms": [
            "docker pull ubuntu 提示：Error response from daemon: Get https://registry-1.docker.io/v2/: net/http: request canceled",
            "原本可用的第三方国内镜像加速地址全部返回 404 或 403 无法拉取镜像"
        ],
        "rootCauses": [
            "官方 Docker Hub 在国内遭到深度阻断，且政策原因导致国内几乎所有公开镜像站关闭",
            "Docker Daemon 守护进程是系统底层服务，不会自动走当前用户的桌面 HTTP 代理"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：为 Docker Daemon 服务配置 systemd 专用代理环境",
                "detail": "在 Linux 服务器上创建服务配置覆盖目录，写入 HTTP_PROXY 环境变量并重启 Docker。",
                "code": "sudo mkdir -p /etc/systemd/system/docker.service.d\nsudo tee /etc/systemd/system/docker.service.d/http-proxy.conf <<EOF\n[Service]\nEnvironment=\"HTTP_PROXY=http://127.0.0.1:7890\"\nEnvironment=\"HTTPS_PROXY=http://127.0.0.1:7890\"\nEnvironment=\"NO_PROXY=localhost,127.0.0.1,docker-registry.somecorporation.com\"\nEOF\n\nsudo systemctl daemon-reload\nsudo systemctl restart docker"
            },
            {
                "stepTitle": "步骤 2：Windows / Mac 桌面端 Docker Desktop 配置",
                "detail": "直接打开 Docker Desktop 设置 ->「Resources」->「Proxies」-> 开启「Manual proxy configuration」-> Web Server 填 http://127.0.0.1:7890，点击「Apply & restart」即可秒速拉取全球镜像。"
            }
        ],
        "faqTips": "配置完成后，运行 docker info 检查输出最下方的 HTTP Proxy 项，确认代理参数是否已经生效加载。",
        "relatedSlugs": ["wsl2-ubuntu-windows-proxy-setup", "curl-wget-terminal-proxy-environment"]
    },
    {
        "id": "faq-94",
        "slug": "git-clone-github-ssh-proxy-config",
        "title": "Git 命令行与 SSH 访问 GitHub 极慢的代理配置实用技巧",
        "category": "routing",
        "categoryLabel": "系统分流与穿透",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "手把手指导如何为 git clone (无论是 HTTPS 还是 git@github.com SSH 协议) 配置高速代理。",
        "symptoms": [
            "git clone 仓库长时间卡在 Cloning into... 速度只有 10 KB/s",
            "报错：Failed to connect to github.com port 443: Timed out",
            "SSH 协议报错：ssh: connect to host github.com port 22: Connection timed out"
        ],
        "rootCauses": [
            "Git 默认使用系统底层的独立网络套接字，不会自动感知图形界面的系统代理开关"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：为 Git HTTPS 协议一键配置全局代理",
                "detail": "在终端中运行以下两行命令，将 Git 的 HTTP 和 HTTPS 流量统一转发至 Clash 混合端口：",
                "code": "git config --global http.proxy \"http://127.0.0.1:7890\"\ngit config --global https.proxy \"http://127.0.0.1:7890\""
            },
            {
                "stepTitle": "步骤 2：为 SSH 密钥协议配置 ~/.ssh/config 转发",
                "detail": "如果使用 git@github.com 形式 clone，编辑用户目录下的 ~/.ssh/config 文件，添加 connect 命令中转：",
                "code": "Host github.com\n  User git\n  ProxyCommand connect -H 127.0.0.1:7890 %h %p"
            }
        ],
        "faqTips": "如果要取消 Git 代理，只需运行 git config --global --unset http.proxy 即可随时恢复默认状态。",
        "relatedSlugs": ["pip-conda-npm-proxy-terminal", "github-copilot-proxy-wsl-ide"]
    },
    {
        "id": "faq-95",
        "slug": "pip-conda-npm-proxy-terminal",
        "title": "Python pip、conda、npm 终端命令行代理环境变量终极设置",
        "category": "routing",
        "categoryLabel": "系统分流与穿透",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "开发者在命令行执行 pip install、npm install、conda install 频繁超时的优雅解决办法。",
        "symptoms": [
            "pip install 报 ReadTimeoutError 或 HTTPSConnectionPool Max retries exceeded",
            "npm install 卡在 idealTree: sill install loadTypicalDeps 无反应",
            "Anaconda 下载第三方库几 KB/s 甚至直接断开"
        ],
        "rootCauses": [
            "各大包管理器默认不会走浏览器的代理，必须读取系统环境变数或专用配置文件"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：PowerShell / CMD 快速设置临时会话环境变量",
                "detail": "在执行安装命令的同一个终端窗口中，先输入以下指令即可瞬间打通网络：",
                "code": "# PowerShell 中运行：\n$env:http_proxy=\"http://127.0.0.1:7890\"\n$env:https_proxy=\"http://127.0.0.1:7890\"\n\n# 随后直接正常执行安装：\npip install torch"
            },
            {
                "stepTitle": "步骤 2：直接开启 Clash Verge Rev 的 TUN 模式（一劳永逸）",
                "detail": "开启 TUN 模式后，虚拟网卡在驱动层接管全机流量，pip/npm/conda 自动享受透明代理加速，无需修改任何代码和环境变量！"
            }
        ],
        "faqTips": "临时设置环境变量仅对当前打开的终端小黑窗有效，关闭窗口后自动失效，不会污染整机开发环境。",
        "relatedSlugs": ["git-clone-github-ssh-proxy-config", "huggingface-model-download-proxy"]
    },
    {
        "id": "faq-96",
        "slug": "bypass-private-lan-ip-clash",
        "title": "避免局域网 NAS (192.168.x.x) 访问误走代理的白名单配置",
        "category": "routing",
        "categoryLabel": "系统分流与穿透",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "开启代理或 TUN 模式后，局域网共享打印机断开、群晖 NAS 与路由器管理后台进不去的排错。",
        "symptoms": [
            "开启客户端后，访问 192.168.1.1 路由器登录后台提示拒绝连接",
            "访问局域网 NAS (群晖/威联通/极空间) 极其缓慢，文件传输直接超时",
            "无法连接办公室局域网共享打印机"
        ],
        "rootCauses": [
            "TUN 模式或全局模式把发往私有保留 IP 段（192.168.x.x、10.x.x.x）的流量也当作公网流量打包丢给了境外节点"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：在 Clash Verge 中添加系统代理跳过名单 (Bypass)",
                "detail": "在客户端「系统代理」设置的「绕过域名/IP」列表里，确保包含以下私有网段：",
                "code": "localhost; 127.*; 10.*; 172.16.*; 172.17.*; 172.18.*; 172.19.*; 172.20.*; 172.21.*; 172.22.*; 172.23.*; 172.24.*; 172.25.*; 172.26.*; 172.27.*; 172.28.*; 172.29.*; 172.30.*; 172.31.*; 192.168.*; <local>"
            },
            {
                "stepTitle": "步骤 2：确保分流规则置顶私有 IP 直连",
                "detail": "在规则 rules 列表最顶部添加：GEOIP,private,DIRECT,no-resolve，让核心直接放行所有本地内网通信。"
            }
        ],
        "faqTips": "如果访问群晖使用的是自建的二级域名（如 nas.myhome.com），请务必在分流规则中将该私有域名显式划为 DIRECT 直连。",
        "relatedSlugs": ["clash-verge-custom-rules-override", "synology-nas-docker-proxy-download"]
    },
    {
        "id": "faq-97",
        "slug": "clash-tun-fake-ip-vs-redir-host",
        "title": "Fake-IP 与 Redir-Host 模式有什么本质区别？到底该怎么选？",
        "category": "routing",
        "categoryLabel": "系统分流与穿透",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "从底层原理解析 Clash 两种 DNS 接管模式的优劣势，为你挑选最佳配置方案。",
        "symptoms": [
            "不知道在 Clash 设置中该勾选 Fake-IP 还是 Redir-Host",
            "看到 ping 任何外网域名都返回 198.18.0.x 以为系统中毒中招"
        ],
        "rootCauses": [
            "Fake-IP 模式：本地直接返回一个虚拟 IP（198.18.x.x），真正的 DNS 查询推迟到远端代理节点完成，彻底杜绝本地 DNS 污染，首包响应速度极快！",
            "Redir-Host 模式：本地必须先拿到目标网站的真实 IP 才能建立代理，在国内易遭 DNS 污染导致连不上"
        ],
        "solutions": [
            {
                "stepTitle": "结论与推荐：99% 的场景无脑选用「Fake-IP 模式」",
                "detail": "Fake-IP 是现代科学上网的标准规范。它完全避免了本地向国内运营商询问 Google IP 导致的污染拦截，网页打开速度比 Redir-Host 快 200ms 以上！"
            },
            {
                "stepTitle": "仅在一种情况下使用 Redir-Host：极小众老旧局域网软路由应用",
                "detail": "只有当你的局域网内存在某些必须校验真实 IP 且对 198.18 虚拟 IP 报错的老旧物联网设备时，才考虑切换回 Redir-Host。"
            }
        ],
        "faqTips": "只要你在电脑上使用 Clash Verge Rev 或 Mihomo Party，保持默认的 Fake-IP 模式就是最强性能。",
        "relatedSlugs": ["dns-leak-detection-fix", "domestic-speed-slow-when-proxy-on"]
    },
    {
        "id": "faq-98",
        "slug": "surge-enhanced-mode-router-gateway",
        "title": "Surge 网关模式 (Router Gateway) 为全家所有设备托管翻墙方案",
        "category": "routing",
        "categoryLabel": "系统分流与穿透",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "利用一台闲置的 Mac mini 或日常开机的 Mac 电脑运行 Surge，让全屋电视、音响免装软件翻墙。",
        "symptoms": [
            "电视 Apple TV、小天才电话手表、扫地机器人等无法安装代理软件",
            "不想折腾经常崩溃死机的硬路由固件"
        ],
        "rootCauses": [
            "Surge Mac 版具备顶级的虚拟网络网关能力，可以向局域网广播自己作为主路由网关"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：在 Mac 版 Surge 中开启「增强模式」与「网关模式」",
                "detail": "进入 Surge Mac 偏好设置 -> 勾选「增强模式」，在「网关」选项卡中勾选开启「充当局域网网关与 DHCP 服务器」。"
            },
            {
                "stepTitle": "步骤 2：在目标设备上修改网关与 DNS 指向 Mac 的 IP",
                "detail": "例如将 Apple TV 的 IPv4 设为手动，IP 填 192.168.1.50，子网掩码 255.255.255.0，路由器/网关填 Mac 的 IP（192.168.1.88），DNS 填 192.168.1.88 即可！"
            }
        ],
        "faqTips": "Surge 网关模式极其稳定且具备可视化的全设备流量抓包面板，是果粉家庭网络的终极形态。",
        "relatedSlugs": ["apple-tv-tvos-surge-clash-proxy", "lan-share-proxy-switch-ps5-xbox"]
    },
    {
        "id": "faq-99",
        "slug": "adguard-home-clash-dns-coexistence",
        "title": "AdGuard Home 去广告与 Clash 分流 DNS 完美共存架构设计",
        "category": "routing",
        "categoryLabel": "系统分流与穿透",
        "readTime": "6 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "家庭极客搭建全屋去广告与智能科学上网时，避免 DNS 互相争抢端口与死循环回环的标准拓扑图。",
        "symptoms": [
            "同时开启 AdGuard Home 和 Clash 后，全家设备无法上网",
            "日志显示 53 端口冲突或 DNS queries loop",
            "广告被拦截了但翻墙失效，或者翻墙正常但广告拦截失效"
        ],
        "rootCauses": [
            "两者在处理 DNS 请求时形成首尾相接的无限死循环"
        ],
        "solutions": [
            {
                "stepTitle": "黄金架构：客户端 -> AdGuard Home (去广告) -> Clash (智能分流) -> 公网",
                "detail": "让设备把 DNS 查询先交给 AdGuard Home（过滤广告规则与跟踪脚本），过滤后的干净请求再作为上游交给 Clash 进行智能出海分流。"
            },
            {
                "stepTitle": "步骤 2：端口精细化配置",
                "detail": "将 AdGuard Home 监听在系统标准 53 端口上；将 Clash 内置 DNS 监听在非标端口 1053 上。在 AdGuard Home 的上游 DNS 中填入 127.0.0.1:1053 即可。"
            }
        ],
        "faqTips": "这种分工明确的链路架构既能享受到秒级无广告的清爽网页，又能保证境外流量精准分流。",
        "relatedSlugs": ["dns-leak-detection-fix", "openwrt-openclash-double-routing-crash"]
    },
    {
        "id": "faq-100",
        "slug": "tailscale-wireguard-clash-conflict",
        "title": "Tailscale / ZeroTier 虚拟组网与 Clash TUN 模式路由冲突排查",
        "category": "routing",
        "categoryLabel": "系统分流与穿透",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "远程办公时同时使用 Tailscale/WireGuard 组网工具和科学上网，导致无法访问公司内网的解决。",
        "symptoms": [
            "开启 Clash TUN 后，原本可以连通的远程 NAS 或公司服务器 (100.x.x.x) 突然全部 ping 不通",
            "Tailscale 图标频繁黄灯提示 reconnecting",
            "关掉 Clash 后远程连接立即恢复"
        ],
        "rootCauses": [
            "Clash 的 TUN 模式默认创建了一条覆盖全局 0.0.0.0/0 的默认路由，其跃点数 (Metric) 高于 Tailscale 虚拟网卡，强行捕获了组网流量"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：将 Tailscale 虚拟网段排除在 TUN 之外",
                "detail": "在 Clash 的 tun 配置中，使用 route-exclude-address 显式排除 CGNAT 组网保留网段 100.64.0.0/10。",
                "code": "tun:\n  enable: true\n  stack: mixed\n  route-exclude-address:\n    - 100.64.0.0/10\n    - 192.168.0.0/16"
            },
            {
                "stepTitle": "步骤 2：在分流规则中设置 Tailscale 节点直连",
                "detail": "在 rules 中追加：IP-CIDR,100.64.0.0/10,DIRECT,no-resolve，让组网打洞流量直接原路返回。"
            }
        ],
        "faqTips": "排除后，外网科学上网走高速专线，公司与家里设备互通走 Tailscale P2P 直连，二者互不干扰。",
        "relatedSlugs": ["bypass-private-lan-ip-clash", "clash-tun-mode-virtual-nic-fail"]
    },
    {
        "id": "faq-101",
        "slug": "multi-wan-load-balancing-proxy",
        "title": "双软路由 / 双宽带叠加环境下的多 WAN 口代理分流高级设置",
        "category": "routing",
        "categoryLabel": "系统分流与穿透",
        "readTime": "5 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "家里同时拉了电信+移动双宽带进行负载均衡叠加时，防止代理连接不断断线重连的策略。",
        "symptoms": [
            "网页频繁提示需要重新登录，会话频繁失效",
            "玩外服游戏时每隔几分钟跳出一次网络异常",
            "单线程下载速度在两条宽带之间来回震荡"
        ],
        "rootCauses": [
            "多 WAN 负载均衡采用了按数据包 (Per-Packet) 轮询，导致同一个代理 TCP 握手的前后两个包从不同的宽带公网 IP 发出，被机场服务端安全防火墙判定为非法串流而强制断连！"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：将多 WAN 策略修改为「按源与目的 IP 绑定 (Source/Dest IP Hash)」",
                "detail": "在主路由 MWAN3 策略中，确保将同一台设备发往同一个目的地的连接固定在同一条物理宽带上，杜绝出口 IP 漂移。"
            },
            {
                "stepTitle": "步骤 2：指定所有出境代理流量走质量更优的电信/联通宽带",
                "detail": "移动宽带晚高峰国际出口丢包高，建议在路由器策略路由中，将所有代理端口 (7890/443) 强制绑定走电信或联通宽带出境。"
            }
        ],
        "faqTips": "双宽带叠加适合国内大文件下载，但对于科学上网和外服联机，稳定的单一出口比盲目叠加更重要。",
        "relatedSlugs": ["openwrt-openclash-double-routing-crash", "error-connection-reset-by-peer"]
    },
    {
        "id": "faq-102",
        "slug": "wechat-bank-app-proxy-risk-control",
        "title": "手机开着代理登录手机银行或微信支付跳风控预防方案",
        "category": "routing",
        "categoryLabel": "系统分流与穿透",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "防止手机开着科学上网时打开招商银行、中国银行 App 提示「检测到境外异常登录」的规避攻略。",
        "symptoms": [
            "打开手机银行 App 提示风险控制，甚至被强制锁定非柜面交易",
            "微信支付突然要求重新刷脸人脸识别",
            "国内政务类 App 提示禁止境外 IP 访问"
        ],
        "rootCauses": [
            "手机客户端开启了全局模式，或者分流规则未收录最新的国内银行与金融结算中心域名，导致鉴权包绕道境外"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：必须开启客户端分流中的「应用分流 / 分应用代理」",
                "detail": "在安卓版 Clash 或 v2rayNG 中，开启「分应用代理 (Per-App Proxy)」，在列表中仅勾选 Chrome、YouTube、Telegram 等海外软件，将所有国内银行、微信、支付宝彻底排除在代理之外！"
            },
            {
                "stepTitle": "步骤 2：iOS 用户选用智能规则集",
                "detail": "iOS 小火箭用户确保分流模式为「配置」，且规则集中包含完整的 ChinaMax 白名单，金融金融类直连率 100%。"
            }
        ],
        "faqTips": "敏感金融类软件永远坚持纯原生国内直连，保障资金账户安全无风控。",
        "relatedSlugs": ["domestic-speed-slow-when-proxy-on", "global-vs-rule-vs-direct-difference"]
    },
    {
        "id": "faq-103",
        "slug": "curl-wget-terminal-proxy-environment",
        "title": "Linux / macOS 终端 curl 和 wget 走代理的 .bashrc 配置全解",
        "category": "routing",
        "categoryLabel": "系统分流与穿透",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "掌握命令行终端网络环境配置，一键让 bash/zsh 终端命令秒级走通代理的经典配置。",
        "symptoms": [
            "终端运行 curl -I https://google.com 报 Failed to connect port 443: Connection refused",
            "wget 下载海外脚本一直卡在 connecting to server...",
            "自动化运维脚本在无代理环境下报错失败"
        ],
        "rootCauses": [
            "标准 Unix 终端工具遵守环境变量标准，不会自动读取图形界面的操作系统代理注册表"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：在 ~/.bashrc 或 ~/.zshrc 中添加极简开关别名",
                "detail": "打开终端配置文件并追加以下函数别名：",
                "code": "alias proxy='export http_proxy=http://127.0.0.1:7890 https_proxy=http://127.0.0.1:7890 all_proxy=socks5://127.0.0.1:7890 && echo \"Proxy Enabled\"'\nalias unproxy='unset http_proxy https_proxy all_proxy && echo \"Proxy Disabled\"'\nalias myip='curl -L cip.cc'"
            },
            {
                "stepTitle": "步骤 2：执行 proxy 别名并验证当前出口 IP",
                "detail": "输入 proxy 回车即可开启，随后运行 myip 即可直接查看当前终端出口是否已经变成境外代理 IP。"
            }
        ],
        "faqTips": "此方法适用于 Ubuntu、CentOS、macOS 等所有标准 Unix 环境，简单优雅又可控。",
        "relatedSlugs": ["pip-conda-npm-proxy-terminal", "git-clone-github-ssh-proxy-config"]
    },
    {
        "id": "faq-104",
        "slug": "bilibili-taiwan-hk-unblock-rule",
        "title": "仅让 B站港澳台限定番剧走代理、普通视频走直连的分流规则配置",
        "category": "routing",
        "categoryLabel": "系统分流与穿透",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "B站追番党福利：教你如何精准配置分流，只让「仅限港澳台地区」的正版动漫走香港/台湾节点，其余视频全速走国内千兆直连。",
        "symptoms": [
            "看 B站番剧提示：非常抱歉，根据版权方要求，您所在的地区无法观看本片",
            "如果直接开全局代理看 B站，普通国产 UP 主视频加载极其缓慢且弹幕同步卡顿"
        ],
        "rootCauses": [
            "B站只在番剧播放页加载前请求一次地理版权验证 API，而实际的视频推流依然由国内 CDN 承载"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：添加 B站专属智能解锁规则段",
                "detail": "在客户端规则集中添加以下定向策略，将版权鉴权接口精准导向香港或台湾专线节点：",
                "code": "rules:\n  # B站港澳台地区版权检测 API 走代理\n  - DOMAIN,api.bilibili.com,🇭🇰 香港专线\n  - DOMAIN,api.bilibili.tv,🇭🇰 香港专线\n  - DOMAIN-SUFFIX,bilibili.com,DIRECT\n  - DOMAIN-SUFFIX,bilivideo.com,DIRECT"
            },
            {
                "stepTitle": "步骤 2：配合油猴脚本「解除 B站区域限制」体验更完美",
                "detail": "在浏览器安装 Tampermonkey 扩展并安装「解除 B站区域限制」开源脚本，一键实现全自动解锁与 4K 高画质解析。"
            }
        ],
        "faqTips": "这种分流策略只消耗几 KB 的鉴权流量，实际播放走的依然是国内 CDN，既快又完全不费机场流量！",
        "relatedSlugs": ["bahamut-ani-gamer-taiwan-ip", "clash-verge-custom-rules-override"]
    },
    {
        "id": "faq-105",
        "slug": "bypass-steam-epic-game-download",
        "title": "游戏下载不走代理直接跑满千兆宽带的高级分流技巧 (Steam / Epic)",
        "category": "routing",
        "categoryLabel": "系统分流与穿透",
        "readTime": "4 分钟",
        "updatedAt": "2025年最新实测",
        "summary": "避免下载几十 GB 的 3A 大作时瞬间吸干机场全部月流量的保姆级规则防坑指南。",
        "symptoms": [
            "在 Steam 或 Epic 下载一个《赛博朋克 2077》或《黑神话》，机场 200G 流量一夜之间全部清零",
            "下载速度只有几 MB/s，没有跑满家里千兆物理宽带"
        ],
        "rootCauses": [
            "客户端开启了全局模式，或者默认规则将所有非 CN 域名统统丢给了代理出口，而 Steam/Epic 的海外 CDN 被误判为境外流量"
        ],
        "solutions": [
            {
                "stepTitle": "步骤 1：在分流规则中将各大游戏下载 CDN 强制绑定 DIRECT 直连",
                "detail": "在自定义规则顶部添加以下游戏下载域名白名单：",
                "code": "rules:\n  # Steam / Epic 满速直连下载白名单\n  - DOMAIN-SUFFIX,steamcontent.com,DIRECT\n  - DOMAIN-SUFFIX,steamserver.net,DIRECT\n  - DOMAIN-SUFFIX,epicgames.com,DIRECT\n  - DOMAIN-SUFFIX,gog.com,DIRECT"
            },
            {
                "stepTitle": "步骤 2：在客户端下载设置中选择「中国-上海/北京/广州」下载节点",
                "detail": "在 Steam 设置 ->「下载」中，将下载地区固定为你所在的国内省份，CDN 自动从腾讯云/阿里机房极速拉取，千兆光纤几分钟下完！"
            }
        ],
        "faqTips": "一定要记住：科学上网节点是用来加速网页浏览、跨越阻断和联机对战的，海量游戏文件下载一定要走国内直连。",
        "relatedSlugs": ["steam-community-error-101-118", "traffic-drain-fast-background-leaks"]
    }
]

print(f"Loaded {len(ROUTING_FAQS)} routing FAQs.")
