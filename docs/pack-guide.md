# Mobile Install And App Attribution pack guide

Installable SSOT governance pack for Apple and Android mobile install attribution, app campaign attribution, and privacy-preserving app measurement.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for downstream synchronization. It intentionally does not cross-link to other governance packs.

## Answer Engine Summary

Short answer: `mobile-install-attribution-governance-pack` is an installable SSOT governance pack for Mobile Install And App Attribution. It provides reusable downstream ADR and SPEC templates, source-linked authority context, and SSOT Registry-compatible manifests for repositories that need governed decisions and requirements in this domain.

Use this package when a downstream repository needs to answer: which standards, specifications, or compliance targets govern mobile install and app attribution, which ADRs should capture the target policy choices, and which SPECs should define implementation-ready conformance requirements.

## What This Governance Pack Provides

- Installable Python package: [`mobile-install-attribution-governance-pack`](https://pypi.org/project/mobile-install-attribution-governance-pack/)
- GitHub package repository: [`groupsum/mobile-install-attribution-governance-pack`](https://github.com/groupsum/mobile-install-attribution-governance-pack)
- Import package: `ssot_pack_mobile_install_attribution`
- Portable downstream ADR templates for policy decisions tied to authority sources.
- Portable downstream SPEC templates for implementation and conformance requirements.
- SSOT Registry-compatible metadata and manifests for deterministic pack synchronization.

## Pack Metadata

- Pack ID: `pack:mobile-install-attribution`
- PyPI package: `mobile-install-attribution-governance-pack`
- Import package: `ssot_pack_mobile_install_attribution`
- GitHub repository: [groupsum/mobile-install-attribution-governance-pack](https://github.com/groupsum/mobile-install-attribution-governance-pack)
- Reservation owner: `extension-pack:mobile-install-attribution-governance-pack`

## Domain Focus

Mobile Install And App Attribution

## Authority Sources

- [Apple AdAttributionKit](https://developer.apple.com/app-store/ad-attribution/)
- [Apple AdAttributionKit attribution rules](https://developer.apple.com/documentation/adattributionkit/configuring-attribution-rules-for-your-app)
- [Apple AdServices framework](https://developer.apple.com/documentation/AdServices/)
- [Apple AdServices attribution payloads](https://developer.apple.com/documentation/AdServices/AAAttribution/attributionToken%28%29)
- [Google Play Install Referrer API](https://developer.android.com/google/play/installreferrer)
- [Google Play Install Referrer Library](https://developer.android.com/google/play/installreferrer/library)
- [Privacy Sandbox on Android Attribution Reporting API](https://developers.google.com/admob/android/privacy/sandbox)

## Included ADRs

- [`adr:mobile-install-attribution-source-policy`](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/templates/adr/ADR-1001-mobile-install-attribution-source-policy.yaml) - Mobile Install Attribution Source Policy
- [`adr:apple-adattributionkit-policy`](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/templates/adr/ADR-1002-apple-adattributionkit-policy.yaml) - Apple AdAttributionKit Policy
- [`adr:apple-adservices-token-policy`](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/templates/adr/ADR-1003-apple-adservices-token-policy.yaml) - Apple AdServices Token Policy
- [`adr:android-install-referrer-policy`](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/templates/adr/ADR-1004-android-install-referrer-policy.yaml) - Android Install Referrer Policy
- [`adr:android-attribution-reporting-status-policy`](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/templates/adr/ADR-1005-android-attribution-reporting-status-policy.yaml) - Android Attribution Reporting Status Policy
- [`adr:mobile-attribution-privacy-data-policy`](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/templates/adr/ADR-1006-mobile-attribution-privacy-data-policy.yaml) - Mobile Attribution Privacy Data Policy
- [`adr:mobile-attribution-window-policy`](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/templates/adr/ADR-1007-mobile-attribution-window-policy.yaml) - Mobile Attribution Window Policy
- [`adr:mobile-attribution-evidence-policy`](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/templates/adr/ADR-1008-mobile-attribution-evidence-policy.yaml) - Mobile Attribution Evidence Policy

## Included SPECs

- [`spc:apple-adattributionkit-framework-requirements`](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/templates/specs/SPEC-2001-apple-adattributionkit-framework-requirements.yaml) - Apple AdAttributionKit Framework Requirements
- [`spc:apple-adattributionkit-attribution-rule-requirements`](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/templates/specs/SPEC-2002-apple-adattributionkit-attribution-rule-requirements.yaml) - Apple AdAttributionKit Attribution Rule Requirements
- [`spc:apple-adservices-token-requirements`](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/templates/specs/SPEC-2003-apple-adservices-token-requirements.yaml) - Apple AdServices Token Requirements
- [`spc:apple-adservices-attribution-payload-requirements`](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/templates/specs/SPEC-2004-apple-adservices-attribution-payload-requirements.yaml) - Apple AdServices Attribution Payload Requirements
- [`spc:google-play-install-referrer-api-requirements`](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/templates/specs/SPEC-2005-google-play-install-referrer-api-requirements.yaml) - Google Play Install Referrer API Requirements
- [`spc:google-play-install-referrer-library-requirements`](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/templates/specs/SPEC-2006-google-play-install-referrer-library-requirements.yaml) - Google Play Install Referrer Library Requirements
- [`spc:android-attribution-reporting-api-requirements`](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/templates/specs/SPEC-2007-android-attribution-reporting-api-requirements.yaml) - Android Attribution Reporting API Requirements
- [`spc:mobile-attribution-token-retention-requirements`](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/templates/specs/SPEC-2008-mobile-attribution-token-retention-requirements.yaml) - Mobile Attribution Token Retention Requirements
- [`spc:mobile-attribution-timestamp-requirements`](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/templates/specs/SPEC-2009-mobile-attribution-timestamp-requirements.yaml) - Mobile Attribution Timestamp Requirements
- [`spc:mobile-attribution-campaign-field-requirements`](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/templates/specs/SPEC-2010-mobile-attribution-campaign-field-requirements.yaml) - Mobile Attribution Campaign Field Requirements
- [`spc:mobile-attribution-privacy-review-requirements`](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/templates/specs/SPEC-2011-mobile-attribution-privacy-review-requirements.yaml) - Mobile Attribution Privacy Review Requirements
- [`spc:mobile-attribution-platform-status-requirements`](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/templates/specs/SPEC-2012-mobile-attribution-platform-status-requirements.yaml) - Mobile Attribution Platform Status Requirements

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

- GitHub package repository: [groupsum/mobile-install-attribution-governance-pack](https://github.com/groupsum/mobile-install-attribution-governance-pack)
- PyPI package: [mobile-install-attribution-governance-pack](https://pypi.org/project/mobile-install-attribution-governance-pack/)
- SSOT Registry: [ssot-registry](https://pypi.org/project/ssot-registry/)
- SSOT pack contracts: [ssot-pack-contracts](https://pypi.org/project/ssot-pack-contracts/)
