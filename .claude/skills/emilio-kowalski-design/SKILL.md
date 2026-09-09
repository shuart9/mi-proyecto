---
name: emilio-kowalski-design
description: |
  Diseña y critica cualquier pieza visual con los principios de Emilio Kowalski:
  jerarquía por contraste, espaciado como sistema, alineación óptica, tipografía
  afinada, color restringido, profundidad por capas y motion con easing.
  Úsala SIEMPRE que se pida diseñar, rediseñar, mejorar, criticar o "que se vea
  pro": miniaturas de YouTube, portadas y carruseles de Instagram/TikTok, posters,
  landing pages, UI, slides, banners, logos, lower-thirds y animaciones.
  También cuando el usuario diga que algo "se ve amateur", "le falta algo",
  "no se ve limpio", "hazlo más premium" o pida un design review.
  NO es para escribir copy sin componente visual ni para generar imágenes
  fotorrealistas de producto (usa las skills de Higgsfield para eso).
argument-hint: "[critica|diseña|sistema] [descripción de la pieza o ruta al archivo]"
---

# Emilio Kowalski Design

Sistema de decisiones visuales. No opiniones: reglas verificables.
Regla madre: **todo elemento debe justificar su existencia y su posición. Si no comunica, fuera.**

## 0. Antes de tocar nada

Responde 3 cosas en una línea cada una:
1. **Mensaje único** — qué debe entender alguien en 0.4s.
2. **Punto focal** — qué elemento carga ese mensaje (solo UNO).
3. **Contexto** — tamaño real de visualización (feed móvil, grid de YouTube, pantalla completa).

Si la pieza es para feed/miniatura: diseña mirándola al 15% de su tamaño. Si a ese tamaño no se lee el mensaje, el diseño está mal, no el espectador.

## 1. Jerarquía = contraste, no decoración

- Un elemento domina, uno secundario, el resto sirve. Nunca dos protagonistas.
- Crea jerarquía con, en este orden: **tamaño → peso → color/luminancia → espacio → posición**.
- Salto de escala real: cada nivel al menos **1.5–2x** del anterior. Diferencias tímidas (18px vs 20px) leen como error, no como jerarquía.
- El elemento más importante recibe el mayor contraste contra su fondo, no el color más llamativo.
- Nunca uses efectos (glow, outline, degradado, sombra dura) para arreglar jerarquía. Arregla escala y contraste primero; los efectos son el último 5%.

## 2. Espaciado: el sistema que separa amateur de pro

- Usa una **escala** y nada fuera de ella: 4, 8, 12, 16, 24, 32, 48, 64, 96, 128.
- **Proximidad = pertenencia.** Elementos relacionados se pegan; el espacio entre grupos siempre mayor que el espacio dentro del grupo (mínimo 2x). El 80% de los diseños que "se ven raros" fallan aquí.
- El espacio bajo un título pertenece al título: menos espacio a su subtítulo que al bloque siguiente.
- Márgenes exteriores ≥ espacio interior máximo. Nada respirando contra el borde.
- Espacio negativo generoso = percepción de premium. Apretado = barato. Si dudas, quita elementos antes de reducir espacio.

## 3. Alineación

- Todo se alinea con algo. Cero elementos flotando "a ojo".
- Máximo 2 ejes de alineación por composición.
- **Alineación óptica > matemática**: comillas, puntuación, formas redondas (círculos, triángulos, iconos) y textos con mucho espacio lateral requieren corrección manual. Confía en el ojo, no en el valor de X.
- Texto centrado solo en bloques cortos (≤3 líneas). Párrafos: siempre alineados a la izquierda.
- Ilusión óptica clave: un círculo debe ser ~2-4% mayor que un cuadrado para pesar igual; un triángulo dentro de un botón play va desplazado a la derecha respecto al centro geométrico.

## 4. Tipografía

- Máximo **2 familias** (o 1 familia con varios pesos). Si dudas: una sola, bien usada.
- Contraste de pesos real: 400 vs 700, no 500 vs 600.
- **Tracking inverso al tamaño**: títulos grandes → tracking negativo (-1% a -3%); texto pequeño y mayúsculas → tracking positivo (+2% a +8%).
- **Line-height inverso al tamaño**: display 0.9–1.1, cuerpo 1.4–1.6.
- Ancho de línea 45–75 caracteres. Más = ilegible.
- Nunca estires ni condenses tipografía manualmente. Usa la versión condensed real.
- Evita fuentes de sistema por defecto en piezas de marca; delatan falta de decisión.
- Jamás uses color para crear jerarquía cuando el tamaño y el peso pueden hacerlo.

## 5. Color

- Estructura: **1 color dominante + neutros + 1 acento** usado en menos del 10% del área.
- El acento solo en lo que quieres que se mire. Si todo es acento, nada lo es.
- Fondos grandes: baja saturación. Elementos pequeños: alta saturación permitida.
- Nunca #000 puro ni #FFF puro en piezas de marca. Usa negros y blancos teñidos con el hue dominante.
- Sombras: no negro con opacidad; sombra del hue complementario/oscuro del fondo, muy suave, gran radio, offset corto.
- Verifica **contraste de luminancia**, no de hue: convierte a escala de grises mentalmente. Si el texto desaparece en gris, no es legible.
- Degradados: solo entre hues cercanos, sutiles. Un degradado de 2 colores opuestos siempre se ve barato.

## 6. Profundidad y capas

- Profundidad se construye con: escala + desenfoque + superposición + luminancia, no con sombras duras.
- Lo cercano: grande, nítido, con más contraste. Lo lejano: pequeño, difuso, desaturado.
- Superponer elementos (recorte sobre texto, sujeto rompiendo el marco) crea capas y dirige la mirada — el recurso más rentable en miniaturas.

## 7. Motion (si la pieza se anima)

- **Nada lineal.** Easing por defecto: ease-out para entradas, ease-in-out para transiciones, ease-in solo para salidas.
- Duración: 150–300ms para UI, 400–800ms para piezas de marca. Si se nota "lento", quita 100ms.
- **Stagger** de 40–80ms entre elementos de un mismo grupo; entran en orden de jerarquía.
- Anticipación y overshoot leves (5–10%) para elementos con personalidad; cero overshoot en UI funcional.
- La cámara/composición se mueve en una sola dirección por escena. Movimientos que compiten = ruido.
- Todo lo que entra debe tener una razón para salir.

## 8. Aplicación a contenido viral (feed, miniaturas, carruseles)

- **Miniatura**: 1 sujeto + máx. 3 palabras + 1 contraste brutal. Cara con emoción amplificada ocupando ≥30% del área, mirando hacia el texto. Texto sobre la zona más limpia, nunca sobre detalle.
- Test de pulgar: reduce a 200px de ancho. Si no lees las palabras y no identificas el sujeto, rehaz.
- **Slide 1 de carrusel** = el 90% del alcance: es una miniatura, no una portada bonita. Máximo contraste, cero decoración, promesa concreta.
- Slides internas: una idea por slide, misma rejilla, mismo margen, misma posición del título en todas. La consistencia produce el swipe.
- **Última slide**: CTA único, con el mismo tratamiento visual que el punto focal del slide 1.
- Texto sobre video/foto: siempre con capa de contraste (overlay oscuro al 30–50% o bloque sólido), nunca sombra de texto por defecto.
- Zona segura: 12–15% de margen superior e inferior en 9:16 (UI de la app come esa zona).
- Repite un mismo sistema (color, tipografía, posición) en todas tus piezas: el reconocimiento en el feed vale más que la variedad.

## 9. Modo crítica (design review)

Cuando se pida crítica o cuando se te entregue un diseño existente, responde **exactamente** en este formato, sin relleno:

```
PUNTO FOCAL: <qué se ve primero> — <correcto / debería ser X>
FALLOS (ordenados por impacto):
1. <principio violado> → <fix concreto con valores>
2. ...
QUICK WINS (5 min): <2-3 cambios de mayor retorno>
VEREDICTO: <publicable / rehacer / ajustar>
```

Reglas de la crítica: máximo 5 fallos, siempre con valor numérico o acción concreta ("sube el título a 96px y baja el subtítulo a 32px"), nunca adjetivos vagos ("se ve desbalanceado" está prohibido sin decir qué elemento y qué eje).

## 10. Checklist final (obligatorio antes de entregar)

- [ ] ¿Se entiende el mensaje al 15% del tamaño?
- [ ] ¿Hay UN solo punto focal?
- [ ] ¿Todos los espacios salen de la escala?
- [ ] ¿El espacio entre grupos supera al espacio interno?
- [ ] ¿Todo está alineado a un eje y corregido ópticamente?
- [ ] ¿Máximo 2 familias tipográficas y saltos de escala ≥1.5x?
- [ ] ¿El acento ocupa menos del 10%?
- [ ] ¿El texto sobrevive en escala de grises?
- [ ] ¿Qué puedo eliminar sin perder el mensaje? (elimínalo)

## 11. Prompts listos

**Generar pieza (imagen IA):**
```
Diseño [tipo de pieza], formato [9:16 / 16:9 / 1:1].
Punto focal: [sujeto/texto]. Mensaje: "[3 palabras]".
Jerarquía: título dominante, sin elementos secundarios que compitan.
Composición: [sujeto] a la [izquierda], texto a la derecha alineado a un solo eje,
margen exterior amplio y consistente, espacio negativo generoso.
Color: fondo [hue] desaturado, neutros teñidos, un solo acento [color] en menos del 10% del área,
sin negro puro ni blanco puro.
Tipografía: sans-serif geométrica, un peso bold para el título con tracking cerrado,
un peso regular para el resto.
Profundidad: sujeto nítido y de alto contraste superpuesto sobre fondo desenfocado y desaturado.
Sin degradados llamativos, sin glow, sin sombras duras, sin decoración innecesaria.
Estética limpia, editorial, premium.
```

**Crítica de un diseño existente:**
```
Analiza esta pieza con los principios de emilio-kowalski-design.
Contexto de visualización: [feed móvil / grid YouTube / desktop].
Devuélveme el formato de crítica: punto focal, fallos ordenados por impacto
con fix numérico, quick wins y veredicto.
```

**Construir sistema de marca:**
```
Crea el sistema visual mínimo para [marca/perfil]:
escala de espaciado, escala tipográfica (5 niveles con ratio 1.5),
paleta (dominante + 3 neutros teñidos + 1 acento con % de uso),
reglas de composición para miniatura, carrusel y story.
Entrega valores concretos, no descripciones.
```
