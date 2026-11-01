# Preguntas frecuentes (FAQ)

## ¿Es un proyecto oficial de ESP32 Marauder?

No. Es una adaptación española comunitaria realizada por Fran Gonzas a partir del **ESP32 Marauder v1.20.0** de Just Call Me Koko. Se conserva la atribución y la licencia MIT original. [Origen y créditos](ORIGEN_Y_LICENCIA.md).

## ¿Qué placa necesita?

La variante **Marauder v6.1/v6.2**, basada en **ESP32 clásico**. No se debe utilizar en ESP32-C5, ESP32-S3, versiones v6.0 o placas con otro perfil. Consulta el hardware admitido en la documentación upstream.

## Mi dispositivo tiene dos ESP32. ¿Instalo este archivo en ambos?

**No.** Algunos modelos MaKing Lab emplean un microcontrolador para la pantalla y otro ESP32-C5 para WiFi de 5 GHz. Este firmware está destinado únicamente al sistema que utiliza el perfil **Marauder v6.1/v6.2**. El ESP32-C5 requiere su imagen específica.

## ¿Qué cambia respecto al firmware original?

Solo la localización y algunas cadenas de identificación en la interfaz; no es una modificación de las rutinas inalámbricas. V4 presenta **Marauder ES V4** y **Fran Gonzas** al arrancar. No se han reprogramado ni añadido funciones de WiFi, Bluetooth, GPS o radio.

## ¿Está completamente traducido?

Se ha alcanzado una traducción muy amplia de los menús, pero pueden quedar abreviaturas, etiquetas técnicas sin traducir o textos ASCII sin tildes. El usuario de referencia estimó alrededor del 95 % en la V3; no es una medición automatizada de cobertura lingüística.

## ¿Qué archivo debo descargar?

La edición actual recomendada es `ESP32_MARAUDER_v1.20.0_ES_V4_FRAN_GONZAS.bin`. Conservamos V1–V3 por trazabilidad y recuperación de versiones anteriores.

## ¿Cómo sé que el binario es auténtico?

Verifica el SHA-256 con la tabla de [integridad](INTEGRIDAD.md). Para V4 es `802f5ed2b6ec5ba13586fb85b469047204641b4dbdc089203b30f103dde938d5`.

## ¿Hay código fuente para recompilar esta versión?

No se ha recompilado desde fuentes: esta edición modifica de manera controlada cadenas del binario oficial. Se incluye una herramienta Python y parches por versión que reconstruyen exactamente los cuatro `.bin` y verifican cada SHA-256. El **código fuente original** está en el [repositorio de Just Call Me Koko](https://github.com/justcallmekoko/ESP32Marauder).

## ¿Cómo informar un error?

Crea una incidencia usando la plantilla del repositorio. Incluye la ruta del menú, el texto visto y una propuesta de traducción. Nunca adjuntes secretos, contraseñas ni volcados completos de flash.
