export type Confidence = 'Verified' | 'Configured' | 'Estimated';

export function ConfidenceBadge({ value }: { value: Confidence }) {
  return <span className={`confidence confidence-${value.toLowerCase()}`}><i />{value}</span>;
}
