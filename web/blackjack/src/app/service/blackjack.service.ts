import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface CreateGameResponse {
  game_id: string;
}

export interface CreatePlayerRequest {
  name: string;
}

export interface CreatePlayerResponse {
  player_id: string;
}

export interface GameMetadataResponse {
  you: PlayerMetadataResponse;
  players: PlayerMetadataResponse[];
  results?: ResultsMetadataResponse;
}

export interface PlayerMetadataResponse {
  name: string;
  score?: number;
  their_turn: boolean;
  cards: CardMetadataResponse[];
}

export interface ResultsMetadataResponse {
  result: string;
  winning_player: PlayerMetadataResponse;
}

export interface CardMetadataResponse {
  value?: string;
  suit?: string;
  is_hidden: boolean;
}

@Injectable({
  providedIn: 'root'
})
export class BlackjackService {

  private readonly endpoint = 'http://localhost:5000/blackjack'
  private readonly options: any = { responseType: 'json' }

  constructor(private http: HttpClient) { }

  createGame(): Observable<CreateGameResponse> {
    return this.http.post<CreateGameResponse>(this.endpoint + '/api/v1/games', {});
  }

  getGame(gameId: string, playerId: string) {
    return this.http.get<GameMetadataResponse>(`${this.endpoint}/api/v1/games/${gameId}/players/${playerId}`);
  }

  // hit(gameId: string, playerId: string) {

  // }

  // stay(gameId: string, playerId: string) {

  // }

  createPlayer(gameId: string, name: string): Observable<CreatePlayerResponse> {
    const playerRequest: CreatePlayerRequest = {
      name
    }
    return this.http.post<CreatePlayerResponse>(`${this.endpoint}/api/v1/games/${gameId}/players`, playerRequest);
  }

}
