# 🔐 Política de Seguridad — FTRT Cosmic Model

## Versiones soportadas

Este proyecto se encuentra en desarrollo activo. Solo la rama `main`
recibe actualizaciones de seguridad.

| Versión | Soportada |
|---------|-----------|
| main (última) | ✅ |
| ramas antiguas | ❌ |

## 🚨 Reportar una vulnerabilidad

Si descubres una vulnerabilidad de seguridad en este proyecto,
**NO abras un Issue público**. En su lugar, repórtala de forma privada:

- **Email:** ia.mechmind@gmail.com
- **Asunto sugerido:** `[SECURITY] FTRT Cosmic Model — <breve descripción>`

### Qué incluir en el reporte

1. Descripción clara del problema.
2. Pasos para reproducirlo (comandos exactos).
3. Versión afectada (commit hash o rama).
4. Impacto potencial (ej: ejecución remota, fuga de datos, DoS).
5. Si es posible, una propuesta de solución (PoC o parche).

### Tiempos de respuesta esperados

| Etapa | Tiempo objetivo |
|-------|-----------------|
| Confirmación de recepción | 48 horas |
| Evaluación inicial | 7 días |
| Corrección / mitigación | 30 días |

## 🔒 Buenas prácticas para contribuidores

- No subas **tokens, API keys, contraseñas** ni archivos `.env`.
- Usa variables de entorno o `~/.config` para credenciales locales.
- Revisa que `requirements.txt` no incluya paquetes con CVEs conocidos.
- Ejecuta `pip-audit` antes de cada PR:

  ```bash
  pip install pip-audit
  pip-audit -r requirements.txt
```

🤖 Dependabot

Este repositorio tiene Dependabot activado (.github/dependabot.yml)
para recibir actualizaciones automáticas semanales de dependencias Python
y parches de seguridad.

📜 Divulgación responsable

Pedimos a los investigadores que sigan el principio de divulgación
responsable: danos tiempo razonable para corregir el problema antes
de hacerlo público. En agradecimiento, acreditaremos tu hallazgo en el
CHANGELOG (si lo deseas).

📞 Contacto

· Mantenedor: Mechmind DWV
· Email: ia.mechmind@gmail.com
· Repositorio: https://github.com/mechmind-dwv/Ftrt_Cosmic_Model

---

Última actualización: 2026-09-11
