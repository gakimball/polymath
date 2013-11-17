;(function($) {

  var Player = function($obj) {

    this.$player = $obj;
    this.$audio  = $obj.find('[data-audio]').eq(0);
    this.initialized = false;

    this.ui = {
      bPlayPause:   $obj.find('[data-playpause]'),
      bPrevTrack:   $obj.find('[data-prevtrack]'),
      bNextTrack:   $obj.find('[data-nexttrack]'),
      uSlider:      $obj.find('[data-slider]'),
      iTrackTitle:  $obj.find('[data-title]').eq(0),
      iArtistName:  $obj.find('[data-artist]').eq(0),
      iCurrentTime: $obj.find('[data-currenttime]').eq(0),
      iTotalTime:   $obj.find('[data-totaltime]').eq(0),
    };

    this.playlist = [];
    this.playlistIndex = 0;

    this.server = window.location.origin;
    this.api    = '/api/tracks/';

    this.events();
  }

  Player.prototype = {
    initialize: function() {
      this.initialized = true;
    },

    events: function() {
      self = this;

      // Internal triggers
      this.$audio.on({
        'ended': function() {
          self.nextTrack();
        },
        'timeupdate': function() {
          self.updateTimeUI();
        },
      });
      this.$player.on({
        'player-playlistloaded': function() {
          self.loadTrack(self.playlistIndex);
        },
        'player-playpause': function() {
          if (self.$audio[0].paused === true) {
            self.$audio[0].play();
          }
          else {
            self.$audio[0].pause();
          }
        },
        'player-nexttrack': function() {
          self.nextTrack();
        },
        'player-prevtrack': function() {
          self.prevTrack();
        },
      });

      this.ui.bPlayPause.click(function(){
        self.$player.trigger('player-playpause');
      });
      this.ui.bPrevTrack.click(function(){
        self.$player.trigger('player-prevtrack')
      });
      this.ui.bNextTrack.click(function(){
        self.$player.trigger('player-nexttrack')
      });
    },

    loadPlaylist: function(tracklist) {
      var self = this;

      if (tracklist instanceof Array) {
        $.getJSON(this.server + this.api + tracklist.join(','), function(data) {
          self.playlist = data;
          self.$player.trigger('player-playlistloaded');
        });
      }
    },
    loadTrack: function(index) {
      var wasPlaying = !this.$audio[0].paused || !this.initialized;
      this.$audio.empty();
      console.log(index);

      // MP3 file
      var mp3_source = document.createElement('source');
      mp3_source.setAttribute('type', 'audio/mpeg; codecs="mp3"');
      mp3_source.setAttribute('src', this.playlist[index]['audio_mp3']);
      this.$audio.append(mp3_source);

      // Ogg file
      var ogg_source = document.createElement('source');
      ogg_source.setAttribute('type', 'audio/ogg; codes="vorbis"');
      ogg_source.setAttribute('src', this.playlist[index]['audio_ogg']);
      this.$audio.append(ogg_source);

      this.$audio[0].load();
      if (wasPlaying === true) this.$audio[0].play();
      this.updatePlayerUI();
      this.updateTimeUI();

      if (this.initialized === false) this.initialize();
    },

    updatePlayerUI: function() {
      var track = this.playlist[this.playlistIndex];
      this.ui.iTrackTitle.text(track['title']);
      this.ui.iArtistName.text(track['artist']);
      this.ui.iTotalTime.text(track['length']);
    },
    updateTimeUI: function() {
      var cur = this.$audio[0].currentTime;
      var sec = (cur % 60 < 10) ? ('0'+parseInt(cur % 60)) : parseInt(cur % 60);
      this.ui.iCurrentTime.text(parseInt(cur / 60)+':'+sec);
    },

    prevTrack: function() {
      if (this.playlistIndex !== 0) {
        this.playlistIndex--;
        this.loadTrack(this.playlistIndex);
      }
    },
    nextTrack: function() {
      if (this.playlist.length !== this.playlistIndex + 1) {
        this.playlistIndex++;
        this.loadTrack(this.playlistIndex);
      }
    },
  }

  $(function(){
    var masterPlayer = new Player($('[data-player]'));

    $('body').on('click', '[data-player-track]', function(e){
      e.preventDefault();

      var clicked_track = $(this).attr('data-player-track');
      var collection = $(this).closest('[data-player-collection]').find('[data-player-track]');

      var track_ids = [];
      collection.each(function(index){
        var track_id = $(this).attr('data-player-track');
        track_ids.push(track_id);
        if (track_id == clicked_track) {
          masterPlayer.playlistIndex = index;
        }
      });

      masterPlayer.loadPlaylist(track_ids);
    });
  });

})(window.Zepto || window.jQuery);