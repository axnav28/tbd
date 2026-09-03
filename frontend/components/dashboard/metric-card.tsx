import { ConfidenceBadge, Confidence } from '../confidence-badge';

export function MetricCard({ label, value, meta, confidence }: { label: string; value: string; meta: string; confidence: Confidence }) {
  return <section className="metric-card"><div className="card-label">{label}<ConfidenceBadge value={confidence} /></div><div className="metric-value">{value}</div><div className="card-meta">{meta}</div></section>;
}
