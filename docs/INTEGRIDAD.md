# Procedencia, integridad y reconstrucción

## Fuente primaria

Imagen upstream desde el [release oficial v1.20.0](https://github.com/justcallmekoko/ESP32Marauder/releases/tag/v1.20.0), variante **`_v6_1.bin`**, publicada el 28-10-2026.

La reconstrucción se interrumpe si el archivo descargado no tiene SHA-256 `7207c20fcd7f543d7544de878dc1582052dd4d2253bee8a28159a42ab5847cc6`.

## Matriz de hashes verificados

| Imagen | SHA-256 |
|---|---|
| Original upstream | `7207c20fcd7f543d7544de878dc1582052dd4d2253bee8a28159a42ab5847cc6` |
| V1 | `89b8d2662b202ae463b406efeab615446f311c318c29118314b01d3c7bcf2905` |
| V2 | `cff11b743e500e596cc1a1f75dd5599e6fbd6411575f0da0c22c0a11e1c84b0d` |
| V3 | `98c3593ebcfec5e078e63b1b67c3f096b1f137d42a4fb0cd50b96a2422efdd13` |
| V4 | `802f5ed2b6ec5ba13586fb85b469047204641b4dbdc089203b30f103dde938d5` |

Los cuatro binarios contienen 1.831.408 bytes. V4 es la versión recomendada.

## Construcción reproducible

```bash
python3 tools/reconstruir_firmwares.py --outdir firmware
```

Requisitos: Python 3.9+ y acceso HTTPS a los releases públicos de GitHub. Solo se usan módulos de la biblioteca estándar. El programa descarga la versión original y verifica SHA-256, aplica secuencialmente parches comprimidos `patches/v1...` a `patches/v4...`, comprueba la integridad por versión y produce los cuatro archivos `.bin`.

Formato de parche: flujo LZMA-ALONE codificado en Base64 de secuencias [*salto relativo*, *longitud*, *bytes reemplazados*], con enteros de longitud variable (LEB128 sin signo). Cada salto se calcula desde el final del rango anterior. No se modifican bytes no enumerados. Los SHA-256 de etapa son condición obligatoria para escribir las imágenes.

No se incluye respaldo completo de flash de ningún usuario, credenciales, memoria NVS ni datos sensibles.

## Verificación de publicación

El flujo de GitHub Actions intenta reconstruir el binario, comprobar los hashes, publicarlo en el directorio `firmware/` y crear una publicación de versión. Cualquier fallo debe tratarse como **publicación no verificada**; el código fuente y los deltas por sí solos no garantizan que el binario esté disponible en GitHub.

El histórico de pruebas de hardware fue comunicado por el propietario en un MaKing Lab con objetivo Marauder v6.1; no existe laboratorio acreditado ni certificación de radio.
