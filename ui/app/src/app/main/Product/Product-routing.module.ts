import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ProductHomeComponent } from './home/Product-home.component';
import { ProductNewComponent } from './new/Product-new.component';
import { ProductDetailComponent } from './detail/Product-detail.component';

const routes: Routes = [
  {path: '', component: ProductHomeComponent},
  { path: 'new', component: ProductNewComponent },
  { path: ':id', component: ProductDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Product-detail-permissions'
      }
    }
  },{
    path: ':product_id/Discount', loadChildren: () => import('../Discount/Discount.module').then(m => m.DiscountModule),
    data: {
        oPermission: {
            permissionId: 'Discount-detail-permissions'
        }
    }
},{
    path: ':product_id/Item', loadChildren: () => import('../Item/Item.module').then(m => m.ItemModule),
    data: {
        oPermission: {
            permissionId: 'Item-detail-permissions'
        }
    }
},{
    path: ':product_id/PurchaseOrderItem', loadChildren: () => import('../PurchaseOrderItem/PurchaseOrderItem.module').then(m => m.PurchaseOrderItemModule),
    data: {
        oPermission: {
            permissionId: 'PurchaseOrderItem-detail-permissions'
        }
    }
}
];

export const PRODUCT_MODULE_DECLARATIONS = [
    ProductHomeComponent,
    ProductNewComponent,
    ProductDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ProductRoutingModule { }