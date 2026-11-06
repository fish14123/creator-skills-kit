# Creator Skills Kit（创作者工具包）

一组可在 Cursor / 兼容 Agent 中使用的创作 Skill，覆盖选题评估、标题优化、长文结构、事实核查、内容复盘，以及多平台分发草稿。

开源的是**工具方法与模板**，不是「懒笔头」会员知识库正文。

## 包含的 Skill

| Skill | 简介 |
| --- | --- |
| `creator-topic-evaluator` | 评估公众号、视频或知识内容选题是否值得投入，适用于选题、素材碎片、热点想法，或规划选题库与优先级。 |
| `creator-title-optimizer` | 为公众号技术、效率和创作类文章生成、诊断和筛选标题；兼顾打开率与技术词准确性。 |
| `creator-longform-structure` | 将零散观察、访谈、案例或研究材料组织成适合公众号的长文结构与大纲。 |
| `creator-fact-checker` | 为 AI、工具、平台规则、数据与案例类内容做资料研究和事实核查，建立主张台账。 |
| `creator-content-review` | 复盘发布后表现，识别可验证的下一轮改进假设，避免凭单篇波动下结论。 |
| `creator-distribution-kit` | 将已完成文章改写为不同平台的发布草稿，保留观点、事实边界与真实表达。 |

## 安装与使用

1. 把 `skills/` 下需要的目录拷到你自己的 Agent skills 目录（或按各环境的 Skill 安装方式放置）。
2. 打开对应目录中的 `SKILL.md`，按其中的工作流使用；模板在各 Skill 的 `assets/`，细则在 `references/`。
3. 也可只复制某一个 Skill，不必整包安装。

## 边界（请先读）

- **不代发**：分发类 Skill 只生成草稿与清单，不会代替你在任何平台发布。
- **不编造事实**：核查与写作流程要求删除、降格或标明不确定内容；不得用虚构引用补空缺。
- **开源范围**：本仓 MIT 仅覆盖本仓库文件中的工具方法与模板，**不是**懒笔头会员知识库正文。

更多说明见 [NOTICE.md](./NOTICE.md)。

## 进阶：懒笔头公众号写作助手 · 会员版（腾讯 IMA）

若你需要更完整的写作方法、案例与持续更新的会员知识库，可了解：

- 链接：https://ima.qq.com/wiki/?shareId=5ca82565e36f0fd30a6c66aa2349a438e5c2f0328b8ec9b9435298917544ae52
- 宣传海报（扫码订阅）：[`assets/ima-member-poster-with-qr.png`](./assets/ima-member-poster-with-qr.png)

**说明**：会员库内容与订阅按腾讯 IMA / 商品条款执行，**不受**本仓 MIT 许可覆盖。

## 许可

[MIT](./LICENSE) © 2026 Teng Dai / 懒笔头
