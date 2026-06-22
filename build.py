# -*- coding: utf-8 -*-
"""
Generador · 100 Conceptos de Startup (de cero a experto) — guía + glosario visual.
Diseño = design system OFICIAL AECODE (violeta #4A3AC1 + verde #17B14E + azul #4465EE,
navy #0E1121 / lavanda #F5F5F6), motor de slides del Deck Maestro AECODE.
Cada concepto: cómo funciona · analogía · ejemplo real (grandes startups + AECODE).
Autocontenido: un solo index.html.  Ejecutar:  python build.py
"""
import html, datetime, pathlib, math

def esc(s): return html.escape(str(s))

# ---------- helpers de contenido ----------
def chip(t):     return f'<span class="chip reveal">{t}</span>'
def kicker(t):   return f'<div class="kicker reveal">{esc(t)}</div>'
def title(t):    return f'<h2 class="s-title reveal">{t}</h2>'
def lead(t):     return f'<p class="lead reveal">{t}</p>'
def note(t):     return f'<div class="vnote reveal">{t}</div>'

def card(head, body, num="", tag="", tone="violet"):
    num_h=f'<div class="card-num">{esc(num)}</div>' if num else ""
    tag_h=f'<div class="card-tag">{esc(tag)}</div>' if tag else ""
    return (f'<div class="card reveal card-{tone}">{num_h}{tag_h}'
            f'<div class="card-head">{head}</div><div class="card-body">{body}</div></div>')

def bullets(items):
    return '<ul class="bullets">'+"".join(f'<li class="reveal">{b}</li>' for b in items)+'</ul>'
def grid(items, cols=3, extra=""):
    return f'<div class="grid grid-{cols} {extra}">{"".join(items)}</div>'
def table(headers, rows, hi=None):
    hi=hi or []
    th="".join(f"<th>{h}</th>" for h in headers)
    body=""
    for r in rows:
        tds="".join(f'<td class="{("cell-hi" if j in hi else "")}">{c}</td>' for j,c in enumerate(r))
        body+=f'<tr class="reveal">{tds}</tr>'
    return f'<div class="table-wrap reveal"><table class="dt"><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>'
def quote(t):
    return f'<blockquote class="bigquote reveal">{t}</blockquote>'

# ---------- diagramas / ilustraciones (SVG + CSS animado) ----------
def dgm(inner, cls=""):
    return f'<div class="dgm {cls} reveal">{inner}</div>'

def ring_cycle(nodes, c_top, c_bot, flywheel=False):
    """Ciclo circular animado (lean loop, growth loop, flywheel)."""
    n=len(nodes); R=39; tones=["violet","blue","green"]
    nh=""
    for i,(lab,sub) in enumerate(nodes):
        ang=math.radians(-90+i*360.0/n)
        x=50+R*math.cos(ang); y=50+R*math.sin(ang)
        nh+=(f'<div class="rc-node tone-{tones[i%3]}" style="left:{x:.1f}%;top:{y:.1f}%">'
             f'<b>{lab}</b><span>{sub}</span></div>')
    svg=('<svg viewBox="0 0 200 200" class="rc-svg" aria-hidden="true">'
         '<circle cx="100" cy="100" r="74" class="rc-track"/>'
         '<g class="rc-arcg"><circle cx="100" cy="100" r="74" class="rc-arc"/></g>'
         '<g class="rc-run"><circle cx="100" cy="26" r="6" class="rc-dot"/></g></svg>')
    center=f'<div class="rc-center"><b>{c_top}</b><span>{c_bot}</span></div>'
    return dgm(f'<div class="ring-cycle {"fly" if flywheel else ""}">{svg}{center}{nh}</div>',"d-ring")

def tamsamsom(items):
    """Anillos concéntricos TAM/SAM/SOM."""
    legend="".join(
        f'<div class="tss-leg"><span class="dot d{i}"></span><div><b>{l}</b> · {v}<small>{d}</small></div></div>'
        for i,(l,v,d) in enumerate(items))
    rings=('<div class="tss-rings"><div class="ring r0"><span>TAM</span></div>'
           '<div class="ring r1"><span>SAM</span></div>'
           '<div class="ring r2"><span>SOM</span></div></div>')
    return dgm(f'<div class="tss">{rings}<div class="tss-legend">{legend}</div></div>',"d-tss")

def curve(kind="pmf"):
    """Curva animada: pmf (palo de hockey) o jcurve (valle de la muerte)."""
    if kind=="pmf":
        pre='M22,168 C90,166 150,160 232,150'; post='M232,150 C300,140 350,92 462,20'
        mark='<line x1="232" y1="22" x2="232" y2="178" class="cv-mark"/><circle cx="232" cy="150" r="6" class="cv-pt"/>'
        leg=('<div class="cv-legend"><span class="l-pre">Antes · tú empujas</span>'
             '<span class="l-pmf">PMF</span><span class="l-post">Después · te jalan</span></div>')
    else:
        pre='M22,60 C90,90 150,150 232,160'; post='M232,160 C320,168 380,110 462,22'
        mark='<line x1="232" y1="22" x2="232" y2="178" class="cv-mark"/><circle cx="232" cy="160" r="6" class="cv-pt"/>'
        leg=('<div class="cv-legend"><span class="l-pre">Inversión · valle de la muerte</span>'
             '<span class="l-pmf">Punto bajo</span><span class="l-post">Escala · retorno</span></div>')
    svg=(f'<svg viewBox="0 0 484 196" class="cv-svg" aria-hidden="true">'
         f'<line x1="22" y1="178" x2="462" y2="178" class="cv-axis"/>'
         f'<line x1="22" y1="178" x2="22" y2="14" class="cv-axis"/>'
         f'<path d="{pre}" class="cv-pre draw"/><path d="{post}" class="cv-post draw"/>{mark}</svg>')
    return dgm(f'<div class="curve">{svg}{leg}</div>',"d-curve")

def funnel_v(stages):
    """Embudo vertical (AARRR u otros). stages: (label, width%, metric, tone)."""
    rows=""
    for lab,w,m,t in stages:
        rows+=(f'<div class="fnl-row band-{t}" style="--w:{w}%"><span>{lab}</span><b>{m}</b></div>')
    return dgm(f'<div class="fnl">{rows}</div>',"d-fnl")

def scale_compare(cac, ltv, ratio):
    """Comparativa CAC vs LTV con badge de ratio."""
    body=(f'<div class="sc-row"><div class="sc-lab">CAC<small>cuesta conseguirlo</small></div>'
          f'<div class="sc-track"><i class="sc-bar sc-cac" style="--w:18%"></i></div>'
          f'<b class="sc-val sc-vcac">{cac}</b></div>'
          f'<div class="sc-row"><div class="sc-lab">LTV<small>vale el cliente</small></div>'
          f'<div class="sc-track"><i class="sc-bar sc-ltv" style="--w:90%"></i></div>'
          f'<b class="sc-val sc-vltv">{ltv}</b></div>'
          f'<div class="sc-badge">{ratio}<span>regla sana</span></div>')
    return dgm(f'<div class="scale">{body}</div>',"d-scale")

def canvas_mini(cells):
    """Mini Business Model Canvas 3x3. cells: list de (label, tone)."""
    cs="".join(f'<div class="cv-cell tone-{t}">{l}</div>' for l,t in cells)
    return dgm(f'<div class="bmc">{cs}</div>',"d-bmc")

def fund_bars(stages):
    """Barras crecientes de rondas. stages: (label, height%, amount, tone)."""
    cols=""
    for lab,h,amt,t in stages:
        cols+=(f'<div class="fund-col"><b class="fund-amt tone-{t}">{amt}</b>'
               f'<div class="fund-bar band-{t}" style="--h:{h}%"></div>'
               f'<span class="fund-lab">{lab}</span></div>')
    return dgm(f'<div class="fund">{cols}</div>',"d-fund")

def moat_layers(layers):
    """Capas concéntricas de defensibilidad (outer→core)."""
    inner=""
    for lab,sub in reversed(layers):
        inner=f'<div class="moat-l"><b>{lab}</b><span>{sub}</span>{inner}</div>'
    return dgm(f'<div class="moat">{inner}</div>',"d-moat")

def timeline_h(items):
    """Línea de tiempo horizontal. items: (etapa, detalle, win)."""
    n=len(items); cells=""
    for et,det,win in items:
        cells+=(f'<div class="th-item {"win" if win else ""}"><div class="th-dot"></div>'
                f'<div class="th-stage">{et}</div><div class="th-meta">{det}</div></div>')
    return dgm(f'<div class="th" style="grid-template-columns:repeat({n},1fr)">{cells}</div>',"d-th")

def concept_web(center, spokes):
    """Hub de relaciones: centro + radios animados."""
    n=len(spokes); R=41; lines=""; nodes=""
    for i,(lab,tone) in enumerate(spokes):
        ang=math.radians(-90+i*360.0/n)
        x=50+R*math.cos(ang); y=50+(R*1.0)*math.sin(ang)
        lines+=(f'<line x1="50" y1="50" x2="{x:.1f}" y2="{y:.1f}" class="cw-line" '
                f'vector-effect="non-scaling-stroke"/>')
        nodes+=f'<div class="cw-node tone-{tone}" style="left:{x:.1f}%;top:{y:.1f}%">{lab}</div>'
    svg=f'<svg viewBox="0 0 100 100" preserveAspectRatio="none" class="cw-svg">{lines}</svg>'
    return dgm(f'<div class="concept-web">{svg}{nodes}<div class="cw-center">{center}</div></div>',"d-web")

def ladder(steps):
    """Escalera ascendente principiante→experto. steps: (nivel, titulo, desc, height%)."""
    cols=""
    for lvl,ti,de,h in steps:
        cols+=(f'<div class="ld-step" style="--h:{h}%"><div class="ld-lvl">{lvl}</div>'
               f'<div class="ld-h">{ti}</div><div class="ld-d">{de}</div></div>')
    return dgm(f'<div class="ladder">{cols}</div>',"d-ladder")

# ---------- definición de slides ----------
SLIDES=[]
def S(theme, chapter, layout, content):
    SLIDES.append(dict(theme=theme, chapter=chapter, layout=layout, content=content))

def concept(num, level_name, name, eng, works, analogy, example, ex_tag, formula=None, theme="dark"):
    eng_h = f'<span class="c-eng">{esc(eng)}</span>' if eng else ''
    form_h = (f'<div class="c-formula reveal"><span>Cómo se calcula</span><code>{formula}</code></div>'
              if formula else '')
    content = f"""
  {kicker(level_name)}
  <div class="c-head reveal"><span class="c-num">{num:03d}</span>
    <h2 class="c-name">{name}{eng_h}</h2></div>
  <div class="c-works reveal">{works}</div>
  {form_h}
  <div class="split">
    <div class="split-l">{card("Analogía", analogy, tag="Piénsalo así", tone="blue")}</div>
    <div class="split-r">{card("Ejemplo real", example, tag=ex_tag, tone="green")}</div>
  </div>"""
    S(theme, level_name, "concept", content)

def divider(idx, theme, chapter, title_html, sub):
    S(theme, chapter, "divider", f"""
  <div class="div-index reveal">{idx:02d}</div>
  <h2 class="div-title reveal">{title_html}</h2>
  <p class="div-sub reveal">{sub}</p>
""")

# ======================= PORTADA =======================
S("dark","100 Conceptos Startup","cover", f"""
  <div class="cover-logo reveal"><img class="logo-dark" src="brand/assets/logos/aecode-logo-principal-fondo-oscuro.png" alt="AECODE"><img class="logo-light" src="brand/assets/logos/aecode-logo-principal-fondo-blanco.png" alt="AECODE"></div>
  <img class="aecodito reveal" src="brand/assets/reference/aecodito-home.png" alt="">
  <h1 class="cover-title reveal">100 conceptos que<br>todo <span class="grad">founder</span> debe<br>dominar</h1>
  <p class="cover-sub reveal">El glosario + guía visual de startups, <b>de lo más básico a nivel experto</b>. Cada concepto: cómo funciona, una analogía y un ejemplo real de las startups más grandes y de AECODE.</p>
  <div class="cover-meta reveal"><span>10 niveles</span><span class="dot">·</span><span>100 conceptos</span><span class="dot">·</span><span>{datetime.date.today().strftime('%b %Y')}</span></div>
  <div class="cover-hint reveal">← → navegar · <b>T</b> tema · <b>F</b> pantalla completa · <b>O</b> índice</div>
""")

# ======================= CÓMO LEER =======================
S("dark","Cómo usar esta guía","cards", f"""
  {kicker("La anatomía de cada concepto")}
  {title('Cada tarjeta te da <span class="grad">3 ángulos</span> del mismo concepto')}
  {grid([
   card("① Cómo funciona","La definición operativa: <b>qué es y cómo opera</b> en una startup real, sin paja.", num="◆"),
   card("② Analogía","Una imagen cotidiana para <b>fijar la idea</b> en segundos y poder explicarla a cualquiera.", num="◆", tone="blue"),
   card("③ Ejemplo real","Cómo lo usa una <b>startup gigante</b> o <b>AECODE</b>, para ver el concepto en acción.", num="◆", tone="green"),
  ], 3)}
  {lead('Recórrela en orden para subir de <b>nivel 1 (fundamentos)</b> a <b>nivel 10 (experto)</b>, o salta a un concepto con el índice (tecla <b>O</b>). Pensada para <i>entender, explicar y aplicar</i>.')}
""")

# ======================= MAPA DE NIVELES =======================
S("dark","Mapa de la guía","table", f"""
  {kicker("Los 10 niveles")}
  {title('Un camino de <span class="grad">cero a experto</span> en 100 conceptos')}
  {table(["Nivel","Bloque","Qué aprendes","Conceptos"],[
   ["<b>1</b>","Fundamentos","Qué es una startup y cómo se valida una idea","01–10"],
   ["<b>2</b>","Cliente y mercado","A quién sirves y cuán grande es el juego","11–20"],
   ["<b>3</b>","Producto","Del MVP al Product-Market Fit","21–30"],
   ["<b>4</b>","Modelo de negocio","Cómo capturas valor y cobras","31–40"],
   ["<b>5</b>","Unit economics","Si el negocio gana o pierde por unidad","41–50"],
   ["<b>6</b>","Métricas y crecimiento","Qué medir para crecer de verdad","51–60"],
   ["<b>7</b>","Growth y GTM","Cómo adquieres clientes a escala","61–70"],
   ["<b>8</b>","Estrategia y defensa","Por qué nadie te copia","71–80"],
   ["<b>9</b>","Fundraising y capital","Cómo se financia una startup","81–90"],
   ["<b>10</b>","Escala y experto","De startup a categoría y exit","91–100"],
  ], hi=[0,1])}
""")

# ======================= SÍNTESIS · EL VIAJE =======================
S("dark","El viaje de la startup","synthwide", f"""
  {kicker("Cómo encaja todo")}
  {title('El <span class="grad">viaje</span> de una startup, etapa por etapa')}
  {timeline_h([
    ("Idea & Problema","Niveles 1 · qué resolver", False),
    ("Cliente & Mercado","Nivel 2 · para quién", False),
    ("MVP & Validación","Niveles 1–3 · construye y prueba", False),
    ("Product-Market Fit","Nivel 3 · el mercado te jala", True),
    ("Modelo & Unit Econ.","Niveles 4–5 · cómo ganas", False),
    ("Métricas & Growth","Niveles 6–7 · cómo escalas", False),
    ("Defensa & Capital","Niveles 8–9 · foso y fondos", False),
    ("Escala & Exit","Nivel 10 · categoría y salida", True),
  ])}
  {lead('No memorices 100 términos sueltos: cada nivel resuelve <b>una etapa</b> del viaje. Ubica dónde estás hoy, domina esa etapa y usa el resto como <i>mapa</i> de lo que viene.')}
""")

# ======================= SÍNTESIS · CONEXIONES =======================
S("light","Cómo se conectan","synthwide", f"""
  {kicker("El mapa de relaciones")}
  {title('100 conceptos, <span class="grad">una sola red</span>')}
  <div class="split">
    <div class="split-l">{concept_web("PROBLEMA real", [
      ("Solución","violet"),("PMF","green"),("ICP / Cliente","blue"),
      ("CAC ↔ LTV","violet"),("North Star","green"),("Moat","blue"),
      ("Growth","violet"),("Capital","green")])}</div>
    <div class="split-r">
      {lead('Los conceptos no viven sueltos: forman <b>cadenas</b>. Dominar startups es ver cómo unos jalan a otros.')}
      {grid([
        card("Cadena de valor",'Problema → Solución → <b>PMF</b>. Sin dolor real no hay solución que pegue, y sin encaje no hay negocio.', tag="①"),
        card("Cadena económica",'CAC → LTV → Churn → <b>Runway</b>. Lo que cuesta y vale un cliente decide cuánto vives.', tag="②", tone="blue"),
        card("Cadena de defensa",'Red + costos de cambio + datos → <b>Moat</b> → Flywheel. Así nadie te copia.', tag="③", tone="green"),
      ], 3, "cards-sm")}
    </div>
  </div>
""")

# ======================= NIVELES Y CONCEPTOS =======================
LEVELS = [
 dict(no=1, name="Nivel 1 · Fundamentos", theme="dark", accent="violet",
   title='Nivel 1 — <span class="grad">Fundamentos</span>',
   sub="Qué es realmente una startup y cómo se pasa de una corazonada a una idea que el mercado valida.",
   concepts=[
    ("Startup","la empresa diseñada para crecer",
     "Una organización temporal que <b>busca un modelo de negocio repetible y escalable</b> bajo incertidumbre extrema. No es una empresa pequeña: es una máquina diseñada para <i>crecer rápido</i>.",
     "Es un cohete, no un auto. Un auto te lleva del punto A al B; el cohete se construye para <b>despegar y multiplicarse</b>, aunque pueda explotar.",
     "<b>AECODE</b> no es una academia más: es una startup que busca un modelo escalable para convertir conocimiento técnico AEC en capacidad verificable, con presencia en <b>14 países</b>.","AECODE"),
    ("El Problema","pain point",
     "El dolor real y frecuente del cliente que justifica que exista tu startup. Si nadie sufre el problema, <b>no hay negocio</b>: la regla es 'enamórate del problema, no de tu solución'.",
     "Eres médico antes que vendedor: primero <b>diagnosticas el dolor</b>; recetar sin diagnóstico es vender vitaminas a quien necesita una cirugía.",
     "<b>Airbnb</b> nació de un dolor doble y real: viajeros sin hotel asequible y anfitriones que necesitaban ingresos extra para pagar la renta.","Airbnb"),
    ("Propuesta de Valor","value proposition",
     "La promesa concreta de <b>por qué un cliente te elige a ti</b>: qué problema resuelves, para quién y qué te hace distinto. Se resume en una frase clara.",
     "Es el titular de una noticia: si en <b>una línea</b> no entiendo qué gano, paso de página.",
     "<b>AECODE:</b> «convierte conocimiento técnico AEC en <b>capacidad real demostrada con evidencia</b>». Aprende · Aplica · Demuestra.","AECODE"),
    ("Idea vs Oportunidad","idea ≠ opportunity",
     "Una idea es una ocurrencia; una <b>oportunidad</b> es una idea con mercado, timing y forma de ganar dinero. Las ideas son baratas; <i>la ejecución sobre una oportunidad real es lo escaso</i>.",
     "Una idea es una semilla; la oportunidad es la semilla <b>más</b> tierra fértil, clima y estación correcta. Sin lo segundo, no germina.",
     "El video P2P existía antes que <b>YouTube</b>; la oportunidad llegó con banda ancha barata, Flash y cámaras masivas: el <i>timing</i> hizo la diferencia.","YouTube"),
    ("Founder-Market Fit","encaje fundador-mercado",
     "El grado en que los fundadores son <b>las personas correctas</b> para este problema: experiencia, red y obsesión genuina. Reduce el riesgo de ejecución más que cualquier plan.",
     "Es un cirujano operando de lo suyo: no quieres al más entusiasta, quieres al que <b>ya conoce el cuerpo</b> por dentro.",
     "<b>AECODE</b> lo tiene en AEC + IA: el equipo viene del sector construcción y educación tech, no llegó de afuera a 'disrumpir' algo que no entiende.","AECODE"),
    ("Visión y Misión","norte de largo plazo",
     "La <b>visión</b> es el mundo que quieres crear (destino); la <b>misión</b> es lo que haces cada día para acercarte (vehículo). Alinean al equipo cuando todo lo demás cambia.",
     "La visión es la estrella polar; la misión, el barco y la ruta. La estrella no se toca, pero te orienta cada noche.",
     "<b>Tesla:</b> visión = «acelerar la transición mundial a energía sostenible»; misión = construir autos eléctricos deseables y masivos para financiarla.","Tesla"),
    ("Lean Startup","build–measure–learn",
     "Método para construir bajo incertidumbre con <b>ciclos cortos</b>: construye algo mínimo, mídelo con clientes reales, aprende y vuelve a iterar. Minimiza el desperdicio de tiempo y dinero.",
     "Es cocinar probando la sopa cada minuto, no servir un banquete de 3 horas y <b>recién</b> al final descubrir que estaba salado.",
     "<b>Dropbox</b> validó con un <i>video</i> demo (no producto) y su lista de espera saltó de 5.000 a 75.000 en una noche: aprendió antes de construir.","Dropbox"),
    ("Hipótesis y Experimentos","supuestos a probar",
     "Tratas tus creencias del negocio como <b>hipótesis falsables</b> y diseñas el experimento más barato para confirmarlas o tumbarlas antes de apostar fuerte.",
     "Eres científico, no profeta: en vez de jurar que lloverá, <b>pones un experimento</b> que te diga si llevar paraguas mañana.",
     "<b>Zappos</b> testeó «¿la gente compra zapatos online?» fotografiando zapatos de tiendas y comprándolos al recibir el pedido, sin inventario.","Zappos"),
    ("MVP","producto mínimo viable",
     "La versión más simple que <b>entrega valor real y genera aprendizaje</b> con el mínimo esfuerzo. No es un producto a medias: es el experimento más pequeño que prueba tu hipótesis central.",
     "Para cruzar la ciudad, primero una <b>patineta</b> que ya rueda, no un cuarto de auto que no se mueve. Cada versión transporta de verdad.",
     "<b>AECODE</b> usa una skill piloto —«generar un reporte técnico de obra asistido por IA»— como MVP: evidencia clara en ≤90 min, sin construir toda la plataforma.","AECODE"),
    ("Customer Discovery","validación con clientes",
     "Salir a <b>hablar con clientes reales</b> antes de construir, para validar problema y solución con evidencia, no con opiniones de la oficina. «Get out of the building» (Steve Blank).",
     "Es probar la receta con comensales <b>antes</b> de abrir el restaurante, no decorar el local y rezar para que alguien entre.",
     "<b>Superhuman</b> entrevistó usuarios hasta que el 40% diría que se sentiría «muy decepcionado» sin el producto: midió el deseo antes de escalar.","Superhuman"),
   ]),
 dict(no=2, name="Nivel 2 · Cliente y Mercado", theme="light", accent="violet",
   title='Nivel 2 — <span class="grad">Cliente y Mercado</span>',
   sub="A quién le resuelves, qué trabajo le haces y cuán grande es el juego al que entras.",
   concepts=[
    ("Cliente vs Usuario","quién paga ≠ quién usa",
     "El <b>usuario</b> usa el producto; el <b>cliente</b> es quien paga. A veces coinciden, a veces no, y confundirlos hace que diseñes para uno y cobres al otro mal.",
     "En un colegio el alumno <b>usa</b> la clase, pero el padre la <b>paga</b>. Si solo enamoras al alumno y olvidas al padre, no renuevan.",
     "<b>AECODE B2B2C:</b> el profesional <i>usa</i> y aprende; la empresa AEC <i>paga</i> por upskilling medible del equipo. Hay que satisfacer a ambos.","AECODE"),
    ("ICP","ideal customer profile",
     "El <b>perfil de cliente ideal</b>: el tipo de empresa o persona a la que tu producto le calza perfecto, paga bien y se queda. Enfocarte en él multiplica la eficiencia comercial.",
     "Es la talla exacta de zapato: vender a todos es vender tropezando; vender a tu talla es <b>caminar rápido y cómodo</b>.",
     "<b>Slack</b> arrancó con su ICP claro: equipos de tecnología de 10–50 personas, donde el dolor de email interno era más agudo y la adopción viral.","Slack"),
    ("Buyer Persona","arquetipo de comprador",
     "Una <b>representación semi-ficticia</b> de tu cliente: rol, objetivos, frustraciones y cómo decide. Te hace diseñar y comunicar para una persona concreta, no para 'el mercado'.",
     "Es darle nombre, cara y biografía a tu cliente para escribirle como a <b>un amigo</b>, no como a una multitud anónima.",
     "<b>AECODE</b> perfila a «Coordinador BIM/VDC, 3–8 años, quiere subir de rol y demostrar impacto»: cada ruta y mensaje le habla a ese arquetipo.","AECODE"),
    ("Jobs To Be Done","el trabajo a resolver",
     "La gente no compra productos: <b>'contrata'</b> soluciones para hacer un progreso en su vida. El JTBD es ese trabajo funcional, social y emocional que quiere lograr.",
     "«No quieres un taladro, quieres el <b>hueco en la pared</b>» —y en realidad, colgar la foto de tu familia.",
     "<b>McDonald's</b> descubrió que su malteada se «contrataba» para el trayecto aburrido al trabajo: competía con plátanos y donas, no con otras malteadas.","McDonald's"),
    ("Segmentación","dividir el mercado",
     "Partir el mercado en <b>grupos homogéneos</b> por necesidad, comportamiento o tamaño, para priorizar a quién atacar primero en vez de querer servir a todos.",
     "Es pescar con red en el banco de peces correcto, no echar el anzuelo <b>en todo el océano</b> a la vez.",
     "<b>AECODE</b> segmenta: junior (CV/portafolio), intermedio (automatizar), coordinador BIM, empresa B2B y experto/instructor — cada uno con oferta distinta.","AECODE"),
    ("TAM · SAM · SOM","tamaño del mercado",
     "Tres círculos concéntricos: <b>TAM</b> (todo el mercado), <b>SAM</b> (el que puedes servir con tu modelo) y <b>SOM</b> (el que realmente capturarás a corto plazo).",
     "TAM es todo el pastel; SAM, la porción que alcanza tu cuchillo; SOM, <b>el bocado</b> que de verdad te comerás este año.",
     "<b>AECODE</b> internamente: TAM upskilling AEC LATAM ~US$2.5B, SAM hispano US$600–800M, SOM ~US$3–5M capturable a 3 años.","AECODE"),
    ("Beachhead Market","mercado playa",
     "El <b>nicho inicial</b> donde concentras toda tu fuerza para ganar de forma dominante antes de expandirte. Cabeza de playa: tomas un punto pequeño y desde ahí avanzas.",
     "Como en el ajedrez o un desembarco: <b>aseguras una casilla</b> primero y la usas de trampolín, en vez de dispersarte por todo el tablero.",
     "<b>Facebook</b> dominó Harvard, luego las Ivy League, luego universidades, antes de abrirse al mundo: un beachhead a la vez.","Facebook"),
    ("Early Adopters","primeros usuarios",
     "El pequeño grupo que <b>siente el dolor con tanta intensidad</b> que adopta soluciones imperfectas antes que nadie y te da feedback brutal. Son tus primeros 100 fans.",
     "Son los que acampan afuera de la tienda por el lanzamiento: <b>perdonan los bugs</b> a cambio de ser los primeros.",
     "<b>Tesla</b> empezó con el Roadster caro para entusiastas que perdonaban limitaciones; con su dinero financió los modelos masivos.","Tesla"),
    ("Why Now","el timing",
     "Por qué <b>esta idea es viable hoy</b> y no hace 5 años: qué cambió en tecnología, regulación, costos o conducta que abre la ventana. El timing mata más startups que la competencia.",
     "Es surfear: la misma tabla que te ahoga sin ola <b>te impulsa</b> cuando la ola correcta llega. Hay que remar en el momento justo.",
     "<b>AECODE</b> tiene su 'why now': inflexión de IA 2025–26 (77% del capital contech va a IA) + Plan BIM Perú obligatorio + brecha de talento crítica.","AECODE"),
    ("Customer Development","desarrollo de clientes",
     "El proceso de Steve Blank en 4 pasos —descubrir, validar, crear y construir clientes— para <b>buscar el modelo de negocio en paralelo al producto</b>, no después.",
     "Construyes el puente <b>y</b> verificas que haya gente queriendo cruzarlo, al mismo tiempo, no terminas el puente y luego buscas tráfico.",
     "<b>Dropbox</b> y miles más nacen de aquí: validar demanda (lista de espera) antes de invertir años en la ingeniería completa.","Steve Blank"),
   ]),
 dict(no=3, name="Nivel 3 · Producto", theme="dark", accent="violet",
   title='Nivel 3 — <span class="grad">Producto</span>',
   sub="Del primer prototipo al momento mágico en que el mercado tira del producto: Product-Market Fit.",
   concepts=[
    ("Product-Market Fit","PMF",
     "El punto donde tienes un producto que <b>un mercado quiere con tanta fuerza</b> que la demanda te empuja. Antes de PMF: empujas; después de PMF: te jalan. Es el objetivo #1 de toda startup temprana.",
     "Es cuando dejas de pedalear cuesta arriba y de pronto vas <b>cuesta abajo</b>: el producto rueda solo porque la gente lo pide.",
     "<b>Notion</b> sintió PMF cuando los usuarios empezaron a crear plantillas y a evangelizar solos; la retención y el boca a boca se dispararon.","Notion"),
    ("Value Proposition Canvas","encaje problema-solución",
     "Una herramienta para <b>encajar</b> lo que ofreces (productos, aliviadores de dolor, generadores de alegría) con lo que el cliente necesita (trabajos, dolores, alegrías).",
     "Es armar un rompecabezas: tu pieza (producto) debe <b>encajar exacto</b> en el hueco del cliente, no a la fuerza.",
     "Equipos usan el canvas de Strategyzer para evitar el error #1: construir <i>aliviadores</i> de dolores que el cliente en realidad no tiene.","Strategyzer"),
    ("Iteración","mejora continua",
     "Avanzar por <b>versiones sucesivas</b>, cada una mejor gracias al feedback real. El producto nunca está 'terminado'; está en una mejor versión que ayer.",
     "Es esculpir: no sacas la estatua de un golpe, la <b>vas tallando</b> capa por capa hasta que aparece.",
     "<b>Instagram</b> iteró desde Burbn (app de check-ins saturada) hasta quedarse solo con la función de fotos+filtros que la gente sí amaba.","Instagram"),
    ("Pivot","cambio de rumbo",
     "Un <b>cambio estructural de estrategia</b> manteniendo lo aprendido: cambias producto, segmento o modelo cuando los datos dicen que el camino actual no lleva a PMF.",
     "Es girar sobre un pie fijo en básquet: <b>un pie no se mueve</b> (lo aprendido), el otro busca un mejor ángulo de tiro.",
     "<b>Slack</b> era un videojuego (Glitch) que fracasó; pivotaron a la herramienta de chat interno que habían construido para ellos mismos.","Slack"),
    ("Roadmap","hoja de ruta",
     "El <b>plan priorizado</b> de qué construirás y por qué, conectando la visión con las entregas concretas. Comunica el rumbo sin prometer fechas imposibles.",
     "Es el mapa de una expedición: marca <b>los hitos</b> y la dirección, pero deja espacio para rodear los obstáculos del camino.",
     "<b>AECODE</b> ordena su roadmap por capas: primero Live Training (caja), luego microlearning con evidencia, luego plataforma y B2B dashboard.","AECODE"),
    ("Onboarding / Activación","primer valor",
     "El proceso que lleva al usuario nuevo a <b>experimentar el valor por primera vez</b> rápido. Una activación pobre mata más usuarios que un mal producto.",
     "Es el anfitrión que te recibe en la fiesta y te presenta a alguien: si te deja solo en la puerta, <b>te vas</b>.",
     "<b>Duolingo</b> te pone a aprender en la primera pantalla, sin registro: sientes el valor antes de que te pida crear cuenta.","Duolingo"),
    ("Aha Moment","momento de revelación",
     "El instante exacto en que el usuario <b>'capta'</b> el valor y dice «ahora sí lo entiendo». Identificarlo y llevar a todos hacia él es clave para la retención.",
     "Es el clic de un truco de magia: hay un segundo en que <b>todo encaja</b> y ya no puedes 'des-verlo'.",
     "<b>Facebook</b> halló que su aha era «llegar a 7 amigos en 10 días»: quien lo lograba se quedaba; todo el onboarding se diseñó hacia eso.","Facebook"),
    ("Time to Value","TTV",
     "El <b>tiempo que tarda</b> un usuario en obtener su primer resultado útil. Cuanto más corto, mejor activación, retención y conversión a pago.",
     "Es lo que esperas para probar bocado en un restaurante: si tardan una hora, te vas <b>antes</b> del plato fuerte.",
     "<b>AECODE</b> diseña su skill piloto para dar evidencia visible en <b>≤90 minutos</b> (métrica TTFP, time to first practice): valor casi inmediato.","AECODE"),
    ("Wedge","producto cuña",
     "El <b>punto de entrada estrecho</b> y muy valioso por el que entras al cliente, para luego expandirte a más uso y más gasto. Empiezas pequeño pero indispensable.",
     "Es la cuña que abre la puerta: <b>delgada al inicio</b>, pero una vez dentro, ensanchas el hueco.",
     "<b>AECODE:</b> el profesional entra por productividad/relevancia (wedge), la empresa luego paga por transformar al equipo (engine).","AECODE"),
    ("Productización","de servicio a producto",
     "Convertir un <b>servicio manual</b> y a medida en un producto repetible, estandarizado y escalable, que no depende de horas humanas para crecer.",
     "Es pasar del sastre que cose un traje por cliente a la <b>marca de ropa</b> con tallas: misma calidad, infinitas copias.",
     "<b>AECODE</b> hace 'live-to-platform': cada curso en vivo se convierte en cápsulas, rúbricas y evidencias reutilizables — el servicio se vuelve producto.","AECODE"),
   ]),
 dict(no=4, name="Nivel 4 · Modelo de Negocio", theme="light", accent="violet",
   title='Nivel 4 — <span class="grad">Modelo de Negocio</span>',
   sub="Cómo creas, entregas y —sobre todo— capturas valor: la mecánica de cómo ganas dinero.",
   concepts=[
    ("Business Model Canvas","el lienzo del negocio",
     "Un mapa de <b>9 bloques</b> (clientes, propuesta, canales, relaciones, ingresos, recursos, actividades, aliados, costos) para ver todo el negocio en una hoja.",
     "Es el plano de una casa: ves <b>todas las habitaciones</b> y cómo conectan antes de poner un solo ladrillo.",
     "Usado por equipos de Strategyzer en todo el mundo para diseñar y, sobre todo, <i>cuestionar</i> el modelo de negocio en una sola página.","Strategyzer"),
    ("Lean Canvas","canvas para startups",
     "Adaptación de Ash Maurya enfocada en <b>problema, solución, métricas clave y ventaja injusta</b>: ideal para la incertidumbre de una startup temprana.",
     "Es la versión 'bisturí' del plano: quita los muros decorativos y deja <b>solo lo que puede matar o salvar</b> al negocio.",
     "Miles de fundadores arrancan con un Lean Canvas porque obliga a nombrar el problema y la <i>unfair advantage</i> antes que el producto.","Ash Maurya"),
    ("Revenue Streams","fuentes de ingreso",
     "Las distintas <b>formas en que entra dinero</b>: venta directa, suscripción, comisión, publicidad, licencias. Diversificarlas con cabeza estabiliza el negocio.",
     "Son los afluentes de un río: <b>varias corrientes</b> alimentando el mismo caudal lo hacen más difícil de secar.",
     "<b>AECODE</b> combina 4 motores: live training B2C, B2B institucional, on-demand+IA y B2B2C — un solo flywheel, varias entradas de caja.","AECODE"),
    ("Pricing","estrategia de precio",
     "Cómo <b>fijas el precio</b>: por costo, por competencia o —el correcto— por <b>valor percibido</b>. El precio no es un número, es posicionamiento y filtro de cliente.",
     "El precio es la etiqueta de un vino: el mismo líquido sabe distinto a $10 que a $100. <b>Comunica</b> tanto como cobra.",
     "<b>AECODE</b> usa una escalera: Free (adquisición) → créditos S/49–99 → premium → ruta certificada → B2B team → in-house S/8k–60k.","AECODE"),
    ("Freemium","gratis + premium",
     "Ofreces un núcleo <b>gratis</b> para adquirir masa de usuarios y cobras por funciones avanzadas. Funciona si lo gratis engancha y lo pago resuelve un dolor real.",
     "Es la entrada gratis al parque, pero <b>las atracciones top</b> se pagan: muchos entran, algunos compran el pase premium.",
     "<b>Spotify</b> y <b>Dropbox</b> escalaron con freemium: gratis con límites (anuncios, espacio) y pago para quitarlos. AECODE lo aplica para adquirir.","Spotify"),
    ("SaaS / Suscripción","software as a service",
     "Vendes <b>acceso recurrente</b> a un software (mensual/anual) en vez de una licencia única. Genera ingresos predecibles y relación de largo plazo con el cliente.",
     "Es Netflix en vez de comprar el DVD: pagas <b>mientras lo usas</b> y siempre tienes la última versión.",
     "<b>Salesforce</b> inventó el SaaS moderno («the end of software»): hoy es el modelo dominante por su MRR predecible y altos márgenes.","Salesforce"),
    ("Marketplace","mercado de dos lados",
     "Conectas <b>oferta y demanda</b> y cobras por facilitar la transacción. El reto es el 'problema del huevo y la gallina': sin oferta no hay demanda y viceversa.",
     "Eres el dueño de la feria: no produces ni compras nada, <b>cobras por el puesto</b> y por juntar a vendedores con compradores.",
     "<b>Airbnb</b>, <b>Uber</b> y <b>Mercado Libre</b> son marketplaces: su valor está en la red de ambos lados, no en activos propios.","Mercado Libre"),
    ("B2B · B2C · B2B2C","a quién le vendes",
     "<b>B2C</b> vendes a personas, <b>B2B</b> a empresas, <b>B2B2C</b> una empresa paga/impulsa y el consumidor final usa. Cada uno cambia ciclo de venta, ticket y canal.",
     "B2C es la tienda al público; B2B, el mayorista; B2B2C, la marca que <b>pone sus productos en góndola</b> de otra tienda para llegar a ti.",
     "<b>AECODE</b> es B2B2C: la empresa AEC paga el upskilling, el profesional aprende y la evidencia valida — comunidad barata + ticket alto.","AECODE"),
    ("Take Rate","comisión",
     "El <b>porcentaje que se queda</b> el marketplace de cada transacción. Demasiado alto ahuyenta oferta; demasiado bajo no sostiene el negocio. Es un equilibrio delicado.",
     "Es la propina obligatoria del intermediario: un <b>pedacito de cada trato</b> que pasa por tu plataforma.",
     "<b>Uber</b> retiene ~20–25% de cada viaje; <b>Airbnb</b> cobra a huésped y anfitrión: el take rate es su motor de ingresos.","Uber"),
    ("Monetización","cómo cobras",
     "El <b>cómo y cuándo</b> conviertes valor entregado en ingreso. Puedes tener millones de usuarios y cero negocio si no resuelves la monetización.",
     "Es ponerle caja registradora a la fuente de valor: muchos construyen una catarata hermosa pero <b>olvidan dónde cobrar la entrada</b>.",
     "<b>WhatsApp</b> creció a 450M usuarios casi sin monetizar; <b>Instagram</b> monetizó vía ads. Ambos resolvieron la pregunta de forma distinta.","WhatsApp"),
   ]),
 dict(no=5, name="Nivel 5 · Unit Economics", theme="dark", accent="violet",
   title='Nivel 5 — <span class="grad">Unit Economics</span>',
   sub="La pregunta que decide si una startup vive: ¿ganas o pierdes dinero con cada cliente?",
   concepts=[
    ("Unit Economics","economía por unidad",
     "Los ingresos y costos asociados a <b>una sola unidad</b> (un cliente, un pedido). Si la unidad no cierra, escalar solo multiplica las pérdidas.",
     "Es probar una galleta antes de hornear 10.000: si <b>una</b> sale mal o cuesta más de lo que vendes, la fábrica entera quiebra.",
     "<b>AECODE</b> mide unit economics por motor: B2C (LTV:CAC ~4.5×), B2B (~30×) y on-demand (~12×) — cada cliente debe cerrar antes de pisar el acelerador.","AECODE"),
    ("CAC","costo de adquisición",
     "Lo que <b>gastas en marketing y ventas</b> para conseguir un cliente nuevo. Es el precio de la gasolina del crecimiento: si sube sin control, te arruina.",
     "Es cuánto cuesta el anzuelo, la carnada y la gasolina del bote <b>por cada pez</b> que pescas.",
     "<b>AECODE</b> logra un CAC blended de ~<b>US$35</b>, ~8× mejor que el benchmark EdTech, gracias a su comunidad orgánica de +95k.","AECODE",
     "CAC = gasto en ventas y marketing ÷ nº de clientes nuevos"),
    ("LTV","valor de vida del cliente",
     "El <b>ingreso total</b> que deja un cliente durante toda su relación contigo. Cuanto más retienes y más expandes, más vale cada cliente conseguido.",
     "Un cliente no es una venta, es una <b>suscripción a la revista</b>: importa cuántos años renueva, no solo el primer número.",
     "Empresas SaaS como <b>Netflix</b> viven del LTV: un cliente que se queda 4 años vale 48 mensualidades, no una.","Netflix",
     "LTV = ticket medio × frecuencia × años de retención × margen"),
    ("LTV : CAC","el ratio que importa",
     "La <b>relación</b> entre lo que vale un cliente y lo que cuesta conseguirlo. Regla de oro: <b>&gt;3×</b> es sano; &lt;1× significa que pierdes dinero con cada venta.",
     "Es invertir $1 y recibir $3: por debajo de eso, estás <b>vendiendo billetes de $10 a $12</b> y celebrando el volumen.",
     "<b>AECODE</b> reporta LTV:CAC de <b>3.1×</b> (sobre el gate de inversión de 3×), con motores B2B que llegan a ~30×.","AECODE",
     "LTV : CAC — sano si es mayor a 3 : 1"),
    ("Payback Period","periodo de recuperación",
     "Los <b>meses que tardas en recuperar</b> el CAC con el margen del cliente. Cuanto más corto, menos capital necesitas para crecer.",
     "Es cuánto tarda un panel solar en pagarse con el ahorro de luz: hasta ese día, <b>solo recuperas</b> tu inversión.",
     "<b>AECODE</b> recupera el CAC en ~<b>7 meses</b>, dentro del benchmark sano (&lt;12). Menos payback = crecimiento autofinanciado.","AECODE",
     "Payback = CAC ÷ margen bruto mensual por cliente"),
    ("Gross Margin","margen bruto",
     "El <b>% que queda</b> de cada venta tras restar el costo directo de entregarla. Define cuánto te sobra para marketing, equipo y utilidad. SaaS sano: 70–85%.",
     "De cada $100 de pizza vendida, lo que sobra <b>después</b> de harina, queso y horno — antes de pagar el local y el sueldo.",
     "<b>AECODE</b> plataforma apunta a ~<b>74%</b> de gross margin, cercano a SaaS, muy por encima del servicio puro intensivo en horas.","AECODE"),
    ("Contribution Margin","margen de contribución",
     "Lo que <b>aporta cada venta</b> a cubrir los costos fijos, tras restar los costos variables. Cuando la suma supera los fijos, empiezas a ganar.",
     "Es cuánto pone <b>cada plato vendido</b> al bote común que paga el alquiler del restaurante: si pone poco, necesitas vender muchísimo.",
     "Aerolíneas viven de esto: cada asiento extra vendido casi no añade costo variable, así que su contribución marginal es altísima.","Aerolíneas"),
    ("Burn Rate","ritmo de quema",
     "El <b>dinero neto que gastas por mes</b> mientras no eres rentable. Controlarlo es literalmente controlar cuánto tiempo de vida le queda a la empresa.",
     "Es el oxígeno que consume un buzo: <b>cuanto más rápido respiras</b>, menos tiempo tienes antes de volver a la superficie (a levantar capital).",
     "En el crash de 2022, decenas de startups recortaron equipo para bajar su burn y estirar la vida: el burn rate define la urgencia.","Startups 2022"),
    ("Runway","pista de despegue",
     "Los <b>meses de vida</b> que te quedan al ritmo de quema actual con el efectivo en caja. Es el reloj real de la startup: cuando llega a cero, se acaba el juego.",
     "Es la gasolina en el tanque medida en <b>kilómetros</b>: te dice cuánto puedes avanzar antes de necesitar otra gasolinera (ronda).",
     "La regla VC: levanta para ~18–24 meses de runway, suficiente para alcanzar el siguiente hito que justifique una valoración mayor.","Regla VC",
     "Runway (meses) = efectivo en caja ÷ burn rate mensual"),
    ("Break-even","punto de equilibrio",
     "El nivel de ventas en que <b>ingresos = costos</b>: ni ganas ni pierdes. Cruzarlo significa que cada venta adicional ya es utilidad.",
     "Es la cima de la montaña: hasta ahí solo gastas energía subiendo; <b>pasada la cima</b>, todo es bajada y a favor.",
     "Una startup que llega a break-even deja de depender de inversionistas para sobrevivir: gana <i>opcionalidad</i> y poder de negociación.","Default alive"),
   ]),
 dict(no=6, name="Nivel 6 · Métricas y Crecimiento", theme="light", accent="violet",
   title='Nivel 6 — <span class="grad">Métricas y Crecimiento</span>',
   sub="Qué medir para crecer de verdad y no engañarte con números que se ven bien pero no dicen nada.",
   concepts=[
    ("Vanity vs Actionable","métricas que mienten",
     "Las <b>vanity metrics</b> (descargas, seguidores, page views) se ven bien pero no guían decisiones; las <b>accionables</b> (activación, retención, ingreso) sí.",
     "El número de gente que pasa frente a tu tienda vs. cuántos <b>compran y vuelven</b>: lo segundo paga el alquiler.",
     "Muchas startups celebraron «millones de descargas» y murieron; lo que importaba era cuántos usaban el producto a la semana 4.","Lección dura"),
    ("North Star Metric","métrica estrella",
     "La <b>única métrica</b> que mejor captura el valor que entregas al cliente. Alinea a todo el equipo: si sube, el negocio sube de forma sana.",
     "Es la estrella polar de los marineros: <b>todos reman</b> hacia el mismo punto, sin discutir cada noche hacia dónde ir.",
     "<b>AECODE:</b> «skills verificadas con evidencia / usuario activo». No se infla con marketing: o verificas la skill, o no.","AECODE"),
    ("AARRR","pirate metrics",
     "El <b>embudo de 5 etapas</b> de Dave McClure: Adquisición, Activación, Retención, Revenue y Referido. Te dice <i>dónde</i> exactamente pierdes usuarios.",
     "Es un examen médico por sistemas: en vez de «me siento mal», ubicas <b>qué órgano</b> (etapa) falla y lo tratas.",
     "Startups usan AARRR para diagnosticar: si adquieres mucho pero no activas, el problema es el onboarding, no el marketing.","Dave McClure"),
    ("Activación","el primer éxito",
     "El % de usuarios nuevos que <b>llegan a su primer momento de valor</b>. Es la bisagra entre adquirir y retener: sin activación, todo lo demás se fuga.",
     "Es lograr que el invitado <b>pruebe el primer bocado</b>: si solo entra y mira, nunca se queda a cenar.",
     "<b>AECODE</b> activa con TTFP: que el usuario complete su primera práctica con evidencia rápido, antes de aburrirse o irse.","AECODE"),
    ("Retención","que vuelvan",
     "El % de usuarios que <b>siguen usando</b> el producto con el tiempo. Es la métrica más honesta de PMF: si no retienes, no hay negocio que escale.",
     "No importa cuánta agua eches al balde si está <b>perforado</b>: la retención es tapar los hoyos antes de abrir la canilla del marketing.",
     "<b>AECODE</b> tiene retención W4 de ~38% (sobre benchmark B2C 25–35%): el loop de evidencia+validación hace que el progreso se <i>sienta</i> real.","AECODE"),
    ("Churn","tasa de abandono",
     "El % de clientes que <b>te dejan</b> en un periodo. Es la fuga del balde: un churn alto obliga a correr cada vez más rápido solo para no caer.",
     "Es el agua que se va por el desagüe: si entra a la misma velocidad que sale, <b>la tina nunca se llena</b>.",
     "Para SaaS, un churn mensual &gt;5% es alarma. AECODE vigila su churn (~8% borde alto) como prioridad para que el MRR componga.","SaaS"),
    ("Cohort Analysis","análisis por cohortes",
     "Agrupar usuarios por <b>cuándo entraron</b> y seguir su comportamiento en el tiempo. Revela si el producto mejora: ¿las cohortes nuevas retienen mejor?",
     "Es seguir a la <b>generación que entró en marzo</b> vs. la de junio, como un colegio mide cada promoción por separado.",
     "<b>Facebook</b> obsesionaba con cohortes de retención; ver la curva «aplanarse» (no caer a cero) fue su señal temprana de PMF.","Facebook"),
    ("MRR / ARR","ingreso recurrente",
     "<b>MRR</b> = ingreso recurrente mensual; <b>ARR</b> = anual. Es el latido de un negocio por suscripción: predecible, componible y lo que más valoran los inversionistas.",
     "Es un sueldo fijo vs. trabajos sueltos: el MRR <b>entra cada mes</b> sin volver a vender desde cero.",
     "Una startup SaaS se valora en múltiplos de ARR; pasar de US$1M a US$10M ARR es el rito de paso hacia Serie B.","SaaS",
     "ARR = MRR × 12"),
    ("NRR · Expansion","retención neta de ingresos",
     "El % de ingreso que <b>conservas y expandes</b> de tus clientes actuales (upgrades, más asientos) menos lo que pierdes por churn. <b>&gt;100%</b> = creces sin clientes nuevos.",
     "Es un jardín donde las plantas que ya tienes <b>crecen tanto</b> que el bosque se expande aunque no plantes nuevas.",
     "<b>Snowflake</b> presume NRR de ~158%: sus clientes gastan cada vez más. Es el santo grial del SaaS.","Snowflake"),
    ("Growth Rate · T2D3","ritmo de crecimiento",
     "La <b>velocidad</b> a la que creces (semanal o anual). El patrón <b>T2D3</b> describe el camino de élite: triplicar, triplicar, duplicar, duplicar, duplicar el ingreso.",
     "Es el interés compuesto del crecimiento: crecer 7% <b>semanal</b> parece poco, pero en un año te multiplica por 33.",
     "Y Combinator pide a sus startups una meta de ~5–7% de crecimiento semanal: la pendiente importa más que el tamaño hoy.","Y Combinator"),
   ]),
 dict(no=7, name="Nivel 7 · Growth y GTM", theme="dark", accent="violet",
   title='Nivel 7 — <span class="grad">Growth y Go-to-Market</span>',
   sub="Cómo consigues clientes a escala de forma repetible: los motores de adquisición y distribución.",
   concepts=[
    ("Growth Hacking","crecimiento por experimentos",
     "Crecer mediante <b>experimentos rápidos y creativos</b> en todo el embudo, usando producto, datos e ingenio más que grandes presupuestos de publicidad.",
     "Es ganar la guerra con <b>guerrilla</b>, no con tanques: tácticas ágiles y baratas que explotan palancas que otros no ven.",
     "<b>Dropbox</b> hackeó su crecimiento regalando espacio por cada amigo invitado: convirtió a los usuarios en su fuerza de ventas.","Dropbox"),
    ("Funnel · AIDA","embudo de conversión",
     "El recorrido del cliente por etapas —<b>Atención, Interés, Deseo, Acción</b>— donde en cada paso pierdes gente. Optimizar el embudo es ganar sin gastar más arriba.",
     "Es un embudo real: entra mucho líquido por arriba y <b>gotea</b> al final; ensanchar los cuellos hace caer más al vaso.",
     "<b>AECODE</b> mide su funnel B2C con gates: lead→reto→1ª evidencia→skill verificada→premium, cada uno con su tasa de conversión.","AECODE"),
    ("Viral Loop · K-factor","viralidad",
     "Cuando <b>cada usuario trae a otros</b> usando el producto. El <b>K-factor</b> mide cuántos nuevos genera cada uno; si K&gt;1, el crecimiento se vuelve exponencial.",
     "Es un contagio: <b>cada 'infectado'</b> contagia a más de uno y la cosa se propaga sola, sin pagar por cada nuevo caso.",
     "<b>Hotmail</b> añadió «PS: Get your free email» al pie de cada correo: pasó de 0 a 12M usuarios en 18 meses casi sin marketing.","Hotmail"),
    ("Network Effects","efecto red",
     "Cuando el producto se <b>vuelve más valioso</b> cuantos más lo usan. Genera un círculo virtuoso y una de las defensas más fuertes que existen.",
     "Es un teléfono: <b>inútil si eres el único</b> que tiene uno, imprescindible cuando lo tiene todo el mundo.",
     "<b>WhatsApp</b>, <b>LinkedIn</b> y los marketplaces viven de esto: tú no te vas porque <i>ahí está todo el mundo</i>.","LinkedIn"),
    ("Product-Led Growth","crecimiento por producto",
     "El <b>producto mismo</b> es el principal motor de adquisición, conversión y expansión: pruebas gratis, valor inmediato y viralidad, con menos peso de ventas.",
     "Es dejar que el plato <b>se venda por su sabor</b>: das una muestra gratis tan buena que el cliente pide la orden completa solo.",
     "<b>Figma</b>, <b>Slack</b> y <b>Notion</b> crecieron PLG: un usuario lo prueba, lo ama, lo lleva a su equipo y la empresa termina pagando.","Figma"),
    ("Go-To-Market","estrategia GTM",
     "El <b>plan de cómo llegas al mercado</b>: a qué segmento, por qué canal, con qué mensaje y modelo de venta. Define cómo conviertes producto en clientes.",
     "Es el plan de batalla antes de la invasión: <b>dónde desembarcas</b>, con qué tropas y por qué ruta, no improvisas en la playa.",
     "<b>AECODE</b> GTM: comunidad orgánica (CAC bajo) como wedge B2C → casos de evidencia → entrada B2B con pilotos de 30 días y dashboard de ROI.","AECODE"),
    ("Inbound · Content","marketing de atracción",
     "<b>Atraer</b> clientes creando contenido útil que resuelve sus dudas, en vez de perseguirlos con anuncios. Construye audiencia, autoridad y un canal propio barato.",
     "Es ser el faro, no el cazador: <b>el barco viene a ti</b> porque emites luz útil, no porque lo persigas en la oscuridad.",
     "<b>HubSpot</b> creó la categoría enseñando inbound gratis; <b>AECODE</b> aplica el patrón BuildWitt: medios propios → audiencia → conversión barata.","HubSpot"),
    ("Sales Pipeline","pipeline de ventas",
     "La <b>fila de oportunidades</b> en cada etapa de venta (lead, calificado, propuesta, cierre). Gestionarlo te dice cuánto cerrarás y dónde se atascan los tratos.",
     "Es una tubería con válvulas: ves <b>cuánta agua</b> hay en cada tramo y cuál válvula medio cerrada frena todo el flujo.",
     "Equipos B2B usan CRMs como <b>Salesforce</b> o HubSpot para mover deals por el pipeline y pronosticar ingresos con realismo.","B2B Sales"),
    ("NPS","net promoter score",
     "Mide la <b>lealtad</b> con una pregunta: «¿qué tan probable es que nos recomiendes (0–10)?». Promotores menos detractores. Predice boca a boca y retención.",
     "Es preguntar a los invitados de la boda si <b>recomendarían</b> al organizador: los que dan 9–10 te traen las próximas bodas.",
     "<b>AECODE</b> reporta NPS de cohortes de 66–78, muy por encima de la media de EdTech: señal de que el valor se siente real.","AECODE",
     "NPS = % promotores (9–10) − % detractores (0–6)"),
    ("Referral","boca a boca",
     "El crecimiento por <b>recomendación</b> de usuarios satisfechos. Es el canal más barato y de mayor confianza: un cliente feliz convierte mejor que cualquier anuncio.",
     "Es el restaurante al que vas porque <b>tu amigo juró</b> que era buenísimo: confías en él más que en cualquier valla publicitaria.",
     "<b>PayPal</b> pagaba $10 por referir y $10 al referido: compró su red inicial, pero el boca a boca la volvió viral y autosostenida.","PayPal"),
   ]),
 dict(no=8, name="Nivel 8 · Estrategia y Defensa", theme="light", accent="violet",
   title='Nivel 8 — <span class="grad">Estrategia y Defensibilidad</span>',
   sub="Por qué, una vez que ganas, nadie te puede quitar el mercado: ventajas que se acumulan con el tiempo.",
   concepts=[
    ("Ventaja Competitiva","por qué ganas",
     "La razón <b>estructural</b> por la que ganas y sostienes clientes mejor que los rivales: costo, marca, tecnología o red. Sin ella, compites solo por precio.",
     "Es jugar de local con el viento a favor: el rival puede ser bueno, pero <b>el campo te beneficia</b> sistemáticamente.",
     "<b>Amazon</b> compite por escala y logística: precios y entrega que un competidor pequeño simplemente no puede igualar.","Amazon"),
    ("Moat","foso defensivo",
     "La <b>barrera duradera</b> que protege tu negocio de la competencia (red, marca, costos de cambio, datos). Buffett invierte solo en empresas con foso ancho.",
     "Es el foso de agua alrededor del castillo: no impide que ataquen, pero hace que <b>conquistarte sea carísimo</b> y lento.",
     "<b>AECODE</b> construye su moat con el Skill Graph AEC y la data de evidencia: cada vuelta del loop lo hace más difícil de replicar.","AECODE"),
    ("Flywheel","volante de inercia",
     "Un <b>círculo virtuoso</b> donde cada parte impulsa a la siguiente y el sistema gana momentum: cuesta arrancar, pero luego gira casi solo.",
     "Es un volante pesado: las primeras vueltas cuestan muchísimo, pero una vez girando, <b>un empujón lo acelera</b> sin parar.",
     "<b>Amazon:</b> más selección → más clientes → más vendedores → mejores precios → más clientes. AECODE: más usuarios → más datos → mejores rutas.","Amazon"),
    ("Switching Costs","costos de cambio",
     "Lo que le <b>cuesta al cliente</b> irse con un competidor: tiempo, datos, aprendizaje, integraciones. Altos costos de cambio = clientes pegados.",
     "Es mudarte de casa con 10 años de cosas: aunque haya una mejor, <b>la pereza de empacar todo</b> te mantiene donde estás.",
     "<b>Salesforce</b> y los ERP: una vez que tu empresa tiene todo dentro, migrar es tan caro y riesgoso que casi nadie lo hace.","Salesforce"),
    ("Economías de Escala","ventaja por tamaño",
     "Cuando tu <b>costo por unidad baja</b> al crecer el volumen. El grande produce más barato que el chico y puede defender precio o margen.",
     "Es comprar al por mayor: el costo del envío y la negociación se <b>reparten entre miles</b> de unidades, no entre diez.",
     "<b>Tesla</b> con sus Gigafactories baja el costo por batería al escalar volumen: una ventaja que los rivales tardan años en igualar.","Tesla"),
    ("Plataforma / Ecosistema","negocio de plataforma",
     "Pasar de producto a <b>plataforma</b> donde terceros construyen sobre ti, multiplicando el valor sin que tú hagas todo. El ecosistema se vuelve barrera.",
     "Es ser el sistema operativo, no una app: <b>otros crean encima de ti</b> y, mientras más construyen, más imposible es reemplazarte.",
     "<b>Apple</b> App Store y <b>Shopify</b>: miles de desarrolladores crean valor para sus usuarios; el ecosistema es el verdadero foso.","Shopify"),
    ("Blue Ocean","océano azul",
     "Crear un <b>espacio de mercado nuevo</b> sin competencia directa, en vez de pelear en un 'océano rojo' saturado y sangriento por precio.",
     "En vez de pelear por un pez en un charco lleno de tiburones, <b>nadas a un lago</b> nuevo donde eres el único.",
     "<b>Cirque du Soleil</b> creó un océano azul fusionando circo y teatro; <b>Nintendo Wii</b> dejó la guerra de poder gráfico por el juego casual.","Cirque du Soleil"),
    ("Data Moat","foso de datos",
     "Una ventaja que <b>se acumula con los datos</b>: más uso → más datos → mejor producto → más uso. La IA convierte los datos propios en una barrera compuesta.",
     "Es una bola de nieve rodando: <b>cada vuelta junta más nieve</b> y se hace más grande y más difícil de detener.",
     "<b>AECODE</b> acumula evidencia y eventos de aprendizaje: cada usuario mejora las rutas y la evaluación sin escalar horas humanas.","AECODE"),
    ("First Mover vs Fast Follower","mover primero o seguir",
     "<b>First mover</b>: ventaja por llegar primero (red, marca); pero a veces el <b>fast follower</b> gana al aprender de los errores ajenos sin pagar la educación del mercado.",
     "El primero abre la trocha en la selva y se llena de espinas; el segundo <b>camina por el sendero</b> ya despejado, más rápido.",
     "<b>Google</b> no fue el primer buscador (lo fueron AltaVista, Yahoo); fue el fast follower que lo hizo claramente mejor.","Google"),
    ("Innovación Disruptiva","disruption",
     "Teoría de Christensen: una solución <b>más simple y barata</b> entra por abajo del mercado, mejora con el tiempo y termina desplazando a los líderes establecidos.",
     "Es el pez chico que empieza comiendo migajas que el grande desprecia, <b>crece</b> y termina dominando el arrecife.",
     "<b>Netflix</b> (DVDs por correo) parecía inferior a Blockbuster; subió hasta destruirlo. La disrupción casi nunca se ve venir desde arriba.","Netflix"),
   ]),
 dict(no=9, name="Nivel 9 · Fundraising y Capital", theme="dark", accent="violet",
   title='Nivel 9 — <span class="grad">Fundraising y Capital</span>',
   sub="Cómo se financia una startup, quién pone el dinero y qué entregas a cambio: el lenguaje del capital.",
   concepts=[
    ("Bootstrapping","crecer con caja propia",
     "Financiar la startup con <b>ingresos propios y ahorros</b>, sin levantar capital externo. Conservas control y disciplina, a cambio de crecer más lento.",
     "Es construir la casa <b>ladrillo a ladrillo</b> con tu sueldo, sin pedir hipoteca: avanzas despacio pero la casa es 100% tuya.",
     "<b>Mailchimp</b> creció a US$700M en ingresos sin un dólar de VC y se vendió por US$12.000M: bootstrapping llevado al extremo.","Mailchimp"),
    ("Fundraising","levantar capital",
     "El proceso de <b>conseguir inversión</b> a cambio de participación, para acelerar más rápido de lo que la caja permitiría. Es vender futuro para comprar velocidad.",
     "Es echar más leña a una fogata que ya prende: <b>no enciende</b> leña mojada (idea sin tracción), pero aviva una llama real.",
     "<b>AECODE</b> avanza con ProInnóvate (Hito 1 aprobado) y prepara su data room conciliando tracción y unit economics antes de una ronda externa.","AECODE"),
    ("Etapas de Ronda","pre-seed a Serie C",
     "El capital llega por <b>etapas</b>: pre-seed (idea), seed (PMF temprano), Serie A (escalar el modelo), B/C (expansión). Cada una con hitos y montos mayores.",
     "Son los <b>grados escolares</b> del financiamiento: no saltas a la universidad sin pasar primaria; cada nivel exige probar el anterior.",
     "<b>Uber</b> recorrió de seed (~$200k) a megarrondas de miles de millones; cada Serie financió una fase concreta de expansión.","Uber"),
    ("Ángel y Venture Capital","quién invierte",
     "El <b>ángel</b> invierte su dinero propio temprano y aporta mentoría; el <b>VC</b> gestiona un fondo de terceros y busca retornos de 10×+ en empresas escalables.",
     "El ángel es el tío que cree en ti y pone de su bolsillo; el VC es el <b>banco de apuestas</b> que juega fuerte buscando el gran golpe.",
     "<b>Y Combinator</b>, Sequoia y a16z apostaron temprano por Airbnb, Stripe y Dropbox cuando casi nadie lo veía claro.","Sequoia"),
    ("Valoración","cuánto vales",
     "El <b>valor asignado</b> a tu startup. <b>Pre-money</b> = antes de la inversión; <b>post-money</b> = pre + lo invertido. Define cuánto % entregas por el capital.",
     "Es tasar una casa antes de vender una habitación: <b>el precio total</b> decide qué fracción das por el dinero que recibes.",
     "Si vales US$4M pre-money y levantas US$1M, el post-money es US$5M y el inversionista se queda con el 20%.","Ejemplo",
     "% inversionista = inversión ÷ valoración post-money"),
    ("Cap Table","tabla de capitalización",
     "El <b>registro de quién posee qué</b> % de la empresa: fundadores, inversionistas, empleados. Mantenerla limpia es vital para futuras rondas y para el exit.",
     "Es el <b>reparto de la pizza</b> escrito en papel: cada ronda corta nuevas rebanadas y conviene saber exactamente quién se come cuánto.",
     "Un cap table desordenado (demasiados socios pequeños) espanta a los VCs serios: prefieren una mesa de socios limpia y alineada.","Buenas prácticas"),
    ("Dilución","reparto al crecer",
     "Cuando emites <b>nuevas acciones</b> en una ronda, el % de los socios existentes se reduce. No es malo si la torta crece: prefieres 5% de algo gigante a 100% de nada.",
     "Tu rebanada de pizza se hace <b>más fina</b>, pero la pizza entera creció tanto que tu trozo vale mucho más que antes.",
     "Tras varias rondas, los fundadores de <b>Google</b> quedaron con un % pequeño, pero de una empresa de billones: dilución bien hecha.","Google"),
    ("SAFE / Convertible","instrumentos tempranos",
     "Formas de invertir <b>sin fijar valoración hoy</b>: el dinero entra ya y se convierte en acciones en la siguiente ronda, con descuento o cap. Rápido y simple.",
     "Es un <b>vale</b>: «te doy el dinero ahora y luego lo canjeo por acciones al precio que se fije», sin discutir el valor exacto todavía.",
     "El <b>SAFE</b> de Y Combinator estandarizó la inversión pre-seed: cierras en días, no en meses de negociación legal.","Y Combinator"),
    ("Equity · Vesting · ESOP","participación del equipo",
     "El <b>equity</b> es propiedad; el <b>vesting</b> la entrega gradualmente (típico: 4 años, 1 de cliff); el <b>ESOP</b> es el pool de acciones para empleados clave.",
     "Es ganarte la casa <b>pagando cuotas con tu trabajo</b>: si te vas el primer año (antes del cliff), no te llevas nada.",
     "<b>Startups</b> atraen talento top con equity: un ingeniero temprano de Stripe o Coinbase pudo volverse millonario por su vesting.","Talento"),
    ("Due Diligence","auditoría del inversor",
     "La <b>investigación a fondo</b> que hace el inversionista antes de poner el dinero: finanzas, legal, métricas, equipo y tecnología. Tu data room debe sostenerla.",
     "Es la <b>revisión mecánica</b> antes de comprar el auto usado: levantan el capó, revisan papeles y prueban que todo lo dicho sea cierto.",
     "<b>AECODE</b> prepara su due diligence conciliando ventas, analytics y CRM: las cifras de pitch deben cuadrar con la contabilidad real.","AECODE"),
   ]),
 dict(no=10, name="Nivel 10 · Escala y Experto", theme="light", accent="violet",
   title='Nivel 10 — <span class="grad">Escala y Experto</span>',
   sub="De startup que funciona a empresa que define una categoría: escalar, componer ventajas y materializar el valor.",
   concepts=[
    ("Escalabilidad","crecer sin crecer costos",
     "La capacidad de <b>multiplicar ingresos sin multiplicar costos</b> en la misma proporción. Es lo que separa a una startup de un negocio de servicios lineal.",
     "Es un molde de galletas vs. esculpir cada una a mano: el software te deja servir a <b>1 o a 1 millón</b> casi al mismo costo.",
     "<b>WhatsApp</b> servía a 450M usuarios con ~55 empleados: el producto escalaba, el equipo no necesitaba crecer al mismo ritmo.","WhatsApp"),
    ("Blitzscaling","escalar a toda velocidad",
     "Priorizar la <b>velocidad sobre la eficiencia</b> en mercados 'winner-take-all' para ganar escala dominante antes que la competencia, aun quemando capital.",
     "Es correr cuesta abajo tan rápido que <b>casi te caes</b>: arriesgado, pero si el premio es todo el mercado, frenar es perder.",
     "<b>Uber</b> y <b>Airbnb</b> blitzscalearon globalmente: aceptaron caos y pérdidas para capturar el mercado antes que cualquier clon.","Uber"),
    ("Scale-up","de startup a scale-up",
     "Una startup que <b>ya encontró PMF</b> y crece de forma sostenida (típico: +20% anual en ingresos o equipo). El reto pasa de 'descubrir' a 'ejecutar y no romperse'.",
     "Es pasar de inventar la receta a <b>abrir 100 sucursales</b> sin que la calidad ni la cultura se diluyan.",
     "<b>Nubank</b> pasó de startup a scale-up y luego a banco gigante de LATAM: el desafío fue escalar sistemas, equipo y cultura a la vez.","Nubank"),
    ("Unicornio","valoración de US$1.000M",
     "Una startup privada valorada en <b>más de US$1.000 millones</b>. El término (Aileen Lee, 2013) marcaba lo raro; hoy hay cientos, y existen 'decacornios' (US$10B+).",
     "Era tan raro como ver un unicornio; ahora es más como ver un caballo <b>muy</b> caro, pero sigue siendo la liga mayor.",
     "<b>Rappi</b> y <b>Nubank</b> fueron unicornios latinoamericanos; alcanzar esa marca abre acceso a capital y talento global.","Rappi"),
    ("Pensamiento 10x","moonshot",
     "Apuntar a mejorar <b>10 veces</b>, no un 10%. El salto radical obliga a replantear desde cero y abre espacios que la mejora incremental nunca alcanza.",
     "Para llegar a la Luna no construyes una <b>escalera más alta</b>: cambias de vehículo. El 10x exige reinventar, no optimizar.",
     "<b>Google X</b> persigue moonshots (autos autónomos, Loon); SpaceX bajó 10× el costo de ir al espacio reusando cohetes.","SpaceX"),
    ("Compounding · AI Flywheel","ventaja que compone",
     "Ventajas que <b>se acumulan e interactúan</b> en el tiempo (datos, marca, red), creciendo de forma exponencial. Con IA, los datos propios componen el foso.",
     "Es el interés compuesto: pequeño hoy, pero <b>se acelera solo</b> y en años se vuelve imbatible. El tiempo juega a tu favor.",
     "<b>Tesla</b> compone datos de conducción de millones de autos para mejorar su autopilot, que atrae más autos, que generan más datos.","Tesla"),
    ("M&A","fusiones y adquisiciones",
     "Crecer o salir <b>comprando o fusionándote</b> con otra empresa, para ganar tecnología, talento, mercado o eliminar a un rival. Vía común de exit y de expansión.",
     "Es absorber a otro equipo para <b>sumar sus jugadores</b> de golpe, en vez de formar cada talento desde la cantera.",
     "<b>Facebook</b> compró Instagram (US$1B) y WhatsApp (US$19B): neutralizó amenazas y sumó redes enteras de un solo movimiento.","Meta"),
    ("Exit","la salida",
     "El evento en que fundadores e inversionistas <b>materializan el valor</b>: venta (M&A) o salida a bolsa (IPO). Es cuando el papel se vuelve dinero real.",
     "Es vender la casa que renovaste por años: <b>recién en la venta</b> conviertes todo el esfuerzo en efectivo en el bolsillo.",
     "El exit de <b>WhatsApp</b> a Facebook (US$19B) convirtió a un equipo de ~55 personas en una de las ventas más rentables de la historia.","WhatsApp"),
    ("IPO","salida a bolsa",
     "<b>Oferta Pública Inicial</b>: la empresa vende acciones al público en bolsa, consigue capital masivo y liquidez, a cambio de transparencia y escrutinio permanente.",
     "Es pasar de un club privado a <b>un estadio abierto</b>: entra muchísimo público (capital), pero ahora todos miran cada jugada.",
     "El IPO de <b>Airbnb</b> (2020) la valoró en ~US$47B; salir a bolsa fue el rito final de startup a empresa pública madura.","Airbnb"),
    ("Category Creation","crear una categoría",
     "En vez de competir en un mercado existente, <b>defines uno nuevo</b> y te conviertes en su rey. El 'category king' suele capturar la mayor parte del valor.",
     "Es no ser 'otro refresco' sino <b>inventar la cola</b>: cuando creas la categoría, tu nombre se vuelve el del producto entero.",
     "<b>Salesforce</b> creó el CRM en la nube; <b>AECODE</b> apunta a crear la categoría «capa de capacidad verificable» para el sector AEC.","AECODE"),
   ]),
]

# ---- intro de nivel enriquecida (lista lo que verás) ----
def level_intro(L, start):
    chips=""
    for i,c in enumerate(L["concepts"]):
        chips+=f'<span class="li-item"><span class="li-n">{start+i:02d}</span>{esc(c[0])}</span>'
    content=f"""
  <div class="div-index reveal">{L['no']:02d}</div>
  <h2 class="div-title reveal">{L['title']}</h2>
  <p class="div-sub reveal">{L['sub']}</p>
  <div class="li-list reveal">{chips}</div>
"""
    S(L["theme"], L["name"], "divider", content)

# ---- síntesis visual por nivel (diagrama animado + cómo se conecta) ----
SYNTH = {
 1: ('El motor de los fundamentos: <span class="grad">Construir → Medir → Aprender</span>',
     ring_cycle([("Construir","un MVP"),("Medir","con clientes reales"),("Aprender","iterar o pivotar")],"Lean","loop infinito"),
     'Los fundamentos no son una lista: son un <b>ciclo</b>. Cada vuelta convierte incertidumbre en evidencia y acerca tu idea al mercado.',
     '<b>Se conecta con:</b> el MVP (09) alimenta el ciclo y el Customer Discovery (10) lo valida; el resultado deseado es el <i>Product-Market Fit</i> del Nivel 3.'),
 2: ('Dimensiona el juego: <span class="grad">TAM · SAM · SOM</span>',
     tamsamsom([("TAM","todo el mercado","el universo total"),("SAM","el que puedes servir","tu modelo y alcance"),("SOM","el que capturarás","realista a corto plazo")]),
     'Conocer al <b>cliente</b> (ICP, persona, JTBD) sin medir el <b>tamaño</b> del mercado es construir a ciegas. Primero a quién, luego cuán grande.',
     '<b>Se conecta con:</b> el ICP (12) define tu SAM; el beachhead (17) es tu primer SOM; el «why now» (19) abre la ventana. Lleva al producto del Nivel 3.'),
 3: ('La meta de toda startup temprana: <span class="grad">Product-Market Fit</span>',
     curve("pmf"),
     'Antes del PMF <b>tú empujas</b> el producto al mercado; después, el mercado <b>te jala</b>. La curva se dobla cuando la retención y el boca a boca despegan.',
     '<b>Se conecta con:</b> sin PMF, gastar en growth (Nivel 7) es echar agua a un balde roto. El PMF se mide con la retención del Nivel 6.'),
 4: ('Cómo capturas valor: el <span class="grad">modelo de negocio</span>',
     canvas_mini([("Aliados","violet"),("Actividades","blue"),("Propuesta de valor","green"),
                  ("Recursos","blue"),("Clientes","violet"),("Relación","blue"),
                  ("Canales","green"),("Costos","violet"),("Ingresos","green")]),
     'El modelo conecta <b>a quién sirves</b> con <b>cómo cobras</b>. Pricing, freemium, SaaS o marketplace son distintas formas de capturar el valor que creas.',
     '<b>Se conecta con:</b> el modelo define tus ingresos, que alimentan los unit economics del Nivel 5. El B2B2C (38) es el modelo de AECODE.'),
 5: ('La pregunta que decide todo: <span class="grad">¿gana cada cliente?</span>',
     scale_compare("US$35","≈US$110","3.1×"),
     'Si el <b>LTV</b> (lo que vale un cliente) supera al <b>CAC</b> (lo que cuesta) por <b>3× o más</b>, el negocio escala sano. Si no, crecer solo multiplica pérdidas.',
     '<b>Se conecta con:</b> el CAC baja con growth orgánico (Nivel 7); el LTV sube con retención (Nivel 6). El burn y runway marcan el reloj de la caja.'),
 6: ('Mide lo que importa: el embudo <span class="grad">AARRR</span>',
     funnel_v([("Adquisición","100","llegan","violet"),("Activación","62","primer valor","blue"),
               ("Retención","40","vuelven","green"),("Revenue","26","pagan","violet"),
               ("Referido","16","recomiendan","green")]),
     'Las «pirate metrics» te dicen <b>exactamente dónde</b> pierdes usuarios. Optimizar una etapa rinde más que gastar más arriba del embudo.',
     '<b>Se conecta con:</b> la North Star (52) resume el embudo en una métrica; la retención (55) es la etapa que más predice el PMF.'),
 7: ('Crece en bucle: el <span class="grad">growth loop</span>',
     ring_cycle([("Usuario","obtiene valor"),("Comparte","invita / evidencia"),("Atrae","nuevos usuarios"),("Activa","y vuelve a empezar")],"Loop","crecimiento compuesto"),
     'El crecimiento de élite no es un embudo lineal, es un <b>bucle</b>: cada usuario produce el siguiente. Así operan PLG, viralidad y network effects.',
     '<b>Se conecta con:</b> el viral loop (63) y los network effects (64) hacen girar el bucle; un buen GTM (66) lo arranca. Refuerza el moat del Nivel 8.'),
 8: ('Por qué nadie te copia: el <span class="grad">moat</span>',
     moat_layers([("Marca & comunidad","te eligen por confianza"),("Costos de cambio","irse cuesta caro"),("Efecto red","más valor con más gente"),("Datos / producto","núcleo que mejora solo")]),
     'Un foso es una ventaja que <b>se acumula con el tiempo</b>. Se construye por capas: red, costos de cambio, datos y marca lo hacen casi imposible de replicar.',
     '<b>Se conecta con:</b> los network effects (64) y switching costs (74) forman el foso; el flywheel (73) lo hace girar. Es lo que defiende tu categoría (100).'),
 9: ('Combustible por etapas: el <span class="grad">fundraising</span>',
     fund_bars([("Pre-seed","20","idea","violet"),("Seed","38","PMF temprano","blue"),
                ("Serie A","60","escalar","green"),("Serie B","82","expandir","violet"),
                ("Serie C","100","dominar","green")]),
     'El capital llega por <b>rondas crecientes</b>, cada una atada a un hito. Levantas valoración a cambio de equity, y la dilución se compensa si la torta crece.',
     '<b>Se conecta con:</b> cada ronda compra runway (Nivel 5) para alcanzar el siguiente hito; la tracción del Nivel 6 sostiene tu valoración y el due diligence (90).'),
 10:('De startup a categoría: la <span class="grad">curva J</span> al exit',
     curve("jcurve"),
     'Escalar implica un <b>valle</b> (inviertes y quemas) antes del despegue. Quien sobrevive el valle y compone ventajas llega a la escala, la categoría y el exit.',
     '<b>Se conecta con:</b> el blitzscaling (92) acelera la subida; el compounding (96) la sostiene; el M&A (97), IPO (99) y la categoría (100) materializan el valor.'),
}
def level_synth(L):
    ttl,d,body,rel = SYNTH[L["no"]]
    content=f"""
  {kicker("Síntesis visual · "+L["name"])}
  {title(ttl)}
  <div class="split synth-split">
    <div class="split-l">{d}</div>
    <div class="split-r">{lead(body)}{note(rel)}</div>
  </div>"""
    S(L["theme"], L["name"], "synth", content)

# ---- emitir intro + conceptos + síntesis por nivel ----
num = 0
for L in LEVELS:
    level_intro(L, num+1)
    for c in L["concepts"]:
        num += 1
        name, eng, works, analogy, example, ex_tag = c[0], c[1], c[2], c[3], c[4], c[5]
        formula = c[6] if len(c) > 6 else None
        concept(num, L["name"], name, eng, works, analogy, example, ex_tag,
                formula=formula, theme=L["theme"])
    level_synth(L)

# ======================= RUTA DE DOMINIO =======================
S("light","Tu ruta de dominio","synthwide", f"""
  {kicker("De principiante a experto")}
  {title('Tu <span class="grad">ruta</span> de dominio en 4 escalones')}
  {ladder([
    ("N1–3","Principiante","Entiendes el problema, validas y llegas a PMF. Hablas el idioma.","32"),
    ("N4–6","Operador","Diseñas modelo, cuidas unit economics y mides crecimiento real.","56"),
    ("N7–8","Estratega","Construyes growth en bucle y un foso que nadie puede copiar.","80"),
    ("N9–10","Experto · Founder","Financias, escalas, defines categoría y materializas el valor.","100"),
  ])}
  {lead('Sube un escalón a la vez: cada uno <b>asume el anterior</b>. No necesitas saberlo todo hoy — necesitas saber <i>en qué escalón estás</i> y cuál es el siguiente.')}
""")

# ======================= CIERRE =======================
S("dark","Cierre","close", f"""
  <div class="cover-logo reveal"><img class="logo-dark" src="brand/assets/logos/aecode-logo-principal-fondo-oscuro.png" alt="AECODE"><img class="logo-light" src="brand/assets/logos/aecode-logo-principal-fondo-blanco.png" alt="AECODE"></div>
  {title('De saber los conceptos a <span class="grad">construir con ellos</span>')}
  <div class="close-cols">
    <div class="reveal"><div class="close-h">Cómo usar esta guía</div>{bullets([
      "Domina <b>nivel por nivel</b>: cada uno asume el anterior.",
      "Para cada decisión, pregunta <i>qué concepto aplica</i>.",
      "Explica cada idea con su analogía: si no puedes, repásala.",
    ])}</div>
    <div class="reveal"><div class="close-h">Aplicado a AECODE</div>{bullets([
      "Wedge → Engine → Moat como tesis de crecimiento.",
      "North Star: skills verificadas / usuario activo.",
      "Unit economics: CAC US$35 · LTV:CAC 3.1× · payback 7m.",
    ])}</div>
  </div>
  {quote('100 conceptos, una sola disciplina: <span class="grad">enamórate del problema, mide lo que importa y construye lo que nadie pueda copiar.</span>')}
  <div class="close-cta reveal">AECODE · Guía Maestra de Startups · {datetime.date.today().strftime('%b %Y')}</div>
""")

# ======================= RENDER =======================
def render_slide(i,s):
    return (f'<section class="slide" data-base="{s["theme"]}" data-idx="{i}">'
            f'<div class="slide-inner layout-{s["layout"]}">{s["content"]}</div>'
            f'<img class="slide-mark" src="brand/assets/logos/aecode_isotipo_principal.png" alt="">'
            f'<div class="slide-foot"><span class="foot-ch">{esc(s["chapter"])}</span>'
            f'<span class="foot-n">{i+1:02d}<i>/</i>{len(SLIDES):02d}</span></div></section>')
slides_html="\n".join(render_slide(i,s) for i,s in enumerate(SLIDES))
total=len(SLIDES)
toc_items="".join(
   f'<button class="toc-item" data-go="{i}"><span class="toc-n">{i+1:02d}</span>'
   f'<span class="toc-t">{esc(s["chapter"])}</span></button>' for i,s in enumerate(SLIDES))

CSS = r"""
:root{
  --violet:#4A3AC1; --blue:#4465EE; --violet2:#6D70F9; --green:#17B14E; --lavender:#A6A7FF;
  --ease:cubic-bezier(.22,.61,.36,1); --ease-out:cubic-bezier(.16,1,.3,1);
}
.is-light{
  --bg:#F5F5F6; --bg2:#EDEBF9; --surface:#FFFFFF; --fg:#202231; --muted:#3A4065;
  --line:#C7C2EC; --card:#FFFFFF; --card-line:#E3E0F5;
  --accent:#4A3AC1; --accent2:#4465EE; --accent3:#17B14E; --ink-soft:#4A3AC1;
  --grad:linear-gradient(100deg,#4465EE,#6D12E3);
  --grad3:linear-gradient(100deg,#17B14E,#4A3AC1);
  --mesh-a:rgba(74,58,193,.10); --mesh-b:rgba(23,177,78,.10);
  --chip-bg:#EDEBF9;
}
.is-dark{
  --bg:#0E1121; --bg2:#1B1E3C; --surface:#13172F; --fg:#EEF3F8; --muted:#A2B4CB;
  --line:rgba(124,126,223,.24); --card:rgba(27,30,60,.72); --card-line:rgba(124,126,223,.32);
  --accent:#A6A7FF; --accent2:#7E97FF; --accent3:#2FD06E; --ink-soft:#C9D0F5;
  --grad:linear-gradient(100deg,#7E97FF,#9A5CFF);
  --grad3:linear-gradient(100deg,#2FD06E,#8C97DC);
  --mesh-a:rgba(74,58,193,.46); --mesh-b:rgba(23,177,78,.20);
  --chip-bg:rgba(124,126,223,.16);
}
*{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%}
body{background:#05060f;color:#fff;overflow:hidden;font-family:Manrope,"Plus Jakarta Sans",system-ui,sans-serif;-webkit-font-smoothing:antialiased}
.deck{position:fixed;inset:0;display:grid;place-items:center}
.stage{width:1280px;height:720px;position:relative;transform-origin:center}
.slide{position:absolute;inset:0;display:grid;place-items:center;background:var(--bg);color:var(--fg);
  opacity:0;visibility:hidden;pointer-events:none;transition:opacity .5s var(--ease);overflow:hidden}
.slide::before{content:"";position:absolute;inset:-12%;z-index:0;
  background:radial-gradient(38% 50% at 14% 12%,var(--mesh-a),transparent 70%),
             radial-gradient(44% 52% at 88% 90%,var(--mesh-b),transparent 72%)}
.slide.active{opacity:1;visibility:visible;pointer-events:auto}
.slide-inner{position:relative;z-index:2;width:100%;height:100%;padding:54px 72px 60px;
  display:flex;flex-direction:column;justify-content:center;gap:16px}
.slide-foot{position:absolute;z-index:3;left:72px;right:72px;bottom:22px;display:flex;
  justify-content:space-between;font-size:12.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
.foot-ch{font-weight:700} .foot-n{font-variant-numeric:tabular-nums;font-weight:700}
.foot-n i{opacity:.4;font-style:normal;margin:0 3px}
.reveal{opacity:0;transform:translateY(16px);transition:opacity .55s var(--ease-out),transform .55s var(--ease-out)}
.slide.active .reveal{opacity:1;transform:none}
/* typo */
.kicker{font-weight:800;font-size:13px;letter-spacing:.22em;text-transform:uppercase;color:var(--accent);
  display:flex;align-items:center;gap:11px}
.kicker::before{content:"";width:30px;height:3px;border-radius:3px;background:var(--grad)}
.s-title{font-weight:800;font-size:clamp(30px,3.9vw,48px);line-height:1.03;letter-spacing:-.02em;
  text-wrap:balance;max-width:21ch}
.lead{font-size:clamp(16px,1.45vw,20px);line-height:1.5;color:var(--muted);max-width:66ch}
.lead b{color:var(--fg);font-weight:700} .lead i{font-style:italic;color:var(--accent)}
.grad{background:var(--grad);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent}
.chip{display:inline-flex;align-items:center;gap:9px;align-self:flex-start;font-size:14px;font-weight:700;
  padding:9px 17px;border-radius:100px;border:1px solid var(--card-line);background:var(--chip-bg);color:var(--fg)}
.chip::before{content:"\25C6";color:var(--accent3);font-size:10px}
.vnote{font-size:13.5px;line-height:1.45;color:var(--muted);padding:12px 16px;border-radius:12px;
  background:var(--bg2);border:1px dashed var(--card-line)}
.vnote b{color:var(--accent)}
/* cover */
.layout-cover,.layout-close{align-items:flex-start;justify-content:center;gap:18px}
.cover-logo img{height:50px;width:auto;display:block}
.logo-light{display:none}
.slide.is-light .logo-light{display:block} .slide.is-light .logo-dark{display:none}
.layout-close .cover-logo img{height:42px}
.slide-mark{position:absolute;top:30px;right:34px;height:30px;width:auto;z-index:3;opacity:.92;pointer-events:none}
.layout-cover .slide-mark,.layout-close .slide-mark,.layout-divider .slide-mark{display:none}
.layout-cover{padding-right:336px}
.aecodito{position:absolute;right:52px;bottom:58px;width:244px;height:auto;z-index:1;
  filter:drop-shadow(0 22px 44px rgba(74,58,193,.42));animation:float 6s var(--ease) infinite}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-13px)}}
@media (prefers-reduced-motion:reduce){.aecodito{animation:none}}
.cover-title{font-weight:800;font-size:clamp(38px,5.2vw,66px);line-height:1.0;letter-spacing:-.03em;text-wrap:balance}
.cover-sub{font-size:clamp(15px,1.5vw,20px);color:var(--muted);max-width:58ch;line-height:1.45}
.cover-sub b{color:var(--fg)}
.cover-meta{display:flex;gap:13px;align-items:center;flex-wrap:wrap;font-size:14.5px;color:var(--fg);margin-top:4px}
.cover-meta .dot{color:var(--accent3)}
.cover-hint{font-size:13px;color:var(--muted);margin-top:8px} .cover-hint b{color:var(--accent)}
/* statement / divider */
.layout-statement,.layout-divider{gap:24px}
.bigquote{font-weight:800;line-height:1.16;letter-spacing:-.02em;font-size:clamp(23px,2.85vw,37px);
  text-wrap:balance;max-width:28ch;border-left:4px solid var(--accent3);padding-left:28px}
.div-index{font-weight:800;font-size:clamp(58px,9vw,118px);line-height:1;color:transparent;-webkit-text-stroke:2px var(--accent);opacity:.5}
.div-title{font-weight:800;font-size:clamp(38px,5.2vw,64px);line-height:1.02;letter-spacing:-.025em}
.div-sub{font-size:clamp(16px,1.55vw,20px);color:var(--muted);max-width:58ch;line-height:1.45}
/* split */
.split{display:grid;grid-template-columns:1fr 1fr;gap:24px;align-items:stretch;margin-top:2px}
.split-l,.split-r{display:flex;flex-direction:column;gap:14px}
.split-l>.card,.split-r>.card{height:100%}
/* cards */
.grid{display:grid;gap:14px}
.grid-3{grid-template-columns:repeat(3,1fr)} .grid-4{grid-template-columns:repeat(4,1fr)}
.card{position:relative;padding:18px 18px 16px;border-radius:15px;background:var(--card);border:1px solid var(--card-line);
  display:flex;flex-direction:column;gap:8px;overflow:hidden}
.card::before{content:"";position:absolute;left:0;top:0;width:100%;height:3px;background:var(--accent)}
.card-green::before{background:var(--accent3)} .card-blue::before{background:var(--accent2)}
.card-num{font-weight:800;font-size:21px;color:var(--accent)}
.card-tag{font-size:11.5px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--accent)}
.card-green .card-tag,.card-green .card-num{color:var(--accent3)}
.card-blue .card-tag,.card-blue .card-num{color:var(--accent2)}
.card-head{font-weight:800;font-size:18px;line-height:1.2;color:var(--fg)}
.card-body{font-size:14.5px;line-height:1.45;color:var(--muted)}
.card-body b{color:var(--fg)} .card-body i{font-style:normal;color:var(--accent)}
.card-big{font-weight:800;font-size:30px;color:var(--accent);display:block;margin-bottom:1px}
.card-green .card-big{color:var(--accent3)} .card-blue .card-big{color:var(--accent2)}
.cards-sm .card-head{font-size:16.5px} .cards-sm .card-body{font-size:13.5px}
/* concept layout */
.layout-concept{justify-content:flex-start;padding-top:54px;gap:13px}
.c-head{display:flex;align-items:baseline;gap:16px}
.c-num{font-weight:800;font-size:clamp(28px,3.4vw,44px);line-height:1;color:transparent;
  -webkit-text-stroke:1.6px var(--accent);font-variant-numeric:tabular-nums;flex:none;opacity:.6}
.c-name{font-weight:800;font-size:clamp(24px,3.0vw,38px);line-height:1.05;letter-spacing:-.02em;color:var(--fg)}
.c-eng{display:block;font-size:14px;font-weight:600;font-style:italic;color:var(--accent2);margin-top:3px;letter-spacing:0}
.c-works{font-size:clamp(15px,1.42vw,18.5px);line-height:1.5;color:var(--muted);max-width:104ch}
.c-works b{color:var(--fg);font-weight:700} .c-works i{font-style:italic;color:var(--accent)}
.c-formula{display:inline-flex;align-items:center;gap:11px;align-self:flex-start;padding:8px 15px;border-radius:11px;
  background:var(--bg2);border:1px solid var(--card-line)}
.c-formula span{font-size:10.5px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--accent3);flex:none}
.c-formula code{font-family:ui-monospace,monospace;font-size:13.5px;color:var(--accent2);font-weight:600}
.layout-concept .split{margin-top:auto}
.layout-concept .card-body{font-size:14px;line-height:1.42}
.layout-concept .card-head{font-size:15px;color:var(--accent3)} .card-blue .card-head{color:var(--accent2)}
/* bullets */
.bullets{list-style:none;display:flex;flex-direction:column;gap:8px}
.bullets li{position:relative;padding-left:22px;font-size:15px;line-height:1.4;color:var(--muted)}
.bullets li b{color:var(--fg);font-weight:700} .bullets li i{font-style:normal;color:var(--accent)}
.bullets li::before{content:"";position:absolute;left:2px;top:7px;width:8px;height:8px;border-radius:2px;background:var(--accent3);transform:rotate(45deg)}
.card .bullets li{font-size:13.5px}
/* table */
.table-wrap{width:100%;border-radius:13px;border:1px solid var(--card-line);overflow:hidden}
.dt{width:100%;border-collapse:collapse;font-size:14.5px;background:var(--card)}
.dt th{font-weight:800;text-align:left;padding:11px 16px;font-size:12px;letter-spacing:.08em;text-transform:uppercase;
  color:var(--accent);background:var(--bg2);border-bottom:1px solid var(--card-line)}
.dt td{padding:9px 16px;border-bottom:1px solid var(--line);color:var(--muted);line-height:1.35;vertical-align:top}
.dt td b{color:var(--fg)} .dt tr:last-child td{border-bottom:none}
.dt .cell-hi{color:var(--fg);font-weight:700}
/* close */
.layout-close{justify-content:center;gap:16px}
.close-cols{display:grid;grid-template-columns:1fr 1fr;gap:28px;margin-top:4px}
.close-h{font-weight:800;font-size:15px;color:var(--accent);letter-spacing:.04em;margin-bottom:9px;text-transform:uppercase}
.close-cta{font-weight:700;font-size:15px;color:var(--fg);margin-top:6px;padding-top:14px;border-top:1px solid var(--line)}
/* ===== synth layouts + level intro ===== */
.layout-synth,.layout-synthwide{justify-content:center;gap:16px}
.synth-split{align-items:center;gap:30px}
.dgm{width:100%;display:flex;justify-content:center;align-items:center}
.card{transition:transform .25s var(--ease),box-shadow .25s var(--ease),opacity .5s var(--ease-out)}
.card:hover{transform:translateY(-3px);box-shadow:0 14px 32px rgba(74,58,193,.16)}
@media (hover:none){.card:hover{transform:none;box-shadow:none}}
.li-list{display:flex;flex-wrap:wrap;gap:8px;max-width:94ch;margin-top:8px}
.li-item{display:inline-flex;align-items:center;gap:8px;font-size:13px;font-weight:600;color:var(--fg);
  background:var(--chip-bg);border:1px solid var(--card-line);padding:7px 13px;border-radius:100px}
.li-n{font-weight:800;color:var(--accent3);font-variant-numeric:tabular-nums}
.band-violet{background:linear-gradient(100deg,#5a4ad0,#4a3ac1)} .band-blue{background:linear-gradient(100deg,#4465ee,#3f7be0)}
.band-green{background:linear-gradient(100deg,#26b96f,#1fa9a0)}
/* keyframes */
@keyframes spin{to{transform:rotate(360deg)}}
@keyframes drawline{to{stroke-dashoffset:0}}
@keyframes grow-line{to{width:90%}}
/* ring cycle */
.ring-cycle{position:relative;width:340px;height:300px;max-width:100%}
.rc-svg{position:absolute;inset:0;width:100%;height:100%}
.rc-track{fill:none;stroke:var(--card-line);stroke-width:2;stroke-dasharray:2 7}
.rc-arc{fill:none;stroke:var(--accent2);stroke-width:3;stroke-linecap:round;stroke-dasharray:330 465;opacity:.55}
.rc-arcg{transform-origin:100px 100px} .slide.active .rc-arcg{animation:spin 11s linear infinite}
.rc-run{transform-origin:100px 100px} .slide.active .rc-run{animation:spin 6s linear infinite}
.rc-dot{fill:var(--accent3)}
.fly .rc-arc{stroke-dasharray:150 465;opacity:.7} .slide.active .fly .rc-arcg{animation:spin 4.5s linear infinite}
.rc-center{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);text-align:center;width:118px}
.rc-center b{display:block;font-weight:800;font-size:19px;color:var(--fg);line-height:1} .rc-center span{font-size:11px;color:var(--muted)}
.rc-node{position:absolute;transform:translate(-50%,-50%);width:108px;text-align:center;background:var(--card);
  border:1px solid var(--card-line);border-radius:12px;padding:9px 7px;box-shadow:0 6px 18px rgba(20,18,60,.10)}
.rc-node b{display:block;font-size:13.5px;font-weight:800;color:var(--fg);line-height:1.12} .rc-node span{font-size:10.5px;color:var(--muted);line-height:1.18}
.rc-node.tone-violet{border-top:3px solid var(--accent)} .rc-node.tone-blue{border-top:3px solid var(--accent2)} .rc-node.tone-green{border-top:3px solid var(--accent3)}
/* tam sam som */
.tss{display:flex;gap:24px;align-items:center;flex-wrap:wrap}
.tss-rings{position:relative;width:210px;height:210px;flex:none}
.ring{position:absolute;border-radius:50%;display:grid;place-items:start center;padding-top:9px;font-weight:800;font-size:12px;left:50%;top:50%;transform:translate(-50%,-50%)}
.ring span{color:#fff;letter-spacing:.1em}
.ring.r0{width:210px;height:210px;background:rgba(74,58,193,.18);border:1px solid var(--violet)}
.ring.r1{width:144px;height:144px;background:rgba(68,101,238,.26);border:1px solid var(--blue)}
.ring.r2{width:80px;height:80px;background:var(--green);border:1px solid var(--green);place-items:center;padding:0}
.is-light .ring.r0 span,.is-light .ring.r1 span{color:#2a2470}
.tss-legend{display:flex;flex-direction:column;gap:11px;flex:1;min-width:200px}
.tss-leg{display:flex;gap:11px;align-items:flex-start;font-size:14px;color:var(--muted)}
.tss-leg .dot{width:14px;height:14px;border-radius:4px;margin-top:3px;flex:none}
.tss-leg .d0{background:var(--violet)} .tss-leg .d1{background:var(--blue)} .tss-leg .d2{background:var(--green)}
.tss-leg b{color:var(--fg);font-weight:800} .tss-leg small{display:block;color:var(--muted);font-size:12px}
/* curve */
.curve{width:100%;max-width:520px;display:flex;flex-direction:column;gap:8px}
.cv-svg{width:100%;height:auto}
.cv-axis{stroke:var(--card-line);stroke-width:2}
.cv-pre,.cv-post{fill:none;stroke-linecap:round}
.cv-pre{stroke:var(--accent);stroke-width:3;opacity:.65} .cv-post{stroke:var(--accent3);stroke-width:4.5}
.draw{stroke-dasharray:640;stroke-dashoffset:640} .slide.active .draw{animation:drawline 1.7s var(--ease-out) forwards}
.slide.active .cv-post{animation-delay:.5s}
.cv-mark{stroke:var(--accent2);stroke-width:1.5;stroke-dasharray:4 4;opacity:.7} .cv-pt{fill:var(--accent2)}
.cv-legend{display:flex;justify-content:space-between;font-size:12px;font-weight:700}
.cv-legend .l-pre{color:var(--accent)} .cv-legend .l-pmf{color:var(--accent2)} .cv-legend .l-post{color:var(--accent3)}
/* funnel */
.fnl{display:flex;flex-direction:column;gap:8px;align-items:center;width:100%;max-width:480px}
.fnl-row{width:var(--w);min-width:150px;display:flex;justify-content:space-between;align-items:center;gap:10px;
  padding:12px 18px;border-radius:10px;color:#fff;transform:scaleX(.6);opacity:0;transform-origin:center;
  transition:transform .6s var(--ease-out),opacity .6s}
.slide.active .fnl-row{transform:scaleX(1);opacity:1}
.fnl-row span{font-weight:800;font-size:14.5px} .fnl-row b{font-size:12px;opacity:.92;font-weight:600}
/* scale compare */
.scale{width:100%;max-width:470px;display:flex;flex-direction:column;gap:16px;position:relative}
.sc-row{display:flex;align-items:center;gap:13px}
.sc-lab{width:52px;font-weight:800;font-size:16px;color:var(--fg);flex:none}
.sc-lab small{display:block;font-size:10px;font-weight:600;color:var(--muted);letter-spacing:0}
.sc-track{flex:1;height:26px;border-radius:8px;background:var(--bg2);border:1px solid var(--card-line);overflow:hidden}
.sc-bar{display:block;height:100%;width:var(--w);transform:scaleX(0);transform-origin:left;transition:transform 1s var(--ease-out);border-radius:8px}
.sc-cac{background:linear-gradient(100deg,#7b6df0,#4a3ac1)} .sc-ltv{background:linear-gradient(100deg,#26b96f,#1fa9a0)}
.slide.active .sc-bar{transform:scaleX(1)}
.sc-val{font-weight:800;font-size:16px;font-variant-numeric:tabular-nums;width:74px;text-align:right;flex:none}
.sc-vcac{color:var(--accent)} .sc-vltv{color:var(--accent3)}
.sc-badge{align-self:center;margin-top:2px;font-weight:800;font-size:26px;color:#fff;background:var(--grad3);
  padding:8px 20px;border-radius:100px;display:flex;align-items:baseline;gap:8px}
.sc-badge span{font-size:11px;font-weight:700;opacity:.9;text-transform:uppercase;letter-spacing:.1em}
/* bmc canvas */
.bmc{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;width:100%;max-width:430px}
.cv-cell{padding:14px 10px;border-radius:11px;font-weight:700;font-size:13px;text-align:center;color:var(--fg);
  background:var(--card);border:1px solid var(--card-line);min-height:62px;display:grid;place-items:center;line-height:1.2}
.cv-cell.tone-violet{border-bottom:3px solid var(--accent)} .cv-cell.tone-blue{border-bottom:3px solid var(--accent2)} .cv-cell.tone-green{border-bottom:3px solid var(--accent3)}
/* fund bars */
.fund{display:flex;align-items:flex-end;gap:13px;height:240px;width:100%;max-width:460px}
.fund-col{flex:1;display:flex;flex-direction:column;justify-content:flex-end;gap:7px;height:100%;text-align:center}
.fund-amt{font-weight:800;font-size:13px} .fund-amt.tone-violet{color:var(--accent)} .fund-amt.tone-blue{color:var(--accent2)} .fund-amt.tone-green{color:var(--accent3)}
.fund-bar{width:100%;border-radius:9px 9px 0 0;height:var(--h);transform:scaleY(0);transform-origin:bottom;transition:transform .9s var(--ease-out)}
.slide.active .fund-bar{transform:scaleY(1)}
.fund-lab{font-size:12px;font-weight:700;color:var(--muted)}
/* moat */
.moat{width:100%;max-width:430px}
.moat-l{border:1.5px solid var(--card-line);border-radius:18px;padding:14px 16px 16px;background:var(--card);text-align:center;display:flex;flex-direction:column;gap:6px}
.moat-l b{font-weight:800;font-size:14.5px;color:var(--fg)} .moat-l span{font-size:11.5px;color:var(--muted)}
.moat-l .moat-l{margin-top:8px}
.moat-l:not(:has(.moat-l)){background:var(--grad3);border:none} .moat-l:not(:has(.moat-l)) b{color:#fff} .moat-l:not(:has(.moat-l)) span{color:rgba(255,255,255,.88)}
/* timeline */
.th{display:grid;position:relative;width:100%;margin:14px 0 8px}
.th::before{content:"";position:absolute;left:5%;right:5%;top:8px;height:3px;border-radius:3px;background:var(--card-line)}
.th::after{content:"";position:absolute;left:5%;top:8px;height:3px;border-radius:3px;background:var(--grad);width:0}
.slide.active .th::after{animation:grow-line 1.5s var(--ease-out) forwards}
.th-item{position:relative;padding:0 9px;display:flex;flex-direction:column;gap:7px;align-items:flex-start}
.th-dot{width:18px;height:18px;border-radius:50%;background:var(--accent);box-shadow:0 0 0 4px var(--bg),0 0 14px rgba(74,58,193,.4);z-index:2}
.th-item.win .th-dot{background:var(--accent3);box-shadow:0 0 0 4px var(--bg),0 0 16px rgba(38,185,111,.5)}
.th-stage{font-weight:800;font-size:14px;color:var(--fg);line-height:1.1} .th-item.win .th-stage{color:var(--accent3)}
.th-meta{font-size:11.5px;color:var(--muted);line-height:1.3}
/* concept web */
.concept-web{position:relative;width:530px;max-width:100%;height:300px}
.cw-svg{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
.cw-line{stroke:var(--card-line);stroke-width:1.5px;stroke-dasharray:600;stroke-dashoffset:600}
.slide.active .cw-line{animation:drawline 1.2s var(--ease-out) forwards}
.cw-center{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);background:var(--grad);color:#fff;
  font-weight:800;font-size:13.5px;width:100px;height:100px;border-radius:50%;display:grid;place-items:center;text-align:center;line-height:1.12;z-index:3;box-shadow:0 10px 30px rgba(74,58,193,.4)}
.cw-node{position:absolute;transform:translate(-50%,-50%);background:var(--card);border:1px solid var(--card-line);
  border-radius:9px;padding:7px 11px;font-size:12.5px;font-weight:800;color:var(--fg);white-space:nowrap;z-index:2;box-shadow:0 4px 14px rgba(20,18,60,.10)}
.cw-node.tone-violet{border-color:var(--accent);color:var(--accent)} .cw-node.tone-blue{border-color:var(--accent2);color:var(--accent2)} .cw-node.tone-green{border-color:var(--accent3);color:var(--accent3)}
/* ladder */
.ladder{display:flex;align-items:flex-end;gap:13px;width:100%;height:300px;margin-top:6px}
.ld-step{flex:1;height:var(--h);min-height:130px;background:var(--card);border:1px solid var(--card-line);border-bottom:3px solid var(--accent3);
  border-radius:14px 14px 0 0;padding:16px 15px;display:flex;flex-direction:column;gap:7px;justify-content:flex-start;
  transform:translateY(18px);opacity:0;transition:transform .6s var(--ease-out),opacity .6s}
.slide.active .ld-step{transform:none;opacity:1}
.ld-lvl{align-self:flex-start;font-weight:800;font-size:11px;letter-spacing:.08em;color:var(--accent3);background:var(--chip-bg);border:1px solid var(--card-line);padding:4px 10px;border-radius:100px}
.ld-h{font-weight:800;font-size:18px;color:var(--accent);line-height:1.1} .ld-d{font-size:13px;color:var(--muted);line-height:1.4}
/* ===== responsive (reflow en móvil) ===== */
@media (max-width:860px){
  body{overflow:auto}
  .deck{position:static;display:block;height:auto}
  .stage{transform:none!important;width:100%;height:auto}
  .slide{position:relative;display:none;height:auto;min-height:100vh;opacity:1!important;visibility:visible}
  .slide.active{display:grid}
  .slide-inner{position:relative;padding:62px 20px 76px;justify-content:flex-start;height:auto;min-height:100vh}
  .layout-cover .slide-inner,.layout-close .slide-inner,.layout-divider .slide-inner,.layout-statement .slide-inner{justify-content:center}
  .split,.grid-3,.grid-4,.synth-split,.close-cols{grid-template-columns:1fr!important}
  .s-title,.cover-title,.div-title{font-size:clamp(26px,7vw,40px)}
  .c-name{font-size:clamp(23px,6.4vw,34px)}
  .c-works,.lead{font-size:clamp(15px,4vw,18px)}
  .layout-cover{padding-right:20px}
  .aecodito{position:relative;right:auto;bottom:auto;width:140px;margin-top:8px;align-self:center}
  .layout-concept{padding-top:0} .layout-concept .split{margin-top:16px}
  .slide-foot{left:20px;right:20px;bottom:9px;font-size:10px}
  .ladder{height:auto;flex-direction:column}
  .ld-step{height:auto!important;min-height:0;border-bottom:none;border-left:3px solid var(--accent3);border-radius:0 14px 14px 0;transform:none;opacity:1}
  .fund{height:160px;max-width:100%} .th{grid-template-columns:1fr!important}
  .th::before,.th::after{display:none}
  .th-item{flex-direction:row;align-items:center;gap:11px;padding:7px 0}
  .ring-cycle{width:290px;height:270px} .concept-web{height:290px}
  .toc-grid{grid-template-columns:repeat(2,1fr)} .toc{padding:38px 18px}
  .counter{display:none} .ctrl{bottom:12px;right:12px}
}
/* chrome */
.chrome{position:fixed;inset:0;z-index:50;pointer-events:none}
.progress{position:absolute;top:0;left:0;height:3px;background:linear-gradient(90deg,var(--violet),var(--green));width:0;transition:width .45s var(--ease)}
.ctrl{position:absolute;bottom:20px;right:24px;display:flex;gap:8px;pointer-events:auto}
.ctrl button{width:39px;height:39px;border-radius:11px;border:1px solid rgba(255,255,255,.16);background:rgba(20,26,61,.62);
  color:#fff;backdrop-filter:blur(10px);cursor:pointer;font-size:15px;display:grid;place-items:center;transition:transform .15s,background .2s}
.ctrl button:hover{background:rgba(74,58,193,.7)} .ctrl button:active{transform:scale(.92)}
.ctrl button:focus-visible{outline:2px solid var(--green);outline-offset:2px}
.counter{position:absolute;bottom:28px;left:24px;font-weight:700;font-size:13px;letter-spacing:.1em;color:#fff;opacity:.6;
  font-variant-numeric:tabular-nums;background:rgba(20,26,61,.5);padding:7px 13px;border-radius:9px;backdrop-filter:blur(8px)}
.arrow-zone{position:fixed;top:0;bottom:0;width:13%;z-index:40;cursor:pointer}
.arrow-zone.left{left:0}.arrow-zone.right{right:0}
.toc{position:fixed;inset:0;z-index:60;background:rgba(8,10,28,.96);backdrop-filter:blur(14px);padding:48px 60px;overflow:auto;display:none}
.toc.open{display:block}
.toc h3{font-weight:800;font-size:13px;letter-spacing:.22em;text-transform:uppercase;color:#8b7df0;margin-bottom:18px}
.toc-grid{display:grid;grid-template-columns:repeat(6,1fr);gap:8px}
.toc-item{display:flex;flex-direction:column;gap:3px;padding:10px 12px;border-radius:10px;background:rgba(30,37,78,.7);
  border:1px solid rgba(255,255,255,.08);color:#fff;cursor:pointer;text-align:left;transition:transform .15s,border-color .2s}
.toc-item:hover{transform:translateY(-3px);border-color:#43d98f}
.toc-n{font-weight:800;font-size:15px;color:#43d98f} .toc-t{font-size:11px;color:#a9b2da;line-height:1.2}
.toc-close{position:absolute;top:24px;right:34px;font-size:22px;background:none;border:none;color:#fff;cursor:pointer}
@media (prefers-reduced-motion:reduce){
  .reveal{transition:none!important;opacity:1!important;transform:none!important}
}
"""

JS = r"""
const slides=[...document.querySelectorAll('.slide')];const total=slides.length;let cur=0;
const stage=document.querySelector('.stage'),progress=document.querySelector('.progress'),
counter=document.querySelector('.counter');
let mode=localStorage.getItem('aecode-s100-mode')||'mix';
const reduced=matchMedia('(prefers-reduced-motion:reduce)').matches;
function applyTheme(){slides.forEach(s=>{const b=s.dataset.base,e=mode==='mix'?b:mode;
  s.classList.toggle('is-dark',e==='dark');s.classList.toggle('is-light',e==='light');});}
const mob=()=>matchMedia('(max-width:860px)').matches;
function fit(){if(mob()){stage.style.transform='none';return;}
  stage.style.transform='scale('+Math.min(innerWidth/1280,innerHeight/720)+')';}
function go(n){n=Math.max(0,Math.min(total-1,n));slides[cur].classList.remove('active');cur=n;
  const s=slides[cur];s.classList.add('active');
  [...s.querySelectorAll('.reveal')].forEach((el,i)=>el.style.transitionDelay=(reduced?0:Math.min(i*45,560))+'ms');
  progress.style.width=((cur+1)/total*100)+'%';
  counter.textContent=String(cur+1).padStart(3,'0')+' / '+String(total).padStart(3,'0');
  if(mob())scrollTo(0,0);location.hash=cur+1;}
function next(){go(cur+1)}function prev(){go(cur-1)}
addEventListener('keydown',e=>{const k=e.key.toLowerCase();
  if(e.key==='ArrowRight'||e.key==='PageDown'||e.key===' '){e.preventDefault();next()}
  else if(e.key==='ArrowLeft'||e.key==='PageUp'){e.preventDefault();prev()}
  else if(e.key==='Home')go(0);else if(e.key==='End')go(total-1);
  else if(k==='t')cycleMode();else if(k==='f')toggleFs();else if(k==='o')toggleToc();
  else if(e.key==='Escape')document.querySelector('.toc').classList.remove('open');});
function cycleMode(){mode=mode==='mix'?'dark':mode==='dark'?'light':'mix';localStorage.setItem('aecode-s100-mode',mode);
  applyTheme();document.querySelector('#mode-ico').textContent=mode==='mix'?'◐':mode==='dark'?'●':'○';}
function toggleFs(){document.fullscreenElement?document.exitFullscreen():document.documentElement.requestFullscreen()}
function toggleToc(){document.querySelector('.toc').classList.toggle('open')}
document.querySelector('.left').onclick=prev;document.querySelector('.right').onclick=next;
document.querySelector('#btn-prev').onclick=prev;document.querySelector('#btn-next').onclick=next;
document.querySelector('#btn-mode').onclick=cycleMode;document.querySelector('#btn-fs').onclick=toggleFs;
document.querySelector('#btn-toc').onclick=toggleToc;document.querySelector('.toc-close').onclick=toggleToc;
document.querySelectorAll('.toc-item').forEach(b=>b.onclick=()=>{go(+b.dataset.go);toggleToc()});
let tx=0;addEventListener('touchstart',e=>tx=e.touches[0].clientX,{passive:true});
addEventListener('touchend',e=>{const dx=e.changedTouches[0].clientX-tx;if(Math.abs(dx)>50)dx<0?next():prev()});
addEventListener('resize',fit);applyTheme();fit();
go(Math.max(0,(parseInt(location.hash.slice(1))||1)-1));
document.querySelector('#mode-ico').textContent=mode==='mix'?'◐':mode==='dark'?'●':'○';
"""

HTML=f"""<!DOCTYPE html><html lang="es"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>100 Conceptos de Startup · AECODE</title>
<meta name="description" content="Guia visual de 100 conceptos de startup, de cero a experto. Cada concepto con como funciona, una analogia y un ejemplo real. Por AECODE.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<div class="deck"><div class="stage">{slides_html}</div></div>
<div class="chrome"><div class="progress"></div><div class="counter">001 / {total:03d}</div>
<div class="ctrl">
<button id="btn-toc" title="Indice (O)" aria-label="Indice">&#9776;</button>
<button id="btn-mode" title="Tema (T)" aria-label="Tema"><span id="mode-ico">&#9680;</span></button>
<button id="btn-prev" title="Anterior" aria-label="Anterior">&#8249;</button>
<button id="btn-next" title="Siguiente" aria-label="Siguiente">&#8250;</button>
<button id="btn-fs" title="Pantalla completa (F)" aria-label="Pantalla completa">&#9974;</button>
</div></div>
<div class="arrow-zone left"></div><div class="arrow-zone right"></div>
<div class="toc"><button class="toc-close" aria-label="Cerrar">&#10005;</button>
<h3>Indice &middot; {total} slides</h3><div class="toc-grid">{toc_items}</div></div>
<script>{JS}</script></body></html>"""

out=pathlib.Path(__file__).parent/"index.html"
out.write_text(HTML,encoding="utf-8")
print(f"OK -> {out} ({total} slides, {len(HTML):,} bytes)")
