import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';

export interface CreateGameResponse {
  game_id: string;
}

export interface JoinGameResponse {
  game_exists: boolean;
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
  has_started: boolean;
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

  private readonly endpoint = environment.apiUrl + '/blackjack';
  private readonly options: any = { responseType: 'json' };

  constructor(private http: HttpClient) { }

  createGame(): Observable<CreateGameResponse> {
    return this.http.post<CreateGameResponse>(this.endpoint + '/api/v1/games', {});
  }

  joinGame(gameId: string): Observable<JoinGameResponse> {
    return this.http.post<JoinGameResponse>(`${this.endpoint}/api/v1/games/${gameId}`, {});
  }

  getGame(gameId: string, playerId: string): Observable<GameMetadataResponse> {
    return this.http.get<GameMetadataResponse>(`${this.endpoint}/api/v1/games/${gameId}/players/${playerId}`);
  }

  startGame(gameId: string): void {
    this.http.post<void>(`${this.endpoint}/api/v1/games/${gameId}/start`, {}).subscribe();
  }

  hit(gameId: string, playerId: string): void {
    this.http.get<void>(`${this.endpoint}/api/v1/games/${gameId}/players/${playerId}/hit`).subscribe();
  }

  stay(gameId: string, playerId: string): void {
    this.http.get<void>(`${this.endpoint}/api/v1/games/${gameId}/players/${playerId}/stay`).subscribe();
  }

  createPlayer(gameId: string, name: string): Observable<CreatePlayerResponse> {
    const playerRequest: CreatePlayerRequest = {
      name
    }
    return this.http.post<CreatePlayerResponse>(`${this.endpoint}/api/v1/games/${gameId}/players`, playerRequest);
  }

}
