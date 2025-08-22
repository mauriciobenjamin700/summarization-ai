from datetime import datetime

mock_chats = [
    {
        "id": "7a1f9d20-4a38-4b2b-9c36-30d9687b0f4e",
        "user_id": "4f6a1c22-8b3e-4d5b-9f10-0a1b2c3d4e5f",
        "role": "user",
        "content": "Poderia resumir este artigo sobre IA?",
        "created_at": datetime(2025, 8, 21, 14, 0, 0),
    },
    {
        "id": "0b5b8e1e-3d1a-4c77-a7b3-0c6f2b91d9ab",
        "user_id": "4f6a1c22-8b3e-4d5b-9f10-0a1b2c3d4e5f",
        "role": "assistant",
        "content": """
        Claro. Envie o texto ou o link e direi os pontos principais.
        """,
        "created_at": datetime(2025, 8, 21, 14, 1, 0),
    },
    {
        "id": "c3e2a4b7-58c2-4d1f-9d32-2f4a9b1c7e8d",
        "user_id": "4f6a1c22-8b3e-4d5b-9f10-0a1b2c3d4e5f",
        "role": "user",
        "content": "Segue o texto. Foque em objetivos, métodos e resultados.",
        "created_at": datetime(2025, 8, 21, 14, 2, 0),
    },
    {
        "id": "f1a7c9e2-0d44-4b9b-85e1-3a2c7d6e5f90",
        "user_id": "4f6a1c22-8b3e-4d5b-9f10-0a1b2c3d4e5f",
        "role": "assistant",
        "content": """
        Resumo: O artigo propõe um modelo leve, 
        avalia em 3 benchmarks e obtém ganho de 7%.
        """,
        "created_at": datetime(2025, 8, 21, 14, 3, 0),
    },
    {
        "id": "9d8c7b6a-5e4d-43c2-91f0-1a2b3c4d5e6f",
        "user_id": "1e2d3c4b-5a6f-4789-9b0c-1d2e3f4a5b6c",
        "role": "user",
        "content": "Gere 3 ações recomendadas com base no resumo.",
        "created_at": datetime(2025, 8, 21, 14, 4, 0),
    },
    {
        "id": "2a3b4c5d-6e7f-48a9-9b0c-1d2e3f4a5b6c",
        "user_id": "1e2d3c4b-5a6f-4789-9b0c-1d2e3f4a5b6c",
        "role": "assistant",
        "content": """Ações: 
        1) Criar POC; 
        2) Comparar custos; 
        3) Planejar testes adicionais.
        """,
        "created_at": datetime(2025, 8, 21, 14, 5, 0),
    },
]
