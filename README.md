# ssot-pack-mobile-install-attribution

Installable SSOT governance pack for Apple and Android mobile install attribution, app campaign attribution, and privacy-preserving app measurement.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for downstream synchronization. It intentionally does not cross-link to other governance packs.

## Pack Metadata

- Pack ID: `pack:mobile-install-attribution`
- Priority: `P1.4`
- PyPI package: `ssot-pack-mobile-install-attribution`
- Import package: `ssot_pack_mobile_install_attribution`
- GitHub repository: `groupsum/mobile-install-attribution-governance-pack`
- Reservation owner: `extension-pack:ssot-pack-mobile-install-attribution`

## Domain Focus

Mobile Install And App Attribution

## Authority Sources

- Apple AdAttributionKit
- Apple AdAttributionKit attribution rules
- Apple AdServices framework
- Apple AdServices attribution payloads
- Google Play Install Referrer API
- Google Play Install Referrer Library
- Privacy Sandbox on Android Attribution Reporting API

## Included ADRs

- `adr:mobile-install-attribution-boundary` - Mobile Install Attribution Boundary
- `adr:platform-privacy-attribution-policy` - Platform Privacy Attribution Policy

## Included SPECs

- `spc:apple-adattributionkit-contract` - Apple AdAttributionKit Contract
- `spc:apple-adservices-contract` - Apple AdServices Contract
- `spc:google-play-install-referrer-contract` - Google Play Install Referrer Contract
- `spc:android-attribution-reporting-contract` - Android Attribution Reporting Contract

## Install With uv

```bash
uv add ssot-pack-mobile-install-attribution
uv add ssot-registry ssot-pack-mobile-install-attribution
```

## Use With The SSOT Registry CLI

```bash
uvx --from ssot-registry ssot pack install ssot-pack-mobile-install-attribution
uvx --from ssot-registry ssot pack sync . ssot-pack-mobile-install-attribution
uv run ssot adr list .
uv run ssot spec list .
```

## Programmatic Usage

```python
from ssot_pack_mobile_install_attribution import load_document_manifest

adr_manifest = load_document_manifest("adr")
spec_manifest = load_document_manifest("spec")
```

## Resources

- GitHub repository: https://github.com/groupsum/mobile-install-attribution-governance-pack
- PyPI package: https://pypi.org/project/ssot-pack-mobile-install-attribution/
- SSOT Registry: https://pypi.org/project/ssot-registry/
