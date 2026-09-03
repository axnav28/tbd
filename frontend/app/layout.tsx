import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = { title: 'TBD | Cyber Risk Intelligence', description: 'Continuous cyber risk quantification platform' };

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="en"><body>{children}</body></html>;
}
