# 100 Conceptos de Startup · de cero a experto

Guía + glosario **visual** de las 100 ideas más importantes que todo founder debería dominar,
organizadas en **10 niveles** (de lo más básico a nivel experto). Cada concepto se explica desde
**3 ángulos**:

1. **Cómo funciona** — la definición operativa, sin paja.
2. **Analogía** — una imagen cotidiana para fijar la idea y poder explicarla a cualquiera.
3. **Ejemplo real** — cómo lo usa una startup gigante (Airbnb, Uber, Stripe, Slack, Notion…) o **AECODE**.

Además, **cada uno de los 100 conceptos** trae una banda de *insight* especial que lo profundiza: un **Dato** (estadística con fuente), una **Clave** (heurística para aplicarlo), una **Anécdota** (historia real), una **Cita** (frase de un grande) o una **Trampa** (error común a evitar) — con su propio ícono y color.

Presentación autocontenida: un solo `index.html`, sin build ni dependencias. **127 slides**,
**responsive** (en móvil hace reflow a lectura vertical), con **diagramas animados** que explican
cada bloque y muestran **cómo se conectan** los conceptos.

**Live:** https://apalpan.github.io/startup-100-conceptos/

## Qué la hace entendible (de principiante a experto)

- **El viaje de la startup** — una línea de tiempo que mapea cada nivel a una etapa real (idea → PMF → escala → exit).
- **Mapa de conexiones** — un hub que muestra las 3 cadenas clave: valor (Problema→Solución→PMF), económica (CAC→LTV→Churn→Runway) y de defensa (red+datos→Moat→Flywheel).
- **Síntesis visual por nivel** — cada bloque cierra con un diagrama **animado**: lean loop, anillos TAM/SAM/SOM, curva de Product-Market Fit, mini Business Model Canvas, balanza CAC vs LTV, embudo AARRR, growth loop, capas del moat, barras de rondas de inversión y la curva J al exit.
- **Intro de cada nivel** que lista los 10 conceptos que verás y cómo se conectan con otros niveles.
- **Ruta de dominio** en 4 escalones: Principiante → Operador → Estratega → Experto/Founder.

## Los 10 niveles

| Nivel | Bloque | Conceptos |
|------|--------|-----------|
| 1 | Fundamentos (qué es una startup, MVP, lean) | 01–10 |
| 2 | Cliente y mercado (ICP, JTBD, TAM/SAM/SOM) | 11–20 |
| 3 | Producto (del MVP al Product-Market Fit) | 21–30 |
| 4 | Modelo de negocio (pricing, freemium, marketplace) | 31–40 |
| 5 | Unit economics (CAC, LTV, burn, runway) | 41–50 |
| 6 | Métricas y crecimiento (North Star, AARRR, churn) | 51–60 |
| 7 | Growth y Go-to-Market (PLG, viral loop, funnel) | 61–70 |
| 8 | Estrategia y defensibilidad (moat, flywheel) | 71–80 |
| 9 | Fundraising y capital (rondas, valuation, SAFE) | 81–90 |
| 10 | Escala y experto (blitzscaling, M&A, IPO, categoría) | 91–100 |

## Cómo usar

- **Abrir**: doble clic en `index.html` (cualquier navegador) o desde Obsidian.
- **Navegar**: `←` / `→` o barra espaciadora · clic en los bordes · swipe en móvil.
- **Índice**: tecla `O` o el botón ☰ (jump directo a cualquiera de los 127 slides).
- **Móvil**: scroll vertical + swipe horizontal para cambiar de slide.
- **Tema**: tecla `T` o el botón ◐ — cicla **mix → todo oscuro → todo claro**.
- **Pantalla completa**: tecla `F`.

## Cómo iterar

Todo el contenido vive en la lista `LEVELS` de `build.py`. Edita y regenera:

```bash
python build.py
```

Cada concepto es una tupla `(nombre, término inglés, cómo funciona, analogía, ejemplo, fuente, [fórmula])`.

## Diseño

Usa el **design system oficial de AECODE**: violeta `#4A3AC1` + verde `#17B14E` + azul `#4465EE`
sobre lavanda claro `#F5F5F6` / navy `#0E1121`. Tipografía Manrope. Ritmo **light + dark combinado**
por nivel, con toggle global. Mismo motor de slides del Deck Maestro AECODE.

---

> Guía maestra de AECODE · 100 conceptos, 10 niveles. Pensada para *entender, explicar y aplicar*
> los fundamentos de startups — con ejemplos del mundo real y de la propia tesis de AECODE.
