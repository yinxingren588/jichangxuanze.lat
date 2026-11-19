import faqsRaw from './faqs.json';

export interface FAQSolution {
  stepTitle: string;
  detail: string;
  code?: string;
}

export interface FAQItem {
  id: string;
  slug: string;
  title: string;
  category: string;
  categoryLabel: string;
  readTime: string;
  updatedAt: string;
  summary: string;
  symptoms: string[];
  rootCauses: string[];
  solutions: FAQSolution[];
  faqTips: string;
  relatedSlugs: string[];
}

export const FAQS_DATA: FAQItem[] = faqsRaw as FAQItem[];

export const FAQ_CATEGORIES = [
  { id: 'all', label: '🚀 全部指南' },
  { id: 'client', label: '💻 客户端与软件' },
  { id: 'connection', label: '⚡ 连接与网络报错' },
  { id: 'ai', label: '🤖 AI与服务风控' },
  { id: 'routing', label: '🌐 系统分流穿透' },
  { id: 'streaming', label: '📺 全球流媒体解锁' },
  { id: 'subscription', label: '💳 订阅与防坑' },
  { id: 'protocols', label: '🔒 底层协议科普' },
  { id: 'hardware', label: '📱 多端设备专病' },
];
