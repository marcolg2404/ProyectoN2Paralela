import { BrowserModule } from '@angular/platform-browser';
import { ErrorHandler, NgModule } from '@angular/core';
import { IonicApp, IonicErrorHandler, IonicModule } from 'ionic-angular';
import { SplashScreen } from '@ionic-native/splash-screen';
import { StatusBar } from '@ionic-native/status-bar';
import { Media } from '@ionic-native/media';
import { File } from '@ionic-native/file';
//import { CargandoPage } from '../pages/cargando/cargando'
import { MyApp } from './app.component';
import { HomePage } from '../pages/home/home';
//import { NativePageTransitions } from '@ionic-native-page-transitions';
@NgModule({
  declarations: [
    MyApp,
    HomePage
    //CargandoPage,
  ],
  imports: [
    BrowserModule,
    IonicModule.forRoot(MyApp)
  ],
  bootstrap: [IonicApp],
  entryComponents: [
    MyApp,
    HomePage,
    //CargandoPage,
  ],
  providers: [
    StatusBar,
    SplashScreen,
    {provide: ErrorHandler, useClass: IonicErrorHandler},
    Media,
    File,
  //  NativePageTransitions,
  ]
})
export class AppModule {}
