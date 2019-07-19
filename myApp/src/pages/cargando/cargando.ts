import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';

/**
 * Generated class for the CargandoPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-cargando',
  templateUrl: 'cargando.html',
})
export class CargandoPage {

  constructor(public navCtrl: NavController, public navParams: NavParams) {
  }
  ngOnInit(){
    setTimeout(() => {
        // this.navCtrl.popToRoot();
        // might try this instead
        this.navCtrl.push('ResultadoPage');
    }, 5000);
}
  ionViewDidLoad() {
    console.log('ionViewDidLoad CargandoPage');
  }

}
