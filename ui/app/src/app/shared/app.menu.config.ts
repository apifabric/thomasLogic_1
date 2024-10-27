import { MenuRootItem } from 'ontimize-web-ngx';

import { CustomerCardComponent } from './Customer-card/Customer-card.component';

import { CustomerAddressCardComponent } from './CustomerAddress-card/CustomerAddress-card.component';

import { DiscountCardComponent } from './Discount-card/Discount-card.component';

import { ItemCardComponent } from './Item-card/Item-card.component';

import { OrderCardComponent } from './Order-card/Order-card.component';

import { PaymentMethodCardComponent } from './PaymentMethod-card/PaymentMethod-card.component';

import { ProductCardComponent } from './Product-card/Product-card.component';

import { PurchaseOrderCardComponent } from './PurchaseOrder-card/PurchaseOrder-card.component';

import { PurchaseOrderItemCardComponent } from './PurchaseOrderItem-card/PurchaseOrderItem-card.component';

import { ShipmentDetailCardComponent } from './ShipmentDetail-card/ShipmentDetail-card.component';

import { ShipperCardComponent } from './Shipper-card/Shipper-card.component';

import { SupplierCardComponent } from './Supplier-card/Supplier-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Customer', name: 'CUSTOMER', icon: 'view_list', route: '/main/Customer' }
    
        ,{ id: 'CustomerAddress', name: 'CUSTOMERADDRESS', icon: 'view_list', route: '/main/CustomerAddress' }
    
        ,{ id: 'Discount', name: 'DISCOUNT', icon: 'view_list', route: '/main/Discount' }
    
        ,{ id: 'Item', name: 'ITEM', icon: 'view_list', route: '/main/Item' }
    
        ,{ id: 'Order', name: 'ORDER', icon: 'view_list', route: '/main/Order' }
    
        ,{ id: 'PaymentMethod', name: 'PAYMENTMETHOD', icon: 'view_list', route: '/main/PaymentMethod' }
    
        ,{ id: 'Product', name: 'PRODUCT', icon: 'view_list', route: '/main/Product' }
    
        ,{ id: 'PurchaseOrder', name: 'PURCHASEORDER', icon: 'view_list', route: '/main/PurchaseOrder' }
    
        ,{ id: 'PurchaseOrderItem', name: 'PURCHASEORDERITEM', icon: 'view_list', route: '/main/PurchaseOrderItem' }
    
        ,{ id: 'ShipmentDetail', name: 'SHIPMENTDETAIL', icon: 'view_list', route: '/main/ShipmentDetail' }
    
        ,{ id: 'Shipper', name: 'SHIPPER', icon: 'view_list', route: '/main/Shipper' }
    
        ,{ id: 'Supplier', name: 'SUPPLIER', icon: 'view_list', route: '/main/Supplier' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    CustomerCardComponent

    ,CustomerAddressCardComponent

    ,DiscountCardComponent

    ,ItemCardComponent

    ,OrderCardComponent

    ,PaymentMethodCardComponent

    ,ProductCardComponent

    ,PurchaseOrderCardComponent

    ,PurchaseOrderItemCardComponent

    ,ShipmentDetailCardComponent

    ,ShipperCardComponent

    ,SupplierCardComponent

];