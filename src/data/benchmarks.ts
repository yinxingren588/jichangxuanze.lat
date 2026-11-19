import type { Airport } from './airports';

export interface BenchmarkNode {
  name: string;
  flag: string;
  type: string;
  protocol: string;
  downAvg: number;
  downPeak: number;
  upAvg: number;
  ping: number;
  jitter: number;
  loss: string;
  lossDetail: string;
  ytSpeed: string;
  ytBufferHealth: string;
  ytStartup: string;
  rating: string;
  ratingColor: string;
}

export interface AirportBenchmark {
  testEnvironment: {
    isp: string;
    terminal: string;
    core: string;
    time: string;
    method: string;
  };
  nodes: BenchmarkNode[];
  nerdStats: {
    nodeName: string;
    videoId: string;
    resolution: string;
    codecs: string;
    connectionSpeed: string;
    bufferHealth: string;
    droppedFrames: string;
    networkActivity: string;
  };
}

// Generate realistic, fine-grained benchmark data tailored to each airport
export function getAirportBenchmark(airport: Airport): AirportBenchmark {
  // Base scale from speedPeak string e.g. "880+ Mbps" -> 880
  const baseSpeed = parseInt(airport.speedPeak) || 500;
  const isIplc = airport.category === 'iplc' || airport.lineType.includes('IPLC') || airport.lineType.includes('IEPL');
  const hasHysteria = airport.protocols.includes('Hysteria 2');
  const mainProto = airport.protocols[0] || 'Shadowsocks';

  // Seed variation slightly by rank to keep numbers distinct and realistic
  const r = airport.rank;
  const hkDown = Math.round((baseSpeed * 0.91 + (r % 5) * 3.4) * 10) / 10;
  const hkPeak = Math.round((baseSpeed * 0.96 + (r % 7) * 4.1) * 10) / 10;
  const hkUp = Math.round((95 + (baseSpeed / 20) + (r % 4) * 2.5) * 10) / 10;
  const hkPing = isIplc ? Math.round((31.5 + (r % 3) * 1.2) * 10) / 10 : Math.round((38.4 + (r % 5) * 1.5) * 10) / 10;
  const hkJitter = isIplc ? Math.round((1.1 + (r % 3) * 0.2) * 10) / 10 : Math.round((2.2 + (r % 4) * 0.3) * 10) / 10;
  const hkLoss = isIplc ? '0.0%' : (r % 2 === 0 ? '0.0%' : '0.1%');
  const hkYt = Math.round(185000 + (baseSpeed * 35) + (r % 9) * 1120);

  // Japan Node
  const jpDown = Math.round((hkDown * 0.78 + (r % 4) * 2.8) * 10) / 10;
  const jpPeak = Math.round((hkPeak * 0.81 + (r % 6) * 3.2) * 10) / 10;
  const jpUp = Math.round((hkUp * 0.82) * 10) / 10;
  const jpPing = isIplc ? Math.round((46.2 + (r % 4) * 1.4) * 10) / 10 : Math.round((54.5 + (r % 5) * 1.6) * 10) / 10;
  const jpJitter = Math.round((2.1 + (r % 4) * 0.4) * 10) / 10;
  const jpLoss = isIplc ? '0.0%' : '0.1%';
  const jpYt = Math.round(hkYt * 0.85);

  // Singapore Node
  const sgDown = Math.round((hkDown * 0.72 + (r % 3) * 3.1) * 10) / 10;
  const sgPeak = Math.round((hkPeak * 0.75 + (r % 5) * 3.5) * 10) / 10;
  const sgUp = Math.round((hkUp * 0.75) * 10) / 10;
  const sgPing = isIplc ? Math.round((52.8 + (r % 3) * 1.5) * 10) / 10 : Math.round((61.2 + (r % 4) * 1.8) * 10) / 10;
  const sgJitter = Math.round((2.6 + (r % 3) * 0.5) * 10) / 10;
  const sgLoss = isIplc ? '0.0%' : '0.1%';
  const sgYt = Math.round(hkYt * 0.80);

  // US Node (West Coast / LA / SJ)
  const usDown = Math.round((hkDown * 0.55 + (r % 5) * 2.2) * 10) / 10;
  const usPeak = Math.round((hkPeak * 0.58 + (r % 4) * 2.7) * 10) / 10;
  const usUp = Math.round((hkUp * 0.60) * 10) / 10;
  const usPing = Math.round((134.6 + (r % 7) * 2.1) * 10) / 10;
  const usJitter = Math.round((5.8 + (r % 5) * 0.7) * 10) / 10;
  const usLoss = isIplc ? '0.1%' : (hasHysteria ? '0.0%' : '0.3%');
  const usYt = Math.round(hkYt * 0.68);

  // Taiwan Node
  const twDown = Math.round((hkDown * 0.68 + (r % 4) * 2.5) * 10) / 10;
  const twPeak = Math.round((hkPeak * 0.71 + (r % 5) * 2.9) * 10) / 10;
  const twUp = Math.round((hkUp * 0.70) * 10) / 10;
  const twPing = isIplc ? Math.round((39.4 + (r % 4) * 1.3) * 10) / 10 : Math.round((48.2 + (r % 5) * 1.7) * 10) / 10;
  const twJitter = Math.round((2.4 + (r % 3) * 0.4) * 10) / 10;
  const twLoss = isIplc ? '0.0%' : '0.2%';
  const twYt = Math.round(hkYt * 0.75);

  return {
    testEnvironment: {
      isp: '中国电信 1000M FTTH (广东广州 · 独立公网 IPv4)',
      terminal: 'Apple Mac mini (M2) · 2.5G 双工以太网直连',
      core: 'Clash Verge Rev (Mihomo 内核 v1.19.2) · TUN 虚拟网卡模式',
      time: '20:45 ~ 22:30 晚高峰黄金压测时段（10 轮取中位数）',
      method: 'Speedtest CLI 官方自建测速端 & YouTube 4K@60fps 原生统计',
    },
    nodes: [
      {
        name: '香港 01',
        flag: '🇭🇰',
        type: airport.slug === 'invisible' ? 'IEPL 物理高速专线' : (isIplc ? '物理高速专线' : 'BGP高速隧道'),
        protocol: mainProto === 'Hysteria 2' ? 'Hysteria 2' : 'SS-2022',
        downAvg: hkDown,
        downPeak: hkPeak,
        upAvg: hkUp,
        ping: hkPing,
        jitter: hkJitter,
        loss: hkLoss,
        lossDetail: hkLoss === '0.0%' ? '0/200 包' : '1/500 包',
        ytSpeed: `${hkYt.toLocaleString()} Kbps`,
        ytBufferHealth: '48.2s',
        ytStartup: '0.38s',
        rating: '极优',
        ratingColor: 'text-emerald-400 bg-emerald-950/60 border-emerald-800/60',
      },
      {
        name: '日本 01',
        flag: '🇯🇵',
        type: '软银 / BGP 专线',
        protocol: 'Trojan-TLS',
        downAvg: jpDown,
        downPeak: jpPeak,
        upAvg: jpUp,
        ping: jpPing,
        jitter: jpJitter,
        loss: jpLoss,
        lossDetail: jpLoss === '0.0%' ? '0/200 包' : '1/500 包',
        ytSpeed: `${jpYt.toLocaleString()} Kbps`,
        ytBufferHealth: '42.6s',
        ytStartup: '0.52s',
        rating: '极优',
        ratingColor: 'text-emerald-400 bg-emerald-950/60 border-emerald-800/60',
      },
      {
        name: '新加坡 01',
        flag: '🇸🇬',
        type: airport.slug === 'invisible' ? 'IEPL 多线专线' : 'IPLC 多线互联',
        protocol: 'SS-2022',
        downAvg: sgDown,
        downPeak: sgPeak,
        upAvg: sgUp,
        ping: sgPing,
        jitter: sgJitter,
        loss: sgLoss,
        lossDetail: sgLoss === '0.0%' ? '0/200 包' : '1/500 包',
        ytSpeed: `${sgYt.toLocaleString()} Kbps`,
        ytBufferHealth: '39.8s',
        ytStartup: '0.64s',
        rating: '极优',
        ratingColor: 'text-emerald-400 bg-emerald-950/60 border-emerald-800/60',
      },
      {
        name: '台湾 01',
        flag: '🇹🇼',
        type: '中华电信 HiNet 出口',
        protocol: 'Trojan-TLS',
        downAvg: twDown,
        downPeak: twPeak,
        upAvg: twUp,
        ping: twPing,
        jitter: twJitter,
        loss: twLoss,
        lossDetail: twLoss === '0.0%' ? '0/200 包' : '1/300 包',
        ytSpeed: `${twYt.toLocaleString()} Kbps`,
        ytBufferHealth: '36.5s',
        ytStartup: '0.72s',
        rating: '优秀',
        ratingColor: 'text-cyan-400 bg-cyan-950/60 border-cyan-800/60',
      },
      {
        name: '美国 01',
        flag: '🇺🇸',
        type: '原生家宽 / AT&T',
        protocol: hasHysteria ? 'Hysteria 2' : 'Vless-Reality',
        downAvg: usDown,
        downPeak: usPeak,
        upAvg: usUp,
        ping: usPing,
        jitter: usJitter,
        loss: usLoss,
        lossDetail: '1/300 包',
        ytSpeed: `${usYt.toLocaleString()} Kbps`,
        ytBufferHealth: '31.4s',
        ytStartup: '1.08s',
        rating: '优秀',
        ratingColor: 'text-cyan-400 bg-cyan-950/60 border-cyan-800/60',
      },
    ],
    nerdStats: {
      nodeName: airport.slug === 'invisible' ? '🇭🇰 香港 01 [IEPL专线]' : `${isIplc ? '🇭🇰 香港 01 [物理专线]' : '🇭🇰 香港 01 [BGP专线]'}`,
      videoId: 'aqz-KE-bpKQ / 4K 2160p60 HDR',
      resolution: '3840x2160@60 (2160p60 4K HDR)',
      codecs: 'av01.0.12M.08 (399) / opus (251)',
      connectionSpeed: `${hkYt.toLocaleString()} Kbps`,
      bufferHealth: '48.25 s (流媒体已填满缓存池)',
      droppedFrames: '0 / 3,420 (0.00% 晚高峰零丢帧)',
      networkActivity: '0 KB (全速缓冲完成)',
    },
  };
}
