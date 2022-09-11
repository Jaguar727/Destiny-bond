const express = require("express");
const mongoose = require("mongoose");
const messages = require("./config/messages.config");
const config = require("./config/application.config");
const app = express();
const PokemonController = require("./routes/pokemon.route");


/**
 * Set up the MongoDB connection.
 */

mongoose.connect(config.mongo.url, config.mongo.config, (err) => {
	if (err) {
		console.error(err);
		process.exit();
	}

	console.log("MongoDB connected successfully");
});

/**
 * Load the json module to parse POST and PUT request.
 */
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

/**
 * Load controllers
 */

app.use("/pokemon", PokemonController);
/**
 * 404 request handling
 */
app.use((req, res) => {
	res.status(404).send({ message: messages.not_found });
});

module.exports = app;
