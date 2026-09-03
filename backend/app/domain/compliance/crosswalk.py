"""Curated, source-linked compliance crosswalk for a focused control subset."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Mapping:
    framework: str
    reference: str
    title: str
    objective: str
    source: str


MAPPINGS = (
    Mapping("ISO 27001:2022", "A.5.15", "Access control", "identity and access governance", "https://www.iso.org/standard/27001.html"),
    Mapping("ISO 27001:2022", "A.8.8", "Management of technical vulnerabilities", "vulnerability and patch management", "https://www.iso.org/standard/27001.html"),
    Mapping("NIST CSF 2.0", "PR.AA-05", "Access permissions are managed and reviewed", "identity and access governance", "https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf"),
    Mapping("NIST CSF 2.0", "PR.PS", "Platform security", "vulnerability and patch management", "https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf"),
    Mapping("CIS Controls v8", "6.5", "Require MFA for Administrative Access", "identity and access governance", "https://www.cisecurity.org/controls/v8"),
    Mapping("CIS Controls v8", "7.7", "Remediate Detected Vulnerabilities", "vulnerability and patch management", "https://www.cisecurity.org/controls/v8"),
    Mapping("RBI IT Governance Directions 2023", "Chapter IV", "Information security governance and controls", "financial-sector cyber governance", "https://www.rbi.org.in/"),
    Mapping("SEBI CSCRF", "Circular 2024/113", "Cybersecurity and Cyber Resilience Framework", "securities-sector cyber governance", "https://www.sebi.gov.in/legal/circulars/aug-2024/cybersecurity-and-cyber-resilience-framework-cscrf-for-sebi-regulated-entities-res-_85964.html"),
)


def crosswalk(framework: str | None = None) -> list[Mapping]:
    """Return only curated mappings; no inferred clause numbers are generated."""
    return [item for item in MAPPINGS if framework is None or item.framework == framework]
