# ESP32 Marauder — Edición Española (Fran Gonzas)

**Adaptación comunitaria no oficial al español de ESP32 Marauder v1.20.0, para hardware Marauder v6.1/v6.2 (ESP32 clásico).**

> **Autor y proyecto original:** [Just Call Me Koko — ESP32 Marauder](https://github.com/justcallmekoko/ESP32Marauder).  
> **Versión original utilizada:** [v1.20.0, publicada el 28 de octubre de 2026](https://github.com/justcallmekoko/ESP32Marauder/releases/tag/v1.20.0).  
> **Adaptación española, pruebas en dispositivo y personalización:** **Fran Gonzas**.  
> **Licencia:** MIT, conservando el aviso de copyright de la obra original.  
> Este repositorio **no es oficial** ni está afiliado, patrocinado o avalado por Just Call Me Koko.

## ¿Qué ofrece esta edición?

Se ha adaptado la interfaz de usuario al español mediante modificaciones controladas de cadenas de texto de la imagen binaria oficial. La traducción se desarrolló en cuatro revisiones (V1, V2, V3 y V4), comprobadas sucesivamente en un equipo MaKing Lab con perfil **Marauder v6.1**. La V4 añade una pantalla de inicio identificada como **Marauder ES V4**, mantiene el logo original y presenta el crédito **Fran Gonzas**. El código ejecutable original no se modifica intencionadamente.

**Importante:** esto es una **modificación binaria y localización**, no una recompilación del código fuente ni una versión oficial de Marauder. La traducción es amplia, pero pueden quedar etiquetas técnicas en inglés y abreviaturas sin tildes para respetar el espacio de memoria.

## Descarga

La edición recomendada es **V4**, para **Marauder v6.1/v6.2**. Encontrarás los binarios en `firmware/` cuando finalice su proceso automático de publicación y, cuando esté disponible, en [Releases](../../releases). Consulta [INSTALACION.md](docs/INSTALACION.md) antes de flashear.

| Imagen | SHA-256 |
|---|---|
| Upstream oficial v1.20.0 `_v6_1.bin` | `7207c20fcd7f543d7544de878dc1582052dd4d2253bee8a28159a42ab5847cc6` |
| Edición española V4 | `802f5ed2b6ec5ba13586fb85b469047204641b4dbdc089203b30f103dde938d5` |

Se publica un procedimiento de **reconstrucción reproducible** que descarga la imagen original desde el release oficial, verifica su SHA-256, aplica solamente el parche documentado y verifica el SHA-256 final. **No** contiene imágenes de flash completas, secretos, credenciales ni copias de seguridad particulares.

## Documentación

- [Instalación, requisitos y recuperación](docs/INSTALACION.md)
- [Origen del software, créditos y términos de redistribución](docs/ORIGEN_Y_LICENCIA.md)
- [Historial de las cuatro versiones](CHANGELOG.md)
- [Integridad y reproducibilidad](docs/INTEGRIDAD.md)
- [Seguridad, uso responsable y reporte de incidencias](SECURITY.md)

## Alcance y compatibilidad

**Solo** firmware para el microcontrolador **ESP32 clásico** del objetivo **Marauder v6.1/v6.2**. **No es compatible** con ESP32-C5, ESP32-S3 ni otras placas que emplean archivos específicos. Algunos dispositivos de doble procesador contienen un ESP32-C5 independiente: **no instales este firmware en ese chip**.

Las pruebas de usuario confirman instalación, encendido y funcionamiento de la interfaz en el hardware indicado, pero **no** constituyen certificación exhaustiva de todas las funciones inalámbricas ni garantía de compatibilidad con otros dispositivos.

## Licencia y procedencia

El firmware original y sus partes derivadas mantienen el aviso original **Copyright (c) 2020 Just Call Me Koko**, y los términos de la **licencia MIT** en [LICENSE](LICENSE). Los documentos y cambios aportados por Fran Gonzas se distribuyen bajo los mismos términos, en la medida aplicable. Se preserva la atribución al proyecto original y se evita presentarlo como creación íntegramente nueva.

**Uso exclusivamente en sistemas propios o con autorización.** Respeta la legislación de radiofrecuencia y las normas de tu jurisdicción.
