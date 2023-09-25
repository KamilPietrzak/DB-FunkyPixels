<p align="center">
  <img src="https://space.monetapietrzak.com/project_funkypixels_logo.webp" alt="Funky Pixels logo." height=150 width=150>
</p>
<h1 align="center">DB Funky Pixels</h1>
<p align="center">
  Database project in <b>🐘PostgreSQL🐘</b> for small and simplified social platform based on the idea of <a href="https://kwejk.pl/" alt="Link to kwejk.pl.">kwejk</a>.
</p>

## ℹ️ About Funky Pixels
Funky Pixels is social platform project, created to share humorous multimedia content.

The idea for this project comes from an initiative that me and my friends took in high school. Unfortunately, due to lack of skills and experience, the project was terminated after three years of work and was never completed. Because I enjoy fixing things that don't work properly, and I find it an interesting challenge, I decided to try again after more than a year and a half break.

It is worth remembering that the project was prepared for educational purposes, with some simplifications, and is not intended to create a real product.</p>

## 💾 Funky Pixels repos 
* [KamilPietrzak/DB-FunkyPixels](https://github.com/KamilPietrzak/DB-FunkyPixels "Link to repo with a database.") - Database project in **🐘PostgreSQL🐘** for small and simplified social platform based on the idea of [kwejk](https://kwejk.pl/ "Link to kwejk.pl.").

## ▶️ Run project
There are 2 ways to start a repository.

### Start with conda
1. Create a conda environment by following the command:

```
conda env create -f environment.yml
```

Also, if you already have an environment, you can update it:

```
conda env update -f environment.yml
```

2. Activate a conda enviroment:

```
conda activate db-funky_pixels
```

### Star with venv
> **Notice:** Before you run the project, you need to install Python 3.10.x
1. Create venv:

```
python -m venv venv
```

2. Activate venv:

Linux: 
```
source venv/bin/activate
```

Windows: 
```
venv\Scripts\activate
```

3. Back to repo folder and install <code>requirements.txt</code>:

```
pip install -r requirements.txt
```


-----------------------------------------
### Run project:
> **Notice:** Before you run the project, you need to create a database named <code>dbfunkypixels</code> in your database server.

> **Notice:** Before you run the project, you need to create a <code>.env</code> file in the <code>/project</code> folder. The <code>.env</code> file must include all the required variables to establish a connection. <br>
> Example: <br>
> HOST = '127.0.0.1' <br>
> PORT = 5432 <br>
> USER= 'postgres' <br>
> PASSWORD = 'password'

**To start the project, follow:**

```
python project/run.py
```


## 🤖 Information on the use of AI ##
**Logo**
Logo created by [Leonardo.ai](https://app.leonardo.ai "Link to Leonardo.ai."). Model Leonardo Diffusion.
  
*Prompt:*
<code>An image showing a cartoon version of the silhouette of a Corgi dog's muzzle from the doge meme. Picture in style Synthwave.</code>

*Negative prompt:*
<code>Don't genre the whole dog silhouette.</code>

## 📜 [LICENSE](LICENSE "Licence")

MIT License

Copyright (c) 2023 Kamil Pietrzak 'Moneta'

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


<h2>📫 Contact</h2>
<br>
<p align="center"><b>monetapietrzak@gmail.com</b></p>
<br>
<hr>
<p align="center"><b>Find me also...</b></p>
<p align="center">
  <a href="https://twitter.com/Moneta_Pietrzak" alt="Link to profile Kamil Pietrzak 'Moneta' in X (Twitter).">X (Twitter)</a> |
  <a href="https://www.linkedin.com/in/kamil-pietrzak-wroc/" alt="Link to profile Kamil Pietrzak 'Moneta' in LinkedIn.">LinkedIn</a> |
  <a href="https://stackoverflow.com/users/10077312/kamil-pietrzak-moneta" alt="Link to profile Kamil Pietrzak 'Moneta' in StackOverflow.">StackOverflow</a> |
  <a href="https://www.codewars.com/users/Moneta-Pietrzak" alt="Link to profile Kamil Pietrzak 'Moneta' in Codewars.">Codewars</a>
</p>
<hr>
<br>
<p align="center">More about me<br><a href="https://www.monetapietrzak.com/" alt="Link to Kamil pietrzak 'Moneta' site.">www.monetapietrzak.com</a> (only Polish)</p>
