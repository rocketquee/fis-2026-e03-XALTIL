import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon, Rectangle, Circle
from matplotlib.backends.backend_pdf import PdfPages

plt.rcParams["font.family"] = "DejaVu Sans"

W, H = 100, 100
LANE_HEADER = "#D9E2F3"
LANE_BODY = ["#F7F9FC", "#FFFFFF", "#F2F6FC"]
NODE = "#DEEAF6"
NODE_EDGE = "#2F5597"
DECISION = "#FFF2CC"
START = "#E2EFDA"


def lane(ax, y0, y1, label, color):
    ax.add_patch(Rectangle((1, y0), 98, y1 - y0, facecolor=color,
                           edgecolor="#7F7F7F", linewidth=1.0, zorder=0))
    ax.add_patch(Rectangle((1, y0), 12, y1 - y0, facecolor=LANE_HEADER,
                           edgecolor="#7F7F7F", linewidth=1.0, zorder=1))
    ax.text(7, (y0 + y1) / 2, label, ha="center", va="center", fontsize=9.5,
            fontweight="bold", color="#1F3864", wrap=True, zorder=2)


def box(ax, x, y, w, h, text, fc=NODE, fs=9):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                                boxstyle="round,pad=0.25,rounding_size=0.9",
                                facecolor=fc, edgecolor=NODE_EDGE, linewidth=1.1, zorder=3))
    ax.text(x, y, text, ha="center", va="center", fontsize=fs, color="#1F1F1F",
            zorder=4, linespacing=1.25)


def diamond(ax, x, y, w, h, text, fs=8.6):
    pts = [(x, y + h / 2), (x + w / 2, y), (x, y - h / 2), (x - w / 2, y)]
    ax.add_patch(Polygon(pts, closed=True, facecolor=DECISION, edgecolor=NODE_EDGE,
                         linewidth=1.1, zorder=3))
    ax.text(x, y, text, ha="center", va="center", fontsize=fs, zorder=4, linespacing=1.2)


def start(ax, x, y):
    ax.add_patch(Circle((x, y), 1.7, facecolor=START, edgecolor="#548235",
                        linewidth=1.3, zorder=3))


def end(ax, x, y):
    ax.add_patch(Circle((x, y), 2.0, facecolor="#404040", edgecolor="#000000",
                        linewidth=1.2, zorder=3))
    ax.add_patch(Circle((x, y), 2.9, facecolor="none", edgecolor="#404040",
                        linewidth=1.3, zorder=3))


def arrow(ax, p1, p2, label=None, lx=None, ly=None, rad=0.0, fs=8):
    ax.annotate("", xy=p2, xytext=p1,
                arrowprops=dict(arrowstyle="-|>", color="#404040", lw=1.2,
                                shrinkA=0, shrinkB=0,
                                connectionstyle=f"arc3,rad={rad}"),
                zorder=5)
    if label:
        ax.text(lx if lx is not None else (p1[0] + p2[0]) / 2,
                ly if ly is not None else (p1[1] + p2[1]) / 2,
                label, fontsize=fs, color="#404040", ha="center", va="center",
                bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.9),
                zorder=6)


def new_page(title):
    fig, ax = plt.subplots(figsize=(11.69, 8.27))
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.axis("off")
    ax.text(50, 96.5, title, ha="center", va="center", fontsize=17,
            fontweight="bold", color="#1F3864")
    ax.text(50, 93.2, "Proyecto XALTIL — Equipo Webtons",
            ha="center", va="center", fontsize=10, color="#595959")
    return fig, ax


with PdfPages("docs/U2/DIAGRAMAS .pdf") as pdf:
    # ---------------- TO-BE ----------------
    fig, ax = new_page("DIAGRAMA TO-BE (PROPUESTO)")
    lane(ax, 69, 91, "Paciente o familiar", LANE_BODY[0])
    lane(ax, 44, 68, "Personal de recepción\ny administrativo", LANE_BODY[1])
    lane(ax, 8, 43, "Sistema XALTIL", LANE_BODY[2])

    start(ax, 18, 84)
    box(ax, 33, 84, 17, 6.5, "Ingresa ubicación y\nespecialidad requerida")
    box(ax, 54, 84, 17, 6.5, "Consulta centros y\ncompara opciones")
    diamond(ax, 74, 84, 15, 10, "¿Hay disponibilidad\nadecuada?")
    box(ax, 74, 74, 15, 5.5, "Elige otro centro")
    box(ax, 90, 84, 12, 6.5, "Solicita turno\no cita", fs=8.4)
    box(ax, 90, 74, 12, 6.5, "Recibe\nconfirmación", fs=8.4)
    end(ax, 90, 70.5)

    box(ax, 30, 56, 21, 7, "Mantiene actualizados ocupación\ny disponibilidad del centro")
    box(ax, 70, 56, 20, 7, "Valida la solicitud y\nconfirma el cupo")

    box(ax, 22, 30, 17, 6.5, "Consolida datos\nde los centros")
    box(ax, 43, 30, 17, 6.5, "Calcula saturación,\nespera y traslado")
    box(ax, 64, 30, 17, 6.5, "Muestra centros,\nsaturación y tiempos")
    box(ax, 82, 19, 16, 6.5, "Verifica disponibilidad\nen tiempo real")
    box(ax, 60, 19, 15, 6.5, "Registra el turno\no cita")
    box(ax, 39, 19, 15, 6.5, "Envía confirmación\nal paciente")

    arrow(ax, (18, 85.7), (24.5, 85.7))
    arrow(ax, (41.5, 84), (45.5, 84))
    arrow(ax, (62.5, 84), (66.5, 84))
    arrow(ax, (74, 79), (74, 76.8), "No", 76.5, 77.9)
    arrow(ax, (81.5, 84), (84, 84), "Sí", 82.7, 85.1)
    arrow(ax, (90, 80.8), (90, 77.3))
    arrow(ax, (90, 70.7), (90, 68.7))

    # Retorno del centro alternativo
    arrow(ax, (66.5, 74), (54, 80.7), rad=0.25)

    # Datos del personal al sistema
    arrow(ax, (30, 52.5), (22, 33.3), "datos", 25.0, 42.5)
    # Resultados del sistema al paciente
    arrow(ax, (64, 33.3), (54, 80.7), "resultados", 61.0, 55.0)

    arrow(ax, (30.5, 30), (34.5, 30))
    arrow(ax, (51.5, 30), (55.5, 30))

    # Solicitud del paciente al sistema
    arrow(ax, (90, 70.7), (88, 22.3), "solicitud", 91.5, 46.0)
    # Verificación del sistema al personal
    arrow(ax, (82, 22.3), (74, 52.5), "disponibilidad", 80.0, 37.0)
    # Confirmación del personal al sistema
    arrow(ax, (70, 52.5), (63, 22.3), "confirmación", 64.0, 37.0)
    # Registro y confirmación al paciente
    arrow(ax, (67.5, 19), (52.5, 19))
    arrow(ax, (39, 22.3), (90, 70.7), "confirmación", 45.0, 56.0)

    pdf.savefig(fig, bbox_inches="tight")
    plt.close(fig)

    # ---------------- AS-IS ----------------
    fig, ax = new_page("DIAGRAMA AS-IS (SITUACIÓN ACTUAL)")
    lane(ax, 55, 91, "Paciente o familiar", LANE_BODY[0])
    lane(ax, 8, 54, "Personal de recepción", LANE_BODY[1])

    start(ax, 17, 84)
    box(ax, 33, 84, 18, 7, "Busca información en internet\no pregunta a conocidos")
    box(ax, 53, 84, 17, 7, "Llama por teléfono al\ncentro de salud")
    box(ax, 72, 84, 17, 7, "Se desplaza al centro\nde salud")
    box(ax, 90, 84, 12, 7, "Solicita atención\nen recepción", fs=8.2)
    box(ax, 72, 62, 17, 7, "Espera su turno")
    box(ax, 33, 62, 18, 7, "Busca otro centro\nde salud")
    end(ax, 90, 58.5)

    box(ax, 90, 43, 12, 7, "Recibe al\npaciente", fs=8.4)
    box(ax, 71, 43, 19, 7, "Verifica disponibilidad en el\nsistema interno del centro")
    diamond(ax, 49, 43, 16, 11, "¿Hay\ndisponibilidad?")
    box(ax, 27, 49, 18, 6.5, "Informa y asigna turno")
    box(ax, 27, 37, 18, 6.5, "Informa que no hay\ndisponibilidad")

    arrow(ax, (17, 85.7), (24, 85.7))
    arrow(ax, (42, 84), (44.5, 84))
    arrow(ax, (61.5, 84), (63.5, 84))
    arrow(ax, (80.5, 84), (84, 84))
    arrow(ax, (90, 80.5), (90, 46.8), "acude", 93.5, 63.5)
    arrow(ax, (84, 43), (80.5, 43))
    arrow(ax, (61.5, 43), (57, 43))
    arrow(ax, (41, 43), (36, 45.9), "Sí", 39.5, 45.5)
    arrow(ax, (41, 43), (36, 40.1), "No", 39.5, 39.5)
    arrow(ax, (27, 52.3), (72, 63.2), "turno asignado", 50.0, 60.5)
    arrow(ax, (72, 65.5), (72, 65.5))
    arrow(ax, (72, 62), (90, 60.5))
    arrow(ax, (27, 33.8), (33, 58.5), "reinicia", 24.0, 48.0)
    arrow(ax, (33, 65.5), (53, 80.5), "nuevo intento", 44.0, 75.0)

    pdf.savefig(fig, bbox_inches="tight")
    plt.close(fig)

print("PDF generado")
