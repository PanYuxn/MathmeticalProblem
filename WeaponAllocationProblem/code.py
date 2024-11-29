'''
Author: PanYuxn
Email: shhspyx@163.com
Date: 2024-11-20 03:29:48
Description: 
'''
import coptpy
import pandas as pd
from coptpy import *

# Load the data from Excel files
df_zhandi = pd.read_csv('work/input/阵地信息.csv')
df_weapon = pd.read_csv('work/input/可用武器信息.csv')
df_efficiency = pd.read_csv('work/input/武器攻击效率.csv')
df_target = pd.read_csv('work/input/攻击目标信息.csv')

# Sets
K = df_zhandi['阵地类型'].unique()  # 阵地集合
I = df_weapon['武器类型'].unique()  # 武器集合
J = df_target['目标'].unique()  # 目标集合

# Parameters
a_i = df_weapon.set_index('武器类型')['可用数量'].to_dict()
w_i = df_weapon.set_index('武器类型')['使用成本'].to_dict()
v_j = df_target.set_index('目标')['目标价值'].to_dict()
d_j = df_target.set_index('目标')['防御系数'].to_dict()


class Para:
    def __init__(self):
        self.front_budget = 1000  # 阵地预算额度
        self.deploy_weapon_max_number = 10  # 阵地可部署武器个数上限


params = Para()
# Create a new model

env = coptpy.Envr()
model = env.createModel('Weapon_Allocation')
obj = LinExpr()

# Variables
# var1阵地k使用武器i攻击目标j的个数
y = model.addVars(K, I, J, vtype=COPT.INTEGER, nameprefix='y')
# var2 目标j是否被摧毁
destroyed = model.addVars(J, vtype=COPT.BINARY, nameprefix='destroyed')
# var3 阵地k部署武器i的个数
x = model.addVars(K, I, vtype=COPT.INTEGER, nameprefix='x')
# Objective functions
# obj1 - 最大化损伤价值
obj += quicksum(v_j[j] * destroyed[j] for j in J)

# # obj2 - 最小化部署费用
obj += -1 * (quicksum(x[k, i]*w_i[i] for k in K for i in I))

model.setObjective(obj, COPT.MAXIMIZE)
# Constraint1 - 目标摧毁约束
model.addConstrs(
    (sum(df_efficiency.set_index('武器类型').loc[i, j] * y[k, i, j] for i in I for k in K) >= d_j[j] * destroyed[j]
     for j in J),
    nameprefix='destroy'
)
# Constraint2 - 武器数量限制约束
model.addConstrs(
    (sum(y[k, i, j] for k in K for j in J) <= a_i[i] for i in I),
    nameprefix='weapon_limit'
)

# Constraint3 - 目标敏感约束
model.addConstr(destroyed[J[2]] + destroyed[J[4]] <= 1
                )

# Constraint4 - 阵地可部署武器上限
model.addConstrs(
    (sum(x[k, i] for i in I) <= params.deploy_weapon_max_number for k in K)
)

# Constraint5 - 阵地武器上限
model.addConstrs(
    (sum(y[k, i, j] for j in J) <= x[k, i] for k in K for i in I)
)

# Constraint6 - 成本预算约束
model.addConstrs(
    sum(x[k, i] for i in I) <= params.front_budget for k in K
)

# Optimize model
model.solve()

# Extract and display the results
solution_destroyed = {j: destroyed[j].X for j in J}
solution_weapon_allocation = {(k, i): x[k, i].X for k in K for i in I}

# Prepare data for output
df_destroyed = pd.DataFrame(list(solution_destroyed.items()), columns=['目标', '是否摧毁'])
df_weapon_allocation = pd.DataFrame(
    [(k, i, solution_weapon_allocation[k, i]) for k in K for i in I],
    columns=['阵地', '武器', '数量']
)

# Filter out rows where '数量' is 0
df_weapon_allocation = df_weapon_allocation[df_weapon_allocation['数量'] != 0]

# Save to CSV
df_destroyed.to_csv('work/output/攻击目标信息_结果.csv', index=False)
df_weapon_allocation.to_csv('work/output/阵地武器配备_结果.csv', index=False)
