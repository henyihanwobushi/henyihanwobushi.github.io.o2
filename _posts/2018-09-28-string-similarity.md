---
layout: post
title: 字符串相似度计算
date: 2018-09-28 01:02 +0800
---

字符串相似度是一个非常有意思的问题，之前没有仔细考虑过这个问题，只是项目有一个相关的需求，场景比较局限，解决的方案也不叫*hack*，尚未验证效果，但应该能满足当下的场景的需求。本文并不打算做一个全面的关于相似度匹配的综述，只是提供一个使用特定场景的简单方案。
具体业务场景就不做还原了，数据基本是两组字符串，字符串之前期望是相同，亦或者略有差异，差异较大则为异常数据，需要将差异较大的数据筛选出来。如：

| id | origin | target
| ---|--------|-------
| 1  | abcdef | abcdef
| 2  | qwerty | qwerry
| 3  | abcdef | qwerty

> 其中1、2属于正常数据，3则为异常数据

简单检索了一下，比较匹配的算法是编辑距离算法，编辑距离算法的基本思路是将两个字符串分别作为原始字符串和目标字符串，相互对比，计算从原始字符串需要经过多少次编辑（插入、替换、删除）能够得到目标字符串。
比较直接的思路是用递归算法，可以用动态规划优化，这里直接给出编辑距离计算的代码：
```
public static Integer distance(String a, String b) {
    if (a.length() == 0) {
        return b.length();
    }
    if (b.length() == 0) {
        return a.length();
    }

    int[][] distance = new int[a.length() + 1][b.length() + 1];
    int i, j;

    for (i = 0; i <= a.length(); i++) {
        distance[i][0] = i;
    }
    for (j = 0; j <= b.length(); j++) {
        distance[0][j] = j;
    }

    for (i = 0; i < a.length(); i++) {
        for (j = 0; j < b.length(); j++) {
            if (a.charAt(i) == b.charAt(j)) {
                distance[i + 1][j + 1] = distance[i][j];
            } else {
                distance[i + 1][j + 1] = Math.min(distance[i][j + 1], Math.min(distance[i + 1][j], distance[i][j])) + 1;
            }
        }
    }
    return distance[a.length()][b.length()];
}
```
编辑距离算法比较简单，算法的核心在于在字符不相等的情况下如何计算当前的编辑距离。编辑距离的思路比较简单，也可以清晰的解释结果的含义，但是与字符串长度相关性不高，在数据中字符串长度差异较大的场景下，需要将编辑距离与字符串长度综合考虑。比较合理的方法是：
```
public static Double si(String a, String b) {
    Integer d = distance(a, b);
    return 1. - (d * 1.0) / (a.length() + b.length());
}
```
计算比较简单，但是在某些边界条件下对比会产生值，比较诡异，如两个完全不相同的字符串匹配：`"abcd"`, `"qwer"`，相似度达到`0.5`，当然为了更加合理的匹配可以给距离乘2，又会在`""`与`"abcd"`这种场景下发生异常（结果为`-1`）。

为了计算更合理的相似度，转变思路，从编辑距离的反方向入手，以原字符串向目标字符串编辑的过程中保留的字符的长度为依据，综合考虑保留字符在两个字符串之间所占比例的，得到相似度，代码如下：
```
public static Double similarity(String a, String b) {
    if (a == null || b == null) {
        return null;
    }
    if (a.equals(b)) {
        return 1.;
    }
    if (a.length() == 0 || b.length() == 0) {
        return 0.;
    }

    Integer m = match(a, b);
    return 1. * (m * m) / (a.length() * b.length());
}

private static Integer match(String a, String b) {
    int[][] match = new int[a.length() + 1][b.length() + 1];

    for (int i = 0; i < a.length(); i++) {
        for (int j = 0; j < b.length(); j++) {
            if (a.charAt(i) == b.charAt(j)) {
                match[i + 1][j + 1] = match[i][j] + 1;
            } else {
                match[i + 1][j + 1] = Math.max(match[i][j], Math.max(match[i + 1][j], match[i][j + 1]));
            }
        }
    }
    return match[a.length()][b.length()];
}
```
> 此处对两个字符串的相似度进行相乘，其实也可以进行平均，相乘的方法对字符串中的异常值处罚力度更大，数据相似度普遍较高的情况下，结果的区分度更高。

