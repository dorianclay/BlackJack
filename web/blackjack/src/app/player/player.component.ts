import { Component, OnInit, Input } from '@angular/core';
import { PlayerModel } from './player-model';
import { Card, Suit } from '../card';
import { textFormatForCard } from '../card-text.utils';

@Component({
  selector: 'app-player',
  templateUrl: './player.component.html',
  styleUrls: ['./player.component.scss']
})
export class PlayerComponent implements OnInit {

  @Input() playerModel!: PlayerModel;

  constructor() {}

  ngOnInit(): void {
    if (!this.playerModel) {
      console.error('expected a playerModel to be provided as input.')
    }
  }

  textForCard(card: Card): string {
    return textFormatForCard(card);
  }

  onHit(): void {
    const newCard = new Card(Suit.DIAMONDS, 2);
    this.playerModel.cards.push(newCard);
  }
}
