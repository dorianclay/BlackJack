import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';
import { BlackjackService, JoinGameResponse } from "../../service/blackjack.service";

@Component({
  selector: 'app-create-game',
  templateUrl: './create-game.component.html',
  styleUrls: ['./create-game.component.scss']
})

export class CreateGameComponent implements OnInit {

  public gameId: string = '';

  public no_gameId: boolean = false;

  constructor(private blackjackService: BlackjackService, private router: Router) { }

  ngOnInit(): void {
  }

  onCreateGame(): void {
    this.blackjackService.createGame().subscribe((response) => {
      this.router.navigate([`/game/${response.game_id}`]);
    });
  }

  onJoinGame(): void {
    response = this.blackjackService.joinGame(this.gameId).subscribe()

    if (this.gameId == '' || response.status == 502) {
      this.no_gameId = true;
    } else {
      this.router.navigate([`/game/${this.gameId}`]);
    }
  }

}
