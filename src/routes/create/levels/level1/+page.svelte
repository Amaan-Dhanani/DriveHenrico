<script>
  import { Input } from '$lib/components';
	import { enhance } from '$app/forms';
	import '$lib/css/app.css';
	export let data;
	export let form;
</script>
<div>
  <script src="https://cdn.jsdelivr.net/npm/phaser@3.55.2/dist/phaser.min.js"></script>

  <style>
    canvas { display: block; height: 100vh; margin: auto; }
    .control-button {
      position: absolute;
      width: 80px;
      height: 80px;
      background: rgba(0, 0, 0, 0.5);
      border-radius: 50%;
      text-align: center;
      line-height: 80px;
      font-size: 40px;
      color: white;
      user-select: none;
      touch-action: none;
      z-index: 10;
    }
    #jumpButton { bottom: 20px; left: 20px; }
    #leftButton { bottom: 20px; right: 200px; }
    #rightButton { bottom: 20px; right: 100px; }

    /* Modal styles */
    .modal {
      display: none; /* Hidden by default */
      position: fixed;
      z-index: 1000;
      left: 0; top: 0;
      width: 100%; height: 100%;
      overflow: auto;
      background-color: rgba(0,0,0,0.5);
    }
    .modal-content {
      background-color: white;
      margin: 15% auto;
      padding: 20px;
      border-radius: 10px;
      width: 300px;
      text-align: center;
    }
  </style>

  <!-- Control buttons -->
  <div id="leftButton" class="control-button">◀</div>
  <div id="rightButton" class="control-button">▶</div>
  <div id="jumpButton" class="control-button">▲</div>

  <!-- WIN modal: defined directly in HTML -->
  <div id="winModal" class="modal">
    <div class="modal-content">
      <form
					method="POST"
					autocomplete="off"
					use:enhance
					class="box-border flex flex-grow flex-col rounded-t-2xl bg-white px-6 py-8"
				>
        <h2>YOU WIN!</h2>
					<Input
						id="res"
						name="res"
						value="win"
						readonly
						required
						class="invisible h-[0px]"
					/>
					<button
						type="submit"
						class="mt-[20px] h-12 w-full rounded-xl bg-[#3d5cff] text-center text-white hover:cursor-pointer"
					>
						Continue
					</button>
				</form>
    </div>
  </div>

  <!-- LOSE modal: defined directly in HTML -->
  <div id="loseModal" class="modal">
    <div class="modal-content">
      <form
					method="POST"
					autocomplete="off"
					use:enhance
					class="box-border flex flex-grow flex-col rounded-t-2xl bg-white px-6 py-8"
				>
        <h2>YOU LOSE!</h2>
					<Input
						id="res"
						name="res"
						value="lose"
						readonly
						required
						class="invisible h-[0px]"
					/>
					<button
						type="submit"
						class="mt-[20px] h-12 w-full rounded-xl bg-[#3d5cff] text-center text-white hover:cursor-pointer"
					>
						Continue
					</button>
				</form>
    </div>
  </div>

  <script>
    const config = {
      type: Phaser.AUTO,
      width: 1000,
      height: 600,
      physics: {
        default: 'arcade',
        arcade: {
          gravity: { y: 500 },
          debug: false
        }
      },
      scene: { preload, create, update }
    };

    let player, cursors;
    let platforms;
    let winZone, loseZone;
    let moveLeft = false, moveRight = false;
    const game = new Phaser.Game(config);

    function preload() {
      this.load.image('background', 'https://media-public.canva.com/hu0-w/MAF-ONhu0-w/1/tl.png');
      this.load.image('player', 'https://media-public.canva.com/rtras/MAFtCNrtras/1/t.png');
      this.load.image('platform', 'https://media-public.canva.com/oEi0c/MAGLA0oEi0c/1/tl.png');
      this.load.image('winZone', 'https://media-public.canva.com/foCZ0/MAGCrCfoCZ0/1/t.png');
      this.load.image('loseZone', 'https://media-public.canva.com/iDVd4/MAEonCiDVd4/1/tl.png');
    }

    function create() {
      this.add.image(500, 300, 'background').setDisplaySize(1000, 600);

      platforms = this.physics.add.staticGroup();
      const platformPositions = [
        [100, 400], [265, 400], [430, 400], [595, 400],
        [100, 440], [265, 440], [430, 440], [595, 440],
        [100, 480], [265, 480], [430, 480], [595, 480],
        [760, 400], [760, 440], [760, 480],
        [100, 520], [100, 560], [100, 600],
        [265, 520], [265, 560], [265, 600],
        [430, 520], [430, 560], [430, 600],
        [595, 520], [595, 560], [595, 600],
        [760, 520], [760, 560], [760, 600]
      ];
      platformPositions.forEach(pos => platforms.create(pos[0], pos[1], 'platform').setScale(0.3).refreshBody());

      player = this.physics.add.sprite(100, 0, 'player').setScale(0.25).setCollideWorldBounds(true);
      this.physics.add.collider(player, platforms);

      winZone = this.physics.add.staticSprite(820, 320, 'winZone').setScale(0.5);
      loseZone = this.physics.add.staticSprite(400, 200, 'loseZone');

      this.physics.add.collider(player, winZone, () => {
        showModal('winModal');
      });

      this.physics.add.collider(player, loseZone, () => {
        showModal('loseModal');
      });

      cursors = this.input.keyboard.createCursorKeys();

      const leftButton = document.getElementById('leftButton');
      const rightButton = document.getElementById('rightButton');
      const jumpButton = document.getElementById('jumpButton');

      leftButton.addEventListener('touchstart', () => { moveLeft = true; });
      leftButton.addEventListener('touchend', () => { moveLeft = false; });
      rightButton.addEventListener('touchstart', () => { moveRight = true; });
      rightButton.addEventListener('touchend', () => { moveRight = false; });

      let jumpHeld = false;
      jumpButton.addEventListener('touchstart', () => { jumpHeld = true; });
      jumpButton.addEventListener('touchend', () => { jumpHeld = false; });

      this.events.on('update', () => {
        if (jumpHeld && player.body.blocked.down) {
          player.setVelocityY(-300);
        }
      });
    }

    function update() {
      if (cursors.left.isDown || moveLeft) {
        player.setVelocityX(-160);
        player.flipX = false;
      } else if (cursors.right.isDown || moveRight) {
        player.setVelocityX(160);
        player.flipX = true;
      } else {
        player.setVelocityX(0);
      }

      if (cursors.up.isDown && player.body.blocked.down) {
        player.setVelocityY(-300);
      }
    }

    function showModal(id) {
      document.getElementById(id).style.display = 'block';
      game.scene.pause();
    }

    function hideModal(id) {
      document.getElementById(id).style.display = 'none';
      game.scene.resume();
    }

    document.getElementById('winForm').addEventListener('submit', (e) => {
      e.preventDefault();
      const name = e.target.name.value.trim();
      if(name) {
        alert(`Congratulations, ${name}!`);
        hideModal('winModal');
        location.replace('/levels/next-level');
      }
    });

    document.getElementById('loseForm').addEventListener('submit', (e) => {
      e.preventDefault();
      alert('Thanks for your feedback!');
      hideModal('loseModal');
      location.replace('/dashboard/my-quests/fail-level');
    });

    document.getElementById('winCloseBtn').addEventListener('click', () => {
      hideModal('winModal');
    });
    document.getElementById('loseCloseBtn').addEventListener('click', () => {
      hideModal('loseModal');
    });
  </script>
</div>
