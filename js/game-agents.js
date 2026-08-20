/**
 * ImpactMojo Game Agents Client
 * Version: 2.0.0
 * Date: August 20, 2026
 *
 * Drives the AI opponents in the Games library from a local personality
 * engine: cooperation bias, memory weight and risk tolerance, per agent.
 *
 * v2.0.0 removed the LLM path. Every decision used to POST to a
 * `game-agent` Supabase Edge Function that was **never deployed**, so the
 * call 404'd and fell through to this engine — on every move, in twelve
 * games, silently. The engine was doing all the work already; the round
 * trip only added latency and a provider menu no page ever rendered.
 * The unused function source was deleted with it.
 *
 * USAGE (in any game HTML):
 *   <script src="https://www.impactmojo.in/js/game-agents.js"></script>
 *
 *   // Initialise for a specific game
 *   var agents = new IMGameAgents('public-good-game');
 *
 *   // Get a single agent's decision
 *   agents.getDecision('pg-altruist', {
 *     round: 3,
 *     totalRounds: 10,
 *     history: [...],
 *     availableActions: ['contribute'],
 *     context: { max_contribution: 100 }
 *   }).then(function(decision) {
 *     console.log(decision.action, decision.amount, decision.reasoning);
 *   });
 *
 *   // Get ALL agents' decisions for a round (parallel)
 *   agents.getAllDecisions({
 *     round: 3,
 *     totalRounds: 10,
 *     history: [...],
 *     availableActions: ['cooperate', 'defect']
 *   }).then(function(decisions) {
 *     // decisions is { 'pg-altruist': {...}, 'pg-freerider': {...}, ... }
 *   });
 *
 *   // Get agent roster (names, roles, personalities) for UI display
 *   agents.getRoster().then(function(roster) {
 *     roster.forEach(function(a) {
 *       console.log(a.name, a.role, a.personality.archetype);
 *     });
 *   });
 */

(function () {
  'use strict';

  // ── Configuration ──────────────────────────────────────────────────

  var CONFIG = {
    // Agent personalities and rosters. This is the only network call the
    // client makes, and it is cached after the first load.
    AGENT_DATA_URL: 'https://www.impactmojo.in/data/game-agents.json'
  };

  // ── Agent data cache ───────────────────────────────────────────────

  var _agentDataCache = null;
  var _agentDataPromise = null;

  function loadAgentData() {
    if (_agentDataCache) return Promise.resolve(_agentDataCache);
    if (_agentDataPromise) return _agentDataPromise;

    _agentDataPromise = fetch(CONFIG.AGENT_DATA_URL)
      .then(function (resp) {
        if (!resp.ok) throw new Error('Failed to load agent data');
        return resp.json();
      })
      .then(function (data) {
        _agentDataCache = data;
        return data;
      })
      .catch(function (err) {
        console.warn('[IMGameAgents] Could not load agent data:', err);
        _agentDataPromise = null;
        return null;
      });

    return _agentDataPromise;
  }

  // ── Local fallback engine ──────────────────────────────────────────
  // Mirrors the Edge Function's fallback logic for offline/free-tier use.

  function localDecision(agent, opts) {
    var p = agent.personality;
    var actions = opts.availableActions;
    var history = opts.history || [];
    var round = opts.round;
    var totalRounds = opts.totalRounds;
    var ctx = opts.context || {};

    // Binary games (cooperate/defect)
    if (actions.indexOf('cooperate') !== -1 && actions.indexOf('defect') !== -1) {
      var cooperateProb = p.cooperation_bias;

      if (history.length > 0 && p.memory_weight > 0) {
        var lastRound = history[history.length - 1];
        if (lastRound.player_action === 'defect') {
          cooperateProb -= 0.3 * p.memory_weight;
        }
      }

      if (round > totalRounds * 0.8) {
        cooperateProb -= 0.15 * p.risk_tolerance;
      }

      cooperateProb = Math.max(0.05, Math.min(0.95, cooperateProb));
      var action = Math.random() < cooperateProb ? 'cooperate' : 'defect';

      return {
        action: action,
        amount: null,
        reasoning: agent.name + ' ' + (action === 'cooperate'
          ? 'decides to cooperate — ' + p.archetype + ' instincts.'
          : 'defects — ' + p.archetype + ' calculus.'),
        agent_id: agent.id,
        agent_name: agent.name,
        personality: p.archetype
      };
    }

    // Contribution games
    if (actions.indexOf('contribute') !== -1) {
      var maxC = ctx.max_contribution || 100;
      var base = maxC * p.cooperation_bias;

      if (history.length > 0 && p.memory_weight > 0) {
        var last = history[history.length - 1];
        var contribs = [];
        if (last.agent_actions) {
          var keys = Object.keys(last.agent_actions);
          for (var k = 0; k < keys.length; k++) {
            contribs.push(last.agent_actions[keys[k]].amount || 0);
          }
        }
        if (contribs.length > 0) {
          var avg = contribs.reduce(function (s, v) { return s + v; }, 0) / contribs.length;
          var groupRatio = avg / maxC;
          base = base * (1 - p.memory_weight) + maxC * groupRatio * p.memory_weight;
        }
      }

      var noise = (Math.random() - 0.5) * maxC * 0.2 * p.risk_tolerance;
      var amount = Math.round(Math.max(0, Math.min(maxC, base + noise)));

      return {
        action: 'contribute',
        amount: amount,
        reasoning: agent.name + ' contributes ' + amount + ' — ' + p.archetype + ' approach.',
        agent_id: agent.id,
        agent_name: agent.name,
        personality: p.archetype
      };
    }

    // Extraction games (commons)
    if (actions.indexOf('extract') !== -1) {
      var maxE = ctx.max_extraction || 100;
      var baseE = maxE * (1 - p.cooperation_bias);
      var resLevel = ctx.resource_level != null ? ctx.resource_level : 1.0;

      if (resLevel < 0.4) {
        baseE *= 0.6 + 0.4 * p.risk_tolerance;
      }

      var noiseE = (Math.random() - 0.5) * maxE * 0.15 * p.risk_tolerance;
      var amountE = Math.round(Math.max(0, Math.min(maxE, baseE + noiseE)));

      return {
        action: 'extract',
        amount: amountE,
        reasoning: agent.name + ' extracts ' + amountE + (resLevel < 0.4 ? ' — resource is scarce.' : ' — balancing need with sustainability.'),
        agent_id: agent.id,
        agent_name: agent.name,
        personality: p.archetype
      };
    }

    // Bid games
    if (actions.indexOf('bid') !== -1) {
      var estValue = ctx.estimated_value || 100;
      var bidRatio = 0.5 + p.risk_tolerance * 0.5;
      var noiseB = (Math.random() - 0.5) * estValue * 0.2;
      var amountB = Math.round(Math.max(1, estValue * bidRatio + noiseB));

      return {
        action: 'bid',
        amount: amountB,
        reasoning: agent.name + ' bids ' + amountB + ' — ' + (p.risk_tolerance > 0.6 ? 'aggressive' : 'conservative') + ' strategy.',
        agent_id: agent.id,
        agent_name: agent.name,
        personality: p.archetype
      };
    }

    // Join/wait games (network effects)
    if (actions.indexOf('join') !== -1 && actions.indexOf('wait') !== -1) {
      var netSize = ctx.network_size != null ? ctx.network_size : 0;
      var threshold = 1 - p.risk_tolerance;
      var act = (netSize >= threshold || Math.random() < p.risk_tolerance * 0.5) ? 'join' : 'wait';

      return {
        action: act,
        amount: null,
        reasoning: agent.name + (act === 'join' ? ' joins — sees momentum.' : ' waits — needs more adoption.'),
        agent_id: agent.id,
        agent_name: agent.name,
        personality: p.archetype
      };
    }

    // Default
    return {
      action: actions[0],
      amount: null,
      reasoning: agent.name + ' chooses ' + actions[0] + '.',
      agent_id: agent.id,
      agent_name: agent.name,
      personality: p.archetype
    };
  }

  // ── Main class ─────────────────────────────────────────────────────

  function IMGameAgents(gameId, options) {
    this.gameId = gameId;
    this.options = options || {};
    this._roster = null;
  }

  /**
   * Get the roster of agents for this game (for UI display).
   * Returns a Promise resolving to an array of agent objects.
   */
  IMGameAgents.prototype.getRoster = function () {
    var self = this;

    if (self._roster) return Promise.resolve(self._roster);

    return loadAgentData().then(function (data) {
      if (!data || !data.games || !data.games[self.gameId]) {
        throw new Error('No agents found for game: ' + self.gameId);
      }

      self._roster = data.games[self.gameId].agents;
      return self._roster;
    });
  };

  /**
   * Get a single agent's decision from the personality engine.
   */
  IMGameAgents.prototype.getDecision = function (agentId, opts) {
    var self = this;

    return loadAgentData().then(function (data) {
      if (!data || !data.games[self.gameId]) {
        throw new Error('Agent data unavailable');
      }

      var agents = data.games[self.gameId].agents;
      var agent = null;
      for (var i = 0; i < agents.length; i++) {
        if (agents[i].id === agentId) {
          agent = agents[i];
          break;
        }
      }

      if (!agent) throw new Error('Agent not found: ' + agentId);
      return localDecision(agent, opts);
    });
  };

  /**
   * Get ALL agents' decisions for a round (parallel requests).
   * Returns a Promise resolving to { agentId: decision, ... }
   */
  IMGameAgents.prototype.getAllDecisions = function (opts) {
    var self = this;

    return self.getRoster().then(function (roster) {
      var promises = roster.map(function (agent) {
        return self.getDecision(agent.id, opts).then(function (decision) {
          return { id: agent.id, decision: decision };
        });
      });

      return Promise.all(promises).then(function (results) {
        var decisions = {};
        results.forEach(function (r) {
          decisions[r.id] = r.decision;
        });
        return decisions;
      });
    });
  };

  /**
   * Point the client at a different agent-data file (for forks).
   */
  IMGameAgents.configure = function (options) {
    if (options.agentDataUrl) CONFIG.AGENT_DATA_URL = options.agentDataUrl;
  };

  // ── Export ─────────────────────────────────────────────────────────

  window.IMGameAgents = IMGameAgents;
})();
