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
    # Novo chat: suporte de manutenção de internet em casa
    {
        "id": "a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d",
        "user_id": "9f8e7d6c-5b4a-3c2d-9e0f-a1b2c3d4e5f6",
        "role": "user",
        "content": """Olá, minha internet de casa está oscilando e 
        caindo toda hora. Preciso de suporte para manutenção. Pode me orientar?
        """,
        "created_at": datetime(2025, 8, 21, 14, 6, 0),
    },
    {
        "id": "d5c4b3a2-1f0e-9d8c-7b6a-5f4e3d2c1b0a",
        "user_id": "9f8e7d6c-5b4a-3c2d-9e0f-a1b2c3d4e5f6",
        "role": "assistant",
        "content": """
        Claro! Siga estes passos:
        1) Verifique cabos e luzes do modem/roteador;
        2) Reinicie os equipamentos por 30s;
        3) Teste via cabo e rode um speedtest;
        4) Veja o histórico de quedas no modem;
        5) Se persistir, informe operadora, modelo do roteador e 
        horário das quedas para abrir chamado.
        """,
        "created_at": datetime(2025, 8, 21, 14, 7, 0),
    },
    {
        "id": "e7f6d5c4-b3a2-4190-8d7c-6e5f4d3c2b1a",
        "user_id": "9f8e7d6c-5b4a-3c2d-9e0f-a1b2c3d4e5f6",
        "role": "user",
        "content": """
        Escolhi a opção 2 (reiniciar modem/roteador por 30s) e deu certo: 
        a conexão estabilizou. Suporte concluído com sucesso, obrigado!""",
        "created_at": datetime(2025, 8, 21, 14, 7, 30),
    },
    # Novo chat: apenas indicações de filmes
    {
        "id": "11223344-5566-7788-99aa-bbccddeeff00",
        "user_id": "0a1b2c3d-4e5f-6789-abcd-ef0123456789",
        "role": "user",
        "content": """
        Quero apenas indicações de filmes para hoje à noite. 
        Curto ficção científica e suspense.
        """,
        "created_at": datetime(2025, 8, 21, 14, 8, 0),
    },
    {
        "id": "00ffeedd-ccbb-aabb-8877-665544332211",
        "user_id": "0a1b2c3d-4e5f-6789-abcd-ef0123456789",
        "role": "assistant",
        "content": """
        Sugestões: Ex Machina (2014), Arrival (2016), Blade Runner 2049 (2017), 
        Annihilation (2018), 
        Prisoners (2013).
        """,
        "created_at": datetime(2025, 8, 21, 14, 9, 0),
    },
]
