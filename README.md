# 📈 AI Financial Analyst Agent

Bu proje, **Phidata** framework'ü ve **Groq (Llama 3.3)** modelini kullanarak geliştirilmiş otonom bir finansal analiz asistanıdır. Birden fazla yapay zeka ajanının (Multi-Agent) iş birliğiyle çalışarak, hisse senedi verilerini teknik ve temel analizle birleştirir, aynı zamanda internetteki güncel haberleri tarayarak kapsamlı raporlar sunar.

## 🚀 Özellikler

* **Çoklu Ajan Mimarisi:** Web Arama Ajanı ve Finans Ajanı'nın koordineli çalışması.
* **Canlı Finansal Veriler:** `YFinance` entegrasyonu ile anlık hisse fiyatları, analist tavsiyeleri ve şirket bilançoları.
* **Web Araması:** `DuckDuckGo` entegrasyonu ile şirket hakkındaki en güncel haberler.
* **Yüksek Performans:** Groq API üzerinden Llama 3.3 modeli ile ışık hızında çıkarım (inference).
* **Görsel Arayüz (Playground):** Ajanları test etmek ve etkileşime girmek için kullanıcı dostu web arayüzü.

## 🛠️ Teknolojiler

* **Python**
* **Phidata** (Agent Orchestration)
* **Groq API** (LLM Provider - Llama 3.3 Versatile)
* **YFinance** (Financial Data Tools)
* **DuckDuckGo** (Web Search Tools)
* **FastAPI** (Playground UI Backend)
