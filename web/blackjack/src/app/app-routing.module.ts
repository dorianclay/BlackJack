import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CommonModule } from '@angular/common';
import { CreateGameComponent } from './game/create-game/create-game.component';
import { CreatePlayerComponent } from './game/create-player/create-player.component';
import { GameComponent } from './game/game/game.component';

const routes: Routes = [
  { path: 'create_game', component: CreateGameComponent },
  { path: 'game/:game_id', component: CreatePlayerComponent },
  { path: 'game/:game_id/player/:player_id', component: GameComponent },
  { path: '**', redirectTo: '/create_game', pathMatch: 'full' },
]

@NgModule({
  declarations: [],
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
