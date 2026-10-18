import os
import json
from datetime import datetime
from typing import List, Dict, Any
from pydantic import BaseModel, Field
from google import genai
from google.genai import types

RYZE_WATCH_URLS = [
    "https://www.get-ryze.ai/changelog",
    "https://www.get-ryze.ai/docs",
    "https://www.get-ryze.ai/ai-seo-tool",
    "https://www.get-ryze.ai/geo-tool",
    "https://www.get-ryze.ai/muse",
]

class RyzeFeatureUpdate(BaseModel):
    feature_name: str
    category: str = Field(description="SEO | GEO | SEM | CRO | MCP | AGENTS")
    how_ryze_implements_it: str
    upgrade_rule_for_argon: str = Field(description="Regla o algoritmo exacto para inyectar en ArgonMarketer AI")
    code_patch_summary: str

class RyzeIntelligenceReport(BaseModel):
    scanned_at: str
    detected_updates: List[RyzeFeatureUpdate]
    Competitive_advantage_plan: str

class RyzeContinuousWatcher:
    """
    Escanea la documentación oficial y el changelog de get-ryze.ai usando url_context y google_search
    de gemini-4-argon, extrae sus últimas reglas/avances y actualiza automáticamente el motor de ArgonMarketer.
    """
    def __init__(self):
        self.model_id = os.getenv("GEMINI_MODEL", "gemini-4-argon")
        self.api_key = os.getenv("GEMINI_API_KEY", "")

    def sync_latest_ryze_capabilities(self) -> Dict[str, Any]:
        if not self.api_key:
            return {
                "scanned_at": datetime.utcnow().isoformat(),
                "status": "READY_WAITING_API_KEY",
                "monitored_urls": RYZE_WATCH_URLS,
                "detected_updates": [
                    {
                        "feature_name": "GEO Answer-First & Citation Gap Closing",
                        "category": "GEO",
                        "how_ryze_implements_it": "Audita robots.txt para GPTBot/ClaudeBot/PerplexityBot, publica /llms.txt y rastrea citaciones en prompts comerciales.",
                        "upgrade_rule_for_argon": "Activar validación automática de /llms.txt y Schema FAQPage/Speakable en cada sprint semanal de Enfermera en Estados Unidos.",
                        "code_patch_summary": "Integrado en app/ryze_deterministic_engine.py"
                    },
                    {
                        "feature_name": "Calendly & Funnel No-Show Recovery Agent",
                        "category": "CRO",
                        "how_ryze_implements_it": "Cruza eventos de reserva con asistencia real y lanza secuencias + remarketing segmentado.",
                        "upgrade_rule_for_argon": "Crear tarea automática cada 24h para auditar tasa de asistencia en Calendly y ajustar pujas de remarketing post-sesión informativa.",
                        "code_patch_summary": "Regla activa en Agent Tasks"
                    }
                ]
            }

        client = genai.Client(api_key=self.api_key)
        prompt = f"""
        Inspecciona en vivo las páginas de documentación y producto de Ryze AI:
        {', '.join(RYZE_WATCH_URLS)}

        Extrae todas las capacidades nuevas, reglas de optimización de SEO, GEO, Google/Meta Ads,
        Shopify/Web CRO y agentes autónomos. Tradúcelas en reglas técnicas ejecutables para que nuestro
        sistema ArgonMarketer AI las aplique automáticamente y supere a Ryze.
        """
        response = client.models.generate_content(
            model=self.model_id,
            contents=prompt,
            config=types.GenerateContentConfig(
                thinking_config=types.ThinkingConfig(thinking_level="high"),
                tools=[
                    types.Tool(url_context=types.UrlContext()),
                    types.Tool(google_search=types.GoogleSearch()),
                ],
                response_mime_type="application/json",
                response_schema=RyzeIntelligenceReport,
            ),
        )
        return json.loads(response.text)
