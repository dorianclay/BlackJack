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

  imageSrcForCard(card: Card): string {
    if (card.isHidden) {
      return 'assets/svg-cards/back_of_card.svg';
    }
    const path = `assets/svg-cards/${card.value}_of_${card.suit}.svg`;
    return path.toLocaleLowerCase();
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
