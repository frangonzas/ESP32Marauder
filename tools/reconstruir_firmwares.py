#!/usr/bin/env python3
"""Reconstrucción reproducible de ESP32 Marauder v1.20.0 ES, V1–V4.

Proyecto original: Just Call Me Koko — licencia MIT.
Adaptación no oficial al español: Fran Gonzas.
Únicamente modifica offsets enumerados; NO recompila el código fuente.
"""
from __future__ import annotations
import argparse
import base64
import hashlib
import lzma
from pathlib import Path
import urllib.request

BASE_URL = (
    "https://github.com/justcallmekoko/ESP32Marauder/releases/download/v1.20.0/"
    "esp32_marauder_v1_20_0_20261028_v6_1.bin"
)
EXPECTED = {
    "official": "7207c20fcd7f543d7544de878dc1582052dd4d2253bee8a28159a42ab5847cc6",
    "v1": "89b8d2662b202ae463b406efeab615446f311c318c29118314b01d3c7bcf2905",
    "v2": "cff11b743e500e596cc1a1f75dd5599e6fbd6411575f0da0c22c0a11e1c84b0d",
    "v3": "98c3593ebcfec5e078e63b1b67c3f096b1f137d42a4fb0cd50b96a2422efdd13",
    "v4": "802f5ed2b6ec5ba13586fb85b469047204641b4dbdc089203b30f103dde938d5",
}
FILES = {
    "v1": "ESP32_MARAUDER_v1.20.0_ES_V1.bin",
    "v2": "ESP32_MARAUDER_v1.20.0_ES_V2.bin",
    "v3": "ESP32_MARAUDER_v1.20.0_ES_V3.bin",
    "v4": "ESP32_MARAUDER_v1.20.0_ES_V4_FRAN_GONZAS.bin",
}
ROOT = Path(__file__).resolve().parent.parent

def verify(data: bytes, version: str) -> None:
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED[version]:
        raise ValueError(f"SHA-256 incorrecto {version}: {digest}; esperado {EXPECTED[version]}")
    if len(data) != 1_831_408 or data[:2] != b"\xe9\x06":
        raise ValueError(f"Formato/tamaño inesperado en {version}")
    print(f"[OK] {version}: {len(data):,} bytes; SHA-256 {digest}", flush=True)

def read_varint(raw: bytes, position: int) -> tuple[int, int]:
    value, shift = 0, 0
    while True:
        if position >= len(raw) or shift >= 63:
            raise ValueError("Parche truncado o valor inválido")
        byte = raw[position]
        position += 1
        value |= (byte & 127) << shift
        if byte < 128:
            return value, position
        shift += 7

def apply_patch(base: bytes, filename: Path) -> bytes:
    encoded = filename.read_text(encoding="ascii").strip()
    diff = lzma.decompress(base64.b64decode(encoded, validate=True), format=lzma.FORMAT_ALONE)
    data = bytearray(base)
    end, pos = 0, 0
    while pos < len(diff):
        gap, pos = read_varint(diff, pos)
        size, pos = read_varint(diff, pos)
        start = end + gap
        if not size or pos + size > len(diff) or start + size > len(data):
            raise ValueError(f"Rango de parche inválido en {filename}")
        data[start:start + size] = diff[pos:pos + size]
        pos += size
        end = start + size
    return bytes(data)

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", type=Path, help="Binario oficial descargado localmente")
    parser.add_argument("--outdir", type=Path, default=ROOT / "firmware")
    args = parser.parse_args()
    if args.base:
        data = args.base.read_bytes()
    else:
        print("Descargando imagen oficial v1.20.0 para Marauder v6.1/v6.2...", flush=True)
        req = urllib.request.Request(BASE_URL, headers={"User-Agent": "ESP32Marauder-ES/1.0"})
        with urllib.request.urlopen(req, timeout=90) as response:
            data = response.read()
    verify(data, "official")
    args.outdir.mkdir(parents=True, exist_ok=True)
    for version in ("v1", "v2", "v3", "v4"):
        data = apply_patch(data, ROOT / "patches" / f"{version}.delta.lzma.b64")
        verify(data, version)
        dst = args.outdir / FILES[version]
        dst.write_bytes(data)
        print(f"    Archivo: {dst}", flush=True)
    sums = "".join(f"{EXPECTED[v]}  {FILES[v]}\n" for v in FILES)
    (args.outdir / "SHA256SUMS.txt").write_text(sums, encoding="ascii")
    print("[OK] Reconstrucción reproducible completada.", flush=True)

if __name__ == "__main__":
    main()
