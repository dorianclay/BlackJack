import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { BlackjackService } from "../../service/blackjack.service";

@Component({
  selector: 'app-create-game',
  templateUrl: './create-game.component.html',
  styleUrls: ['./create-game.component.scss']
})

export class CreateGameComponent implements OnInit {

  public code: string = '';

  public no_code: boolean = false;

  constructor(private blackjackService: BlackjackService, private router: Router) { }

  ngOnInit(): void {
  }

  onCreateGame(): void {
    this.blackjackService.createGame().subscribe((response) => {
      this.router.navigate([`/game/${response.game_id}`]);
    });
  }

  onJoinGame(): void {
    if (this.code == '') {
      this.no_code = true;
    } else if (/* code is not in list */) {
      this.no_code = true;
    } else {
      this.router.navigate([`/game/${this.code}`]);
    }
  }

}
