'use client';
import { Area, AreaChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts';

const data = [{x:'P50', y:420},{x:'P75', y:980},{x:'P90', y:1850},{x:'P95', y:3100},{x:'P99', y:5480}];
export function LossChart() { return <div className="chart-wrap"><ResponsiveContainer width="100%" height={220}><AreaChart data={data}><defs><linearGradient id="loss" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stopColor="#71d7c2" stopOpacity={.3}/><stop offset="100%" stopColor="#71d7c2" stopOpacity={0}/></linearGradient></defs><XAxis dataKey="x" axisLine={false} tickLine={false} tick={{fill:'#7d8c9b',fontSize:11}}/><YAxis axisLine={false} tickLine={false} tick={{fill:'#7d8c9b',fontSize:11}} tickFormatter={(v) => `₹${v}k`}/><Tooltip contentStyle={{background:'#111a22',border:'1px solid #273744',borderRadius:8}} formatter={(v) => [`₹${v}k`, 'Loss']} /><Area type="monotone" dataKey="y" stroke="#71d7c2" fill="url(#loss)" strokeWidth={2}/></AreaChart></ResponsiveContainer></div>; }
