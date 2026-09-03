'use client';

import { useCallback, useEffect, useState } from 'react';
import { Radio, Wifi } from 'lucide-react';
import { ConfidenceBadge, Confidence } from '../confidence-badge';

type FeedEvent = { time: string; severity: 'critical' | 'high' | 'watch'; title: string; detail: string; confidence: Confidence };

export function LiveFeed() {
  const [events, setEvents] = useState<FeedEvent[]>([]); const [updated, setUpdated] = useState('connecting'); const [seconds, setSeconds] = useState(60);
  const refresh = useCallback(async () => { try { const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL ?? 'http://localhost:8000'}/api/v1/risk/live-feed`, { cache: 'no-store' }); const body = await response.json() as { events: FeedEvent[]; refreshed_at: string }; setEvents(body.events); setUpdated(new Date(body.refreshed_at).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' })); setSeconds(60); } catch { setUpdated('feed unavailable'); } }, []);
  useEffect(() => { void refresh(); const refreshTimer = window.setInterval(() => void refresh(), 60_000); const countdown = window.setInterval(() => setSeconds((value) => value > 0 ? value - 1 : 60), 1_000); return () => { window.clearInterval(refreshTimer); window.clearInterval(countdown); }; }, [refresh]);
  return <section className="panel feed-panel"><div className="panel-head"><div><div className="section-kicker"><Radio size={12} /> Live threat feed</div><div className="panel-title">Model signals & control watch</div></div><div className="feed-status"><Wifi size={12} /> LIVE <span>refresh / 01:00</span></div></div><div className="feed-meta"><span>Last refresh {updated}</span><span>Next in 00:{String(seconds).padStart(2, '0')}</span></div><div className="feed-list">{events.map((event) => <div className="feed-item" key={event.title}><span className={`severity severity-${event.severity}`} /><div className="feed-content"><div className="feed-title">{event.title}<span className="feed-time">{event.time}</span></div><div className="feed-detail">{event.detail}</div></div><ConfidenceBadge value={event.confidence} /></div>)}</div><div className="feed-footer"><span className="pulse-line" /> Synthetic enterprise telemetry · public intelligence signals refresh separately</div></section>;
}
