let mytip = "";
import { GoogleGenerativeAI } from "@google/generative-ai"; const API_KEY = "AIzaSyCjT3qZw8I6SYEqEH1x_681_4czeQB8OIw";
const generateAI = async () => {
const genAI = new GoogleGenerativeAI(API_KEY);
const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" })
const prompt = "i am a disabled person, give me unique and random quotes everytime i call this api. please make it motivating and self-help, include inspirationational action tips. just deliver the response directly"
try {
const result = await model.generateContent(prompt);
console.log(result.response.text());
mytip = result.response.text();
} catch (error) {
}
}

generateAI()