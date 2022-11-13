const express = require("express");
const messages = require("../config/messages.config");
const router = express.Router();
const Pokemon = require("../models/pokemon.model");

router.get("/", async (req, res) => {
	try {
		res.send(await Pokemon.find());
	} catch (err) {
		console.error(err);
		res.status(500).send({ message: messages.database_error });
	}
});

router.get("/:id", async (req, res) => {
	try {
        const pokemon = await Pokemon.find({ intId: req.params.id })
		res.send(pokemon)
	} catch(err) {
        console.error(err);
		res.status(500).send({ message: messages.database_error });
    }
});

module.exports = router;
