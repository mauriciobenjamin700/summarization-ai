import re
from typing import Any, Callable, Optional

from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama, OllamaLLM
from langgraph.graph.state import CompiledStateGraph
from langgraph.prebuilt import create_react_agent
from pydantic import BaseModel

from src.core.settings import settings


class AIHandler:
    def __init__(self) -> None:
        self.__model = OllamaLLM(model=settings.AI_MODEL)

    def invoke(
        self, template: ChatPromptTemplate, params: dict[str, Any]
    ) -> str:
        """
        Generate a response from the AI model using the provided template
        and parameters.
        """
        prompt_input = template.format(**params)
        response = self.__model.invoke(prompt_input)
        return response

    def summarize(
        self, history: list[dict[str, Any]], echo: bool = False
    ) -> str:
        """
        Summarize the provided chat history.
        """

        chat_history = self.__format_chat_to_llm(history)

        template = self.__summarize_prompt()
        params = {"chat_history": chat_history}
        output = self.invoke(template, params)
        if echo:
            print(self.__extract_think_tag(output))
        return self.__clean_think_tag(output)

    def create_agent(
        self,
        tools: list[Callable[..., Any]],
        response_format: Optional[BaseModel] = None,
    ) -> CompiledStateGraph[Any]:
        return create_react_agent(
            ChatOllama(model=settings.AI_MODEL),
            tools=tools,
            response_format=response_format,
        )

    def execute_agent(
        self, agent: CompiledStateGraph[Any], messages: list[dict[str, Any]]
    ):
        return agent.invoke({"messages": messages})

    def get_agent_structured_response_by_chat(
        self, agent: CompiledStateGraph[Any], messages: list[dict[str, Any]]
    ) -> Optional[BaseModel]:
        messages.append(
            {
                "role": "system",
                "content": """
                You are an AI assistant that provides structured responses 
                based on the conversation history.

                Always provide a concise summary of the key points discussed.
            """,
            }
        )
        return self.execute_agent(agent, messages)["structured_response"]

    def get_structured_response_by_text(
        self, agent: CompiledStateGraph[Any], text: str
    ) -> Optional[BaseModel]:
        messages = [
            {
                "role": "system",
                "content": """
                You are an expert in building structured outputs by 
                summarizing data.""",
            },
            {"role": "user", "content": text},
        ]
        return self.execute_agent(agent, messages)["structured_response"]

    def show_graph(self, agent: CompiledStateGraph[Any]):
        png_data = agent.get_graph().draw_mermaid_png()
        with open("graph.png", "wb") as f:
            f.write(png_data)

    def __extract_think_tag(self, text: str) -> str:
        """
        Extract only the content inside <think>...</think> tags.
        """
        match = re.search(r"<think>(.*?)</think>", text, flags=re.DOTALL)
        return match.group(1).strip() if match else ""

    def __clean_think_tag(self, text: str) -> str:
        """
        Remove <think>...</think> tags and their content from the AI output.
        """
        return re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()

    def __summarize_prompt(self) -> ChatPromptTemplate:
        messages = [
            ("system", "You are a assistant expert in summarization."),
            (
                "user",
                """
                Summarize the following conversation in PT-BR
                with a concise paragraph: 
             
                <conversation>
                {chat_history}
                </conversation>
            """,
            ),
        ]
        return ChatPromptTemplate.from_messages(messages)

    def __format_chat_to_llm(self, chat: list[dict[str, Any]]) -> str:
        """
        Format chat history into a string for LLM input.
        """
        formatted_chat = ""
        for message in chat:
            role = message.get("role", "user")
            content = message.get("content", "")
            formatted_chat += f"{role}: {content}\n"
        return formatted_chat.strip()
