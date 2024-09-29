const mongoose = require("mongoose");


let UserSchema = new mongoose.Schema({
    username: String,
    hashPassword: String,
    previousCourses: [String],
    joinDate: Number,
});

module.exports = {
    UserSchema: UserSchema
}
