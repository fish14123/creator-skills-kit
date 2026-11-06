# Creator Skills Kit（创作者工具包）

一组可在 Cursor 等 Agent 环境中使用的创作 Skill：从选题到标题、长文结构、事实核查、发布后复盘，再到多平台分发草稿。

开源的是**方法与模板**，不是懒笔头会员知识库正文。

## 包含的 Skill

| Skill | 用途 |
|-------|------|
| `creator-topic-evaluator` | 评估选题是否值得投入，并给出现在写 / 补材料 / 暂缓 |
| `creator-title-optimizer` | 生成、诊断并筛选标题，避免无法兑现的承诺 |
| `creator-longform-structure` | 把零散材料组织成公众号长文结构与大纲 |
| `creator-fact-checker` | 建立主张台账，做资料研究与事实核查 |
| `creator-content-review` | 复盘发布后数据，提出可验证的下一轮实验 |
| `creator-distribution-kit` | 把成稿改写成多平台发布**草稿**（不代发） |

## 安装与使用

1. 将 `skills/` 下需要的目录拷到你的 Agent skills 目录（或按各 `SKILL.md` 的说明引用）。
2. 在对话里说明要用哪个 Skill，并按其中工作流与 `assets/` 模板执行。
3. 事实核查与分发类 Skill：**不编造**来源、案例或数据；分发 Skill **不会**替你自动发布。

## 边界

- 不代发、不登录你的社交账号发帖。
- 找不到可靠依据时，应删除、降格表述或标明不确定，而不是补假引用。
- MIT 许可只覆盖本仓库文件；不覆盖任何付费知识库内容。

## 进阶：懒笔头会员知识库（引流）

若你需要持续维护的作者写作参考库（在腾讯 IMA 中使用），可了解：

**懒笔头 · 公众号写作助手（会员版）**  
https://ima.qq.com/wiki/?shareId=5ca82565e36f0fd30a6c66aa2349a438e5c2f0328b8ec9b9435298917544ae52

宣传海报（含订阅二维码）：[`assets/ima-member-poster-with-qr.png`](assets/ima-member-poster-with-qr.png)

会员库按腾讯 IMA / 商品条款提供，**不受本仓库 MIT 覆盖**。开源工具包与付费知识库是两件分开的事。

## 许可

MIT License — 见 [LICENSE](LICENSE)。更多说明见 [NOTICE.md](NOTICE.md)。
