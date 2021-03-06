import { Component, OnInit } from '@angular/core';
import { PlayerModel } from './player/player-model';
import { PlayerMetadata } from './player/player-metadata';
import { Card, Suit } from './card';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'blackjack';
  playerModel!: PlayerModel;

  ngOnInit() {
    const playerMetadata = new PlayerMetadata('id', 'Dorian Clay');
    const cards = [
      new Card(Suit.SPADES, 1),
      new Card(Suit.SPADES, 11),
    ]
    this.playerModel = new PlayerModel(playerMetadata, cards, 21);
  }
}
