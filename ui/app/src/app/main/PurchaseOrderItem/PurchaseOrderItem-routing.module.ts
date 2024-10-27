import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PurchaseOrderItemHomeComponent } from './home/PurchaseOrderItem-home.component';
import { PurchaseOrderItemNewComponent } from './new/PurchaseOrderItem-new.component';
import { PurchaseOrderItemDetailComponent } from './detail/PurchaseOrderItem-detail.component';

const routes: Routes = [
  {path: '', component: PurchaseOrderItemHomeComponent},
  { path: 'new', component: PurchaseOrderItemNewComponent },
  { path: ':id', component: PurchaseOrderItemDetailComponent,
    data: {
      oPermission: {
        permissionId: 'PurchaseOrderItem-detail-permissions'
      }
    }
  }
];

export const PURCHASEORDERITEM_MODULE_DECLARATIONS = [
    PurchaseOrderItemHomeComponent,
    PurchaseOrderItemNewComponent,
    PurchaseOrderItemDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class PurchaseOrderItemRoutingModule { }