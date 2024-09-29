const express = require("express");
const jwt = require("jsonwebtoken");
const mongoose = require("mongoose");
const bcrypt = require("bcryptjs");
const { UserSchema } = require("./database.js");
const cookieParser = require("cookie-parser");
require('dotenv').config();

const app = express();

const key = "hackUMBC2024";
app.use(express.json());
app.use(cookieParser());

function createToken(user) {
  let payload = {
    username: user.username,
  }

  return  jwt.sign(payload, key, {expiresIn: "10h"});
}


function verifyToken(req, res, next) {
  let token = req.header.authorization || req.cookies.Token;

  if(!token) {
    res.json({
     error: "99",
      content: "UNAUTHORIZED USER"
    });
    return;
  }

  jwt.verify(token, key, (err, decoded) => {
    if(err) {
      console.log(err);
      res.json({
        error: "50",
         content: "What the token is going on here"
       });
       return;
    }

    req.user = decoded;
  });

  next();
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

      let salt = await bcrypt.genSalt(10);
      let hashedPassword = await bcrypt.hash(password, salt);

      user = await User.create({
        username: username,
        hashPassword: hashedPassword,
        previousCourses: [],
        joinDate: Date.now()
      });


      if(user) {
        let jwt = createToken({username});
        res.cookie("Token", jwt);
        res.json({
          success: 1,
          Token: jwt
        });
      } else {
        res.json({
          error: "1",
          content: "Something bad happened"
        })
      }
    });


    app.post("/api/login", async (req, res) => {
      let username = req.body.username;
      let password = req.body.password;

      let token = req.header.authorization || req.cookies.Token;
      if(token || req.cookies.Token) {
        res.json({
          error: "2",
          content: "Already logged in"
        });

        return;
      }

      let user = await User.findOne({username}).exec();

      if(!user) {
        res.json({
          error: "2",
          content: "Username not found"
        });
        return;
      }

      let correctPassword = await bcrypt.compare(password, user.hashPassword);

      if(correctPassword) {
        let jwt = createToken({username});

        res.cookie("Token", jwt);
        res.json({
          success: "1",
          content: "Login successful",
          Token: jwt
        });
      }
    })

    app.post("/api/logout", (req, res) => {
      let token = req.header.authorization || req.cookies.Token;

      if(token) {
        res.clearCookie("Token");
        
        res.json({
          success: "3",
          content: "Logout successful goodbye :)",
        });
      } else {
        res.json({
          error: "3",
          content: "User not logged in"
        });
      }
    });

    //LLM Generates Content here
    app.post("/api/search", verifyToken, (req, res) => {
      
    });

    app.get("/api/userdata", verifyToken ,(req, res) => {
      res.json({
        username: req.user.username,
      })
    });
    
    app.listen(8080, (err) => {
      console.log("Listening on port 8080");
    });
  } catch(error) {
    console.log(error);
  }

})();