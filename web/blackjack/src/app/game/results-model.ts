import { PlayerModel } from "../player/player-model";

export class ResultsModel {
    public winningStatement: string;
    public details: string;

    constructor(result: string, winningPlayerModel: PlayerModel) {
        const playerName = winningPlayerModel.metadata.name;
        if (result === 'Win') {
            this.winningStatement = `${playerName} wins this hand!`;
            this.details = `With a winning hand of ${winningPlayerModel.score}`;
        } else {
            this.winningStatement = 'It is a tie.';
            this.details = '';
        }
    }
}