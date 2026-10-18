import os
import json
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from google import genai
from google.genai import types
from fastmcp import FastMCP

from app.workspace_store import RyzeWorkspaceStore
from app.ryze_intel_watcher import RyzeContinuousWatcher

app = FastAPI(title="ArgonMarketer AI — Replica Exacta Mejorada de Ryze AI", version="3.0.0")
store = RyzeWorkspaceStore()
watcher = RyzeContinuousWatcher()

mcp = FastMCP("ArgonMarketer-MCP")

@mcp.tool()
def list_ryze_chats_and_tasks() -> str:
    """Devuelve todos los chats estratégicos y las tareas pendientes de aprobación del agente autónomo."""
    return json.dumps({"chats": store.chats, "agent_tasks": store.agent_tasks, "kpis": store.kpis}, indent=2)

@mcp.tool()
def approve_or_decline_agent_task(task_id: str, decision: str = "APPROVED") -> str:
    """Aprueba (APPROVED) o declina (DECLINED) una tarea del agente autónomo."""
    res = store.decide_task(task_id, decision)
    return json.dumps(res, indent=2)

@mcp.tool()
def sync_ryze_documentation_updates() -> str:
    """Escanea la documentación y changelog de Ryze AI con Gemini 4 Argon y extrae nuevas mejoras."""
    return json.dumps(watcher.sync_latest_ryze_capabilities(), indent=2)

app.mount("/mcp", mcp.http_app())


def ask_gemini_4_argon(prompt: str, thinking_level: str = "medium") -> str:
    api_key = os.getenv("GEMINI_API_KEY", "")
    model_id = os.getenv("GEMINI_MODEL", "gemini-4-argon")
    if not api_key:
        return (
            "⚡ **[Modo Local Activo — Configura `GEMINI_API_KEY` en Cloud Run o `.env` para conectar en vivo a `gemini-4-argon`]**\n\n"
            f"He analizado tu solicitud: *\"{prompt[:120]}\"* para **Enfermera en Estados Unidos (`eeeu`)**.\n"
            "1. **Diagnóstico**: Oportunidad detectada en el embudo de conversión y agendamiento de Calendly.\n"
            "2. **Acción Autónoma Creada**: He enviado la propuesta de optimización a tu pestaña **Agent tasks** para que la apruebes o declines en 1 clic."
        )
    client = genai.Client(api_key=api_key)
    sys_inst = (
        "Eres el AI Marketer de ArgonMarketer (superando a Ryze AI), operando con gemini-4-argon para "
        "Christian Gonzalez en sus empresas 'Enfermera en Estados Unidos' y 'Rnnclex'. "
        "Dominas Google Ads, Meta Ads, SEO técnico, GEO (/llms.txt, citaciones IA), optimización de asistencia en Calendly, "
        "recuperación de inasistentes (no-shows), conversión post-sesión informativa y financiamiento de programas. "
        "Da respuestas accionables con métricas concretas y propón tareas ejecutables."
    )
    response = client.models.generate_content(
        model=model_id,
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=sys_inst,
            thinking_config=types.ThinkingConfig(thinking_level=thinking_level),
            tools=[types.Tool(google_search=types.GoogleSearch())],
        ),
    )
    return response.text


class NewChatReq(BaseModel):
    title: str
    message: str
    workspace_id: str = "eeeu"

class MessageReq(BaseModel):
    message: str

class TaskDecisionReq(BaseModel):
    decision: str # APPROVED | DECLINED | PENDING

class CreateTaskReq(BaseModel):
    title: str
    category: str
    description: str
    impact: str


@app.get("/api/state")
async def get_full_state():
    return {
        "workspaces": store.workspaces,
        "chats": store.chats,
        "agent_tasks": store.agent_tasks,
        "notifications": store.notifications,
        "schedules": store.schedules,
        "integrations": store.integrations,
        "kpis": store.kpis,
        "model": os.getenv("GEMINI_MODEL", "gemini-4-argon"),
    }

@app.post("/api/chats")
async def create_new_chat(req: NewChatReq):
    reply = ask_gemini_4_argon(req.message, thinking_level="medium")
    return store.create_chat(req.title, req.message, reply, req.workspace_id)

@app.post("/api/chats/{chat_id}/messages")
async def send_chat_message(chat_id: str, req: MessageReq):
    try:
        reply = ask_gemini_4_argon(req.message, thinking_level="medium")
        return store.add_message(chat_id, req.message, reply)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.post("/api/tasks/{task_id}/decide")
async def decide_agent_task(task_id: str, req: TaskDecisionReq):
    try:
        return store.decide_task(task_id, req.decision)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.post("/api/tasks")
async def create_custom_task(req: CreateTaskReq):
    new_t = {
        "id": f"task-{len(store.agent_tasks)+101}",
        "workspace_id": "eeeu",
        "agent": "Argon Autonomous Agent",
        "category": req.category,
        "title": req.title,
        "description": req.description,
        "impact": req.impact,
        "status": "PENDING",
        "created_ago": "Just now"
    }
    store.agent_tasks.insert(0, new_t)
    return new_t

@app.post("/api/ryze-watcher/sync")
async def sync_ryze_updates():
    report = watcher.sync_latest_ryze_capabilities()
    store.notifications.insert(0, {
        "id": "notif-sync",
        "title": "Ryze AI Docs & Changelog Sincronizados",
        "body": "Gemini 4 Argon analizó las últimas mejoras de Ryze AI y actualizó las reglas del motor.",
        "time": "Just now",
        "unread": True
    })
    return report

@app.get("/", response_class=HTMLResponse)
async def serve_ryze_ui():
    with open("app/static/index.html", "r", encoding="utf-8") as f:
        return f.read()
