# mobile-install-attribution-governance-pack

<!-- readme-standards:begin branding -->
<p align="center"><a href="https://github.com/groupsum/readme-standards"><img src="https://raw.githubusercontent.com/groupsum/readme-standards/master/docs/assets/readme-standards.svg" alt="Groupsum README Standards" width="300"></a></p>
<p align="center"><strong>mobile-install-attribution-governance-pack</strong></p>
<p align="center">Installable SSOT governance pack for Apple and Android mobile install attribution, app campaign attribution, and privacy-preserving app measurement.</p>
<p align="center">
<a href="https://pypi.org/project/mobile-install-attribution-governance-pack/"><img alt="pypi: mobile-install-attribution-governance-pack" src="https://img.shields.io/pypi/v/mobile-install-attribution-governance-pack?labelColor=1E293B&amp;color=1D4ED8"></a>
<a href="https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/pyproject.toml"><img alt="Source version: 0.1.1.dev1" src="https://img.shields.io/static/v1?label=Source%20version&amp;message=0.1.1.dev1&amp;labelColor=1E293B&amp;color=4338CA"></a>
<a href="https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/pyproject.toml"><img alt="Python: &gt;=3.10,&lt;3.15" src="https://img.shields.io/static/v1?label=Python&amp;message=%3E%3D3.10%2C%3C3.15&amp;labelColor=1E293B&amp;color=0F766E"></a>
<a href="https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/pyproject.toml"><img alt="Layer: governance" src="https://img.shields.io/static/v1?label=Layer&amp;message=governance&amp;labelColor=1E293B&amp;color=6D28D9"></a>
<a href="https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/README.md#lifecycle-and-migration"><img alt="Lifecycle: active" src="https://img.shields.io/static/v1?label=Lifecycle&amp;message=active&amp;labelColor=1E293B&amp;color=166534"></a>
<a href="https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/LICENSE"><img alt="License: Apache-2.0" src="https://img.shields.io/static/v1?label=License&amp;message=Apache-2.0&amp;labelColor=1E293B&amp;color=86198F"></a>
<a href="https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/README.md#notices"><img alt="Notice: not required" src="https://img.shields.io/static/v1?label=Notice&amp;message=not%20required&amp;labelColor=1E293B&amp;color=475569"></a>
</p>
<p align="center">
<a href="https://pypi.org/project/mobile-install-attribution-governance-pack/"><img alt="Monthly PyPI downloads: mobile-install-attribution-governance-pack" src="https://img.shields.io/pypi/dm/mobile-install-attribution-governance-pack?labelColor=1E293B&amp;color=0E7490"></a>
<a href="https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/README.md"><img alt="README hits: mobile-install-attribution-governance-pack" src="https://hits.sh/github.com/groupsum/mobile-install-attribution-governance-pack/README.md.svg?label=README%20hits&amp;labelColor=1E293B&amp;color=0E7490"></a>
</p>
<p align="center">
<a href="https://github.com/groupsum/mobile-install-attribution-governance-pack/actions/workflows/readme-standards.yml"><img alt="README standards: CI gate" src="https://img.shields.io/static/v1?label=README%20standards&amp;message=CI%20gate&amp;labelColor=1E293B&amp;color=1D4ED8"></a>
<a href="https://github.com/groupsum/mobile-install-attribution-governance-pack/actions/workflows/readme-standards.yml"><img alt="Tests: package and example checks" src="https://img.shields.io/static/v1?label=Tests&amp;message=package%20and%20example%20checks&amp;labelColor=1E293B&amp;color=0F766E"></a>
<a href="https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/README.md#certification-status"><img alt="Certification: not certified" src="https://img.shields.io/static/v1?label=Certification&amp;message=not%20certified&amp;labelColor=1E293B&amp;color=92400E"></a>
<a href="https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/docs/governance/pack-authoring-guide.md"><img alt="Governance: pack governance" src="https://img.shields.io/static/v1?label=Governance&amp;message=pack%20governance&amp;labelColor=1E293B&amp;color=4338CA"></a>
<a href="https://github.com/groupsum/mobile-install-attribution-governance-pack/actions/workflows/readme-standards.yml"><img alt="Evidence: README and wheel checks" src="https://img.shields.io/static/v1?label=Evidence&amp;message=README%20and%20wheel%20checks&amp;labelColor=1E293B&amp;color=6D28D9"></a>
</p>
<p align="center"><a href="#overview">Overview</a> · <a href="#installation">Installation</a> · <a href="#quick-start">Quick Start</a> · <a href="#usage">Usage</a> · <a href="#public-api-and-import-surfaces">API</a> · <a href="#contributing">Contributing</a> · <a href="#governance">Governance</a> · <a href="#license">License</a></p>
<!-- readme-standards:end branding -->

---

## Overview

### Summary

Installable SSOT governance pack for Apple and Android mobile install attribution, app campaign attribution, and privacy-preserving app measurement.

### Why This Package

Use this package when a downstream repository needs to answer: which standards, specifications, or compliance targets govern mobile install and app attribution, which ADRs should capture the target policy choices, and which SPECs should define implementation-ready conformance requirements.

### When to Use

Use this pack when a downstream SSOT Registry needs reusable decisions and requirements for Mobile Install And App Attribution.

### Features

**Included ADRs**

- [`adr:mobile-install-attribution-source-policy`](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/templates/adr/ADR-1001-mobile-install-attribution-source-policy.yaml) — Mobile Install Attribution Source Policy
- [`adr:apple-adattributionkit-policy`](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/templates/adr/ADR-1002-apple-adattributionkit-policy.yaml) — Apple AdAttributionKit Policy
- [`adr:apple-adservices-token-policy`](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/templates/adr/ADR-1003-apple-adservices-token-policy.yaml) — Apple AdServices Token Policy
- [`adr:android-install-referrer-policy`](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/templates/adr/ADR-1004-android-install-referrer-policy.yaml) — Android Install Referrer Policy
- [`adr:android-attribution-reporting-status-policy`](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/templates/adr/ADR-1005-android-attribution-reporting-status-policy.yaml) — Android Attribution Reporting Status Policy
- [`adr:mobile-attribution-privacy-data-policy`](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/templates/adr/ADR-1006-mobile-attribution-privacy-data-policy.yaml) — Mobile Attribution Privacy Data Policy
- [`adr:mobile-attribution-window-policy`](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/templates/adr/ADR-1007-mobile-attribution-window-policy.yaml) — Mobile Attribution Window Policy
- [`adr:mobile-attribution-evidence-policy`](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/templates/adr/ADR-1008-mobile-attribution-evidence-policy.yaml) — Mobile Attribution Evidence Policy

**Included SPECs**

- [`spc:apple-adattributionkit-framework-requirements`](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/templates/specs/SPEC-2001-apple-adattributionkit-framework-requirements.yaml) — Apple AdAttributionKit Framework Requirements
- [`spc:apple-adattributionkit-attribution-rule-requirements`](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/templates/specs/SPEC-2002-apple-adattributionkit-attribution-rule-requirements.yaml) — Apple AdAttributionKit Attribution Rule Requirements
- [`spc:apple-adservices-token-requirements`](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/templates/specs/SPEC-2003-apple-adservices-token-requirements.yaml) — Apple AdServices Token Requirements
- [`spc:apple-adservices-attribution-payload-requirements`](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/templates/specs/SPEC-2004-apple-adservices-attribution-payload-requirements.yaml) — Apple AdServices Attribution Payload Requirements
- [`spc:google-play-install-referrer-api-requirements`](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/templates/specs/SPEC-2005-google-play-install-referrer-api-requirements.yaml) — Google Play Install Referrer API Requirements
- [`spc:google-play-install-referrer-library-requirements`](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/templates/specs/SPEC-2006-google-play-install-referrer-library-requirements.yaml) — Google Play Install Referrer Library Requirements
- [`spc:android-attribution-reporting-api-requirements`](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/templates/specs/SPEC-2007-android-attribution-reporting-api-requirements.yaml) — Android Attribution Reporting API Requirements
- [`spc:mobile-attribution-token-retention-requirements`](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/templates/specs/SPEC-2008-mobile-attribution-token-retention-requirements.yaml) — Mobile Attribution Token Retention Requirements
- [`spc:mobile-attribution-timestamp-requirements`](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/templates/specs/SPEC-2009-mobile-attribution-timestamp-requirements.yaml) — Mobile Attribution Timestamp Requirements
- [`spc:mobile-attribution-campaign-field-requirements`](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/templates/specs/SPEC-2010-mobile-attribution-campaign-field-requirements.yaml) — Mobile Attribution Campaign Field Requirements
- [`spc:mobile-attribution-privacy-review-requirements`](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/templates/specs/SPEC-2011-mobile-attribution-privacy-review-requirements.yaml) — Mobile Attribution Privacy Review Requirements
- [`spc:mobile-attribution-platform-status-requirements`](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/templates/specs/SPEC-2012-mobile-attribution-platform-status-requirements.yaml) — Mobile Attribution Platform Status Requirements

### Non-Goals

The pack supplies governance records. A downstream application implements the controls and collects its own conformance evidence.

---

## Getting Started

### Prerequisites

Use Python `>=3.10,<3.15`. Downstream synchronization also requires SSOT Registry and permission to write the target registry.

### Installation

If the desired PyPI release is a prerelease, use its exact version in the installer command.

#### uv

<!-- readme-standards:begin installation.uv -->
```bash
uv add mobile-install-attribution-governance-pack
```
<!-- readme-standards:end installation.uv -->

#### pip

<!-- readme-standards:begin installation.pip -->
```bash
python -m pip install mobile-install-attribution-governance-pack
```
<!-- readme-standards:end installation.pip -->

#### Poetry

<!-- readme-standards:begin installation.poetry -->
```bash
poetry add mobile-install-attribution-governance-pack
```
<!-- readme-standards:end installation.poetry -->

### Quick Start

#### Example

<!-- readme-standards:begin example.quick-start -->
Source: [examples/quick_start.py](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/examples/quick_start.py).

```python
"""Inspect the installed pack identity."""

from ssot_pack_mobile_install_attribution import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:mobile-install-attribution"
print(metadata["origin"]["id"])
```
<!-- readme-standards:end example.quick-start -->

#### Expected Result

The script prints `pack:mobile-install-attribution` from the installed pack metadata.

---

## Usage

### Common Workflows

<!-- readme-standards:begin example.usage -->
Source: [examples/usage.py](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/examples/usage.py).

```python
"""Find a specification and its downstream path in the installed manifest."""

from ssot_pack_mobile_install_attribution import load_document_manifest

specification = next(
    row for row in load_document_manifest("spec")
    if row["id"] == "spc:apple-adattributionkit-framework-requirements"
)
assert specification["target_path"] == ".ssot/specs/SPEC-2001-apple-adattributionkit-framework-requirements.yaml"
```
<!-- readme-standards:end example.usage -->

Use the downstream environment that has both SSOT Registry and `mobile-install-attribution-governance-pack` installed. Inspect the pack and preflight the target registry before approving synchronization.

```bash
uv run ssot pack inspect ssot_pack_mobile_install_attribution
uv run ssot pack preflight . ssot_pack_mobile_install_attribution --all
uv run ssot pack sync . ssot_pack_mobile_install_attribution --all --trust --yes
uv run ssot validate .
```

### Configuration

Select the installed import package `ssot_pack_mobile_install_attribution` in SSOT Registry. Review reservation owner `extension-pack:mobile-install-attribution-governance-pack` and the target's trust policy before syncing.

### Error Handling

If preflight reports a schema, trust, or document-number conflict, resolve it in the target registry and repeat preflight before synchronization.

### Best Practices

Pin the pack version in downstream projects. Reference document IDs in local governance and inspect the change set before granting trust.

---

## Package Boundary

### What It Owns

The pack owns the Mobile Install And App Attribution ADRs and SPECs listed under Features.

### Public API and Import Surfaces

Import `load_pack_metadata`, `load_document_manifest`, and `read_packaged_document_text` from `ssot_pack_mobile_install_attribution` to inspect packaged records.

### Entry Points

<!-- readme-standards:begin entry-points -->
This package declares no command-line, GUI, or plugin entry points in its manifest.
<!-- readme-standards:end entry-points -->

### Injected Dependencies

The package binds its metadata and document loaders through `ssot-pack-contracts`. The caller supplies the target registry to SSOT Registry when synchronizing.

### Protocol Consumers

SSOT Registry uses the pack metadata, document manifests, and bundled templates during inspect, preflight, and sync.

### Extensions

Define downstream policies as local records and reference the pack's document IDs. Send proposed changes to the canonical pack through repository review.

---

## Operations and Readiness

### Operational Requirements

Local inspection reads installed package resources. Synchronization requires an initialized downstream registry and explicit operator approval.

### Health and Observability

Review the preflight and sync output, then use `ssot validate` to check the resulting registry.

### Security and Resource Limits

Implicit trust is disabled. Review the exact distribution, version, records, and reserved IDs before enabling trust in a target registry.

### Compatibility

- Python `>=3.10,<3.15`
- SSOT Registry schema `>=0.4.0`
- SSOT pack contracts `>=0.2.17,<0.3.0`

---

## Verification

### Tests

Run `python -m unittest discover -s tests -v` with the pack installed. The [README workflow](https://github.com/groupsum/mobile-install-attribution-governance-pack/actions/workflows/readme-standards.yml) checks the source README and runs both examples against an installed wheel.

### Certification Status

The pack has no external certification. Downstream adoption requires evidence for the controls an application implements.

### Evidence

See the [README workflow](https://github.com/groupsum/mobile-install-attribution-governance-pack/actions/workflows/readme-standards.yml) for package and documentation verification and the [packaged records](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/templates) for document-level sources.

---

## FAQ

### Why

**Why do document IDs matter?** Downstream records use them to trace an adopted decision or requirement to the pack that owns it.

### How

**How do I preview changes?** Use the registry's pack preflight before approving a sync.

### When

**When should I upgrade?** Read the changelog and preflight the new version against the target registry before applying it.

---

## Documentation and Related Packages

### More Documentation

See the [Pack guide](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/docs/pack-guide.md), [changelog](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/CHANGELOG.md), and [pack metadata](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/src/ssot_pack_mobile_install_attribution/metadata.json).

### Related Packages

[SSOT Registry](https://pypi.org/project/ssot-registry/) manages downstream registries. [SSOT Pack Contracts](https://pypi.org/project/ssot-pack-contracts/) provides the shared pack interface.

### Project Links

<!-- readme-standards:begin project-links -->
- [Homepage](https://github.com/groupsum/mobile-install-attribution-governance-pack)
- [Issues](https://github.com/groupsum/mobile-install-attribution-governance-pack/issues)
- [Repository](https://github.com/groupsum/mobile-install-attribution-governance-pack)
- [pypi: mobile-install-attribution-governance-pack](https://pypi.org/project/mobile-install-attribution-governance-pack/)
<!-- readme-standards:end project-links -->

---

## Contributing

### How to Contribute

Open an [issue](https://github.com/groupsum/mobile-install-attribution-governance-pack/issues) or pull request describing the affected records, their authority, and the expected downstream effect.

### Development Setup

Install the checkout with `python -m pip install -e .`, then run `python -m unittest discover -s tests -v`. On Python 3.11 or newer, run `uvx --from readme-standards==0.1.3 readme-standards check`.

### Notes for Maintainers

Keep source links, document identifiers, and committed manifest hashes aligned. Run `uvx --from readme-standards==0.1.3 readme-standards render --write` after changing generated README inputs.

---

## Governance

### Ownership and Decision Making

Groupsum maintains `pack:mobile-install-attribution`. The pack's reservation owner is `extension-pack:mobile-install-attribution-governance-pack`. Downstream registry operators approve synchronization.

### Standards and Policies

**Authority Sources**

- [Apple AdAttributionKit](https://developer.apple.com/app-store/ad-attribution/)
- [Apple AdAttributionKit attribution rules](https://developer.apple.com/documentation/adattributionkit/configuring-attribution-rules-for-your-app)
- [Apple AdServices framework](https://developer.apple.com/documentation/AdServices/)
- [Apple AdServices attribution payloads](https://developer.apple.com/documentation/AdServices/AAAttribution/attributionToken%28%29)
- [Google Play Install Referrer API](https://developer.android.com/google/play/installreferrer)
- [Google Play Install Referrer Library](https://developer.android.com/google/play/installreferrer/library)
- [Privacy Sandbox on Android Attribution Reporting API](https://developers.google.com/admob/android/privacy/sandbox)

### Lifecycle and Migration

Review [release changes](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/CHANGELOG.md) and preflight the chosen version against each downstream registry.

---

## License and Attribution

### License

<!-- readme-standards:begin license -->
Licensed under `Apache-2.0`. See [LICENSE](https://github.com/groupsum/mobile-install-attribution-governance-pack/blob/master/LICENSE).
<!-- readme-standards:end license -->

### Notices

<!-- readme-standards:begin notices -->
No separate NOTICE file is declared. Review the license and bundled third-party attributions.
<!-- readme-standards:end notices -->
