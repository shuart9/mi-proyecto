---
name: impeccable-design
description: |
  Eleva cualquier salida visual a nivel "impecable": miniaturas, carruseles,
  landing pages, artifacts HTML, decks, banners, portadas y UI. Úsala SIEMPRE
  que el usuario pida diseñar, maquetar, "que se vea pro", mejorar un diseño,
  una miniatura/thumbnail, un carrusel, una landing, una portada, un banner,
  un deck, una web o cuando entregues un artifact visual — incluso si no dice
  la palabra "diseño". También al criticar o auditar un diseño existente.
  NO es para elegir librerías de charts (usa dataviz) ni para redacción pura
  sin componente visual.
---

# Impeccable Design

Regla base: **el diseño no gana por bonito, gana por legible en 0.4 s y por
jerarquía obvia.** Todo lo demás es decoración.

## 1. Decide el trabajo del diseño antes de tocar pixeles

Escribe en una línea: `[Quién lo ve] + [en qué superficie] + [qué debe hacer]`.
Si no puedes escribirla, el diseño no está definido. Ejemplos:

- Miniatura YouTube → scroll en móvil → parar el pulgar y generar duda/curiosidad.
- Landing → tráfico de bio → un solo click al CTA.
- Carrusel IG → swipe → llegar al slide final con la oferta.

Un objetivo por pieza. Dos objetivos = cero.

## 2. Sistema antes que capricho

Define esto ANTES de maquetar y no lo rompas:

- **Escala tipográfica**: 4 tamaños máx. Ratio 1.25–1.5 (ej. 14 / 18 / 28 / 48).
- **Espaciado**: múltiplos de 4 u 8. Nada de "23px porque sí".
- **Color**: 1 neutro base + 1 tinta de texto + **1 acento**. El acento solo
  toca lo accionable (CTA, dato clave). Si el acento está en 5 sitios, ya no acentúa.
- **Radio y sombra**: un valor de cada uno para toda la pieza.
- **Máx. 2 familias tipográficas.** Una sola con pesos 400/700 suele ganar.

## 3. Jerarquía: el 80% del resultado

- Una sola cosa debe ser la más grande de la composición. Solo una.
- Contraste de tamaño ≥ 2× entre nivel 1 y nivel 2. Los saltos tímidos leen a amateur.
- Agrupa por proximidad, no por líneas ni cajas. Borra bordes antes que añadirlos.
- Alinea todo a una rejilla; el ojo detecta 2px de desalineación antes que un color feo.
- Espacio en blanco = confianza. Apretado = barato.

## 4. Reglas por superficie

**Miniatura / portada (móvil, ~180px de ancho real)**
- Máx. **3–4 palabras**, peso extrabold, ocupando ≥ 25% del alto.
- Cara con emoción legible o un objeto grande. Nada de escenas.
- Contraste sujeto/fondo brutal: contorno, blur o color plano detrás.
- Test: mínimízala al 15%. Si no se lee, no sirve. Sin excepciones.

**Carrusel**
- Slide 1 = hook visual + promesa. Slide 2 = tensión/error común. Últimos = acción.
- Un mensaje por slide. Mismo layout en todos, solo cambia el contenido.
- Indicador de continuidad (flecha, corte de texto) para forzar el swipe.

**Landing / web**
- Above the fold: promesa + subtítulo de 1 línea + CTA. Nada más.
- Ancho de lectura 60–75 caracteres.
- El CTA se repite cada ~1.5 pantallas, siempre con el mismo texto.

**Artifact / UI**
- Estados vacíos, de carga y de error diseñados, no improvisados.
- Táctil ≥ 44px. Foco visible. Contraste texto ≥ 4.5:1 (grande ≥ 3:1).
- Funciona en claro y oscuro, y a 360px de ancho.

## 5. Detalles que separan "hecho" de "impecable"

- Comillas tipográficas (" "), guiones em (—), sin viudas en titulares.
- Números tabulares en tablas y precios.
- Imágenes con `object-fit: cover` y ratio fijo: nunca deformadas.
- Transiciones 150–250 ms, `ease-out`. Más lento se siente pesado.
- Cero texto placeholder en la entrega. Contenido real o nada.

## 6. Pasada final obligatoria (antes de entregar)

1. Míralo al 25% de tamaño: ¿la jerarquía sigue clara?
2. Entrecierra los ojos: ¿qué mancha domina? ¿es la correcta?
3. Voltea horizontalmente: los desequilibrios saltan.
4. Quita el color: ¿sigue funcionando en gris?
5. Borra el 20% de los elementos. Si nadie los echa de menos, quedan borrados.
6. ¿Se lee en móvil a la luz del sol? (contraste real, no de monitor)

Si un punto falla, se arregla antes de entregar. No se avisa "quedó pendiente".

## 7. Prompts listos

**Auditar un diseño**
```
Audita esta pieza como director de arte. Formato:
1) Qué debe lograr y si lo logra (sí/no, 1 línea)
2) Los 3 fallos que más le cuestan (jerarquía, contraste, espaciado, tipografía)
3) Fix concreto de cada uno con valores exactos (px, pesos, hex)
4) Qué eliminar
Sin elogios. Sin generalidades.
```

**Generar miniatura**
```
Miniatura 16:9 para [tema]. Sujeto: [X] con expresión de [emoción], plano
cerrado, ocupando el tercio derecho. Fondo: color plano [hex] con viñeta.
Texto: "[3 palabras]" en sans extrabold, blanco con contorno negro de 6px,
tercio izquierdo, ocupando 30% del alto. Alto contraste, legible a 180px.
Sin marcas de agua, sin texto extra.
```

**Rediseñar a nivel impecable**
```
Rediseña [pieza] aplicando: escala tipográfica de 4 pasos, espaciado en
múltiplos de 8, un solo color de acento sobre el CTA, contraste ≥ 2× entre
titular y cuerpo, y ancho de lectura de 65 caracteres. Entrega el resultado
y una lista de qué eliminaste y por qué.
```
