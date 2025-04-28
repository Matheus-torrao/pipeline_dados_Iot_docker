# pipeline_dados_Iot_docker #


 Enunciado:
Criar um pipeline de dados que processa leituras de temperatura de
dispositivos IoT e armazena em um banco de dados PostgreSQL utilizando Docker.

Etapas do Pipeline:
 - Geração de Dados: Sensores IoT (ou simulação) enviam leituras de temperatura.
 - Processamento & Armazenamento: Python recebe os dados e os insere no PostgreSQL.
 - Visualização: Streamlit para visualização e analise dos dados.

Tecnologias Utilizadas:
  - PostgreSQL (armazenamento)
  - Docker (Container para aplicação )
  - Python + SQLAlchemy (processamento e ingestão)
  - Streamlit (Visualização dos dados)
  - Biblioteca Os (Para leitura dos arquivos)
  - Poetry (Para gerenciar dependencias )

Conclusão:
O desenvolvimento de um pipeline de dados para processar leituras de temperatura de dispositivos IoT e armazená-las em um banco de dados PostgreSQL utilizando Docker demonstrou a importância da integração eficiente entre sensores, comunicação, processamento e persistência de dados. A implementação permitiu a coleta, transformação e armazenamento contínuo das informações, garantindo confiabilidade e escalabilidade para futuras expansões.
Além disso, o uso do Docker para o banco de dados trouxe vantagens como isolamento do ambiente, facilidade de implantação e portabilidade, simplificando o gerenciamento da infraestrutura. A solução desenvolvida abre espaço para aprimoramentos, como a inclusão de monitoramento em tempo real, a visualização dos dados para melhor tomada de decisão





