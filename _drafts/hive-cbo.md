---
layout: post
title: Cost-based optimization in Hive
---

# 简介

用户提交的 *SQL* 会被Hive转换为物理操作树，而物理操作树会转换为Tez任务，并且在Hadoop集群中执行。在Hadoop集群中执行的分布式的SQL，对数据中间结果的处理，与普遍的查询引擎不同，Hive查询的结果经常需要对中间结果进行排序、聚合，这些操作都会涉及shuffle操作。

现存的所有的优化器的目的都是以最小化shuffle的消耗。目前用户会通过对join中的表进行排序来进行查询的优化。逻辑优化器可以采用的的优化方案仅限于：
* filter push down
* projection pruning
* partition pruning
CBO可以显著的提升hive的查询效率，

Join重排序和join算法选择是CBO优化的少数场景。CBO会自动的进行优化，不需要用户在进行join排序或指定join算法。

Hive采用calcite作为查询计划优化器以及query执行框架。calcite目前有超过50个的优化规则，对执行树进行调整。并且拥有高效的计划剪枝器，可以选择一个优化方案。

基于 *Calcite* 的CBO在 *hive* 的执行中为阶段性的引入, 在第一阶段： *Calcite* 被用于对.*Calcite* 的顺序进行重排序。

# 介绍

*Hive* 是基于 *Hadoop* 的数仓基础设施，*Hive* 依赖 *Hadoop* 的横向扩展能力