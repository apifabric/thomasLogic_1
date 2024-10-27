import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './PurchaseOrderItem-card.component.html',
  styleUrls: ['./PurchaseOrderItem-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.PurchaseOrderItem-card]': 'true'
  }
})

export class PurchaseOrderItemCardComponent {


}