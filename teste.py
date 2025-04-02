from chatbot.agent.agent import AgentContrato


question = 'fale sobre contrato'

agent = AgentContrato()
response = agent.run(question)
print(response)