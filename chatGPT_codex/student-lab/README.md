# 學生實作區

這裡提供可離線重現的完整練習專案。請不要直接在教材原檔上操作；先建立自己的副本：

```bash
cp -R chatGPT_codex/student-lab/tideflow-portal /tmp/tideflow-portal-lab
cd /tmp/tideflow-portal-lab
./scripts/bootstrap.sh
npm test
```

`bootstrap.sh` 只會在副本內初始化 Git，並建立基準 commit。完成後可依序練習：

1. [Quickstart](../Quickstart/README.md)
2. [Tasks](../Tasks/README.md)
3. [Agent Configuration](../Agent_Configuration/README.md)
4. [GitHub PR Review](../Connectors/03_GitHub/02_PR_Review/README.md)
5. [Parallel Worktrees](../Workspaces/Examples/01_Parallel_Worktrees/README.md)
6. [Weekly Ops Brief](../Automations/Examples/01_Weekly_Ops_Brief/README.md)

卡關時先看 [學生除錯手冊](../Troubleshooting/README.md)；完成後再對照 [參考答案](../Answer_Key/README.md)。

← [返回教材首頁](../README.md)
