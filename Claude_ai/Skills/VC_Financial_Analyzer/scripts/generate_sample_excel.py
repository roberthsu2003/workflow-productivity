import pandas as pd
import numpy as np
import os

def generate_sample_financials(output_path="sample_startup_financials.xlsx"):
    # 設定隨機種子以固定數據
    np.random.seed(42)
    
    # 1. 損益表 (Income Statement / P&L) - 近 12 個月 (2025/01 - 2025/12)
    months = pd.date_range(start="2025-01-01", periods=12, freq="MS").strftime("%Y-%m")
    
    # 模擬 ARR / MRR 成長數據 (新創 SaaS + 訂閱制情境)
    mrr = np.array([50000, 54000, 59000, 65000, 72000, 80000, 89000, 98000, 108000, 119000, 130000, 142000])
    services_revenue = np.random.randint(5000, 15000, size=12)
    total_revenue = mrr + services_revenue
    
    cogs = (total_revenue * 0.22).astype(int) # 毛利率約 78%
    gross_profit = total_revenue - cogs
    
    # 營業費用
    r_and_d = (total_revenue * 0.40 + np.random.randint(2000, 5000, size=12)).astype(int)
    s_and_m = (total_revenue * 0.45 + np.random.randint(3000, 8000, size=12)).astype(int)
    g_and_a = np.full(12, 15000)
    total_opex = r_and_d + s_and_m + g_and_a
    
    ebitda = gross_profit - total_opex
    
    df_pnl = pd.DataFrame({
        "月份 (Month)": months,
        "訂閱收入 (MRR)": mrr,
        "專案/專業服務收入": services_revenue,
        "總營收 (Total Revenue)": total_revenue,
        "營業成本 (COGS)": cogs,
        "營業毛利 (Gross Profit)": gross_profit,
        "研發費用 (R&D)": r_and_d,
        "行銷與業務費用 (S&M)": s_and_m,
        "管理費用 (G&A)": g_and_a,
        "總營業費用 (Total OpEx)": total_opex,
        "營業利潤/損益 (EBITDA)": ebitda
    })
    
    # 2. 現金流量與 Runway (Cash Flow & Runway)
    starting_cash = 1500000 # 初始現金 150萬 USD
    cash_balance = []
    net_burn = []
    
    curr_cash = starting_cash
    for i in range(12):
        burn = abs(ebitda[i]) if ebitda[i] < 0 else 0
        curr_cash = curr_cash + ebitda[i] # ebitda 為負時扣減
        cash_balance.append(curr_cash)
        net_burn.append(burn)
        
    df_cash = pd.DataFrame({
        "月份 (Month)": months,
        "期初現金 (Beginning Cash)": [starting_cash] + cash_balance[:-1],
        "淨現金流出/淨燒錢 (Net Burn)": net_burn,
        "期末現金餘額 (Ending Cash)": cash_balance,
        "預估可營運月數 (Runway Months)": [round(cash_balance[i] / max(net_burn[i], 1), 1) for i in range(12)]
    })
    
    # 3. 營運與客戶指標 (KPIs & Cohort)
    active_customers = [120, 132, 145, 160, 178, 195, 215, 238, 260, 285, 310, 340]
    new_customers = [15, 16, 17, 20, 22, 23, 25, 28, 29, 31, 32, 36]
    churned_customers = [3, 4, 4, 5, 4, 6, 5, 5, 7, 6, 7, 6]
    arpu = [round(mrr[i] / active_customers[i], 1) for i in range(12)]
    
    df_kpi = pd.DataFrame({
        "月份 (Month)": months,
        "活躍客戶數 (Active Customers)": active_customers,
        "本月新進客戶 (New Customers)": new_customers,
        "流失客戶數 (Churned Customers)": churned_customers,
        "平均客單價 ARPU (USD)": arpu,
        "客戶流失率 Churn Rate (%)": [round(churned_customers[i] / active_customers[i] * 100, 2) for i in range(12)],
        "淨營收留存率 NDR (%)": [102, 104, 105, 103, 106, 108, 107, 109, 110, 112, 111, 114]
    })
    
    # 寫入 Excel 檔案
    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        df_pnl.to_excel(writer, sheet_name="損益表 P&L", index=False)
        df_cash.to_excel(writer, sheet_name="現金流與 Runway", index=False)
        df_kpi.to_excel(writer, sheet_name="營運指標 KPIs", index=False)
        
    print(f"✅ 成功生成創投測試財報 Excel 檔案：{output_path}")

if __name__ == "__main__":
    generate_sample_financials()
