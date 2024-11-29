
|                  **Set**                  |                   |
| :---------------------------------------: | ----------------- |
|                     I                     | 武器集合              |
|                     J                     | 目标集合              |
|                     K                     | 阵地集合              |
|                 **Para**                  |                   |
|                 $$a_{i}$$                 | 武器库内可使用武器数量信息     |
|                $$s_{ij}$$                 | 不同武器对不同目标的攻击效率    |
|                 $$v_{j}$$                 | 不同目标的战略价值         |
|                 $$d_{j}$$                 | 不同目标的防御强度         |
|                $$w_{ki}$$                 | 阵地使用武器的成本         |
|                 $$m_{k}$$                 | 某阵地可使用的武器上限       |
|               **Variable**                |                   |
| $$y_{kij},\forall k \in K,i\in I,j\in J$$ | 某阵地使用某类型武器攻击目标的个数 |
|         $$y_{j},\forall j \in J$$         | 某目标是否被摧毁          |
|    $$x_{ki},\forall i \in I,k \in K$$     | 某阵地部署武器的个数        |

**目标函数：**
obj1 - 最大化目标的战略价值
$$\sum_{j\in J}v_{j}y_{j}$$
obj2 - 最小化部署费用
$$\sum_{k\in K}\sum_{i\in I}x_{ki}w_{ki}$$
**约束条件：**
cons1 - 目标摧毁约束：判断对应目标是否被摧毁
$$\sum_{i\in I}(s_{ij}\sum_{k \in K}y_{kij})\ge d_{j}y_{j},\forall j\in J$$
cons2 - 武器数量限制约束：部署的武器类型不能大于武器库武器上限
$$\sum_{k\in K}\sum_{j \in J}y_{kij}\le a_{i},\forall i \in I$$
cons3 - 目标敏感约束：由于目标3和目标5关系连接紧密，不可同时被摧毁。
$$y_{3}+y_{5} \le 1$$

cons4 - 预算约束：使用的所有机器不能超过预算金额
$$\sum_{i\in I}(\sum_{j\in J}\sum_{k\in K}y_{kij}\cdot w_{ki})\le Budget$$
cons5 - 阵地部署上限：每个阵地由于区域限制，需要限制武器部署数量
$$\sum_{i\in I}x_{ki}\le m_{k},\forall k\in K$$
cons6 - 阵地武器上限：阵地使用的武器数量不能多于分配的武器数量
$$\sum_{j \in J}y_{kij}\le x_{ki},\forall k \in K$$


## **相关关系**

|  **变量**  |                                                                             | 含义                              | 是否必选 | 对应Line行 | 关系行 |
| :------: | :-------------------------------------------------------------------------- | ------------------------------- | ---- | ------- | --- |
|   var1   | $$y_{kij},\forall k \in K,i\in I,j\in J$$                                   | 某阵地使用某类型武器攻击目标的个数               | 是    | line1   |     |
|   var2   | $$y_{j},\forall j \in J$$                                                   | 某目标是否被摧毁                        | 是    | line2   |     |
|   var3   | $$x_{ki},\forall i \in I,k \in K$$                                          | 某阵地部署武器的个数                      | 是    | line3   |     |
|  **目标**  |                                                                             |                                 |      |         |     |
|   obj1   | $$\sum_{j\in J}v_{j}y_{j}$$                                                 | 最大化目标的战略价值                      | 是    | line5   |     |
|   obj2   | $$\sum_{k\in K}\sum_{i\in I}x_{ki}w_{ki}$$                                  | 最1小化部署费用                        | 是    | line6   |     |
| **约束条件** |                                                                             |                                 |      |         |     |
|  cons1   | $$\sum_{i\in I}(s_{ij}\sum_{k \in K}y_{kij})\ge d_{j}y_{j},\forall j\in J$$ | 目标摧毁约束：判断对应目标是否被摧毁              | 是    | line7   |     |
|  cons2   | $$\sum_{k\in K}\sum_{j \in J}y_{kij}\le a_{i},\forall i \in I$$             | 武器数量限制约束：部署的武器类型不能大于武器库武器上限     | 是    | line8   |     |
|  cons3   | $$y_{3}+y_{5} \le 1$$                                                       | 目标敏感约束：由于目标3和目标5关系连接紧密，不可同时被摧毁。 | 是    | line9   |     |
|  cons4   | $$\sum_{i\in I}(\sum_{j\in J}\sum_{k\in K}y_{kij}\cdot w_{ki})\le Budget$$  | 预算约束：使用的所有机器不能超过预算金额            |      |         |     |
|  cons5   | $$\sum_{i\in I}x_{ki}\le m_{k},\forall k\in K$$                             | 阵地部署上限：每个阵地由于区域限制，需要限制武器部署数量    | 是    | line10  |     |
|  cons6   | $$\sum_{j \in J}y_{kij}\le x_{ki},\forall k \in K$$                         | 阵地武器上限：阵地使用的武器数量不能多于分配的武器数量     | 是    | line11  |     |
|          |                                                                             |                                 |      |         |     |
|          |                                                                             |                                 |      |         |     |
