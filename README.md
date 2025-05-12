<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>



<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">Medievalica</h3>

  <p align="center">
    A project about finding the best strategy in a made-up game of cards.
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
[![Product Name Screen Shot][product-screenshot]](images/rules.png)

This is a passion project about Game Theory and card games.
Given a game with simple rules, is it possible to find a deterministic strategy that can beat every other strategy?
And what strategies other people may create?

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

Rules of the games are as follows: you and your opponent start with 8 cards in hand.

> 5 Clerics, 2 Knights and 1 Emperor

You play one card per round, for 5 rounds.
Each time, the players get points according to the rules:

 1. Cleric v Cleric ......... 1 point to each player
 2. Knight v Cleric ........ 2 points to the Knight player, 0 to the Cleric player
 3. Emperor v Knight ...... 4 points to the Emperor player, 0 to the Knight player
 4. Other combinations ..... 0 points to each player

Your goal is to get as many points as possible. You have to come up with a strategy that can perform well againts all kinds of opponents.
This will include facing your own strategy and a random strategy. You may devise your strategy as you like, but keep in mind:

 1. it cannot be fully non-deterministic nor random.
 2. it should pick only cards currently in your hand.
 3. it should always pick a card

You will have access to this data for creating you own strategy:

1. myHand .............. list of cards in your hand
2. myScore ............. your current score
3. currentRound ........ current round (starts at 1 and goes up to 5)
4. myStack ............. list of cards you played (in chronological order, starts empty)
5. opponentStack ....... list of cards your opponent played (in chronological order, starts empty)

### Prerequisites

This project relies on Python 3 and nothing else.

### Installation

1. Clone this repo
   ```sh
   git clone https://github.com/redriel/medievalica.git
   ```
2. (optional) Download the zip
3. Launch the program
   ```sh
   py medievalica.py
   ```
4. Look at the results of the current example strategies and convince yourself you can do better.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

You can freely edit this file:

> lib/strategies/yourStrategy.py

You are encouraged to change the name of the file and implement your strategy as you like.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

Time to time, I will add to the `strategies` folder each strategy developed by friends and stragers alike. My goal is to have a large collection of strategies competing to each other in a non-solved meta.

You can Pull Request your strategy and I will include it in the project!

### Top contributors:

 1. Mastrat
 2. Mirror_1
 3. Cavalry

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License.

<p align="right">(<a href="#readme-top">back to top</a>)</p>