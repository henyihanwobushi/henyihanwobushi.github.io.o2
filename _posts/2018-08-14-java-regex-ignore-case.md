---
layout: post
title: Java正则忽略大小写
date: 2018-08-14 19:44 +0800
tags: language
---

Java的正则表达式支持在正则中直接添加修饰符，以调整正则匹配的模式：
> You can add the mode modifiers to the start of the regex. To specify multiple modes, simply put them together as in (?ismx).
> * (?i) makes the regex case insensitive.
> * (?s) for "single line mode" makes the dot match all characters, including line breaks.
> * (?m) for "multi-line mode" makes the caret and dollar match at the start and end of each line in the subject string.
> <div style="text-align: right"> ——<a href="http://www.vogella.com/tutorials/JavaRegularExpressions/article.html#specifying-modes-inside-the-regular-expression">Regular expressions in Java - Tutorial</a></div>

常见的场景如：在SQL语句中对关键字的大小写并不敏感，匹配、替换时需注意：
* 判断语句中是否存在`limit`语法
```java
String sql = "select * from some_table limit 1000";
Boolean limited = sql.matches(".*(?i:limit) +[0-9]+.*");
```

* 对语句中的`limit`进行替换
```java
Integer defaultLimit = 10;
String sql = "select * from some_table limit 1000";
Boolean limited = sql.matches(".*(?i:limit) +[0-9]+.*");
if (limited) {
    sql = sql.replaceAll("(?i)limit +[0-9]+", String.format("limit %d", defaultLimit));
}
```