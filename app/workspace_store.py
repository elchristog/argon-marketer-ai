import uuid
from datetime import datetime
from typing import Dict, Any, List

class RyzeWorkspaceStore:
    def __init__(self):
        self.workspaces = [
            {
                "id": "eeeu",
                "name": "Enfermera en Estados Unidos",
                "slug": "enfermeraenestadosunidos/eeeu",
                "domain": "https://enfermeraenestadosunidos.com",
                "connected_integrations": 7,
            },
            {
                "id": "rnnclex",
                "name": "Rnnclex Academy",
                "slug": "rnnclex/main",
                "domain": "https://rnnclex.com",
                "connected_integrations": 7,
            }
        ]
        # Tus 7 chats reales que aparecen en tu captura de reports.get-ryze.ai
        self.chats: List[Dict[str, Any]] = [
            {
                "id": "chat-1",
                "workspace_id": "eeeu",
                "title": "1-Asistencia Calendly",
                "updated_ago": "26m ago",
                "category": "CRO & Funnel",
                "messages": [
                    {"role": "user", "text": "Analiza cómo subir la tasa de asistencia a las sesiones agendadas en Calendly para Enfermera en Estados Unidos."},
                    {"role": "assistant", "text": "He analizado el embudo de Calendly de Enfermera en Estados Unidos:\n1. **Recordatorio WhatsApp + SMS a las 24h, 3h y 15 min antes** con micro-video de caso de éxito de enfermera homologada (+18% asistencia estimada).\n2. **Página de confirmación interactiva**: incluir diagnóstico rápido de requisitos (CES / CGFNS / NCLEX) antes de la llamada para elevar el compromiso.\n3. He creado una tarea autónoma en **Agent tasks** para activar la audiencia de recordatorio en Meta Ads a quienes agendan y no abren el correo."}
                ]
            },
            {
                "id": "chat-2",
                "workspace_id": "eeeu",
                "title": "0-webapp",
                "updated_ago": "22h ago",
                "category": "Web App & CRO",
                "messages": [
                    {"role": "user", "text": "Revisa la arquitectura SEO/CRO de nuestra webapp y detecta fricciones de conversión."},
                    {"role": "assistant", "text": "Auditoría de WebApp completada con Gemini 4 Argon:\n- **Velocidad y Core Web Vitals**: optimizar carga inicial del bloque hero.\n- **GEO & Schema**: falta inyectar `Course` y `FAQPage` JSON-LD en las rutas principales.\n- Tienes el cambio listo para aprobar en 1 clic en la pestaña **Agent tasks**."}
                ]
            },
            {
                "id": "chat-3",
                "workspace_id": "eeeu",
                "title": "0 - SEO y Linkbuilding",
                "updated_ago": "1d ago",
                "category": "SEO & GEO",
                "messages": [
                    {"role": "user", "text": "Estructura el plan continuo de SEO programático, GEO (/llms.txt) y Linkbuilding para dominar búsquedas de enfermería en EE.UU."},
                    {"role": "assistant", "text": "Plan SEO & GEO activo:\n- **Striking Distance (Posición 4 a 15)**: 14 keywords listas para subir a Top 3.\n- **/llms.txt y /robots.txt**: configurados para permitir GPTBot, ClaudeBot, PerplexityBot y Google-Extended.\n- **Gap Closing**: identificadas 9 páginas donde citan a competidores para lanzar outreach automático."}
                ]
            },
            {
                "id": "chat-4",
                "workspace_id": "eeeu",
                "title": "0-SEM",
                "updated_ago": "2d ago",
                "category": "Google & Meta Ads",
                "messages": [
                    {"role": "user", "text": "Audita las campañas de Google Search y Meta Ads para cortar gasto desperdiciado y escalar ROAS."},
                    {"role": "assistant", "text": "Auditoría SEM en vivo:\n- **Wasted Spend detectado**: $640/mes en términos informacionales ('trabajos sin papeles', 'examen gratis pdf') y horarios de madrugada (11pm–6am).\n- Revisa **Agent tasks** para aprobar las 23 palabras clave negativas exactas y el ajuste de Dayparting."}
                ]
            },
            {
                "id": "chat-5",
                "workspace_id": "eeeu",
                "title": "2-Estrategia para convertir inasistentes en asistentes",
                "updated_ago": "2d ago",
                "category": "Retention & Remarketing",
                "messages": [
                    {"role": "user", "text": "Diseña un flujo automatizado para recuperar a las enfermeras que agendaron sesión pero no asistieron (no-shows)."},
                    {"role": "assistant", "text": "Estrategia Anti No-Show desplegada:\n1. Disparo automático a los 15 minutos de inasistencia con enlace de reagendamiento prioritario en 1 clic.\n2. Secuencia de 3 días mostrando cómo otras enfermeras latinas superaron el bloqueo del inglés y del CGFNS.\n3. Exclusión automática en Ads una vez que reagendan."}
                ]
            },
            {
                "id": "chat-6",
                "workspace_id": "eeeu",
                "title": "3-Estrategia de conversión post sesión informativa",
                "updated_ago": "5d ago",
                "category": "Sales Closing",
                "messages": [
                    {"role": "user", "text": "¿Cómo aceleramos el cierre de matrícula en las 72 horas posteriores a la sesión informativa?"},
                    {"role": "assistant", "text": "Para maximizar cierres en las primeras 72h post-sesión:\n- Anuncio dinámico en Meta/Instagram exclusivo para asistentes mostrando casos reales de aprobación NCLEX y desglose de retorno de inversión salarial en EE.UU.\n- Landing personalizada post-sesión con preguntas frecuentes de contrato y tiempos de trámite."}
                ]
            },
            {
                "id": "chat-7",
                "workspace_id": "eeeu",
                "title": "4-Soluciones de financiamiento para programas de enfermería",
                "updated_ago": "21d ago",
                "category": "Offer & Pricing CRO",
                "messages": [
                    {"role": "user", "text": "Estructurar opciones de pago y financiamiento claras para eliminar la objeción de precio en el programa."},
                    {"role": "assistant", "text": "Se diseñó la calculadora interactiva de cuotas vs. salario de Registered Nurse (RN) en EE.UU. para inyectar en la página de checkout y reducir el abandono de carrito en un 28%."}
                ]
            }
        ]

        # Cola de Tareas del Agente Autónomo (Approve / Decline / Undo)
        self.agent_tasks: List[Dict[str, Any]] = [
            {
                "id": "task-101",
                "workspace_id": "eeeu",
                "agent": "SEM Autonomous Agent",
                "category": "Google Ads · Keywords",
                "title": "Añadir 28 palabras clave negativas exactas ('gratis', 'pdf', 'foro') en Search",
                "description": "Detectados $480/mes en clics sin conversión en los últimos 30 días. Confianza del modelo: 97%.",
                "impact": "+$480/mes ahorrados · +0.4x ROAS",
                "status": "PENDING",
                "created_ago": "14m ago"
            },
            {
                "id": "task-102",
                "workspace_id": "eeeu",
                "agent": "CRO & Calendly Agent",
                "category": "Meta Ads + Calendly",
                "title": "Activar audiencia de recuperación automática de inasistentes (No-Shows últimos 14d)",
                "description": "Sincroniza eventos de inasistencia en Calendly con campaña de revinculación post-sesión informativa.",
                "impact": "+19 sesiones recuperadas/mes · CPA $14",
                "status": "PENDING",
                "created_ago": "38m ago"
            },
            {
                "id": "task-103",
                "workspace_id": "eeeu",
                "agent": "SEO & GEO Agent",
                "category": "GitHub WebApp · Technical GEO",
                "title": "Publicar /llms.txt actualizado + Schema FAQPage en rutas de homologación y NCLEX",
                "description": "Pasa el Quality Gate (94% unicidad, Lighthouse 96). Incrementa citaciones en ChatGPT, Gemini y Perplexity.",
                "impact": "+34% AI Citation Share estimado",
                "status": "PENDING",
                "created_ago": "1h ago"
            },
            {
                "id": "task-104",
                "workspace_id": "eeeu",
                "agent": "Dayparting & Budget Agent",
                "category": "Google & Meta Ads · Schedule",
                "title": "Reducir pujas nocturnas (11:30pm – 5:30am EST) un 80% y reasignar a 9am–8pm",
                "description": "El 93% de los agendamientos efectivos en Calendly ocurren entre 9am y 8pm EST.",
                "impact": "+$310/mes reasignados a horas pico",
                "status": "PENDING",
                "created_ago": "2h ago"
            },
            {
                "id": "task-105",
                "workspace_id": "eeeu",
                "agent": "A/B Testing Agent",
                "category": "WebApp CRO · Experiment",
                "title": "Lanzar Test A/B en página post-sesión informativa (Calculadora de Financiamiento visible above-the-fold)",
                "description": "Basado en el chat '4-Soluciones de financiamiento'. Evalúa incremento en tasa de matrícula durante 7 días con Auto-Rollback.",
                "impact": "+22% CVR proyectado",
                "status": "PENDING",
                "created_ago": "3h ago"
            }
        ]

        self.notifications: List[Dict[str, Any]] = [
            {"id": "notif-1", "title": "Auditoría Autónoma Completada", "body": "El agente detectó 5 nuevas optimizaciones listas para tu aprobación en Enfermera en Estados Unidos.", "time": "14m ago", "unread": True},
            {"id": "notif-2", "title": "Ryze Docs & Changelog Sync", "body": "Sincronizadas las últimas reglas de GEO (/llms.txt y Citation Tracking) con Gemini 4 Argon.", "time": "1h ago", "unread": True},
            {"id": "notif-3", "title": "Alerta de Asistencia Calendly", "body": "El segmento de recordatorio 3h antes subió la asistencia un +14% esta semana.", "time": "4h ago", "unread": False}
        ]

        self.schedules: List[Dict[str, Any]] = [
            {"id": "sch-1", "name": "Auditoría Diaria Google & Meta Ads (Wasted Spend + Negativas)", "cron": "Todos los días · 06:00 AM EST", "status": "ACTIVE", "agent": "SEM Agent"},
            {"id": "sch-2", "name": "Escaneo Search Console (Posición 4-15 & CTR < 2%) + Auto-PR GitHub", "cron": "Todos los días · 07:00 AM EST", "status": "ACTIVE", "agent": "SEO & GEO Agent"},
            {"id": "sch-3", "name": "Evaluador Evergreen 72h (Verifica ROAS/CVR y ejecuta Auto-Rollback si cae)", "cron": "Cada 6 horas", "status": "ACTIVE", "agent": "Evergreen Judge"},
            {"id": "sch-4", "name": "Sincronización de Documentación y Nuevas Funciones de Ryze AI", "cron": "Lunes y Jueves · 08:00 AM EST", "status": "ACTIVE", "agent": "Ryze Intel Watcher"}
        ]

        self.integrations: List[Dict[str, Any]] = [
            {"name": "Google Ads", "status": "Connected", "account": "Enfermera en USA (Search & PMax)", "icon": "🎯"},
            {"name": "Meta Ads", "status": "Connected", "account": "EE.UU. & LatAm Prospecting + Retargeting", "icon": "📣"},
            {"name": "Google Search Console", "status": "Connected", "account": "enfermeraenestadosunidos.com & rnnclex.com", "icon": "🔍"},
            {"name": "Google Analytics 4", "status": "Connected", "account": "GA4 Funnel & Calendly Events", "icon": "📊"},
            {"name": "GitHub WebApp Repo", "status": "Connected", "account": "Auto-Commits SEO/CRO & Auto-Rollback", "icon": "💻"},
            {"name": "Calendly", "status": "Connected", "account": "Sesiones Informativas & Asistencia", "icon": "📅"},
            {"name": "BigQuery Evergreen Memory", "status": "Connected", "account": "Action Ledger & Learned Playbooks", "icon": "🧠"}
        ]

        self.kpis = {
            "spend": 12450,
            "roas": 4.2,
            "conversions": 508,
            "conv_rate": 3.6,
            "clicks": 14200,
            "ctr": 3.8,
            "wasted_spend_recoverable": 1440,
            "seo_striking_keywords": 18,
            "geo_citation_score": 88
        }

    def create_chat(self, title: str, first_message: str, reply: str, workspace_id: str = "eeeu") -> Dict[str, Any]:
        new_chat = {
            "id": f"chat-{uuid.uuid4().hex[:6]}",
            "workspace_id": workspace_id,
            "title": title,
            "updated_ago": "Just now",
            "category": "AI Marketer",
            "messages": [
                {"role": "user", "text": first_message},
                {"role": "assistant", "text": reply}
            ]
        }
        self.chats.insert(0, new_chat)
        return new_chat

    def add_message(self, chat_id: str, user_text: str, reply_text: str) -> Dict[str, Any]:
        for c in self.chats:
            if c["id"] == chat_id:
                c["messages"].append({"role": "user", "text": user_text})
                c["messages"].append({"role": "assistant", "text": reply_text})
                c["updated_ago"] = "Just now"
                return c
        raise ValueError("Chat not found")

    def decide_task(self, task_id: str, decision: str) -> Dict[str, Any]:
        for t in self.agent_tasks:
            if t["id"] == task_id:
                t["status"] = decision.upper() # APPROVED | DECLINED | PENDING
                if decision.upper() == "APPROVED":
                    self.kpis["roas"] = round(self.kpis["roas"] + 0.15, 2)
                    self.kpis["wasted_spend_recoverable"] = max(0, self.kpis["wasted_spend_recoverable"] - 300)
                    self.notifications.insert(0, {
                        "id": f"notif-{uuid.uuid4().hex[:5]}",
                        "title": f"Cambio Ejecutado: {t['title'][:45]}...",
                        "body": f"Aprobado por Christian Gonzalez. El Evaluador Evergreen auditará el impacto real en 72h.",
                        "time": "Just now",
                        "unread": True
                    })
                return t
        raise ValueError("Task not found")
