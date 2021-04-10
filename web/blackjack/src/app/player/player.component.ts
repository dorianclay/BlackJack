import { Component, OnInit, Input } from '@angular/core';
import { PlayerModel } from './player-model';
import { Card } from '../card';
import { BlackjackService } from 'src/app/service/blackjack.service';

@Component({
  selector: 'app-player',
  templateUrl: './player.component.html',
  styleUrls: ['./player.component.scss']
})
export class PlayerComponent {

  @Input() playerModel?: PlayerModel;

  constructor(private blackjackService: BlackjackService) {}

  textForCard(card: Card): string {
    return `${card.value} of ${card.suit}`;
  }

  onHit(): void {
    if (!this.playerModel) {
      console.error('Expected a valid playerModel while trying to hit, something went wrong');
      return;
    }
    this.blackjackService.hit(this.playerModel.metadata.currentGameId, this.playerModel.metadata.id!);
  }

  onStay(): void {
    if (!this.playerModel) {
      console.error('Expected a valid playerModel while trying to stay, something went wrong');
      return;
    }
    this.blackjackService.stay(this.playerModel.metadata.currentGameId, this.playerModel.metadata.id!);
  }
}
