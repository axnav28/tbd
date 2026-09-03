import Link from 'next/link';
import { Activity, BarChart3, Network, Shield, Sparkles, ScrollText } from 'lucide-react';

const links = [
  ['/','Overview',Activity], ['/graph','Attack paths',Network], ['/optimizer','Investment',BarChart3], ['/compliance','Compliance',Shield], ['/query','Ask the graph',Sparkles], ['/audit','Audit ledger',ScrollText],
] as const;

export function Shell({ eyebrow, title, children }: { eyebrow: string; title: string; children: React.ReactNode }) {
  return <div className="app-shell"><aside><div className="brand"><span className="brand-mark">T</span><span>TBD<span className="brand-muted"> / RISK OS</span></span></div><div className="tenant"><span className="live-dot" /> NORTHSTAR FINANCE <small>SYNTHETIC TENANT</small></div><nav>{links.map(([href, label, Icon]) => <Link key={href} href={href}><Icon size={16} />{label}</Link>)}</nav><div className="aside-foot">CONTINUOUS QUANTIFICATION<br /><span>Engine v0.6 · India region</span></div></aside><main className="content"><header><div><div className="eyebrow">{eyebrow}</div><h1>{title}</h1></div><div className="header-state"><span className="live-dot" /> LIVE MODEL <small>Updated moments ago</small></div></header>{children}</main></div>;
}
