export interface NavItem {
  title: string;
  href: string;
  badge?: string;
  isExternal?: boolean;
}

export const SITE_METADATA = {
  title: '机场选择 - 稳定高速翻墙机场评测与推荐指南 (jichangxuanze.lat)',
  shortTitle: '机场选择',
  description: '专业的科学上网与翻墙机场横向评测博客。真实晚高峰测速、IPLC专线推荐、流媒体/ChatGPT解锁检测、Clash/Sing-box保姆级配置教程与最新优惠码汇总。',
  domain: 'jichangxuanze.lat',
  siteUrl: 'https://jichangxuanze.lat',
  updateDate: '2025年最新更新',
  author: '机场选择编辑部',
  notice: '💡 提示：本站所有机场均经过晚高峰（20:00~23:00）真实测速与流媒体解锁实测，拒绝虚标与虚假推广。',
};

export const NAV_ITEMS: NavItem[] = [
  { title: '首页推荐', href: '/' },
  { title: '🏆 机场排行榜', href: '/rankings/' },
  { title: '📝 深度测评', href: '/reviews/' },
  { title: '💡 FAQ 排错指南', href: '/faq/' },
  { title: '📚 客户端教程', href: '/tutorials/' },
  { title: '🎁 优惠码汇总', href: '/promotions/', badge: 'Hot' },
  { title: '❓ 选购指南/避坑', href: '/about/' },
];
