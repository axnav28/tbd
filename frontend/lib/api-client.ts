const baseUrl = process.env.NEXT_PUBLIC_API_URL ?? 'http://localhost:8000';

export async function getBackendHealth(): Promise<Record<string, string>> {
  const response = await fetch(`${baseUrl}/api/v1/health`);
  if (!response.ok) throw new Error(`Backend health request failed: ${response.status}`);
  return response.json() as Promise<Record<string, string>>;
}
