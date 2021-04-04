import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { BlackjackService } from "../../service/blackjack.service";

@Component({
  selector: 'app-create-game',
  templateUrl: './create-game.component.html',
  styleUrls: ['./create-game.component.scss']
})
export class CreateGameComponent implements OnInit {

  constructor(private blackjackService: BlackjackService, private router: Router) { }

  ngOnInit(): void {
  }

  onCreateGame(): void {
    this.blackjackService.createGame().subscribe((response) => {
        this.router.navigate([`/game/${response.game_id}`]);
    });
}

  onJoinGame(): void {
    console.warn('Join game is not implemented yet.');
  }

}
