import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { interval } from 'rxjs';
import { Card } from 'src/app/card';
import { PlayerModel } from 'src/app/player/player-model';
import { BlackjackService, CardMetadataResponse, PlayerMetadataResponse } from 'src/app/service/blackjack.service';

@Component({
  selector: 'app-game',
  templateUrl: './game.component.html',
  styleUrls: ['./game.component.scss']
})
export class GameComponent implements OnInit {

  private gameId: string = '';
  private playerId: string = '';

  public you?: PlayerModel;

  public otherPlayers: PlayerModel[] = [];

  constructor(private route: ActivatedRoute, private blackjackService: BlackjackService) { }

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.gameId = params['game_id'];
      this.playerId = params['player_id'];
      this.fetchGame();
    });

    interval(500).subscribe(() => {
      this.fetchGame();
    });
  }

  private fetchGame(): void {
    this.blackjackService.getGame(this.gameId, this.playerId).subscribe((response) => {
      this.you = this.createPlayer(response.you, this.playerId);
      this.otherPlayers = response.players.map((otherPlayerMetadata) => this.createPlayer(otherPlayerMetadata, undefined));
    });
  }

  private createPlayer(playerMetadata: PlayerMetadataResponse, id?: string): PlayerModel {
    return {
      metadata: {
        currentGameId: this.gameId,
        name: playerMetadata.name,
        id: id,
      },
      cards: playerMetadata.cards.filter((cardMetadata) => !cardMetadata.is_hidden).map((cardMetadata) => new Card(cardMetadata.suit!, cardMetadata.value!)),
      isTheirTurn: playerMetadata.their_turn,
      score: playerMetadata.score,
    };
  }
}