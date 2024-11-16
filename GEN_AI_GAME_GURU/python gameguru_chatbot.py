def get_response(user_input):
    user_input = user_input.lower()

    if "start" in user_input:
        return "Welcome! Let's create a presentation on Generative AI in GameGuru. Would you like an introduction, or should we dive into examples of AI integration in game development?"
    elif "introduction" in user_input:
        return ("Generative AI refers to AI models that can create new content like images, dialogues, and music. "
                "In game development, it automates asset creation, level design, and more. Shall we talk about asset creation next?")
    elif "asset creation" in user_input:
        return ("Generative AI can automate the creation of 3D textures and character models using GANs (Generative Adversarial Networks). "
                "In GameGuru, AI-generated assets can be imported directly, saving time. Would you like to know about AI in level design?")
    elif "level design" in user_input:
        return ("AI can generate dynamic game levels based on player preferences or algorithms, making each playthrough unique. "
                "GameGuru supports importing AI-generated custom levels. Should we discuss NPC dialogues next?")
    elif "npc dialogues" in user_input:
        return ("Using Transformer models like GPT, you can create adaptive NPC dialogues, making the game feel more interactive. "
                "Would you like to learn about AI-generated music and sound effects?")
    elif "music" in user_input or "sound" in user_input:
        return ("Generative AI can create immersive background music and sound effects, enhancing the gaming experience. "
                "These sounds can be customized for different game environments. Want to discuss the challenges in using AI?")
    elif "challenges" in user_input:
        return ("Challenges include ensuring quality across AI-generated assets, avoiding biased content, and handling copyright issues. "
                "Despite these, Generative AI offers great potential in game development. Do you have any other questions?")
    elif "thank you" in user_input or "exit" in user_input:
        return "You're welcome! Good luck with your presentation on Generative AI in GameGuru. Goodbye!"
    else:
        return "I'm here to help with creating your presentation on Generative AI and GameGuru. Please ask a specific question or type 'start' to begin."

def chatbot():
    print("GameGuru Generative AI Chatbot is now active! Type 'start' to begin or 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print(f"Chatbot: {response}")
        if "exit" in user_input.lower():
            break

if __name__ == "__main__":
    chatbot()
