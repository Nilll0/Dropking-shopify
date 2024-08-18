from top.taolord.shopify.business import ReadAllOrders, ReadLegalPolicies, ReadLocations, ReadMerchantApprovalSignals, \
    ReadProductListings, ReadShopifyPaymentsDisputes, ReadShopifyPaymentsPayouts, ReadUsers, WritePaymentSessions, \
    ReadAssignedFulfillmentOrders, WriteAssignedFulfillmentOrders, ReadCheckouts, WriteCheckouts, ReadCustomers, \
    WriteCustomers, ReadDiscounts, WriteDiscounts, ReadFulfillments, WriteFulfillments, ReadInventory, WriteInventory, \
    ReadLocales, WriteLocales, ReadMarketingEvents, WriteMarketingEvents, ReadOrderEdits, WriteOrderEdits, ReadOrders, \
    ReadPaymentMandate, WritePaymentMandate, ReadPaymentGateways, ReadPriceRules, WritePriceRules, ReadProducts, \
    WriteProducts, ReadPublications, WritePublications, ReadPurchaseOptions, WritePurchaseOptions, ReadReturns, \
    WriteReturns, ReadShipping, WriteShipping, ReadOwnSubscriptionContracts, WriteOwnSubscriptionContracts, ReadThemes, \
    WriteThemes, ReadThirdPartyFulfillmentOrders, WriteThirdPartyFulfillmentOrders, ReadTranslations, WriteTranslations

SHOP_NAME = 'ht-shop-api'
API_VERSION = '2023-04'
ACCESS_TOKEN = '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'

# 实例化所有权限类
read_all_orders = ReadAllOrders(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
read_legal_policies = ReadLegalPolicies(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
read_locations = ReadLocations(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
read_merchant_approval_signals = ReadMerchantApprovalSignals(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
read_product_listings = ReadProductListings(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
read_shopify_payments_disputes = ReadShopifyPaymentsDisputes(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
read_shopify_payments_payouts = ReadShopifyPaymentsPayouts(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
read_users = ReadUsers(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
write_payment_sessions = WritePaymentSessions(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
read_assigned_fulfillment_orders = ReadAssignedFulfillmentOrders(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
write_assigned_fulfillment_orders = WriteAssignedFulfillmentOrders(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
read_checkouts = ReadCheckouts(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
write_checkouts = WriteCheckouts(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
read_customers = ReadCustomers(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
write_customers = WriteCustomers(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
read_discounts = ReadDiscounts(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
write_discounts = WriteDiscounts(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
read_fulfillments = ReadFulfillments(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
write_fulfillments = WriteFulfillments(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
read_inventory = ReadInventory(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
write_inventory = WriteInventory(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
read_locales = ReadLocales(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
write_locales = WriteLocales(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
read_marketing_events = ReadMarketingEvents(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
write_marketing_events = WriteMarketingEvents(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
read_order_edits = ReadOrderEdits(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
write_order_edits = WriteOrderEdits(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
read_orders = ReadOrders(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
read_payment_mandate = ReadPaymentMandate(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
write_payment_mandate = WritePaymentMandate(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
read_payment_gateways = ReadPaymentGateways(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
read_price_rules = ReadPriceRules(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
write_price_rules = WritePriceRules(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
read_products = ReadProducts(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
write_products = WriteProducts(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
read_publications = ReadPublications(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
write_publications = WritePublications(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
read_purchase_options = ReadPurchaseOptions(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
write_purchase_options = WritePurchaseOptions(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
read_returns = ReadReturns(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
write_returns = WriteReturns(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
read_shipping = ReadShipping(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
write_shipping = WriteShipping(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
read_own_subscription_contracts = ReadOwnSubscriptionContracts(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
write_own_subscription_contracts = WriteOwnSubscriptionContracts(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
read_themes = ReadThemes(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
write_themes = WriteThemes(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
read_third_party_fulfillment_orders = ReadThirdPartyFulfillmentOrders(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
write_third_party_fulfillment_orders = WriteThirdPartyFulfillmentOrders(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
read_translations = ReadTranslations(SHOP_NAME, API_VERSION, ACCESS_TOKEN)
write_translations = WriteTranslations(SHOP_NAME, API_VERSION, ACCESS_TOKEN)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("")
    print_hi('PyCharm')
"""
所有相关订单，而不是过去 60 天内创建的订单的默认窗口所需权限
配送订单资源分配给您的配送服务管理的位置
结帐
客户和保存的搜索
GraphQL 管理 API 折扣功能
履行服务
库存水平和库存物料
管理 API 商店政策
GraphQL Admin API Shop Locale
位置
营销活动
商户审批信号
放弃的结账、客户、履行、订单和交易资源
付款授权
价格规则
产品、产品多属性、产品图片、收藏、自定义产品系列和智能产品系列
产品列表和产品系列列表
产品发布和产品系列发布
销售计划
运营商服务、国家/地区和省份
购物付款争议资源
Shopify 付款付款、余额和交易资源
订阅合同所需权限在将这些访问范围添加到应用之前，需要从合作伙伴仪表板请求这些访问范围的权限。
返回对象
资产和主题
GraphQL Admin API 可翻译对象
配送订单资源分配给由任何配送服务管理的位置
用户和员工购物加
GraphQL Admin API OrderStaged更改类型和订单编辑功能
支付应用程序 API 付款应用程序配置
支付应用程序 API 支付、捕获、退款和作废
"""
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
