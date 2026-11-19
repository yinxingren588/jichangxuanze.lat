# 机场选择 (jichangxuanze.lat) - 稳定高速翻墙机场评测与推荐博客

> 基于 **Astro 5 + Tailwind CSS** 构建的超轻量、秒级加载、专为 SEO 和高转化率打造的机场评测与推荐站点。

---

## 🌟 核心功能特色

1. **秒开静态化（Zero JS 默认）**：
   - 全站页面编译为原生纯 HTML，首屏毫秒级加载，极度契合 Google SEO 抓取权重与百度等搜索引擎。
2. **交互式机场卡片与无刷新即时筛选**：
   - 支持按「👑 顶级专线 (IPLC)」、「💰 平价性价比」、「📦 按量计费/轻度备用」、「💼 商务高端」即时筛选。
3. **参数横向横评对比表**：
   - 价格、线路类型、晚高峰实测、协议、流媒体解锁（Netflix/Disney+/ChatGPT）直观对比。
4. **一键复制优惠码组件**：
   - 用户点击后自动复制并带动画提示反馈，极大提升 Affiliate 转化率。
5. **全流程页面矩阵已全部生成完毕**：
   - 首页 (`/`)：Hero 横幅 + 核心榜单 + 动态卡片 + 横评对比表 + 避坑 4 大铁律
   - 年度榜单 (`/rankings/`)：专线榜、平价榜、按量计费榜分类细化
   - 评测中心 (`/reviews/`)：包含单站深度评测（晚高峰多地测速图表、流媒体解锁矩阵、优缺点分析）
   - 客户端教程库 (`/tutorials/`)：Clash Verge Rev、小火箭 (Shadowrocket)、Sing-box、排错 FAQ
   - 优惠码汇总 (`/promotions/`)：各大机场实时折扣码一站式领取
   - 关于与声明 (`/about/`)：测试标准环境说明与合规免责声明

---

## 🚀 快速启动与本地预览

在当前项目目录打开终端运行：

```bash
# 启动本地开发热更新服务器 (访问 http://localhost:4321)
npm run dev

# 编译生成生产环境静态文件 (生成在 dist/ 目录，仅需 2 秒)
npm run build

# 本地预览编译后的生产静态网页
npm run preview
```

---

## 🛠️ 如何管理与添加内容？（完全模块化）

无需修改复杂的 HTML 页面代码，所有数据与业务逻辑均已解耦并抽取为纯配置文件：

### 1. 修改/新增推荐的机场
打开 `src/data/airports.ts` 文件：
- 修改已有机场的名称、价格、晚高峰测速、优缺点；
- 将 `affUrl` 替换为你自己的返利推广链接（如 `https://your-aff-link.com`）；
- 修改 `coupon` 优惠码及折扣力度；
- 如需新增机场，直接复制一个对象追加到 `AIRPORTS_DATA` 数组中，全站（首页、对比表、评测页、优惠码页）**将全自动生成对应页面与链接**！

### 2. 修改网站名称与基本信息
打开 `src/data/navigation.ts` 文件：
- 可修改网站标题、描述、公告栏文本、导航菜单项。

### 3. 新增客户端教程
打开 `src/data/tutorials.ts` 文件：
- 追加新的软件教程元数据；在 `src/pages/tutorials/[slug].astro` 中丰富正文步骤。

---

## ☁️ 0 元免费上线部署指引（推荐 Cloudflare Pages）

本站构建输出为标准的静态纯 HTML 页面（`dist/` 目录），推荐以下部署方式：

### 方案 A：直接绑定 GitHub 自动化部署（最省心）
1. 将本项目 push 到你的 GitHub 私有/公开仓库；
2. 登录 [Cloudflare Dashboard](https://dash.cloudflare.com/) -> **Workers & Pages** -> **Create application** -> **Pages** -> **Connect to Git**；
3. 选择该仓库，构建设置配置如下：
   - **Framework preset**：`Astro`
   - **Build command**：`npm run build`
   - **Build output directory**：`dist`
4. 点击保存并部署。在“Custom domains”中绑定你的域名 `jichangxuanze.lat` 即可。

### 方案 B：直接上传文件（无需 Git）
1. 本地运行 `npm run build`；
2. 打开 Cloudflare Pages，选择 **Upload assets**；
3. 直接将项目根目录下的 `dist` 文件夹拖拽上传，立即上线！
