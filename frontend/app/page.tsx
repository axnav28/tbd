"use client";

import { useEffect, useState } from 'react';
import { ShieldCheck } from 'lucide-react';
import { Shell } from '../components/ui/shell';
import { MetricCard } from '../components/dashboard/metric-card';
import { ConfidenceBadge } from '../components/confidence-badge';
import { LossChart } from '../components/charts/loss-chart';
import { getBackendHealth } from '../lib/api-client';

export default function Home() {
  const [backendStatus, setBackendStatus] = useState('connecting');
  const [summary, setSummary] = useState<{ eal: { value: number; currency: string; confidence: 'Estimated' }; var: { value: number; currency: string; confidence: 'Estimated' } } | null>(null);

  useEffect(() => {
    getBackendHealth().then(() => { setBackendStatus('online'); return fetch(`${process.env.NEXT_PUBLIC_API_URL ?? 'http://localhost:8000'}/api/v1/risk/summary`); }).then((response) => response.json()).then(setSummary).catch(() => setBackendStatus('unavailable'));
  }, []);

  const money = (value: number) => `₹${(value / 1000000).toFixed(2)}M`;
  return <Shell eyebrow="Executive view / 03 Sep 2026" title="Risk posture"><div className="grid"><div className="hero-copy"><h2>Northstar Finance, continuously quantified.</h2><p>Translate attack paths into a defensible investment conversation. Every figure carries its evidence state, and every recommendation exposes the scenarios it affects.</p><div className="status"><ShieldCheck size={15} aria-hidden="true" />&nbsp; Model {backendStatus}</div></div><MetricCard label="Expected annual loss" value={summary ? money(summary.eal.value) : '—'} meta="Across 2 modeled scenarios · INR" confidence="Estimated" /><MetricCard label="95% value at risk" value={summary ? money(summary.var.value) : '—'} meta="Monte Carlo loss percentile · INR" confidence="Estimated" /><section className="panel wide section-space"><div className="panel-head"><div><div className="section-kicker">Loss exceedance</div><div className="panel-title">Annual loss distribution</div></div><ConfidenceBadge value="Estimated" /></div><LossChart /></section><section className="panel side section-space"><div className="panel-head"><div><div className="section-kicker">Priority queue</div><div className="panel-title">Top contributors</div></div><span className="panel-note">2 paths</span></div><div className="risk-list"><div className="risk-row"><div><div className="risk-name">Loan origination exposure</div><div className="risk-sub">CVE chain → payment-adjacent asset</div></div><div className="risk-amount">₹0.82M</div><ConfidenceBadge value="Estimated" /></div><div className="risk-row"><div><div className="risk-name">Privileged identity surface</div><div className="risk-sub">Admin accounts → internal systems</div></div><div className="risk-amount">₹0.43M</div><ConfidenceBadge value="Configured" /></div></div></section></div></Shell>;
}
