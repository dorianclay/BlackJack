import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, ParamMap, Router } from '@angular/router';
import { BlackjackService } from "../../service/blackjack.service";

@Component({
  selector: 'app-create-player',
  templateUrl: './create-player.component.html',
  styleUrls: ['./create-player.component.scss']
})
export class CreatePlayerComponent implements OnInit {

  public gameId: string = '';

  public name: string = '';

  public no_name: boolean = false;

  constructor(private route: ActivatedRoute, private blackjackService: BlackjackService, private router: Router) { }

  ngOnInit(): void {
      this.route.params.subscribe(params => {
          this.gameId = params['game_id'];
      });
  }

  onCreatePlayer(): void {
      if (this.name == '') {
          this.no_name = true;
      } else {
          this.blackjackService.createPlayer(this.gameId, this.name).subscribe((response) => {
          console.log(response.player_id);
          this.router.navigate([`/game/${this.gameId}/player/${response.player_id}`]);
      });

      }

  }

}
