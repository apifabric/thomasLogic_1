import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { MainComponent } from './main.component';

export const routes: Routes = [
  {
    path: '', component: MainComponent,
    children: [
        { path: '', redirectTo: 'home', pathMatch: 'full' },
        { path: 'about', loadChildren: () => import('./about/about.module').then(m => m.AboutModule) },
        { path: 'home', loadChildren: () => import('./home/home.module').then(m => m.HomeModule) },
        { path: 'settings', loadChildren: () => import('./settings/settings.module').then(m => m.SettingsModule) },
      
    
        { path: 'Customer', loadChildren: () => import('./Customer/Customer.module').then(m => m.CustomerModule) },
    
        { path: 'CustomerAddress', loadChildren: () => import('./CustomerAddress/CustomerAddress.module').then(m => m.CustomerAddressModule) },
    
        { path: 'Discount', loadChildren: () => import('./Discount/Discount.module').then(m => m.DiscountModule) },
    
        { path: 'Item', loadChildren: () => import('./Item/Item.module').then(m => m.ItemModule) },
    
        { path: 'Order', loadChildren: () => import('./Order/Order.module').then(m => m.OrderModule) },
    
        { path: 'PaymentMethod', loadChildren: () => import('./PaymentMethod/PaymentMethod.module').then(m => m.PaymentMethodModule) },
    
        { path: 'Product', loadChildren: () => import('./Product/Product.module').then(m => m.ProductModule) },
    
        { path: 'PurchaseOrder', loadChildren: () => import('./PurchaseOrder/PurchaseOrder.module').then(m => m.PurchaseOrderModule) },
    
        { path: 'PurchaseOrderItem', loadChildren: () => import('./PurchaseOrderItem/PurchaseOrderItem.module').then(m => m.PurchaseOrderItemModule) },
    
        { path: 'ShipmentDetail', loadChildren: () => import('./ShipmentDetail/ShipmentDetail.module').then(m => m.ShipmentDetailModule) },
    
        { path: 'Shipper', loadChildren: () => import('./Shipper/Shipper.module').then(m => m.ShipperModule) },
    
        { path: 'Supplier', loadChildren: () => import('./Supplier/Supplier.module').then(m => m.SupplierModule) },
    
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MainRoutingModule { }