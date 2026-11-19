# Estado da revisão acadêmica

Atualizado em 19 de novembro de 2026.

## Repositório

- Branch de trabalho: `ai-branch`.
- A branch local estava sincronizada com `origin/ai-branch` antes da criação deste registro.
- `documento.pdf` permanece modificado localmente e não foi incluído nos commits.
- As skills em `.codex/` foram incluídas no repositório e enviadas ao remoto.

## Revisão da introdução

A revisão interativa começou pela introdução de `2-textuais/1-introducao.tex`. Foram apresentadas 15 propostas editoriais, todas aprovadas e aplicadas individualmente. As alterações cobrem:

- o parágrafo de abertura e a motivação sobre previsão econômica;
- a passagem sobre escassez e a distinção entre microeconomia e macroeconomia;
- a transição para a discussão de Keynes e incerteza;
- a redação sobre decisões, sistemas de informação e big data;
- a apresentação de estudos que empregam VAR, ARIMA, DFM, MIDAS e ensemble stacking;
- a formulação da relação entre especificações lineares, relações não lineares e técnicas de IA.

A última proposta foi reformulada após discussão científica. A redação final delimita a observação às formulações usuais, reconhece que elas podem ter dificuldade para captar relações não lineares em determinados contextos e descreve técnicas de IA flexíveis como uma possibilidade de inovação, sem afirmar superioridade universal.

O usuário pediu que a revisão fosse interrompida depois dessa etapa. Portanto, o restante da introdução ainda precisa de revisão interativa, incluindo o parágrafo que começa com “Diante do disso”. Nenhum trecho adicional foi alterado sem aprovação.

## Observações científicas discutidas

“Modelos tradicionais” não é sinônimo de “modelos lineares”: há extensões econométricas não lineares, e algumas técnicas de aprendizado de máquina são lineares. As especificações usuais de VAR, ARIMA, DFM e MIDAS podem representar relações lineares; a capacidade de capturar não linearidades depende da especificação concreta. A literatura consultada aponta que ganhos de métodos não lineares variam conforme o contexto e o horizonte de previsão.

Fontes consultadas para essa avaliação:

- Goulet Coulombe et al., “How is Machine Learning Useful for Macroeconomic Forecasting?”, *Journal of Applied Econometrics*: <https://onlinelibrary.wiley.com/doi/10.1002/jae.2910>
- “Nowcasting GDP using machine learning methods”, *AStA Advances in Statistical Analysis*: <https://link.springer.com/article/10.1007/s10182-024-00515-0>

Essas fontes foram usadas para a avaliação conceitual na conversa. Nenhuma nova referência foi acrescentada ao arquivo `.bib`.

## Controle de versão e verificações

- `c21f64b` — `Revise introducao da monografia`: alterações aprovadas na introdução.
- `f34fafc` — `Adiciona skills locais do Codex`: inclusão dos arquivos `.codex/`.
- Ambos os commits foram enviados para `origin/ai-branch`.
- O diff da introdução foi revisado e os comandos LaTeX e chamadas bibliográficas dos trechos editados foram preservados.
- `git diff --check` não apontou problemas no diff preparado para os commits.
- A monografia não foi compilada.
- Nenhum commit foi feito em `main`, e não houve merge ou reset.

## Próxima etapa

Retomar a revisão interativa da introdução a partir do parágrafo iniciado por “Diante do disso”, apresentando uma proposta por vez e aguardando a decisão do autor antes de editar.
