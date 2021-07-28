import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { BlackjackService } from "../../service/blackjack.service";

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
    if (this.gameId == '') {
      this.no_gameId = true;
    } else {
      this.router.navigate([`/game/${this.gameId}`]);
    }
  }

}
