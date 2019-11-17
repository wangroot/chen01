#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
from threading import Thread

import timeunit
import bs4
from selenium import webdriver
import re

dxAnswer = '''定价决策的基本目标不包括下列哪一项（贡献毛益总额最大）。
某企业生产需要甲材料，年需要量为100千克，如果自制，单位变动成本20元，而且需购买生产设备，每年发生专属固定费用2 000元；如果外购，单价为30元。企业应选择（外购）。
如果开发新产品需要增加专属固定成本，在决策时作为判断方案优劣的标准是各种产品的（剩余贡献毛益总额）。
剩余贡献毛益等于（贡献毛益总额-专属固定成本）。 
为了弥补生产能力不足的缺陷，增加有关装置、设备、工具等长期资产而发生的成本是（专属成本）。
下列情况中，亏损产品应该停产的条件是（亏损产品的贡献毛益小于零）。
新产品开发决策中，如果不追加专属成本，且生产经营能力不确定时，决策应采用的指标是（贡献毛益）。
在经营决策过程中，由于选取最优方案而放弃次优方案所丧失的潜在收益，也就是选择目前接受的方案所付出的代价，这是指（机会成本）。
在决策过程中，由于选取最优方案而放弃次优方案所丧失的潜在收益，也就是选择目前接受的方案所付出的代价的成本是（机会成本）。
在需求导向的定价策略中，对于弹性较小的产品，可以（制定较高的价格）。
差量成本也称为差别成本，形成成本差异的原因是（生产能力利用程度不同）。'''

dxAnswer = '''是按复利计算的某一特定金额在若干期后的本利和（ 复利终值 ）。
不考虑货币时间价值的项目评价指标是（平均报酬率）。
递延年金的特点是（没有第一期的支付额 ）。
某股票每年的股利为8元，若某人想长期持有，则其在股票价格为（80）时才愿意买？假设银行的存款利率为10%。
某人每年末将5000元资金存入银行作为孩子的教育基金，假定期限为10年，10%的年金现值系数为2.594，年金终值系数为15．937。到第10年末，可用于孩子教育资金额为（79685）元。
能使投资方案的净现值等于零的折现率是（内含报酬率 ）。
下列项目中，不属于现金流出项目的是（折旧费 ）。
现金流量中的各项税款是指企业在项目生产经营期依法缴纳的各项税款，其中不包括（ 增值税）。
在项目投资决策的现金流量分析中使用的“营运资本”是指（ 付现成本）。
在长期投资决策的评价指标中，哪个指标属于反指标（投资回收期 ）。
下列项目中哪个属于普通年金终值系数（F/A,i,n ）。'''



mulAnswer = '''定价策略的主要类型有（需求导向的定价策略; 利益导向的定价策略; 竞争导向的定价策略; 成本导向的定价策略）。 
定价决策的影响因素有（政策与法律的约束; 产品的市场生命周期; 供求关系; 产品的价值）。
关于变动成本加成定价，下列说法正确的有（成本加成率=贡献毛益÷变动成本; 单位价格=单位-单位变动成本。
某企业现有生产设备可用于甲、乙、丙三种产品的生产，相关资料如表所示。下列说法正确的有（乙丙两种产品的差别收入为162000元; 甲产品贡献毛益总额为160000元; 甲乙两种产品的差别利润为82000元 ）。
某企业现有用于新产品生产的剩余生产工时为3 000小时，有甲、乙、丙三种新产品可供投入生产，但由于剩余生产能力有限，公司只能选择一种产品进行生产。有关资料如下表所示，不需追加专属成本。下列说法中正确的有（该企业应生产丙产品; 生成丙产品可以获得利润7500元; 乙产品的贡献毛益总额为5250元; 甲产品的单位贡献毛益为70元）。
某企业新投产一种甲产品，预计年产销量1 000件，生产中耗用直接材料250 000元，直接工资50 000元，制造费用50 000元。经研究决定，在产品完全成本的基础上加成40%作为产品的目标售价。下列说法正确的是（单位甲产品的完全成本为350元; 甲产品的目标售价为490元）。
企业短期经营决策的特点有（是多种方案的选择; 有明确的目标; 着眼于未来）。
生产决策要解决的问题主要有三个，即（如何组织和实施生产 ; 利用现有生产能力生产什么产品; 各种产品的生产量是多少 ）。 
属于相关成本的是（付现成本; 重置成本; 专属成本; 机会成本）。
影响短期经营决策的因素主要包括（相关收入; 相关成本; 相关业务量 ）。'''

pdAnswer = '''边际收入是指业务量增加或减少一个单位所引起的收入变动。（对）
差量收入是指与特定决策方案相联系、能对决策产生重大影响、决策时必须予以充分考虑的收入。（错）
根据顾客的不同需求，区别对待，采用不同的定价方式，属于成本导向的定价策略。（错）
机会成本是指在决策过程中，由于选取最优方案而放弃次优方案所丧失的潜在收益，也就是选择目前接受的方案所付出的代价。（对）
跨国公司为了实现整体利益最大化，可以根据不同国家和地区在税率、汇率、外汇管制等方面的差异而采取不同的转移定价政策。这种定价策略属于竞争导向的定价策略。（错）
亏损产品满足单价大于其单位变动成本条件下时，就不应当停产。 （对）
相关成本分析法是指在备选方案收入相同的情况下，只分析各备选方案增加的固定成本和变动成本之和，采用这一方法必须是在备选方案业务量确定的条件下。（对）
相关业务量是指在短期经营决策中必须重视的，与特定决策方案相联系的产量或销量。（对）
以利益为导向的定价策略是根据企业追求利润最大化这一目标，采用不同的定价策略。（对）
在变动成本加成定价法下，成本加成率=贡献毛益÷变动成本。（对）
在新产品开发决策中，如果不追加专属成本时，决策方法可为利润总额比对法。（错）
专属成本是指明确归属于特定决策方案的固定成本。（对）
长期经营决策是对企业的生产经营决策方案进行经济分析。（错）'''


def getAnswerElement(elements, neirong):
    for ele in elements:
        if neirong in ele.text:
            return ele


def getAnswerElementEquals(elements, neirong):
    for ele in elements:
        if "A. " + neirong == ele.text or "B. " + neirong == ele.text or "C. " + neirong == ele.text or "D. " + neirong == ele.text:
            return ele


def danxuanAutoAnswer(answer, dxmap):
    split = answer.split("")
    for i in split:
        if len(i) < 2:
            continue
        i_split = i.split("（")
        dxmap[i_split[0].strip()] = i_split[1].split("）")[0].strip()
    return dxmap


def duoxuanAutoAnswer(answer, map):
    split = answer.split("")
    for i in split:
        if len(i) < 2:
            continue
        i_split = i.split("（")
        map[i_split[0].strip()] = i_split[1].split("）")[0].strip().split("; ")
    return map


def pdAutoAnswer(answer, list):
    split = answer.split("")
    for i in split:
        if len(i) < 2:
            continue
        if '错' in i.split("（")[1]:
            list.append(i.split("（")[0])
    return list


def regexDanxuan(answer,map):
    answer.replace("(","（")
    answer.replace(")","）")
    match = re.match('(.*?)（(.*?)）', answer, re.M | re.I)
    print(match.group())


# print(danxuanAutoAnswer(dxAnswer,{}))

dxAnswer = '''31.对
     32.错 
     33.对
      34.错 
      35.错
       36.对
        37.错
         38.对 
         39.错
          40.对'''
print(dxAnswer)
split = dxAnswer.split("\n")
for i in split:
    print(i.strip().split(".")[1])
