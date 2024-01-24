package main

import (
	"fmt"
	"os"

	"github.com/dstathis/swisstools"
)

func main() {
	tournament := swisstools.NewTournament()
	tournament.AddPlayer("Dylan")
	tournament.AddPlayer("Foivos")
	tournament.AddPlayer("Makis")
	tournament.AddPlayer("Chronis")
	tournament.AddPlayer("Nikos")
	tournament.FormatPlayers(os.Stdout)
	tournament.Pair()
	fmt.Println(tournament.GetPairings())
}
