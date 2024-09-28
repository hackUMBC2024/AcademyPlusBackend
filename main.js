const express = require("express");
const jwt = require("jsonwebtoken");
const mongoose = require("mongoose");
const bycrypt = require("bcryptjs");
const { UserSchema } = require("./database.js");
require('dotenv').config();

const app = express();

const key = "hackUMBC2024";
app.use(express.json());

function createToken(user) {
  let payload = {
    username: user.username,
  }

  return  jwt.sign(payload, key, {expiresIn: "10h"});
}


(async function(){
  try {
    console.log(process.env.MONGO_URI)
    await mongoose.connect(process.env.MONGO_URI);

    console.log("Mongoose Connected");

    let User = new mongoose.model("Users", UserSchema);

    app.get("/", (req, res) => {
      const token = req.headers.authorization;
      res.send("Hello World");
    });
    
    app.post("/api/signup", async (req, res) => {
      let username = req.body.username;
      let password = req.body.password;
    
      let user = await User.findOne({username: username}).exec();

      if(user) {
        res.json({
          error: "1",
          content: "Username taken"
        })
        return;
      }

      let salt = await bycrypt.genSalt(10);
      let hashedPassword = await bycrypt.hashedPassword(password, salt);

      user = await User.create({
        username: username,
        password: hashedPassword,
        joinDate: Date.now()
      });


      if(user) {
        let jwt = await createToken({username});
        res.send("Signup succesful: " + jwt);
      } else {
        res.json({
          error: "1",
          content: "Something bad happened"
        })
      }
    });
    
    app.listen(8080, (err) => {
      console.log("Listening on port 8080");
    });
  } catch(error) {
    console.log(error);
  }

})();