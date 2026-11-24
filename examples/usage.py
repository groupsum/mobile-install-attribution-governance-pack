"""Find a specification and its downstream path in the installed manifest."""

from ssot_pack_mobile_install_attribution import load_document_manifest

specification = next(
    row for row in load_document_manifest("spec")
    if row["id"] == "spc:apple-adattributionkit-framework-requirements"
)
assert specification["target_path"] == ".ssot/specs/SPEC-2001-apple-adattributionkit-framework-requirements.yaml"
