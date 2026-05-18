# mobile-install-attribution-governance-pack

Installable SSOT governance pack for Apple and Android mobile install attribution, app campaign attribution, and privacy-preserving app measurement.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for downstream synchronization. It intentionally does not cross-link to other governance packs.

## Pack Metadata

- Pack ID: `pack:mobile-install-attribution`
- Priority: `P1.4`
- PyPI package: `mobile-install-attribution-governance-pack`
- Import package: `ssot_pack_mobile_install_attribution`
- GitHub repository: `groupsum/mobile-install-attribution-governance-pack`
- Reservation owner: `extension-pack:mobile-install-attribution-governance-pack`

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

- `adr:mobile-install-attribution-source-policy` - Mobile Install Attribution Source Policy
- `adr:apple-adattributionkit-policy` - Apple AdAttributionKit Policy
- `adr:apple-adservices-token-policy` - Apple AdServices Token Policy
- `adr:android-install-referrer-policy` - Android Install Referrer Policy
- `adr:android-attribution-reporting-status-policy` - Android Attribution Reporting Status Policy
- `adr:mobile-attribution-privacy-data-policy` - Mobile Attribution Privacy Data Policy
- `adr:mobile-attribution-window-policy` - Mobile Attribution Window Policy
- `adr:mobile-attribution-evidence-policy` - Mobile Attribution Evidence Policy

## Included SPECs

- `spc:apple-adattributionkit-framework-requirements` - Apple AdAttributionKit Framework Requirements
- `spc:apple-adattributionkit-attribution-rule-requirements` - Apple AdAttributionKit Attribution Rule Requirements
- `spc:apple-adservices-token-requirements` - Apple AdServices Token Requirements
- `spc:apple-adservices-attribution-payload-requirements` - Apple AdServices Attribution Payload Requirements
- `spc:google-play-install-referrer-api-requirements` - Google Play Install Referrer API Requirements
- `spc:google-play-install-referrer-library-requirements` - Google Play Install Referrer Library Requirements
- `spc:android-attribution-reporting-api-requirements` - Android Attribution Reporting API Requirements
- `spc:mobile-attribution-token-retention-requirements` - Mobile Attribution Token Retention Requirements
- `spc:mobile-attribution-timestamp-requirements` - Mobile Attribution Timestamp Requirements
- `spc:mobile-attribution-campaign-field-requirements` - Mobile Attribution Campaign Field Requirements
- `spc:mobile-attribution-privacy-review-requirements` - Mobile Attribution Privacy Review Requirements
- `spc:mobile-attribution-platform-status-requirements` - Mobile Attribution Platform Status Requirements

## Install With uv

```bash
uv add mobile-install-attribution-governance-pack
uv add ssot-registry mobile-install-attribution-governance-pack
```

## Use With The SSOT Registry CLI

```bash
uvx --from ssot-registry ssot pack install mobile-install-attribution-governance-pack
uvx --from ssot-registry ssot pack sync . mobile-install-attribution-governance-pack
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
- PyPI package: https://pypi.org/project/mobile-install-attribution-governance-pack/
- SSOT Registry: https://pypi.org/project/ssot-registry/
