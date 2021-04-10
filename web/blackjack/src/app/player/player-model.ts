import { Card } from '../card';
import { PlayerMetadata } from './player-metadata';

export class PlayerModel {
  constructor(public metadata: PlayerMetadata, public cards: Card[], public isTheirTurn: boolean, public score?: number) {}
}