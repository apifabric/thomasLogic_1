import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {PURCHASEORDERITEM_MODULE_DECLARATIONS, PurchaseOrderItemRoutingModule} from  './PurchaseOrderItem-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    PurchaseOrderItemRoutingModule
  ],
  declarations: PURCHASEORDERITEM_MODULE_DECLARATIONS,
  exports: PURCHASEORDERITEM_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class PurchaseOrderItemModule { }