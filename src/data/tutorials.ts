export interface Tutorial {
  id: string;
  slug: string;
  title: string;
  description: string;
  platform: 'Windows' | 'macOS' | 'iOS' | 'Android' | '全平台';
  clientName: string;
  readTime: string;
  category: 'client' | 'faq' | 'rules';
  date: string;
  downloadUrl?: string;
  recommended: boolean;
}

export const TUTORIALS_DATA: Tutorial[] = [
  {
    id: 'tut-1',
    slug: 'clash-verge-rev-guide',
    title: 'Clash Verge Rev 保姆级配置教程 (Windows / macOS)',
    description: '替代已停更 Clash for Windows 的最新首选开源客户端，支持 Mihomo (Clash Meta) 内核与现代美观 UI。',
    platform: 'Windows',
    clientName: 'Clash Verge Rev',
    readTime: '5 分钟阅读',
    category: 'client',
    date: '2025-01-10',
    downloadUrl: 'https://github.com/clash-verge-rev/clash-verge-rev/releases',
    recommended: true,
  },
  {
    id: 'tut-2',
    slug: 'shadowrocket-ios-guide',
    title: 'iOS 小火箭 (Shadowrocket) 零基础图文使用指南',
    description: '苹果 iOS 平台最流行的科学上网代理软件，涵盖节点订阅导入、智能分流设置与节点测速技巧。',
    platform: 'iOS',
    clientName: 'Shadowrocket',
    readTime: '6 分钟阅读',
    category: 'client',
    date: '2025-01-08',
    recommended: true,
  },
  {
    id: 'tut-3',
    slug: 'sing-box-guide',
    title: 'Sing-box 跨平台全功能通用客户端配置完全手册',
    description: '新一代多协议通用代理核心平台，资源开销极低，原生支持 Hysteria 2、TUIC、Shadowsocks、Vless 等现代协议。',
    platform: '全平台',
    clientName: 'Sing-box',
    readTime: '8 分钟阅读',
    category: 'client',
    date: '2024-12-28',
    downloadUrl: 'https://github.com/SagerNet/sing-box/releases',
    recommended: false,
  },
  {
    id: 'tut-4',
    slug: 'proxy-faq-rules',
    title: '常见排错 FAQ：订阅更新失败、节点超时与国内直连分流失效',
    description: '汇总科学上网过程中最常见的疑难杂症，从 DNS 泄漏、系统时间不同步到分流规则冲突，一站式解决。',
    platform: '全平台',
    clientName: '排错指南',
    readTime: '7 分钟阅读',
    category: 'faq',
    date: '2025-01-02',
    recommended: false,
  }
];
