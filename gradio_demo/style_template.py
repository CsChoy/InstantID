style_list = [
    {
        "name": "(No style)",
        "prompt": "{prompt}",
        "negative_prompt": "",
    },
    {
        "name": "Spring Festival",
        "prompt": "Flat illustration, a Chinese {prompt}, ancient style, wearing a red cloth, smile face, white skin, clean background, fireworks blooming, red lanterns",
        "negative_prompt": "photo, deformed, black and white, realism, disfigured, low contrast, realistic, cropped, worst quality, missing fingers, extra digit, jpeg artifacts, signature, multiple, (lowres, low quality, worst quality:1.2)",
    },
    {
        "name": "Watercolor",
        "prompt": "watercolor painting, {prompt}. vibrant, beautiful, painterly, detailed, textural, artistic",
        "negative_prompt": "(lowres, low quality, worst quality:1.2), (text:1.2), watermark, anime, photorealistic, 35mm film, deformed, glitch, low contrast, noisy",
    },
    {
        "name": "Film Noir",
        "prompt": "film noir style, ink sketch|vector, {prompt} highly detailed, sharp focus, ultra sharpness, monochrome, high contrast, dramatic shadows, 1940s style, mysterious, cinematic",
        "negative_prompt": "(lowres, low quality, worst quality:1.2), (text:1.2), watermark, (frame:1.2), deformed, ugly, deformed eyes, blur, out of focus, blurry, deformed cat, deformed, photo, anthropomorphic cat, monochrome, photo, pet collar, gun, weapon, blue, 3d, drones, drone, buildings in background, green",
    },
    {
        "name": "Neon",
        "prompt": "masterpiece painting, buildings in the backdrop, kaleidoscope, lilac orange blue cream fuchsia bright vivid gradient colors, the scene is cinematic, {prompt}, emotional realism, double exposure, watercolor ink pencil, graded wash, color layering, magic realism, figurative painting, intricate motifs, organic tracery, polished",
        "negative_prompt": "(lowres, low quality, worst quality:1.2), (text:1.2), watermark, (frame:1.2), deformed, ugly, deformed eyes, blur, out of focus, blurry, deformed cat, deformed, photo, anthropomorphic cat, monochrome, photo, pet collar, gun, weapon, blue, 3d, drones, drone, buildings in background, green",
    },
    {
        "name": "Vibrant Color",
        "prompt": "vibrant colorful, ink sketch|vector|2d colors, at nightfall, sharp focus, {prompt}, highly detailed, sharp focus, the clouds,colorful,ultra sharpness",
        "negative_prompt": "(lowres, low quality, worst quality:1.2), (text:1.2), watermark, (frame:1.2), deformed, ugly, deformed eyes, blur, out of focus, blurry, deformed cat, deformed, photo, anthropomorphic cat, monochrome, photo, pet collar, gun, weapon, blue, 3d, drones, drone, buildings in background, green",
    },
    {
        "name": "Line art",
        "prompt": "line art drawing {prompt} . professional, sleek, modern, minimalist, graphic, line art, vector graphics",
        "negative_prompt": "anime, photorealistic, 35mm film, deformed, glitch, blurry, noisy, off-center, deformed, cross-eyed, closed eyes, bad anatomy, ugly, disfigured, mutated, realism, realistic, impressionism, expressionism, oil, acrylic",
    },
    {
        "name": "Anime",
        "prompt": "anime artwork  {prompt}. anime style, key visual, vibrant, studio anime, highly detailed",
        "negative_prompt": "photo, deformed, black and white, realism, disfigured, low contrast",
    },
    {
        "name": "Comic Book",
        "prompt": "anime artwork  {prompt}. anime style, key visual, vibrant, studio anime, highly detailed",
        "negative_prompt": "photograph, deformed, glitch, noisy, realistic, stock photo",
    },
    {
        "name": "Craft Clay",
        "prompt": "play-doh style {prompt} . sculpture, clay art, centered composition, Claymation",
        "negative_prompt": "sloppy, messy, grainy, highly detailed, ultra textured, photo",
    },
    {
        "name": "Digital Art",
        "prompt": "concept art {prompt} . digital artwork, illustrative, painterly, matte painting, highly detailed",
        "negative_prompt": "photo, photorealistic, realism, ugly",
    },
    {
        "name": "Enhance",
        "prompt": "breathtaking {prompt} . award-winning, professional, highly detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, distorted, grainy",
    },
    {
        "name": "Fantasy Art",
        "prompt": "ethereal fantasy concept art of {prompt} . magnificent, celestial, ethereal, painterly, epic, majestic, magical, fantasy art, cover art, dreamy",
        "negative_prompt": "photographic, realistic, realism, 35mm film, dslr, cropped, frame, text, deformed, glitch, noise, noisy, off-center, deformed, cross-eyed, closed eyes, bad anatomy, ugly, disfigured, sloppy, duplicate, mutated, black and white",
    },
    {
        "name": "Neonpunk",
        "prompt": "neonpunk style {prompt} . cyberpunk, vaporwave, neon, vibes, vibrant, stunningly beautiful, crisp, detailed, sleek, ultramodern, magenta highlights, dark purple shadows, high contrast, cinematic, ultra detailed, intricate, professional",
        "negative_prompt": "painting, drawing, illustration, glitch, deformed, mutated, cross-eyed, ugly, disfigured",
    },
    {
        "name": "Ads Advertising",
        "prompt": "advertising poster style {prompt} . Professional, modern, product-focused, commercial, eye-catching, highly detailed",
        "negative_prompt": "noisy, blurry, amateurish, sloppy, unattractive",
    },
    {
        "name": "Artstyle Abstract",
        "prompt": "abstract style {prompt} . non-representational, colors and shapes, expression of feelings, imaginative, highly detailed",
        "negative_prompt": "realistic, photographic, figurative, concrete",
    },
    {
        "name": "Artstyle Graffiti",
        "prompt": "graffiti style {prompt} . street art, vibrant, urban, detailed, tag, mural",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic",
    },
    {
        "name": "Artstyle Renaissance",
        "prompt": "renaissance style {prompt} . realistic, perspective, light and shadow, religious or mythological themes, highly detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, modernist, minimalist, abstract",
    },
    {
        "name": "Futuristic Cybernetic",
        "prompt": "cybernetic style {prompt} . futuristic, technological, cybernetic enhancements, robotics, artificial intelligence themes",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, historical, medieval",
    },
    {
        "name": "Futuristic Cyberpunk Cityscape",
        "prompt": "cyberpunk cityscape {prompt} . neon lights, dark alleys, skyscrapers, futuristic, vibrant colors, high contrast, highly detailed",
        "negative_prompt": "natural, rural, deformed, low contrast, black and white, sketch, watercolor",
    },
    {
        "name": "Futuristic Retro Cyberpunk",
        "prompt": "retro cyberpunk {prompt} . 80’s inspired, synthwave, neon, vibrant, detailed, retro futurism",
        "negative_prompt": "modern, desaturated, black and white, realism, low contrast",
    },
    {
        "name": "Futuristic Retro Futurism",
        "prompt": "retro-futuristic {prompt} . vintage sci-fi, 50s and 60s style, atomic age, vibrant, highly detailed",
        "negative_prompt": "contemporary, realistic, rustic, primitive",
    },
    {
        "name": "Game Fighting Game",
        "prompt": "fighting game style {prompt} . dynamic, vibrant, action-packed, detailed character design, reminiscent of fighting video games",
        "negative_prompt": "peaceful, calm, minimalist, photorealistic",
    },
    {
        "name": "Game Gta",
        "prompt": "GTA-style artwork {prompt} . satirical, exaggerated, pop art style, vibrant colors, iconic characters, action-packed",
        "negative_prompt": "realistic, black and white, low contrast, impressionist, cubist, noisy, blurry, deformed",
    },
    {
        "name": "Game Mario",
        "prompt": "Super Mario style {prompt} . vibrant, cute, cartoony, fantasy, playful, reminiscent of Super Mario series",
        "negative_prompt": "realistic, modern, horror, dystopian, violent",
    },
    {
        "name": "Game Pokemon",
        "prompt": "Pokémon style {prompt} . vibrant, cute, anime, fantasy, reminiscent of Pokémon series",
        "negative_prompt": "realistic, modern, horror, dystopian, violent",
    },
    {
        "name": "Game Retro Game",
        "prompt": "retro game art {prompt} . 16-bit, vibrant colors, pixelated, nostalgic, charming, fun",
        "negative_prompt": "realistic, photorealistic, 35mm film, deformed, glitch, low contrast, noisy",
    },
    {
        "name": "Game RPG Fantasy Game",
        "prompt": "role-playing game (RPG) style fantasy {prompt} . detailed, vibrant, immersive, reminiscent of high fantasy RPG games",
        "negative_prompt": "photo, deformed, black and white, realism, disfigured, low contrast",
    },
    {
        "name": "Game Zelda",
        "prompt": "Legend of Zelda style {prompt} . vibrant, fantasy, detailed, epic, heroic, reminiscent of The Legend of Zelda series",
        "negative_prompt": "sci-fi, modern, realistic, horror",
    },
    {
        "name": "Misc Dreamscape",
        "prompt": "dreamscape {prompt} . surreal, ethereal, dreamy, mysterious, fantasy, highly detailed",
        "negative_prompt": "realistic, concrete, ordinary, mundane",
    },
    {
        "name": "Misc Fairy Tale",
        "prompt": "fairy tale {prompt} . magical, fantastical, enchanting, storybook style, highly detailed",
        "negative_prompt": "realistic, modern, ordinary, mundane",
    },
    {
        "name": "Misc Kawaii",
        "prompt": "kawaii style {prompt} . cute, adorable, brightly colored, cheerful, anime influence, highly detailed",
        "negative_prompt": "dark, scary, realistic, monochrome, abstract",
    },
    {
        "name": "Misc Manga",
        "prompt": "manga style {prompt} . vibrant, high-energy, detailed, iconic, Japanese comic style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, Western comic style",
    },
    {
        "name": "Misc Metropolis",
        "prompt": "metropolis-themed {prompt} . urban, cityscape, skyscrapers, modern, futuristic, highly detailed",
        "negative_prompt": "rural, natural, rustic, historical, simple",
    },
    {
        "name": "Misc Monochrome",
        "prompt": "monochrome {prompt} . black and white, contrast, tone, texture, detailed",
        "negative_prompt": "colorful, vibrant, noisy, blurry, deformed",
    },
    {
        "name": "Misc Nautical",
        "prompt": "nautical-themed {prompt} . sea, ocean, ships, maritime, beach, marine life, highly detailed",
        "negative_prompt": "landlocked, desert, mountains, urban, rustic",
    },
    {
        "name": "Misc Space",
        "prompt": "space-themed {prompt} . cosmic, celestial, stars, galaxies, nebulas, planets, science fiction, highly detailed",
        "negative_prompt": "earthly, mundane, ground-based, realism",
    },
    {
        "name": "Misc Stained Glass",
        "prompt": "stained glass style {prompt} . vibrant, beautiful, translucent, intricate, detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic",
    },
    {
        "name": "Misc Techwear Fashion",
        "prompt": "techwear fashion {prompt} . futuristic, cyberpunk, urban, tactical, sleek, dark, highly detailed",
        "negative_prompt": "vintage, rural, colorful, low contrast, realism, sketch, watercolor",
    },
    {
        "name": "Misc Tribal",
        "prompt": "tribal style {prompt} . indigenous, ethnic, traditional patterns, bold, natural colors, highly detailed",
        "negative_prompt": "modern, futuristic, minimalist, pastel",
    },
    {
        "name": "Misc Zentangle",
        "prompt": "zentangle {prompt} . intricate, abstract, monochrome, patterns, meditative, highly detailed",
        "negative_prompt": "colorful, representative, simplistic, large fields of color",
    },
    {
        "name": "Papercraft Collage",
        "prompt": "collage style {prompt} . mixed media, layered, textural, detailed, artistic",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic",
    },
    {
        "name": "Papercraft Paper Quilling",
        "prompt": "paper quilling art of {prompt} . intricate, delicate, curling, rolling, shaping, coiling, loops, 3D, dimensional, ornamental",
        "negative_prompt": "photo, painting, drawing, 2D, flat, deformed, noisy, blurry",
    },
    {
        "name": "Papercraft Thick Layered Papercut",
        "prompt": "thick layered papercut art of {prompt} . deep 3D, volumetric, dimensional, depth, thick paper, high stack, heavy texture, tangible layers",
        "negative_prompt": "2D, flat, thin paper, low stack, smooth texture, painting, drawing, photo, deformed",
    }
]

styles = {k["name"]: (k["prompt"], k["negative_prompt"]) for k in style_list}
