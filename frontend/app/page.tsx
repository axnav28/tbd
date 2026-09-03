"use client";

import { useEffect, useState } from 'react';
import { ShieldCheck } from 'lucide-react';
import { getBackendHealth } from '../lib/api-client';

export default function Home() {
  const [backendStatus, setBackendStatus] = useState('connecting');

  useEffect(() => {
    getBackendHealth().then(() => setBackendStatus('online')).catch(() => setBackendStatus('unavailable'));
  }, []);

  return <main><div className="eyebrow">TBD / Cyber risk intelligence</div><h1>Make security exposure legible in financial terms.</h1><p>The Phase 0 service scaffold is online. Risk quantification, attack-path analysis, and bounded investment recommendations will land in the next phases.</p><div className="status"><ShieldCheck size={17} aria-hidden="true" />&nbsp; Backend {backendStatus}</div></main>;
}
