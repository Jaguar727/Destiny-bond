const mongoose = require("mongoose");

const pokemonSchema = mongoose.Schema({
	id: {
		type: String,
		index: true,
	},

	name: {
		type: String,
	},

	icon: {
		type: String,
	},

	types: [],

	abilities: [],

	hp: {
		type: Number,
	},

	attack: {
		type: Number,
	},

	defense: {
		type: Number,
	},

	sp_attack: {
		type: Number,
	},

	sp_defense: {
		type: Number,
	},

	speed: {
		type: Number,
	},
});

const Pokemon = mongoose.model("Pokemon", pokemonSchema);

module.exports = Pokemon;
