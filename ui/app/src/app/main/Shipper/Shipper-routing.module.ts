import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ShipperHomeComponent } from './home/Shipper-home.component';
import { ShipperNewComponent } from './new/Shipper-new.component';
import { ShipperDetailComponent } from './detail/Shipper-detail.component';

const routes: Routes = [
  {path: '', component: ShipperHomeComponent},
  { path: 'new', component: ShipperNewComponent },
  { path: ':id', component: ShipperDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Shipper-detail-permissions'
      }
    }
  },{
    path: ':shipper_id/ShipmentDetail', loadChildren: () => import('../ShipmentDetail/ShipmentDetail.module').then(m => m.ShipmentDetailModule),
    data: {
        oPermission: {
            permissionId: 'ShipmentDetail-detail-permissions'
        }
    }
}
];

export const SHIPPER_MODULE_DECLARATIONS = [
    ShipperHomeComponent,
    ShipperNewComponent,
    ShipperDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ShipperRoutingModule { }