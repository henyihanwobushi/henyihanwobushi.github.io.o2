SELECT `channel` AS `channel`, sum(`plan_downpayment_money`) AS `sum([plan_downpayment_money])
_1`,max(`real_downpayment_money`) AS `max([real_downpayment_money])_2`,round(`plan_month_payment_money`,2) AS `round([plan_month_payment_money],2)_3` FROM `dw_innovative_order_driv
er_order_detail` GROUP BY `channel` limit 1000