"""Resolve and read a packaged specification without synchronizing it."""

from ssot_pack_mobile_install_attribution import load_document_manifest, read_packaged_document_text

spec = next(row for row in load_document_manifest("spec") if row["id"] == "spc:apple-adattributionkit-framework-requirements")
document = read_packaged_document_text("spec", spec["filename"])
assert spec["id"] in document
