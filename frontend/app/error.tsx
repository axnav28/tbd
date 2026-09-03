'use client';

export default function Error({ reset }: { error: Error & { digest?: string }; reset: () => void }) {
  return <main><div className="eyebrow">TBD / Recovery</div><h1>We couldn&apos;t load this view.</h1><p>The model service may be temporarily unavailable. Retry the request when the backend is reachable.</p><button className="action" onClick={() => reset()}>Retry view</button></main>;
}
