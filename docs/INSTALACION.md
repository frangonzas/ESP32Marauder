# Instalación segura — ESP32 Marauder ES V4

## Requisitos

- Dispositivo compatible con el objetivo **Marauder v6.1/v6.2 (ESP32 clásico)**; verificar inscripción de la PCB y modelo exacto.
- Firmware actual operativo y, preferiblemente, copia probada de recuperación (por ejemplo, V3).
- Tarjeta microSD funcional con su sistema de archivos habitual.
- Método documentado de recuperación por USB/serial si la actualización falla.

**No usar** este binario en ESP32-C5, ESP32-S3, Flipper Zero WiFi Dev Board, Marauder v6.0 ni otras placas. En equipos de doble procesador, el firmware de la pantalla y el del ESP32-C5 son independientes.

## Archivos y autenticidad

Versión recomendada: `firmware/ESP32_MARAUDER_v1.20.0_ES_V4_FRAN_GONZAS.bin`.

Antes de flashear, comprobar SHA-256:

```bash
shasum -a 256 ESP32_MARAUDER_v1.20.0_ES_V4_FRAN_GONZAS.bin
```

Resultado esperado:

```text
802f5ed2b6ec5ba13586fb85b469047204641b4dbdc089203b30f103dde938d5
```

## Actualización desde microSD

1. Guardar el binario anterior y, si procede, exportar los datos de configuración.
2. Copiar el firmware V4 a la raíz de la microSD.
3. Si tu actualizador de Marauder busca `update.bin`, renombrar **una copia** del archivo V4 a `update.bin`. Evitar varios archivos con el mismo nombre.
4. Introducir la tarjeta y usar **Dispositivo / Actualizar firmware / Actualización SD**, o el menú equivalente de la versión instalada.
5. Mantener alimentación estable y no interrumpir la escritura ni el primer reinicio.
6. Confirmar el arranque, la versión, la traducción y la disponibilidad de los menús habituales.

La ruta exacta puede variar con el firmware instalado. Consultar las [instrucciones oficiales de actualización](https://github.com/justcallmekoko/ESP32Marauder/wiki/update-firmware).

## Verificaciones tras instalar

- Aparece **Marauder ES V4** al iniciar, se conserva el logotipo original y se identifica **Fran Gonzas**.
- El sistema sigue mostrando la versión base **v1.20.0**.
- Pantalla táctil, acceso a microSD, menús WiFi/BLE y apagado/reinicio se comportan normalmente.
- Las funciones inalámbricas que se utilicen deben probarse únicamente en entornos propios o autorizados.

## Recuperación y limitaciones

Si la actualización falla, **no flashear imágenes de otra placa**. Restaurar la imagen compatible anterior mediante el procedimiento oficial de actualización/recuperación y, si fuera necesario, el puerto USB/serie según el hardware concreto.

La prueba satisfactoria en una unidad MaKing Lab no garantiza compatibilidad con todas las revisiones, pantallas ni memorias flash. Los cambios han sido validados estáticamente y probados en el equipo del adaptador, no sometidos a certificación completa.
