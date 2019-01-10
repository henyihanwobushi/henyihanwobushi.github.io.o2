---
layout: post
title: MathJax basic tutorial and quick reference
---

This is for practice, the content is basicly from [MathJax basic tutorial and quick reference](https://math.meta.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference)

# Basic

1. To see how any formula was written in any question or answer, including this one, right-click on the expression it and choose "Show Math As > TeX Commands". (When you do this, the '$' will not display. Make sure you add these. See the next point.)
2. *For inline formulas*, enclose the formula in ```$...$```. For displayed formulas, use ```$$...$$```.
These render differently. For example, type ``` $\sum_{i=0}^n i^2 = \frac{(n^2+n)(2n+1)}{6}$``` to show $\sum_{i=0}^n i^2 = \frac{(n^2+n)(2n+1)}{6}$ (which is inline mode) or type ```$$\sum_{i=0}^n i^2 = \frac{(n^2+n)(2n+1)}{6}$$``` to show:
    $$\sum_{i=0}^n i^2 = \frac{(n^2+n)(2n+1)}{6}$$
3. For *Greek letters*, use `\alpha`, `\beta`,..., `\omega`: $\alpha, \beta, … \omega$. For uppercase, use `\Gamma`, `\Delta`,..., `\Omega`: $\Gamma, \Delta, …, \Omega$.
4. For superscripts and subscripts, use *^* and *_*. For example, ```x_i^2```: $x_i^2$, ```\log_2 x```: $\log_2 x$.
5. *Groups*. Superscripts, subscripts, and other operations apply only to the next “group”. A “group” is either a single symbol, or any formula surrounded by curly braces `{…}`. If you do `10^10`, you will get a surprise: $10^10$. But `10^{10}` gives what you probably wanted: $10^{10}$.<br/>Use curly braces to delimit a formula to which a superscript or subscript applies: `x^5^6` is an error;  `{x^y}^z` is ${x^y}^z$, and `x^{y^z}` is $x^{y^z}$. Observe the difference between `x_i^2`: $x_i^2$ and `x_{i^2}`: $x_{i^2}$.
6. Parentheses Ordinary symbols `()[]` make parentheses and brackets `$(2+3)[4+4]$`. Use `\{` and `\}` for curly braces `$\{\}$`.<br/>
These do not scale with the formula in between, so if you write `(\frac{\sqrt x}{y^3})` the parentheses will be too small: $(\frac{\sqrt x}{y^3})$. Using `\left(…\right)` will make the sizes adjust automatically to the formula they enclose: `\left(\frac{\sqrt x}{y^3}\right)` is $\left(\frac{\sqrt x}{y^3}\right)$.<br/>
`\left` and `\right` apply to all the following sorts of parentheses: `(` and `)` $(x)$, `[` and `]` $[x]$, `\{` and `\}` $\{x\}$, `|` $|x|$, `\vert` $\vert x \vert$, `\Vert` $\Vert x\Vert$, `\langle` and `\rangle` $\langle x \rangle$,  `\lceil` and `\rceil` $\lceil x \rceil$, and `\lfloor` and `\rfloor` $\lfloor x \rfloor$. `\middle` can be used to add additional dividers. There are also invisible parentheses, denoted by `.`: `\left.\frac12\right\rbrace` is $\left.\frac12\right\rbrace$.<br/>
If manual size adjustments are required: `\Biggl(\biggl(\Bigl(\bigl((x)\bigr)\Bigr)\biggr)\Biggr)` gives $\Biggl(\biggl(\Bigl(\bigl((x)\bigr)\Bigr)\biggr)\Biggr)$.
7. Sums and integrals `\sum` and `\int`; the subscript is the lower limit and the superscript is the upper limit, so for example `\sum_1^n` $\sum_1^n$. Don't forget `{…}` if the limits are more than a single symbol. For example, `\sum_{i=0}^\infty i^2` is $\sum_{i=0}^\infty i^2$. Similarly, `\prod` $\prod$, `\int` $\int$, `\bigcup` $\bigcup$, `\bigcap` $\bigcap$, `\iint` $\iint$, `\iiint` $\iiint$, `\idotsint` $\idotsint$.
8. [Fractions](https://math.meta.stackexchange.com/questions/12978/should-dfrac-be-edited-in) There are three ways to make these. `\frac ab` applies to the next two groups, and produces $\frac ab$; for more complicated numerators and denominators use `{…}`: `\frac{a+1}{b+1}` is $\frac {a+1} {b+1}$. If the numerator and denominator are complicated, you may prefer `\over`, which splits up the group that it is in: `{a+1\over b+1}` is ${a+1\over b+1}$. Using `\cfrac{a}{b}' command is useful for continued fractions $\cfrac{a}{b}$, more details for which are given in this [sub-article](https://math.meta.stackexchange.com/a/5058/3111).
9. Fonts

| Command | Font | Uppercase | Lowercase |
|:-:|:-:|:-:|:-:|
| `\mathbb` | \Bbb' for "blackboard bold" | $\mathbb{ABCDEFG}$ | $\mathbb{abcdefg}$ |
| `\mathbf` | boldface | $\mathbf{ABCDEFG}$ | $\mathbf{abcdefg}$ |
| `\mathit` | italics | $\mathit{ABCDEFG}$ | $\mathit{abcdefg}$ |
| `\pmb` | boldfaced italics | $\pmb {ABCDEFG}$ | $\pmb {abcdefg}$ |
| `\mathtt` | "typewriter" font | $\mathtt{ABCDEFG}$ | $\mathtt {abcdefg}$ |
| `\mathrm` | roman font | $\mathrm {ABCDEFG}$ | $\mathrm {abcdefg}$ |
| `\mathsf` | sans-serif font | $\mathsf{ABCDEFG}$ | $\mathsf{abcdefg}$ |
| `\mathcal` | "calligraphic" letters | $\mathcal{ABCDEFG}$ | $\mathcal{abcdefg}$ |
| `\mathscr` | script letters | $\mathscr{ABCDEFG}$ | $\mathscr {abcdefg}$ |
| `\mathfrak` | "Fraktur" (old German style) letters | $\mathfrak {ABCDEFG}$ | $\mathfrak {abcdefg}$ |

10. Radical signs Use sqrt, which adjusts to the size of its argument: `'\sqrt{x^3}` $\sqrt{x^3}$; `\sqrt[3]{\frac xy}` $\sqrt[3]{\frac xy}$. For complicated expressions, consider using `{...}^{1/2}` instead.
11. Some special functions such as "lim", "sin", "max", "ln", and so on are normally set in roman font instead of italic font. Use `\lim`, `\sin`, etc. to make these: `\sin x`: $\sin x$, not `sin x`: $sinx$. Use subscripts to attach a notation to `\lim`: $\lim_{x\to 0}$.
12. There are a very large number of special symbols and notations, too many to list here; see this shorter listing, or this exhaustive listing. Some of the most common include:
    * `\lt`: $\lt$, `\gt`: $\gt$, `\le`: $\le$, `\leq`: $\leq$, `\leqq`: $\leqq$, `\leqslant`: $\leqslant$, `\ge`: $\ge$, `\geq`: $\geq$, `\geqq`: $\geqq$, `\geqslant`: $\geqslant$, `\neq`: $\neq$.<br/>
    You can use `\not` to put a slash through almost anything: `\not\lt`: $\not\lt$ but it often looks bad.
    * `\times`: $\times$, `\div`: $\div$, `\pm`: $\pm$, `\mp`: $\mp$, `\cdot` is a centered dot: $x \cdot y$.
    * `\cup`: $\cup$, `\cap`: $\cap$, `\setminus`: $\setminus$, `\subset`: $\subset$, `\subseteq`: $\subseteq$, `\subsetneq`: $\subsetneq$, `\supset`: $\supset$, `\in`: $\in$, `\notin`: $\notin$, `\emptyset`: $\emptyset$, `\varnothing`: $\varnothing$.
    * `{n+1 \choose 2k}`: ${n+1 \choose 2k}$ or `\binom{n+1}{2k}`: $\binom{n+1}{2k}$,
    * `\to`: $\to$, `\rightarrow`: $\rightarrow$, `\leftarrow`: $\leftarrow$, `\Rightarrow`: $\Rightarrow$, `\Leftarrow`: $\Leftarrow$, `\mapsto`: $\mapsto$
    * `\land`: $\land$, `\lor`: $\lor$, `\lnot`: $\lnot$, `\forall`: $\forall$, `\exists`: $\exists$, `\top`: $\top$, `\bot`: $\bot$, `\vdash`: $\vdash$, `\vDash`: $\vDash$.
    * `\star`: $\star$, `\ast`: $\ast$, `\oplus`: $\oplus$, `\circ`: $\circ$, `\bullet`: $\bullet$
    * `\approx`: $\approx$, `\sim`: $\sim$, `\simeq`: $\simeq$, `\cong`: $\cong$, `\equiv`: $\equiv$, `\prec`: $\prec$, `\lhd`: $\lhd$, `\therefore`: $\therefore$
    * `\infty`: $\infty$, `\aleph_0`: $\aleph_0$
    * `\nabla`: $\nabla$, `\partial`: $\partial$
    * `\Im`: $\Im$, `\Re`: $\Re$
    * For modular equivalence, use `\pmod` like this: `a\equiv b\pmod n`: $a\equiv b\pmod n$.
    * `\ldots` is the dots in $a_1, a_2, a_3, \ldots, a_n$ `a1,a2,…,an`, `\cdots` is the dots in $a_1 + a_2 + a_3 + \cdots + a_n$
    * Some Greek letters have variant forms: `\epsilon`: $\epsilon$, `\varepsilon`: $\varepsilon$, `\phi`: $\phi$, `\varphi`: $\varphi$, and others.
    * Script lowercase l is `\ell`: $\ell$.
    * [Detexify](http://detexify.kirelabs.org/classify.html) lets you draw a symbol on a web page and then lists the TEX symbols that seem to resemble it. These are not guaranteed to work in MathJax but are a good place to start. To check that a command is supported, note that MathJax.org maintains a [list of currently supported LATEX commands](https://docs.mathjax.org/en/latest/tex.html#), and one can also check Dr. Carol JVF Burns's page of [TEX Commands Available in MathJax](http://www.onemathematicalcat.org/MathJaxDocumentation/TeXSyntax.htm).

# Matrices

1. Use `$$\begin{matrix}…\end{matrix}$$` In between the `\begin` and `\end`, put the matrix elements. End each matrix row with `\\`, and separate matrix elements with `&`. For example:
```
$$
    \begin{matrix}
    1 & x & x^2 \\\\
    1 & y & y^2 \\\\
    1 & z & z^2 \\\\
    \end{matrix}
$$
```
produces:<br/>
$$
    \begin{matrix}
    1 & x & x^2 \\
    1 & y & y^2 \\
    1 & z & z^2 \\
    \end{matrix}
$$
<br/>
MathJax will adjust the sizes of the rows and columns so that everything fits.
2. To add brackets, either use \left…\right as in section 6 of the tutorial, or replace matrix with:<br/>
`pmatrix`: $$
    \begin{pmatrix}
    1 & x & x^2 \\
    1 & y & y^2 \\
    1 & z & z^2 \\
    \end{pmatrix}
$$<br/>
`bmatrix`: $$
    \begin{bmatrix}
    1 & x & x^2 \\
    1 & y & y^2 \\
    1 & z & z^2 \\
    \end{bmatrix}
$$<br/>
`Bmatrix`: $$
    \begin{Bmatrix}
    1 & x & x^2 \\
    1 & y & y^2 \\
    1 & z & z^2 \\
    \end{Bmatrix}
$$<br/>
`vmatrix`: $$
    \begin{vmatrix}
    1 & x & x^2 \\
    1 & y & y^2 \\
    1 & z & z^2 \\
    \end{vmatrix}
$$<br/>
`Vmatrix`: $$
    \begin{Vmatrix}
    1 & x & x^2 \\
    1 & y & y^2 \\
    1 & z & z^2 \\
    \end{Vmatrix}
$$

3. Use `\cdots` $\cdots$  `\ddots` $\ddots$ `vdots` $\vdots$ when you want to omit some of the entries:<br/>
$$
    \begin{pmatrix}
         1 & a_1 & a_1^2 & \cdots & a_1^n \\
         1 & a_2 & a_2^2 & \cdots & a_2^n \\
         \vdots  & \vdots& \vdots & \ddots & \vdots \\
         1 & a_m & a_m^2 & \cdots & a_m^n
     \end{pmatrix}
$$
4. For horizontally "augmented" matrices, put parentheses or brackets around a suitably-formatted table; see arrays below for details. Here is an example:<br/>
$$ \left[
\begin{array}{cc|c}
  1&2&3 \\
  4&5&6
\end{array}
\right] $$<br/>
is produced by:
```
$$ \left[
\begin{array}{cc|c}
  1&2&3 \\\\
  4&5&6
\end{array}
\right] $$
```
The `cc|c` is the crucial part here; it says that there are three centered columns with a vertical bar between the second and third.
1. For vertically "augmented" matrices, use `\hline`. For example:<br/>
$$
  \begin{pmatrix}
    a & b\\
    c & d\\
  \hline
    1 & 0\\
    0 & 1
  \end{pmatrix}
$$<br/>
is produced by:
```
$$
    \begin{pmatrix}
        a & b \\\\
        c & d \\\\
        \hline
        1 & 0 \\\\
        0 & 1 
    \end{pmatrix}
$$
```
1. For small inline matrices use `\bigl(\begin{smallmatrix} ... \end{smallmatrix}\bigr)`, e.g. $$\bigl({\begin{smallmatrix}a & b \\ c & d \end{smallmatrix}}\bigr)$$ is produced by: `$$\bigl({\begin{smallmatrix}a & b \\ c & d \end{smallmatrix}}\bigr)$$`.

# Aligned equations

Often people want a series of equations where the equals signs are aligned. To get this, use `\begin{align}…\end{align}`. Each line should end with `\\`, and should contain an ampersand at the point to align at, typically immediately before the equals sign.
For example:<br/>
$$
    \begin{align}
    \sqrt{37} & = \sqrt{\frac{73^2-1}{12^2}} \\
     & = \sqrt{\frac{73^2}{12^2}\cdot\frac{73^2-1}{73^2}} \\
     & = \sqrt{\frac{73^2}{12^2}}\sqrt{\frac{73^2-1}{73^2}} \\
     & = \frac{73}{12}\sqrt{1 - \frac{1}{73^2}} \\
     & \approx \frac{73}{12}\left(1 - \frac{1}{2\cdot73^2}\right)
    \end{align}
$$
<br/>
The usual `$$` marks that delimit the display may be omitted here.

# Symbols

In general, you have to search in long tables about a specific symbol you're looking for, things like Ψ, δ, ζ, ≥, ⊆ ... And it turns out that this operation can be frustrating and time consuming, which can cause the buddy to abandon writing the complete $\LaTeX$ sentence in his answer, or in some cases, the complete answer itself.

Here is the website: [Detexify²](http://detexify.kirelabs.org/classify.html) No more frustration.

# Definitions by cases (piecewise functions)
Use `\begin{cases}…\end{cases}`. End each case with a `\\`, and use `&` before parts that should be aligned.

For example, you get this:

$$
    f(n) =
    \begin{cases}
        n/2,  & \text{if $n$ is even} \\\\
        3n+1, & \text{if $n$ is odd}
    \end{cases}
$$

by write this:

```
    f(n) =
    \begin{cases}
        n/2,  & \text{if $n$ is even} \\
        3n+1, & \text{if $n$ is odd}
    \end{cases}
```


