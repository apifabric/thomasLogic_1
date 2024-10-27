import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'PurchaseOrderItem-new',
  templateUrl: './PurchaseOrderItem-new.component.html',
  styleUrls: ['./PurchaseOrderItem-new.component.scss']
})
export class PurchaseOrderItemNewComponent {
  @ViewChild("PurchaseOrderItemForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}