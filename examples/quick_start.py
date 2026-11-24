"""Inspect the installed pack identity."""

from ssot_pack_mobile_install_attribution import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:mobile-install-attribution"
print(metadata["origin"]["id"])
