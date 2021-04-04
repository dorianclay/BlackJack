import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { PlayerComponent } from './player/player.component';
import { CreateGameComponent } from './game/create-game/create-game.component';
import { AppRoutingModule } from './app-routing.module';
import { CreatePlayerComponent } from './game/create-player/create-player.component';
import { GameComponent } from './game/game/game.component';

@NgModule({
  declarations: [
    AppComponent,
    PlayerComponent,
    CreateGameComponent,
    CreatePlayerComponent,
    GameComponent,
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    FormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
